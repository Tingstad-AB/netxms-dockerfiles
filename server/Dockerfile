# Dockerfile for building NetXMS server image

FROM debian:buster-slim
LABEL org.opencontainers.image.authors="marcus.halmsjo@tingstad.se"
ENV MAJOR_VERSION=4.2 MINOR_VERSION=2

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
    apt-get update && apt-get -y install curl apt-transport-https gnupg tzdata && \
    curl -sL http://packages.netxms.org/netxms.gpg | apt-key add - && \
    echo "deb http://packages.netxms.org/debian/ buster main" > /etc/apt/sources.list.d/netxms.list && \
    apt-get update && apt-get -y install netxms-base="${MAJOR_VERSION}.${MINOR_VERSION}" netxms-server="${MAJOR_VERSION}.${MINOR_VERSION}" netxms-agent="${MAJOR_VERSION}.${MINOR_VERSION}" netxms-dbdrv-odbc="${MAJOR_VERSION}.${MINOR_VERSION}" supervisor && apt-get clean

# Microsoft ODBC Driver and Kerberos
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections && \
	curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
	curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
	echo msodbcsql17 msodbcsql/ACCEPT_EULA boolean true | debconf-set-selections && \
	apt-get update && apt-get -y install msodbcsql18 libgssapi-krb5-2

VOLUME /data

EXPOSE 4701

ENV NETXMS_UNLOCKONSTARTUP=1 NETXMS_STARTAGENT=1 NXAGENT_REGISTERSERVER=127.0.0.1 TZ="Europe/Stockholm"

COPY ./docker-entrypoint.sh ./nxagent.sh /

RUN  chmod 755 /docker-entrypoint.sh /nxagent.sh

CMD ["/docker-entrypoint.sh"]
