# The Airflow

### Good Overviews of Airflow in Production
- [Apache Airflow at Pandora](https://engineering.pandora.com/apache-airflow-at-pandora-1d7a844d68ee)
- [Using Apache Airflow to build reusable ETL on AWS Redshift](https://sonra.io/2018/01/01/using-apache-airflow-to-build-a-data-pipeline-on-aws/)
  - Inputing Connections via the GUI helps "hide" them, perhaps a better way to avoid GUI and still protect your credentials?
  - Great hands-on view of building out your own Operator (e.g. Load data from S3 to RedShift)
- [Yet Another Scalable Apache Airflow With Docker Example Setup (Very Good!)](https://medium.com/@tomaszdudek/yet-another-scalable-apache-airflow-with-docker-example-setup-84775af5c451)
- [How to use the DockerOperator in Apache Airflow](https://marclamberti.com/blog/how-to-use-dockeroperator-apache-airflow/)
- [Airflow with Maxime Beauchemin - Episode 44](https://www.podcastinit.com/episode-44-airflow-with-maxime-beauchemin/)
- [awesome-apache-airflow](https://github.com/jghoman/awesome-apache-airflow) - Curated list of resources about Apache Airflow
- [We’re All Using Airflow Wrong and How to Fix It](https://medium.com/bluecore-engineering/were-all-using-airflow-wrong-and-how-to-fix-it-a56f14cb0753)
- [Apache Airflow on Docker for Complete Beginners](https://medium.com/@itunpredictable/apache-airflow-on-docker-for-complete-beginners-cf76cf7b2c9a)
- [What we learned migrating off Cron to Airflow](https://medium.com/videoamp/what-we-learned-migrating-off-cron-to-airflow-b391841a0da4)
- [Airflow tutorial 2: Set up airflow environment with docker (YouTube)](https://www.youtube.com/watch?v=vvr_WNzEXBE) - 1 video of a series if you want to install on Google Cloud Platform [Playlist here](https://www.youtube.com/playlist?list=PLYizQ5FvN6pvIOcOd6dFZu3lQqc6zBGp2)


### Plugins
- [Airflow Plugins Github Page](https://github.com/airflow-plugins)
- [Airflow Plugins Docs](https://airflow.apache.org/plugins.html)

### An Example Airflow Project (Repo)
- [scaffold of Apache Airflow executing Docker containers](https://github.com/spaszek/airflow_project)

### DAGs
[Example-Airflow-DAGs](https://github.com/airflow-plugins/Example-Airflow-DAGs)

### Docker Airflow Image
- [puckel/docker-airflow](https://hub.docker.com/r/puckel/docker-airflow) [repo](https://github.com/puckel/docker-airflow)

### Airflow vs other Workflow Management solutions
- e.g. Oozie, Luigi, Azkaban, Cron

- [What we learned migrating off Cron to Airflow](https://medium.com/videoamp/what-we-learned-migrating-off-cron-to-airflow-b391841a0da4)



### Airflow Workers

#### LocalExector
After some time you'll likely max out the workers on that local instance and so then you would need something like the `CeleryExecutor` or `MesosExecutor`

### Data Lineage
- Where did this data come from?

- Currently, no built in direct way how objects are related, graphed together.
- Need Metadata and doing analytics on it would lead to featuring these relationships.




### Airflow Workflow

Here is how we manage it for our team.

#### DAGS
- Naming Convention: each DAG file (my_dag_v1.0.py) is also the name of the DAG(my_dag_v1.0, ...). Update the version number each time you update/change/alter that DAG. This makes it easy to go back a version as well as easily distinguish the change over a lot of runs over time.

```python
# my_dag_v1.0.py #file name
from airflow import DAG
from datetime import datetime, timedelta

default_args = {
  'owner': 'airflow',
  'depends_on_past': False,
  'start_date': datetime(2016,10,11,21,53),
  'email': ['airflow@mail.com'],
  'email_on_failure': True
}

dag = DAG(
  'my_dag_v1.0', # update the version whenver you change the DAG .py file
  default_args=default_args,
  schedule_interval="0,15,30,45 * * * *",
  dagrun_timeout=timedelta(hours=24),
  max_active_runs=1)

```

#### Process to update DAGs
- All DAG files are stored in a Git repository. Each time a merge request is merged to our master branch, the CI pipeline (Travis or Circle CI) starts a new build and packages our DAG files into a zip and the file is sent to the Airflow server.
- A potential DEV => STG => PROD testing process and user acceptance can be implemented. Or STG => PROD. This should be automated and could be integrated with a chat service hook like Slack.
