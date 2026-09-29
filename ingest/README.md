# Ingestion

- Ingest with ``uv run ingest/<file>.py``
- Runs in ``dev`` by default (steered by ``TARGET`` in environment)
- Prefix commands with ``TARGET=<env>`` to run in ``test`` or ``prod``
- Examples:
    - Ingest ``country_stats.csv`` to DuckDB in ``dev``
        ```
        uv run ingest/country_stats.csv
        ```
    - Ingest SWAPI for MotherDuck ``prod`` database
        ```
        TARGET="prod" uv run ingest/swapi.py
        ```

## Sources

- ``country_stats.py`` loads data from wikipedia/kaggle about countries, and demonstrates loading from a .csv file using DuckDB in Python
- ``swapi.py`` loads data from SWAPI (Star Wars API), and demonstrates loading with dlt from a REST API
- ``fpl.py`` loads data from the FPL (Fantasy Premier League) API, demonstrating extraction with httpx and minor transformations before loading with dlt resources