# NetXMS WebUI with REST API Docker image

Docker image of NetXMS Web UI and REST API (www.netxms.org).


Run with:
```bash
docker run -ti -e NETXMS_SERVER=<NETXMS_SERVER_HOSTNAME> --rm registry.gitlab.com/matthew-beckett/netxms-dockerfiles/webuirest:3-8-382
```

Environment Variables
* NETXMS\_SERVER\_HOSTNAME - NetXMS Server hostname or IP address

After startup web ui is accessible at:

* `http://\<container\_ip\>:8080/nxmc`
