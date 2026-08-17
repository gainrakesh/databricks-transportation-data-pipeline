from pyspark.sql.functions import col, current_timestamp
from pyspark.sql.functions import md5,concat_ws,sha2
from pyspark import pipelines as dp

source_path = "/Volumes/workspace/default/project_transpotation/city_data/"


@dp.materialized_view(
    name = "transportation.bronze.city",
    comment="City Raw data Processing",
    table_properties = {
        "quality" : "bronze",
        "layer" : "bronze",
        "source_format" : "csv",
        "delta.enableChangeDataFeed":"true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true",
    }
)
def city_bronze():
    df = spark.read.format("csv")\
                    .option("header","true")\
                    .option("inferSchema","true")\
                    .option("mode","PERMISSIVE")\
                    .option("mergeSchema","true")\
                    .option("columnNameOfCorruptRecord","_corrupt_record")\
                    .load(source_path)

    df = df.withColumn("fule_name",col("_metadata.file_path")).withColumn("ingest_time",current_timestamp())
    return df

