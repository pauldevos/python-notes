# Data Engineering Technologies, Tools, and Practices



### Task, Workflow Managers
- Dagster
- sbt
- Papermill
- Airflow
- Luigi
- Oozie
- [Prefect](https://github.com/PrefectHQ/prefect)
  - [Docs](https://docs.prefect.io/)
  - [DataEng Podcast](https://www.dataengineeringpodcast.com/prefect-workflow-engine-episode-86/)
  - [Dask with Prefect](https://docs.prefect.io/guide/tutorials/dask-cluster.html)
  - [Why Not Airflow?](https://medium.com/the-prefect-blog/why-not-airflow-4cfa423299c4)
- [Joblib](https://joblib.readthedocs.io/en/latest/)
- [Dask](https://github.com/dask/dask) - Parallel computing with task scheduling https://dask.org


### Articles
- [Dask vs Celery](https://matthewrocklin.com/blog/work/2016/09/13/dask-and-celery)


### AWS Tools
- [aws-data-wrangler](https://github.com/awslabs/aws-data-wrangler)
- Glue
- Data Pipeline
- Lambda
- Step Functions



# data-engineering-tools
A list of tools and whatnot under the umbrella of Data Engineering

# Workflow Managers - ETL

#### Systems Engineering Overview
- [System Design Primer](https://github.com/donnemartin/system-design-primer)


## Things a Data Engineer should know

### Cloud Computing (e.g. AWS, Google Cloud, Azure)
- AWS resources:
  - S3
  - EC2
  - RDS
  - RedShift
  - EMR
  - Kinesis
  - Athena
  - Lambda
  - VPC
  - Glue
  - Sagemaker
- AWS tools:
  - Boto3 (Python)
  - AWS CLI
----
### Job Scheduling
- Cron, Airflow, Ooozie, Luigi, and/or AWS Step Functions
----
### Frameworks
- Scheduling/Workflows: Airflow, Oozie, Luigi, Cron, and/or AWS Step Functions
- Spark
- Data Transformation: Pandas, Dask
- ML Pipelines: Numpy, Scikit-Learn
----
### Languages
- Python
- Bash
- SQL
- Optional: Scala (for Spark), Java (for Spark, Kafka, or Storm)
----
### Data Modeling
- Fact-Dimensional Warehouses
- Slowly Changing Dimensions
- Star Schema, Snowflake Schema
- Index Tuning
- Query Tuning
- Transactional Processing: Lock and Block
- OLTP vs OLAP
----
### Data Warehousing Architectures
- Lambda Architecture
- Kappa Architecture
- Batch
- Mini-Batch
- Streaming
----
### Business Intelligence Tools
- Click and Drag (e.g. Looker)
- SQL Based (e.g. Tableau, Looker, Mode, Periscope)
- SQL/Python/R based (e.g. Jupyter, Mode)
----
### Data Warehouse Serving Layers
- RedShift
- BigQuery
- Snowflake
- RDBMS (e.g. AWS RDS, Google SQL)
----
### Other Important Development Tools
- Docker
- CI/CD (CircleCI, TravisCI, or Jenkins)
- Pytest (or Unittest)
- Tox

### CLI Tools
- AWS CLI
- Bash (Awk, Grep, Sed)
- Click
- Argparse
- Python-Fire



A quick preview of some favorite tools and/or frameworks are:

- Python
  - Airflow
  - Spark
  - Dask
  - Pandas
  - Boto3 (AWS SDK)
  - Flask
  - Pyramid
  - Scikit-Learn
  - TensorFlow
  - [Apache Arrow](https://arrow.apache.org/) - [PyArrow](https://arrow.apache.org/docs/python/)
  
- Jupyter Notebooks
  - JupyterHub


- DockerHub


- Databases
  - Postgres
  - RedShift
  - Presto
  - MapD (the database)
  - ElasticSearch (index/search engine)
  
  
- Business Intelligence Tools
  - MapD [Database](https://github.com/omnisci/mapd-core), [Charting](https://github.com/omnisci/mapd-charting), [Rendering Engine](https://www.omnisci.com/platform/immerse/) by [OmniSci](https://www.omnisci.com/)
  - SuperSet
  - ELK Stack (Kibana)
  - Bokeh
  - Plotly
  - Dash

- Data Visualization Projects
  - [UW Falcon](https://github.com/uwdata/falcon)
  - [Interactive Python Data Visualization with Bokeh](https://realpython.com/python-data-visualization-bokeh/)
  - [Python Module Imports Visualization](https://chezsoi.org/lucas/blog/python-modules-imports-visualization.html) - [code](https://github.com/Lucas-C/dotfiles_and_notes/blob/master/languages/python/gen_modules_graph.py)
  

## ETL Articles

Links
- https://dwbi.org/etl
- https://dwbi.org/etl/etl/54-incremental-loading-for-dimension-table
- https://gtoonstra.github.io/etl-with-airflow/datavault.html
- https://medium.com/@maximebeauchemin/functional-data-engineering-a-modern-paradigm-for-batch-data-processing-2327ec32c42a
- https://gtoonstra.github.io/etl-with-airflow/datavault2.html
- https://aws.amazon.com/blogs/big-data/top-8-best-practices-for-high-performance-etl-processing-using-amazon-redshift/
- https://gtoonstra.github.io/etl-with-airflow/platform.html
- https://panoply.io/data-warehouse-guide/etl-tutorial/
- https://stefdata.github.io/
- https://medium.com/@natekupp/getting-started-the-3-stages-of-data-infrastructure-556dac82e825
- https://tombreur.wordpress.com/2017/04/30/the-past-and-future-of-dimensional-modeling/
- https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-ii-47c4e7cbda71
- https://medium.com/@rchang/a-beginners-guide-to-data-engineering-part-i-4227c5c457d7



