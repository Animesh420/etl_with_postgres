# ETL pipeline using postgres DB

* [Problem setup](#problem-setup)
* [Understanding the problem](#understanding-the-problem)
* [Designing the Solution](#solutoin-design)
* [Final Solution Walkthrough](#final-solution-walkthrough)
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

### DB Setup on personal system
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
* For this project we have to build a pipeline using postgres (on Udacity or on local machine)
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
