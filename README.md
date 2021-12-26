# ETL pipeline using postgres DB

* [Problem setup](#problem-setup)
* [Understanding the problem](#understanding-the-problem)
* [Designing the Solution](#solutoin-design)
* [Final Solution Walkthrough](#final-solution-walkthrough)
* [Common bugs and troubleshooting](#common-bugs)


## Problem Setup

**Installing docker**
* [Docker Installation for all platforms](https://docs.docker.com/get-docker/)

**Installing Pycharm and Anaconda**
* [Pycharm Community Edition](https://www.jetbrains.com/pycharm/download/)
* [Anaconda Installation](https://docs.anaconda.com/anaconda/install/)

**Project specific setup using Anaconda and Pycharm**
* Clone this repository, watch [tutorial](https://blog.jetbrains.com/idea/2020/10/clone-a-project-from-github/)
* [Recommended Anaconda setup](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html)
* [Anaconda setup with Pycharm for a project](https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/)
* Project specific recommendations:
  * Create a new conda environment with Python 3.6
  * Install all the python packages using `pip install -r requirements.txt`

**[OPTIONAL] Jupyter setup**
* Jupyter support is currently absent from pycharm community edition
* If you want to still have support for jupyter, [refer](https://stackoverflow.com/questions/55788675/-2019-1-ce-no-option-to-create-edit-jupyter-notebook-ipynb-files)

## Understanding the problem
* [What is an ETL (Extract Transform Load) pipeline ?](https://www.snowflake.com/guides/etl-pipeline)
* For this project we have to build a pipeline using postgres (on Udacity or on local machine)
* This pipeline focuses on two types of data
  * Song data: 
    * Located under /data/song_data
    * Data is stored as json and is used to create two dimension tables (Songs and Artists)
  * Log data:
    * Located under /data/log_data
    * Data is stored as "per line json" and is used to create two dimension tables (User and Time)
    * It also creates one fact table (Songplays)
* [What are Fact and Dimension Tables ?](https://docs.microsoft.com/en-us/power-bi/guidance/star-schema)
* The problem requires one to create an ETL workflow for both song and log data to populate dimension table
* Once all the dimension tables are populated, log data information is used to coherently build the fact table
