# NetXMS Server docker image

Docker image of NetXMS Server (www.netxms.org). Uses Microsoft ODBC Driver 17 for SQL Server. Log files are located in docker volume /data.

Run with:
```bash
docker run 
```

Environment Variables

NetXMS Server
- **NETXMS\_UNLOCKONSTARTUP** - set to 1 to unlock database on each container startup (default), set to 0 to skip database unlocking
- **NETXMS\_CONFIG** - Variable to set arbitrary config file entries to _/etc/netxmsd.conf_. Put your configuration options here.
- **NETXMS\_STARTAGENT** - Set to 1 to start the nxagent (default). Set to other value to disable agent startup.

NetXMS agent 
- **NXAGENT_CONFIG** - Config variable to set. Put your configuration options here, for example "EnableSNMPProxy=yes\nServers=server1\nMasterServers=server1". Content of this variable will will replace the agent config file.
- **NXAGENT_REGISTERSERVER** - Agent registration (put your NetXMS server hostname here)
- **NXAGENT_CONFIGSERVER** - Config server hostname
- **NXAGENT_LOGLEVEL** - log level
- **NXAGENT_PLATFORMSUFFIX** - platform suffix

ODBC DSN
- **ODBC_SQL_SERVER** - Network address to database server
- **ODBC_DB_NAME** - Database name
- **ODBC_DB_USER** - Database user
Note: password is set by adding DBPassword=pass in **NETXMS\_CONFIG**
