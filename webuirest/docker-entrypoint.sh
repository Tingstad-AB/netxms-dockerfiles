#!/bin/sh

echo "server=$NETXMS_SERVER\nsessionTimeout=$NETXMS_SESSIONTIMEOUT\nenableAdvancedSettings=$NETXMS_ENABLEADVANCEDSETTINGS" >/usr/local/tomcat/lib/nxmc.properties
echo "netxms.server.address=$NETXMS_SERVER\nnetxms.server.port=$NETXMS_PORT" >/usr/local/tomcat/lib/nxapisrv.properties

catalina.sh run
