# Data Platform Hackathon

Repo to centralise my work for the knowit bolagshack series.

## Data Sources

- Local .csv
- Fantasy Premier League API
- Star Wars API (SWAPI)


## Stack
 
- Dependency Management: uv
- Environment Management: direnv
- Data Warehouse: 
  - ``dev``: DuckDB
  - ``test`` and ``prod``: MotherDuck

## ToDo

- [ ] dbt transformations of FPL data
- [ ] FastMCP on FPL
    - Discover raw data
    - Search players
    - Get latest selection; Auth-request
