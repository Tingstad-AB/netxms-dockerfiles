# Dockerfile for building NetXMS server image

FROM debian:buster-slim
LABEL org.opencontainers.image.authors="marcus.halmsjo@tingstad.se"
ENV MAJOR_VERSION=4.2 MINOR_VERSION=395

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections \
    echo msodbcsql17 msodbcsql/ACCEPT_EULA boolean true | debconf-set-selections \
    curl -sL http://packages.netxms.org/netxms.gpg | apt-key add - \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    echo "deb http://packages.netxms.org/debian/ buster main" > /etc/apt/sources.list.d/netxms.list \
    apt-get update && apt-get install -y \
    curl \
    apt-transport-https \
    gnupg \
    tzdata \
    netxms-base="${MAJOR_VERSION}.${MINOR_VERSION}-1" \
    netxms-server="${MAJOR_VERSION}.${MINOR_VERSION}-1" \
    netxms-agent="${MAJOR_VERSION}.${MINOR_VERSION}-1" \
    netxms-dbdrv-odbc="${MAJOR_VERSION}.${MINOR_VERSION}-1" \
    supervisor \
    msodbcsql17 \
    libgssapi-krb5-2 \
    apt-get clean

VOLUME /data

EXPOSE 4701

ENV NETXMS_UNLOCKONSTARTUP=1 NETXMS_STARTAGENT=1 NXAGENT_REGISTERSERVER=127.0.0.1 TZ="Europe/Stockholm"

COPY ./docker-entrypoint.sh ./nxagent.sh /

RUN  chmod 755 /docker-entrypoint.sh /nxagent.sh

CMD ["/docker-entrypoint.sh"]
