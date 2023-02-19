# Week 4: Analytics engineering

Goal: Transforming the data loaded in DWH to Analytical Views developing a dbt project. Slides

# Basics of analytics engineering

## What is analytics engineering?

## ETL vs ELT
## Data modeling concepts (fact and dim tables)
🎥 Video





# What is dbt? 

## dbt (data build tool) anables data analyst and engineers to transform data in their warehouses.

- dbt (data build tool) is a command line tool to transform data inside warehouses

### Setup dbt

- getdbt signup https://www.getdbt.com/signup/
- create new project, select warehouse (here we'll use BigQuery)
- configure your environment
    - upload a Service Account JSON file (that you download when setup gcloud credentials)
- click "Test Connection" >> Next

- setup repository, here I already have GitHub repository for the course so I'll use it
, select your project on GitHub repo & copy SSH
    - on cloud dbt setup page >> select "Git Clone" >> past on the git SSH key from your repo
    - click "import" and you will get a deploy key
    - go to your GitHub repo >> select settings tab 
    - under security (on the left menu bar) >> select deploy keys
    - click add deploy key and paste the deploy key provided by dbt cloud (title: dbt-connect)
    - make sure to tick on "write access" >> click Add key
    - go back to your cloud.dbt click Next
    - setup completed [Ref.](https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/week_4_analytics_engineering/dbt_cloud_setup.md)


# BigQuery and dbt

# Postgres and dbt

# dbt models

# Testing and documenting

# Deployment to the cloud and locally

# Visualizing the data with google data studio and metabase