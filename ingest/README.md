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

## Files

- ``country_stats.py`` demonstrates loading from a .csv file using DuckDB in Python
- ``swapi.py`` demonstrates loading with dlt from a REST API