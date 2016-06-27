get data files:
  * pages: http://search-archives.s3.amazonaws.com/interview/pages.txt
  * links: http://search-archives.s3.amazonaws.com/interview/links.txt

  put them in the raw_data folder

get docker env:
  * docker pull popart/docker-moat

run docker w/ ports exposed & mounted git repo, neo4j data folder:
  (see scripts/run_docker)

inside container:
  * start neo4j
from host:
  * login to neo4j shell at <container_ip>:7474
  * set a new password

transform the data:
  * convert txt to csv files using scripts/transform_data.py
  * upload into neo4j using scripts/import_data.py

configure the webapp
  copy project/config/env.py.example to env.py
  update db parameters

run the webapp
  see run_webapp


