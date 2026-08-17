# Databricks Transportation Data Pipeline

An end-to-end transportation data engineering pipeline built using **Databricks, PySpark, SQL, Apache Spark, Delta Lake, and Spark Declarative Pipelines**. The project follows the **Medallion Architecture** to transform raw transportation data into clean, validated, and analytics-ready datasets.

---

##Project Overview

This project demonstrates an end-to-end data engineering workflow for processing transportation data using the Databricks platform.

Raw transportation data is stored in a **Databricks Volume** under the `transportation` catalog. The data is processed through a Medallion Architecture consisting of **Bronze, Silver, and Gold layers**.

The pipeline performs:

* Data ingestion
* Data transformation
* Data cleaning
* Data validation
* Data quality checks
* Data enrichment
* Business-level transformations
* City-level analytical processing
* Creation of analytics-ready datasets

The final Gold-layer datasets can be consumed by downstream **BI, analytics, reporting, and data science workloads**.

---

## Architecture

The project follows the Medallion Architecture:

```text
                         Raw Transportation Data
                                  │
                                  ▼
                         ┌─────────────────┐
                         │ Databricks      │
                         │ Volume          │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     BRONZE      │
                         │                 │
                         │ city            │
                         │ trips           │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │     SILVER      │
                         │                 │
                         │ city            │
                         │ trips           │
                         │ calendar        │
                         │                 │
                         │ Cleaning        │
                         │ Validation      │
                         │ Transformation  │
                         └────────┬────────┘
                                  │
                                  ▼
                         ┌─────────────────┐
                         │      GOLD       │
                         │                 │
                         │ fact_trips      │
                         │ City datasets   │
                         └────────┬────────┘
                                  │
                                  ▼
                         Analytics / BI / Reporting
```

For a detailed architecture explanation, see [`docs/architecture.md`](docs/architecture.md).

---

## Bronze Layer

The Bronze layer contains the initial ingested transportation data.

### Tables

```text
transportation
└── bronze
    ├── city
    └── trips
```

### Responsibilities

* Ingest raw source data
* Preserve source information
* Store data in Delta format
* Perform minimal transformations

The Bronze layer is intentionally kept close to the original source data.

---

##Silver Layer

The Silver layer contains cleaned, validated, and transformed datasets.

### Tables

```text
transportation
└── silver
    ├── city
    ├── trips
    └── calendar
```

### Transformations

The Silver layer performs:

* Data type standardization
* Data cleaning
* Null validation
* Data quality checks
* Business-rule validation
* Data enrichment
* Preparation of data for the Gold layer

### Data Quality

Spark Declarative Pipeline expectations are used to validate important business fields.

Examples include:

```text
Valid trip date
Valid driver rating
Valid customer rating
```

The actual validation rules are implemented in the Silver transformation code.

---

##Gold Layer

The Gold layer contains business-ready and analytics-ready datasets.

### Tables

```text
transportation
└── gold
    ├── fact_trips
    ├── trips_jaipur
    ├── trips_kochi
    ├── trips_lucknow
    ├── trips_surat
    └── trips_chandigarh
```

### `fact_trips`

`fact_trips` is the primary analytical fact table containing processed transportation trip information.

It combines the required data from the Silver layer and provides a structured dataset for downstream analytics.

### City-Level Datasets

The project also produces city-specific datasets for:

* Jaipur
* Kochi
* Lucknow
* Surat
* Chandigarh

These datasets can be used for city-level reporting and analytical workloads.

---

## Data Flow

```text
Databricks Volume
       │
       ▼
    Bronze
       │
       │ Ingestion
       ▼
    Silver
       │
       │ Cleaning
       │ Validation
       │ Transformation
       ▼
     Gold
       │
       ├── fact_trips
       ├── trips_jaipur
       ├── trips_kochi
       ├── trips_lucknow
       ├── trips_surat
       └── trips_chandigarh
       │
       ▼
Analytics / BI / Reporting
```

---

## Technologies Used

