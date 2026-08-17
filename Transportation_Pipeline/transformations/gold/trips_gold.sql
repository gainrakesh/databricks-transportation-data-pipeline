CREATE OR REPLACE VIEW transportation.gold.fact_trips
as (
    SELECT 
    t.ID,
    c.City_Name,
    t.date,
    t.City_Id,
    t.passenger_type,
    t.distance_travelled_km,
    t.fare_amount,
    t.passenger_rating,
    t.driver_rating,
    ca.date_key,
    ca.year,
    ca.month,
    ca.quarter
    from transportation.silver.trips t
    join transportation.silver.city c on t.City_Id = c.City_Id 
    join transportation.silver.calender ca on t.date = ca.date
)