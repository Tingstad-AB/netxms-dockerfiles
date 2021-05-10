# Dockerfile for building NetXMS webui

FROM tomcat:10.0.5-jdk15-openjdk-buster
MAINTAINER Matt Beckett <matt@beckett.cloud>

ENV VERSION=3.8.314-1 NETXMS_SERVER=127.0.0.1 NETXMS_SESSIONTIMEOUT=120 NETXMS_ENABLEADVANCEDSETTINGS=true

COPY ./docker-entrypoint.sh /

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get -y install curl apt-transport-https && \
    curl -L http://www.netxms.org/download/webui/nxmc-${VERSION}.war -o /usr/local/tomcat/webapps/nxmc.war && \
    chmod 755 /docker-entrypoint.sh

ENTRYPOINT [ "/docker-entrypoint.sh" ]