* **Databricks** — Data engineering and processing platform
* **Apache Spark** — Distributed data processing
* **PySpark** — Python-based Spark transformations
* **SQL** — Data transformation and analytical processing
* **Delta Lake** — Reliable and transactional data storage
* **Spark Declarative Pipelines** — Declarative pipeline development and data quality
* **Unity Catalog** — Data organization and governance
* **Databricks Volumes** — Raw data storage
* **Git / GitHub** — Source control and project versioning

---

## Project Structure

```text
databricks-transportation-data-pipeline/
│
├── README.md
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
│       ├── trips_chandigarh.sql
│       ├── trips_jaipur.sql
│       ├── trips_kochi.sql
│       ├── trips_lucknow.sql
│       └── trips_surat.sql
│
├── docs/
│   ├── architecture.md
│   └── data_dictionary.md
│
├── screenshots/
│   ├── pipeline_graph.png
│   ├── catalog_structure.png
│   └── pipeline_run.png
```

## Data Source

The raw transportation datasets are stored in a **Databricks Volume** under the `transportation` catalog.

The raw data is intentionally **not committed to GitHub**.

This repository contains the pipeline source code, documentation, configuration, and supporting project artifacts.

Example source structure:

```text
Databricks
└── transportation
    └── Volume
        └── Raw Transportation Data
```

---

##Data Quality

Data quality checks are applied primarily in the Silver layer using Spark Declarative Pipeline expectations.

Examples:

```text
Rule                         Layer       Purpose
----------------------------------------------------------------
Valid trip date               Silver      Validate trip dates
Valid driver rating           Silver      Validate rating range
Valid city ID                 Silver      Validate city relationship
```

The data quality rules are implemented close to the transformation logic so that invalid data can be identified during pipeline processing.



## Pipeline Execution

The pipeline is developed and executed in the Databricks environment using Spark Declarative Pipelines.

High-level execution flow:

```text
1. Raw files are placed in the Databricks Volume
                    ↓
2. Bronze layer ingests the source data
                    ↓
3. Silver layer cleans and validates the data
                    ↓
4. Gold layer creates analytics-ready datasets
                    ↓
5. Gold datasets are consumed for analytics/reporting
```

---

## Data and Security

Raw data is maintained inside the Databricks environment and is not committed to the public GitHub repository.

The repository does not contain:

* Passwords
* Access tokens
* API keys
* Cloud credentials
* Databricks Personal Access Tokens
* Sensitive configuration
* Large raw datasets

Secrets and credentials should be managed using appropriate secret-management mechanisms rather than storing them in source control.

---

##Git Workflow

The project uses Git for source control.

Main branches:

```text
main
│
├── feature/project-documentation
├── feature/data-quality
└── feature/databricks-bundle
```

Feature branches are used for development and changes are merged into `main` after completion.

The `main` branch represents the stable version of the project.

---

##Future Improvements

The project can be extended with additional production-oriented capabilities:

* [ ] Databricks Declarative Automation Bundles
* [ ] CI/CD using GitHub Actions
* [ ] Automated unit and data-quality testing
* [ ] Pipeline monitoring and alerting
* [ ] Incremental data processing
* [ ] Schema evolution
* [ ] Error/quarantine tables
* [ ] Centralized configuration
* [ ] Data lineage and governance
* [ ] Infrastructure as Code

---

##Key Data Engineering Concepts Demonstrated

This project demonstrates practical implementation of:

* End-to-end ETL pipeline development
* Medallion Architecture
* Bronze / Silver / Gold data layers
* Distributed processing with Apache Spark
* PySpark transformations
* SQL transformations
* Delta Lake
* Spark Declarative Pipelines
* Data quality expectations
* Databricks Volumes
* Unity Catalog
* Git and GitHub version control
* Analytics-ready data modeling

---

## Author

**Rakesh Gain**

Cloud Data Engineer | Python | SQL | PySpark | Azure | Databricks

---

## Project

If you find this project useful for learning Data Engineering, feel free to explore the repository and star it.

