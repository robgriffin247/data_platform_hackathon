# Orchestrate

Basic orchestration is performed using a CRON job on modal that ingests the FPL data. Profile and environment in Modal is steered with direnv and ``.env``. Deploy from root with 

```
uv run modal deploy orchestrate/modal_fpl_job.py
```
