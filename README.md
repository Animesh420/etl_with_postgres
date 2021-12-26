# ETL pipeline using postgres DB

* [Problem setup](#problem-setup)
* [Understanding the problem](#understanding-the-problem)
* [Solution Walkthrough](#solution-walkthrough)
* [Common bugs and troubleshooting](#common-bugs)


## Problem Setup

### Installing docker
* [Docker overview](https://docs.docker.com/get-started/overview/)
* [Docker compose overview](https://docs.docker.com/compose/)
* [Docker Installation for all platforms](https://docs.docker.com/get-docker/)
* [Quickstart with Docker](https://docs.docker.com/get-started/)

### Installing Pycharm and Anaconda
* [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/)
* [Anaconda Installation](https://docs.anaconda.com/anaconda/install/)

### Project specific setup using Anaconda and Pycharm
* Clone this repository, watch [tutorial](https://blog.jetbrains.com/idea/2020/10/clone-a-project-from-github/)
* [Recommended Anaconda setup](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
* [Anaconda setup with Pycharm for a project](https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/)
* Project specific recommendations:
  * Create a new conda environment with Python 3.6
  * Install all the python packages using `pip install -r requirements.txt`

### DB Setup on local system
* If you are not using udacity environment to do the assignment and instead want to setup a local working environment then
  * Make sure you can run `docker` and `docker-compose` from your command line (cmd in Windows and bash in Ubuntu/Mac)
  * Best way to ensure this is using docker desktop (installation links [above](#installing-docker))
  * Make sure you understand basics of docker-compose ([refer](#installing-docker))
  * Once installed, navigate to **docker_python_setup** directory and run `docker-compose up`
  * This will fetch the postgres image and map port 5432 into host (your local computer) to the container port 5432
  * We use env_file variable to pass postgres connection information, there are tutorials which pass these in other forms like **environment** section etc
  but this is the most concise way that worked for me. For more [information](https://hub.docker.com/_/postgres)
  * Our initial configuration to postgres is what is used inside create_tables to connect to postgres and then create a new DB sparkify
  * **IMPORTANT**, in the docker-compose.yaml, under volumes one needs to specify a path map
    * **PATH ON LOCAL SYSTEM** : /var/lib/postgresql/data
    * If you have to restart the container for any reason, make sure that this **PATH ON LOCAL SYSTEM** is empty
    otherwise a booting postgres container does not take configuration from database.env correctly
  * With this setup you have the ability to run all the files locally and your local environment setup is complete


### [OPTIONAL] Jupyter setup
* Jupyter support is currently absent from pycharm community edition
* If you want to still have support for jupyter, [refer](https://stackoverflow.com/questions/55788675/-2019-1-ce-no-option-to-create-edit-jupyter-notebook-ipynb-files)

## Understanding the problem
* [What is an ETL (Extract Transform Load) pipeline ?](https://www.snowflake.com/guides/etl-pipeline)
* Official problem statment
  * A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

  * They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.


* This pipeline focuses on two types of data
  * Song data: 
    * Located under /data/song_data
    * Data is stored as json and is used to create two **dimension tables** (Songs and Artists)
  * Log data:
    * Located under /data/log_data
    * Data is stored as "per line json" and is used to create two dimension tables (User and Time)
    * It also creates one **fact table** (Songplays)
* [What are Fact and Dimension Tables ?](https://docs.microsoft.com/en-us/power-bi/guidance/star-schema)
* The problem requires one to create an ETL workflow for both song and log data to populate dimension table
* Once all the dimension tables are populated, log data information is used to coherently build the fact table


## Solution Walkthrough

### Input files
  - create_tables.py: Used to drop database tables and recreate them
  - sql_queries.py: Used to write CRUD queries for postgres database
  - etl.py: Used to run the pipeline
  - etl.ipynb: Used to run small snippets of ETL as a precursor to etl.py
  - test.ipynb: Used to unit test database table changes

### Key points in solution
  * One needs to **make sure to correctly populate create table and delete table statements** in the sql_queries.py
file
  * These CRUD statements are used in the create_tables.py file to create and drop tables in database
  * Once the sql_queries file is correctly created (with right data type and key constraints for each column)
  check by running the create_tables.py file if the creation and deletion of tables/database works perfectly.
  * Once the create_tables.py is operational move to etl.ipynb and implement the etl steps one by one
  * Helpful pandas link:
    * Following links help one to get started with pandas code in the repository, but for more information use stackoverflow
    * [User guid pandas](https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.DataFrame.html)
    * [10 minutes pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
    * [What is loc in pandas](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html?highlight=loc#pandas.DataFrame.loc)
    * [Guide to selecting data by index and columns](https://pandas.pydata.org/pandas-docs/version/0.23.3/indexing.html)
    * [reading json with pandas](https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.read_json.html)
    * [renaming columns in pandas](https://pandas.pydata.org/pandas-docs/version/0.23.3/generated/pandas.DataFrame.rename.html)
  * Based on schema of input data files, use pandas to generate insertable data for SQL tables

