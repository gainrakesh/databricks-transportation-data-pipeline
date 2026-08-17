from pyspark.sql import functions as F
from pyspark import pipelines as dp

start_date = "2025-01-01"
end_date = "2025-12-31"

@dp.materialized_view(
    name = "transportation.silver.calender",
    comment="Calender dimension with comprehensive date attributes",
    table_properties = {
        "quality" : "silver",
        "layer" : "silver",
        "delta.enableChangeDataFeed":"true",
        "delta.autoOptimize.optimizeWrite":"true",
        "delta.autoOptimize.autoCompact":"true",
    }
)
def calender():
    df = spark.sql(f"""
                   select explode(sequence(to_date('{start_date}'),
                   to_date('{end_date}') ,interval 1 day )) as date""")
    df = df.withColumn("date_key",F.date_format(F.col("date"),"yyyymmdd").cast("int"))

    df = (
        df.withColumn("year",F.year(F.col("date")))
            .withColumn("month",F.month(F.col("date")))
            .withColumn("quarter",F.quarter(F.col("date")))
    )
    return df