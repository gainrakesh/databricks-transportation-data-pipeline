from pyspark.sql import functions as F
from pyspark import pipelines as dp


@dp.materialized_view(
    name = "transportation.silver.city",
    comment="Cleaned products dimension with business transformation",
    table_properties = {
        "quality" : "silver",
        "layer" : "silver",
        "delta.enableChangeDataFeed":"true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true",
    }
)
def city_silver():
    df_bronze = spark.read.table("transportation.bronze.city")
    df_silver = df_bronze.select(
        F.col("city_id").alias("City_Id"),
        F.col("city_name").alias("City_Name"),
        F.col("ingest_time").alias("bronze_ingest_time")
    )

    df_silver = df_silver.withColumn("silver_processed_time",F.current_timestamp())
    return df_silver