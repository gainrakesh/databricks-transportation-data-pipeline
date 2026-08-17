from pyspark.sql import functions as F
from pyspark import pipelines as dp


# Creating a staging view for Silver data
@dp.view(
    name="trips_silver_staging",
    comment="Transformed trips data ready for CDC upsert"
)
@dp.expect("valid_date", "year(date) >= 2020")
@dp.expect("valid_driver_rating", "driver_rating between 1 and 10")
def order_silver():

    df_bronze = spark.readStream.table(
        "transportation.bronze.trips"
    )

    df_silver = (
       df_bronze
        .filter(F.col("passenger_rating") >= 3)\
        .withColumnRenamed("city_id", "City_Id")\
        .withColumnRenamed("trip_id", "ID")\
        .withColumn(
            "silver_processed_timestamp",
            F.current_timestamp()
        )
        .select(
            "ID",
            "date",
            "City_Id",
            "passenger_type",
            "distance_travelled_km",
            "fare_amount",
            "passenger_rating",
            "driver_rating",
            "silver_processed_timestamp"
        )
    )

    return df_silver


# Create Silver streaming target table
dp.create_streaming_table(
    name="transportation.silver.trips",
    comment="Cleaned and validated trips with CDC upsert",
    table_properties={
        "quality": "silver",
        "layer": "silver",
        "delta.enableChangeDataFeed": "true",
        "delta.autoOptimize.optimizeWrite": "true",
        "delta.autoOptimize.autoCompact": "true",
    }
)


# Connect staging source to Silver target using CDC
dp.create_auto_cdc_flow(
    target="transportation.silver.trips",
    source="trips_silver_staging",
    keys=["ID"],
    sequence_by=F.col("silver_processed_timestamp"),
    stored_as_scd_type=1
)