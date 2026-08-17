CREATE OR REFRESH MATERIALIZED VIEW transportation.gold.trips_surat AS (
    SELECT * FROM transportation.gold.fact_trips
    where City_Id = "GJ01"
)