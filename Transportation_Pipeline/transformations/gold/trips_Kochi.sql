CREATE OR REFRESH MATERIALIZED VIEW transportation.gold.trips_kochi AS (
    SELECT * FROM transportation.gold.fact_trips
    where City_Id = "KL01"
)