
EXPECT
   ↓
Invalid record
   ↓
Keep it / Drop it / Fail pipeline
Keep invalid records but track them:
@dp.expect("valid_driver_rating", "driver_rating BETWEEN 1 AND 5")

Drop invalid records:
@dp.expect_or_drop(
    "valid_driver_rating",
    "driver_rating BETWEEN 1 AND 5"
)
Fail the pipeline:
@dp.expect_or_fail(
    "valid_trip_id",
    "trip_id IS NOT NULL"
)

Rule Layer Action :
Rule                         Layer       Action
-------------------------------------------------------
valid_date,year(date)>= 2020    Silver      Drop
date must be valid              Silver      Drop
driver_rating 1-10              Silver      Drop
trip_id must not be null        Silver      Drop
city_id must exist              Silver      Drop