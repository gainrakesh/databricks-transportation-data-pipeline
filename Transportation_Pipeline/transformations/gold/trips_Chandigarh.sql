CREATE OR REPLACE VIEW transportation.gold.trpis_chandigarh AS(
    SELECT * 
    from transportation.gold.fact_trips
    where City_Id = "CH01"
)