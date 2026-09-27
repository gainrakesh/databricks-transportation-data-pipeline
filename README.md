# Databricks Transportation Data Pipeline

This is a small data engineering project I built using **Databricks, PySpark, SQL, Spark and Delta Lake**.

The project takes raw transportation data and processes it through **Bronze, Silver and Gold** layers.

## Data Flow

```text
Raw Data
   ↓
Bronze
   ↓
Silver
   ↓
Gold
```

## Bronze

Raw transportation data is loaded into the Bronze layer.

I created:

* `city`
* `trips`

The raw data is stored in Delta format.

## Silver

In Silver, I clean and transform the data before using it for analysis.

I worked on:

* Data cleaning
* Data type changes
* Null checks
* Basic data validation
* Business rules
* Data enrichment

Silver contains:

* `city`
* `trips`
* `calendar`

I also used **Spark Declarative Pipeline expectations** for some data quality checks.

## Gold

The Gold layer contains the final datasets used for analysis.

Main table:

* `fact_trips`

I also created city-level tables for:

* Jaipur
* Kochi
* Lucknow
* Surat
* Chandigarh

## Project Structure

```text
databricks-transportation-data-pipeline/
│
├── README.md
│
├── transformations/
│   ├── bronze/
│   │   ├── city.py
│   │   └── trips.py
│   │
│   ├── silver/
│   │   ├── calendar.py
│   │   ├── city.py
│   │   └── trips.py
│   │
│   └── gold/
│       ├── trips_gold.sql
│       ├── trips_jaipur.sql
│       ├── trips_kochi.sql
│       ├── trips_lucknow.sql
│       └── trips_surat.sql
│
├── docs/
│   ├── architecture.md
│   └── data_dictionary.md
│
└── screenshots/
    ├── pipeline_graph.png
    ├── catalog_structure.png
    └── pipeline_run.png
```


## Technologies Used

* Databricks
* PySpark
* SQL
* Apache Spark
* Delta Lake
* Spark Declarative Pipelines
* Unity Catalog
* Databricks Volumes
* Git / GitHub

## Data

The raw transportation files are stored in a Databricks Volume.

I have not uploaded the raw data to GitHub.


## What I Learned

While building this project, I practiced:

* Medallion Architecture
* PySpark
* SQL
* Delta Lake
* Data quality checks
* Spark Declarative Pipelines
* Databricks Volumes
* Unity Catalog
* Git and GitHub

## Author

**Rakesh Gain**

Cloud Data Engineer | Python | SQL | PySpark | Azure | Databricks
