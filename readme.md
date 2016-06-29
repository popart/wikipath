Requirements:
  12G disk space (for db, raw text inputs, & intermediate files)
get data files:
  * pages: http://search-archives.s3.amazonaws.com/interview/pages.txt
  * links: http://search-archives.s3.amazonaws.com/interview/links.txt

  put them in the data/raw folder

get docker env:
  * docker pull popart/docker-moat

run docker w/ ports exposed & mounted git repo, neo4j data folder:
  (use scripts/run_docker)

inside container:
  * start neo4j
  * /home/neo4j/bin/neo4j start

from host (first time startup):
  * login to neo4j shell at <container_ip>:7474
  * set a new password

transform & import the data into neo4j:
  * convert txt to csv files using scripts/transform_data.py
  * upload into neo4j using scripts/import_data.py
  * create db index w/ `python scripts/setup_db.py`
    * first you need to edit this file and add db auth info

configure the webapp
  copy project/config/env.py.example to env.py
  update db parameters (probably just the password)

run the webapp
  `./run_webapp`
