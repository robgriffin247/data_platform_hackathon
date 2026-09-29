import dlt
import httpx
import os


def get_fpl():
    response = httpx.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    response.raise_for_status()
    data = response.json()

    gameweeks = data.get("events")
    players = data.get("elements")
    teams = data.get("teams")

    return [gameweeks, players, teams]


def get_fixtures():
    response = httpx.get("https://fantasy.premierleague.com/api/fixtures/")
    response.raise_for_status()
    fixtures = response.json()

    return fixtures


def ingest_fpl():
    target = os.getenv("TARGET")

    if target in ["prod", "test"]:
        destination = dlt.destinations.motherduck(
            credentials={
                "database": f"data_platform_hackathon__{os.getenv('TARGET')}",
                "motherduck_token": os.environ["MOTHERDUCK_TOKEN"],
            }
        )
    elif target == "dev":
        destination = dlt.destinations.duckdb(credentials=f"data/data_platform_hackathon__dev.duckdb")
    else:
        raise ValueError(
            f"Invalid TARGET value in environment; expected 'prod', 'test' or 'dev', got '{target}'"
        )

    gameweeks, players, teams = get_fpl()
    fixtures = get_fixtures()

    current_gameweek = next(gw["id"] for gw in gameweeks if gw["is_current"])
    for player in players:
        player["gameweek"] = current_gameweek

    @dlt.resource(name="gameweeks", write_disposition="replace")
    def gameweeks_resource():
        yield gameweeks

    @dlt.resource(
        name="players", write_disposition="merge", primary_key=["id", "gameweek"]
    )
    def players_resource():
        yield players

    @dlt.resource(name="teams", write_disposition="replace")
    def teams_resource():
        yield teams

    @dlt.resource(name="fixtures", write_disposition="replace")
    def fixtures_resource():
        yield fixtures

    pipeline = dlt.pipeline(
        pipeline_name="dph_fpl",
        destination=destination,
        dataset_name="raw_fpl",
    )
    return pipeline.run(
        [
            gameweeks_resource(),
            players_resource(),
            teams_resource(),
            fixtures_resource(),
        ]
    )


if __name__ == "__main__":
    load_info = ingest_fpl()
    print(load_info)
