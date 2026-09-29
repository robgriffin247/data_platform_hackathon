import modal
from ingest.fpl import ingest_fpl
from pathlib import Path
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PROJECT_ROOT = Path(__file__).parent.parent

IMAGE = (
    modal.Image.debian_slim(python_version="3.14")
    .uv_sync(str(PROJECT_ROOT))
    .add_local_dir(PROJECT_ROOT / "orchestrate", "/root/orchestrate")
    .add_local_dir(PROJECT_ROOT / "ingest", "/root/ingest")
)

dlt_volume = modal.Volume.from_name("fantalytic-dlt-state", create_if_missing=True)

app = modal.App("fantalytic-elt", image=IMAGE)


@app.function(
    schedule=modal.Cron("0 4 * * *"),
    secrets=[modal.Secret.from_name("fantalytic-secret")],
    volumes={"/root/.dlt": dlt_volume},
    timeout=120,
    retries=2,
)
def ingest_fpl_job() -> None:
    load_info = ingest_fpl()
    logger.info(load_info)
    load_info.raise_on_failed_jobs()
    dlt_volume.commit()
