# Transportation Data Pipeline — Architecture

## 1. Architecture Overview

This project implements an end-to-end transportation data engineering pipeline using Databricks, Apache Spark, PySpark, SQL, Delta Lake, and Spark Declarative Pipelines.

The pipeline follows the **Medallion Architecture** pattern, where data is progressively refined through three layers:

```text
                         SOURCE
                           │
                           ▼
                ┌─────────────────────┐
                │   Databricks Volume │
                │      city data      │
                │ Raw Transportation  │
                │       Data          │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    BRONZE LAYER     │
                │                     │
                │ city                │
                │ trips               │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │    SILVER LAYER     │
                │                     │
                │ city                │
                │ trips               │
                │ calendar            │
                │                     │
                │ Data Cleaning       │
                │ Data Validation     │
                │ Transformation      │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     GOLD LAYER      │
                │                     │
                │ fact_trips          │
                │ trips_jaipur        │
                │ trips_kochi         │
                │ trips_lucknow       │
                │ trips_surat         │
                │ trips_chandigarh    │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Analytics / BI /    │
                │ Reporting / Users   │
                └─────────────────────┘
```

---

## 2. Source Layer

The raw transportation data is stored in a **Databricks Volume** under the transportation catalog.

The Volume acts as the source location for the pipeline.

```text
Databricks
└── transportation
    └── Volume
        └── Raw Transportation Data
```

The raw files are intentionally not stored in the GitHub repository.

GitHub contains the pipeline source code and documentation, while the raw data remains managed within the Databricks environment.

---

# 3. Bronze Layer

The Bronze layer is responsible for ingesting the source data with minimal transformation.

### Bronze tables

```text
transportation
└── bronze
    ├── city
    └── trips
```

### Responsibilities

* Ingest raw transportation data.
* Preserve source information.
* Store data in Delta format.
* Perform minimal transformations.
* Provide a reliable source for downstream processing.

The Bronze layer should remain as close as possible to the original source data.

---

# 4. Silver Layer

The Silver layer contains cleaned, validated, and transformed data.

```text
transportation
└── silver
    ├── city
    ├── trips
    └── calendar
```

### Responsibilities

* Clean raw data.
* Standardize data types.
* Handle invalid or missing values.
* Apply business rules.
* Validate important columns.
* Enrich transportation data.
* Prepare datasets for analytical processing.

### Data Quality

Data quality expectations are applied during Silver-layer processing using Spark Declarative Pipelines.

Examples of validation rules include:

```text
Trip date must be valid
Driver rating must be within the expected range
Customer rating must be within the expected range
Trip ID should not be NULL
Required identifiers should be available
```

The exact expectations are implemented in the Silver transformation code.

---

# 5. Gold Layer

The Gold layer contains business-ready and analytics-ready datasets.

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

`fact_trips` acts as the primary analytical fact table containing processed transportation trip information.

It combines the required information from the Silver layer and provides a structured dataset for downstream analytics.

### City-specific datasets

The pipeline also produces city-specific Gold datasets:

```text
trips_jaipur
trips_kochi
trips_lucknow
trips_surat
trips_chandigarh
```

These datasets provide filtered or transformed transportation data for individual cities and can be consumed by reporting and analytical workloads.

---

# 6. End-to-End Data Flow

The complete processing flow can be summarized as:

```text
Raw Files
   │
   ▼
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
   │ Enrichment
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

# 7. Processing Technology

The pipeline uses the following technologies:

| Technology                  | Purpose                                                |
| --------------------------- | ------------------------------------------------------ |
| Databricks                  | Data engineering and processing platform               |
| Apache Spark                | Distributed data processing                            |
| PySpark                     | Python-based Spark transformations                     |
| SQL                         | Data transformation and analytical queries             |
| Delta Lake                  | Reliable table storage                                 |
| Spark Declarative Pipelines | Pipeline orchestration and declarative data processing |
| Unity Catalog               | Data and object organization/governance                |
| Databricks Volumes          | Raw data storage                                       |
| Git/GitHub                  | Source control and project versioning                  |

---

# 8. Medallion Architecture

The project follows the Medallion Architecture:

```text
                 ┌───────────────┐
                 │    BRONZE     │
                 │ Raw/Ingested  │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │    SILVER     │
                 │ Cleaned and   │
                 │ Validated     │
                 └───────┬───────┘
                         │
                         ▼
                 ┌───────────────┐
                 │     GOLD      │
                 │ Business and  │
                 │ Analytics     │
                 │ Ready         │
                 └───────────────┘
```

### Bronze

**Purpose:** Store ingested source data.

### Silver

**Purpose:** Clean, validate, transform, and enrich the data.

### Gold

**Purpose:** Provide business-ready datasets for analytics and reporting.

---

# 9. Data Quality Architecture

Data quality checks are primarily applied in the Silver layer.

```text
                 Silver Data
                     │
                     ▼
             Data Quality Checks
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
    Valid Records        Invalid Records
          │                     │
          ▼                     ▼
        Gold             Handle According
                         to Expectations
```

The pipeline uses Spark Declarative Pipeline expectations to enforce data quality rules.

This allows data quality requirements to be defined close to the transformation logic.

---

# 10. Repository Architecture

The GitHub repository contains the source code and project documentation.

```text
Transportation_Pipeline/
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
```

---

# 11. Separation of Data and Code

The project separates raw data from source code.

```text
                 GitHub
                   │
                   │
            Pipeline Source Code
                   │
                   ▼
              Databricks
                   │
                   ▼
          Databricks Volume
                   │
                   ▼
             Raw Data
```

Raw transportation files are maintained in the Databricks Volume rather than committed to GitHub.

This prevents large datasets and potentially sensitive data from being unnecessarily stored in the source-code repository.

---

# 12. Architecture Summary

The project implements a scalable transportation data pipeline using Databricks and Apache Spark.

The architecture follows:

```text
Databricks Volume
       │
       ▼
    Bronze
       │
       ▼
    Silver
       │
       ▼
     Gold
       │
       ▼
Analytics / BI / Reporting
```

The Medallion Architecture provides clear separation between raw ingestion, data transformation and validation, and business-ready analytical datasets.

The pipeline is implemented using PySpark, SQL, Delta Lake, and Spark Declarative Pipelines, while GitHub is used for source control and project documentation.
