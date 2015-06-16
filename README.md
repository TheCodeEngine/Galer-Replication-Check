# Server-Compose

![Travis-CI Build Status](https://travis-ci.org/TheCodeEngine/Galer-Replication-Check.svg?branch=develop "Travis-CI")
[![Code Climate](https://codeclimate.com/github/TheCodeEngine/Galer-Replication-Check/badges/gpa.svg)](https://codeclimate.com/github/TheCodeEngine/Galer-Replication-Check)

Ochestra and Administration tool. Install the python runtime to run the tool.

```sh
$ apt-get install python-mysqldb python-pip
```


## Galera Cluster

Check the status of the galera cluster

```sh
$ ./server-compose check -h ip1 -h ip2 -h ip3
```