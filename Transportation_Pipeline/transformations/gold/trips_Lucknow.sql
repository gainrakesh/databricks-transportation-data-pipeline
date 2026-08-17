CREATE OR REFRESH MATERIALIZED VIEW transportation.gold.trips_lucknow AS (
    SELECT * FROM transportation.gold.fact_trips
    where City_Id = "UP01"
)