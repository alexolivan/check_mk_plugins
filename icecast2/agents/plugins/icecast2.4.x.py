#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
#!/bin/bash
# +---------------------------------------------------------------------+
# |         ___                       _   ____   _  _                   |
# |        |_ _|___ ___  ___ __ _ ___| |_|___ \ | || |  __  __          |
# |         | |/ __/ _ \/ __/ _` / __| __| __) || || |_ \ \/ /          |
# |         | | (_|  __/ (_| (_| \__ \ |_ / __/ |__   _| >  <           |
# |        |___\___\___|\___\__,_|___/\__|_____(_) |_|(_)_/\_\          | 
# |                                                                     |
# | Copyright Alejandro Olivan 2018                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor Icecast 2.4.x servers on Linux          |
# | This file contains plugin agent definition.                         |
# +---------------------------------------------------------------------+
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 


# Imports
import subprocess
import urllib2
import re

cmd = "netstat -tunlp | grep -i icecast | awk '{print $4}'"
icecasts = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
content = icecasts.stdout.readlines()

if content:
	print "<<<icecast2>>>"
	for line in content:
		dataline = str(line).replace("\n", "")
		parts = dataline.split(':')
	
                listeners = []
                def handle_listeners(match):
                        listeners.append(match)

                listener_peaks = []
                def handle_listener_peak(match):
                        listener_peaks.append(match)

		listenurls = []
		def handle_listenurl(match):
		        listenurls.append(match)

		url = "http://%s:%s/status-json.xsl" % (parts[0], parts[1])
        try:
		    response = urllib2.urlopen(url).read()
		    re.sub(r"(listeners\"\:\d+,)", handle_listeners, response)
                    re.sub(r"(listener_peak\"\:\d+,)", handle_listener_peak, response)
                    re.sub(r"(listenurl\"\:\".*?\")", handle_listenurl, response)
	    
		    if len(listenurls) > 0:
			    for index, listenurl in enumerate(listenurls):
				    mountpoint = str(listenurl.groups()).split('/')[-1].rsplit("\"")[0]
				    try:
					    listener_peak_val = str(listener_peaks[index].groups()).split(":")[1].split(",")[0]
				    except:
					    listener_peak_val = "0"			
				    try:
	                                    listeners_val = str(listeners[index].groups()).split(":")[1].split(",")[0]
	                            except:
	                                    listeners_val = "0"
				    print parts[1] + " " + listeners_val + " 1 " + listener_peak_val + " " + mountpoint
		    else:
			    print parts[1] + " 0 0 0"
        catch:
            pass
