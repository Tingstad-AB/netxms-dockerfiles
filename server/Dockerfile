# Dockerfile for building NetXMS server image

FROM debian:buster-slim
MAINTAINER Matt Beckett <matt@beckett.cloud>
ENV MAJOR_VERSION=3.8 MINOR_VERSION=314

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get -y install curl apt-transport-https gnupg && \
    curl -sL http://packages.netxms.org/netxms.gpg | apt-key add - && \
    echo "deb http://packages.netxms.org/debian/ buster main" > /etc/apt/sources.list.d/netxms.list && \
    apt-get update && apt-get -y install netxms-server="${MAJOR_VERSION}.${MINOR_VERSION}-1" netxms-agent="${MAJOR_VERSION}.${MINOR_VERSION}-1" netxms-dbdrv-sqlite3=$NETXMS_VERSION_SERVER supervisor && apt-get clean

VOLUME /data

EXPOSE 4701

ENV NETXMS_UNLOCKONSTARTUP=1 NETXMS_STARTAGENT=1 NXAGENT_REGISTERSERVER=127.0.0.1

COPY ./docker-entrypoint.sh ./nxagent.sh /

RUN  chmod 755 /docker-entrypoint.sh /nxagent.sh

CMD ["/docker-entrypoint.sh"]
