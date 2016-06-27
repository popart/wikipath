FROM pritunl/archlinux

ENV NEO4J_VERSION 3.0.3
ENV NEO4J_URI http://dist.neo4j.org/neo4j-community-${NEO4J_VERSION}-unix.tar.gz

RUN pacman -S --noconfirm python3
RUN pacman -S --noconfirm python-pip
RUN pacman -S --noconfirm jdk8-openjdk
RUN pacman -S --noconfirm vim

RUN curl --fail --silent --show-error --location --output /tmp/neo4j.tar.gz $NEO4J_URI \
  && tar --extract --file /tmp/neo4j.tar.gz \
  && rm /tmp/neo4j.tar.gz
RUN mv neo4j-community-$NEO4J_VERSION /home/neo4j
RUN pip install neo4j-driver
RUN pip install falcon
RUN pip install gunicorn

EXPOSE 7474 7473 7687 8000

COPY neo4j.conf /home/neo4j/conf/neo4j.conf
