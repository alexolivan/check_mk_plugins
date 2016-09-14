#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |       __        __                          ____  _____             |
# |       \ \      / /____      ________ _     / ___|| ____|            |
# |        \ \ /\ / / _ \ \ /\ / /_  / _` |____\___ \|  _|              |
# |         \ V  V / (_) \ V  V / / / (_| |_____|__) | |___             |
# |          \_/\_/ \___/ \_/\_/ /___\__,_|    |____/|_____|            |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor Wowza Stream Engine servers on Linux    |
# | This file contains XML auxiliary parsisng python script.            |
# +---------------------------------------------------------------------+

from xml.dom.minidom import parse
import xml.dom.minidom
import sys

serverinfo = str(sys.argv[1])

DOMTree = xml.dom.minidom.parse(serverinfo)
collection = DOMTree.documentElement

vhosts = collection.getElementsByTagName("VHost")
for vhost in vhosts:
    name = vhost.getElementsByTagName("Name")[0].childNodes[0].data
    conn_limit = vhost.getElementsByTagName("ConnectionsLimit")[0].childNodes[0].data
    conn_current = vhost.getElementsByTagName("ConnectionsCurrent")[0].childNodes[0].data
    conn_total = vhost.getElementsByTagName("ConnectionsTotal")[0].childNodes[0].data
    conn_total_accepted = vhost.getElementsByTagName("ConnectionsTotalAccepted")[0].childNodes[0].data
    conn_total_rejected = vhost.getElementsByTagName("ConnectionsTotalRejected")[0].childNodes[0].data
    print "%s %s %s %s %s %s" % (name, conn_limit, conn_current, conn_total, conn_total_accepted, conn_total_rejected)