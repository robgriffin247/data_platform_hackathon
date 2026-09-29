import os

import dlt
from dlt.sources.helpers.rest_client.paginators import SinglePagePaginator
from dlt.sources.rest_api import rest_api_source

source = rest_api_source(
    {
        "client": {
            "base_url": "https://swapi.info/api/",
            "paginator": SinglePagePaginator(),
        },
        "resources": ["films", "people", "planets", "species", "vehicles", "starships"],
    }
)


dest = (
    dlt.destinations.motherduck(credentials=f"md:data_platform_hackathon__{os.getenv('TARGET')}")
    if os.getenv("TARGET") in ["test", "prod"]
    else dlt.destinations.duckdb(credentials="data/data_platform_hackathon__dev.duckdb")
)


def run_pipeline() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="dph_swapi",
        destination=dest,
        dataset_name="raw_swapi",
    )

    return pipeline.run(source)


if __name__ == "__main__":
    print(run_pipeline())
    
