CREATE OR REFRESH MATERIALIZED VIEW transportation.gold.trips_jaipur AS (
    SELECT * FROM transportation.gold.fact_trips
    where City_Id = "RJ01"
)