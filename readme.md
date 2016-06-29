# Wikipedia Shortest Path Search, using Neo4j & Python Falcon
This project provides sample code for querying a Neo4j database of 5.7 million nodes and 130 million relationships, accessing the database with an API built with Python Falcon, using the Python neo4j-driver. It also demonstrates use of the neo4j-import tool, and writing jQuery ajax requests to autopopulate a form field and display results.

## Requirements
  * 12G disk space (for db, raw text inputs, & intermediate files)
  * Docker

## Get data files:
  * pages: http://search-archives.s3.amazonaws.com/interview/pages.txt
  * links: http://search-archives.s3.amazonaws.com/interview/links.txt
  * put them in the `data/raw` folder

## Get docker env:
  * `docker pull popart/docker-moat`

## Run docker w/ ports exposed and mounts to this repo
  * `scripts/run_docker`

## Inside the docker container:
  * start neo4j with `/home/neo4j/bin/neo4j start`

## From host (first time startup ONLY):
  * login to neo4j shell at <container_ip>:7474
  * set a new password

## Transform & import the data into neo4j:
  * convert txt to csv files using `python scripts/transform_data.py`
  * upload into neo4j using `python scripts/import_data.py`
  * create db indexes w/ `python scripts/setup_db.py`
    * (first you need to edit this file and add db auth info)

## Configure the webapp
  * copy project/config/env.py.example to env.py
  * update db parameters (probably just the password)

## run the webapp
  `./run_webapp`
