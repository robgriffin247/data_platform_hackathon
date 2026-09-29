import duckdb
import os

db = f"md:data_platform_hackathon__{os.getenv('TARGET')}" if os.getenv("TARGET") in ["test", "prod"] else "data/data_platform_hackathon__dev.duckdb"

def load_country_stats():
    with duckdb.connect(db) as con:
        con.sql("create schema if not exists raw_misc")
        con.sql("create or replace table raw_misc.country_stats as (select * from read_csv('data/country_stats.csv'))")

if __name__=="__main__":
    load_country_stats()
