get data files:
  * pages: http://search-archives.s3.amazonaws.com/interview/pages.txt
  * links: http://search-archives.s3.amazonaws.com/interview/links.txt

get docker env:
  * docker pull popart/docker-moat

run docker w/ ports exposed & mounted git repo:
  * docker run -it -P -v /home/<user>/wikipath:/home/wikipath docker-moat /bin/bash

inside container:
  * edit neo4j conf files to accept non-local connections
  * start neo4j and set a new password by logging into web portal from host

transfrom the data:
  * run scripts/transform_data.py to convert to csv files
  * upload into neo4j


