## Week 2: Workflow Orchestration

> If you're looking for Airflow videos from the 2022 edition,
> check the [2022 cohort folder](../cohorts/2022/week_2_data_ingestion/).


### Data Lake (GCS)

* What is a Data Lake
* ELT vs. ETL
* Alternatives to components (S3/HDFS, Redshift, Snowflake etc.)
* [Video](https://www.youtube.com/watch?v=W3Zm6rjOq70&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb)
* [Slides](https://docs.google.com/presentation/d/1RkH-YhBz2apIjYZAxUz2Uks4Pt51-fVWVN9CcH9ckyY/edit?usp=sharing)


### 1. Introduction to Workflow orchestration

* What is orchestration?
* Workflow orchestrators vs. other types of orchestrators
* Core features of a workflow orchestration tool
* Different types of workflow orchestration tools that currently exist 

:movie_camera: [Video](https://www.youtube.com/watch?v=8oLs6pzHp68&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=16)


### 2. Introduction to Prefect concepts

* What is Prefect?
* Installing Prefect
* Prefect flow
* Creating an ETL
* Prefect task
* Blocks and collections
* Orion UI 

:movie_camera: [Video](https://www.youtube.com/watch?v=jAwRCyGLKOY&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=17)

### 3. ETL with GCP & Prefect

* Flow 1: Putting data to Google Cloud Storage 

:movie_camera: [Video](https://www.youtube.com/watch?v=W-rMz_2GwqQ&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=18)


### 4. From Google Cloud Storage to Big Query

* Flow 2: From GCS to BigQuery

:movie_camera: [Video](https://www.youtube.com/watch?v=Cx5jt-V5sgE&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=19)

### 5. Parametrizing Flow & Deployments 

* Parametrizing the script from your flow
* Parameter validation with Pydantic
* Creating a deployment locally
* Setting up Prefect Agent
* Running the flow
* Notifications

:movie_camera: [Video](https://www.youtube.com/watch?v=QrDxPjX10iw&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=20)

### 6. Schedules & Docker Storage with Infrastructure

* Scheduling a deployment
* Flow code storage
* Running tasks in Docker

:movie_camera: [Video](https://www.youtube.com/watch?v=psNSzqTsi-s&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=21)

### 7. Prefect Cloud and Additional Resources 


* Using Prefect Cloud instead of local Prefect
* Workspaces
* Running flows on GCP

:movie_camera: [Video](https://www.youtube.com/watch?v=gGC23ZK7lr8&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=22)

* [Prefect docs](https://docs.prefect.io/)
* [Pefect Discourse](https://discourse.prefect.io/)
* [Prefect Cloud](https://app.prefect.cloud/)
* [Prefect Slack](https://prefect-community.slack.com)

### Code repository

[Code from videos](https://github.com/discdiver/prefect-zoomcamp) (with a few minor enhancements)

### Homework 

To be linked here by Jan. 30


## Community notes

Did you take notes? You can share them here.

* Add your notes here (above this line)


### 2022 notes 

Most of these notes are about Airflow, but you might find them useful.
Most of these notes are about Airflow, but you might find them useful.

* [Notes from Alvaro Navas](https://github.com/ziritrion/dataeng-zoomcamp/blob/main/notes/2_data_ingestion.md)
* [Notes from Aaron Wright](https://github.com/ABZ-Aaron/DataEngineerZoomCamp/blob/master/week_2_data_ingestion/README.md)
* [Notes from Abd](https://itnadigital.notion.site/Week-2-Data-Ingestion-ec2d0d36c0664bc4b8be6a554b2765fd)
* [Blog post by Isaac Kargar](https://kargarisaac.github.io/blog/data%20engineering/jupyter/2022/01/25/data-engineering-w2.html)
* [Blog, notes, walkthroughs by Sandy Behrens](https://learningdataengineering540969211.wordpress.com/2022/01/30/week-2-de-zoomcamp-2-3-2-ingesting-data-to-gcp-with-airflow/)
* Add your notes here (above this line)


My notes here for Week 2 of Prefect

1. Create a virtual machine using "conda create -n zoom pythin=3.9" for working in virtual environment so that our versions of packages do not collide and crash the system, start the conda environment usinf the command "conda activate zoom". Zoom is the name of our conda virtual environment. When coming back to the same conda virtual environment, simply do the steps in Week 1 readme file and come to VS Code, do "conda activate zoom" and get started with the Prefect coursework.

2. Install the required packages using "pip install -r requirements.txt" which has prefect and all the required packages for week 2

3. Start with understanding ingest_data.py script which is the manual way of ingesting data into Postgres database. Make sure to change the host, port, usrrname and password accordingly.

4. Now we transform the ingest_data script into ETL (Extract, Transform, Load) and automate the script with prefect. We made the script in functions because each function can be used as a prefect flow (Need to syudy more about Prefect). E, T and L can be three functions and it makes the task really really easy, Alhamdulillaah

5. To turn on the Prefect UI, we need to run the command "prefect orion start" in another bash terminal after turning on the conda virtual environment.

6. Now after turning on the UI, see what port it is available on and copy the config file to set the path for Prefect.

7. Then we created a SQLAlchemy connector Block using Prefect UI which will connect to our postgres to ingest the data. Till now we successfully saw how do we ingest data to Postgres database from the virtual environment using Prefect and saw how to manage or monitor the workflow from Prefect UI. Alhamdulillaah!!! 

8. The etl_web_to_gcs.py script takes the data from DataTalkClub Github repository, converts it into Pandas Dataframe, then cleans it, and dumps it into local storage, then from local storage, the file is uploaded to GCS using the GCS Bucket block and GCS Credentials block we setup in Prefect UI.

9. The script for etl_web_to_gcs.py was changed to do the Question 1 of Home Work that's why the script is different than what was shown in the video 2.2.3

10. The etl_gcs_to_bq.py script takes the data from Google Cloud Storage and dumps it into BigQuery after doing some transformations. Basically, the etl_gcs_to_bq.py script also doing ETL. Changes were made to the code based on the local storage and Cloud Storage paths and necessary changes like project ID, database name, etc was also changed.

11. 