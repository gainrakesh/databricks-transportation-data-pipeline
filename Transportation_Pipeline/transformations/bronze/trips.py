from pyspark.sql import functions as F
from pyspark import pipelines as dp

source_path = "/Volumes/workspace/default/project_transpotation/trips_data/"

@dp.table(
    name = "transportation.bronze.trips",
    comment="Streaming ingestion of raw order data with Auto Loader",
    table_properties = {
        "quality" : "bronze",
        "layer" : "bronze",
        "source_format" : "csv",
        "delta.enableChangeDataFeed":"true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true",
    }
)
def order_bronze():
    df = (spark.readStream.format("cloudFiles")\
          .option("cloudFiles.format", "csv")\
          .option("cloudFiles.inferColumnTypes","true")\
          .option("cloudFiles.schemaEvolutionMode", "rescue")\
          .option("cloudFiles.maxFilesPerTrigger", 100)\
          .load(source_path)
          )
    df = df.withColumnRenamed(
    "distance_travelled(km)",
    "distance_travelled_km"
    )

    df = df.withColumn("file_name", F.col("_metadata.file_path"))\
            .withColumn("ingest_datetime" , F.current_timestamp())
    return df