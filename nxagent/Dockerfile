# Dockerfile for building NetXMS server image

FROM debian:buster
MAINTAINER Matt Beckett <matt@beckett.cloud>

ENV NETXMS_VERSION_AGENT=3.8.267-1
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get -y install curl apt-transport-https && \
    curl -sL http://packages.netxms.org/netxms.gpg | apt-key add - && \
    echo "deb http://packages.netxms.org/debian/ buster main" > /etc/apt/sources.list.d/netxms.list && \
    apt-get update && apt-get -y install netxms-agent=$NETXMS_VERSION_AGENT && apt-get clean

COPY ./docker-entrypoint.sh /

RUN  chmod 755 /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
