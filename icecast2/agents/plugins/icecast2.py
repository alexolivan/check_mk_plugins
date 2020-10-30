#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |       ___                       _   ____    _____                   |
# |      |_ _|___ ___  ___ __ _ ___| |_|___ \  |___ / __  __            |
# |       | |/ __/ _ \/ __/ _` / __| __| __) |   |_ \ \ \/ /            |
# |       | | (_|  __/ (_| (_| \__ \ |_ / __/ _ ___) | >  <             |
# |      |___\___\___|\___\__,_|___/\__|_____(_)____(_)_/\_\            |
# |                                                                     |
# |                                                                     |
# | Copyright Alejandro Olivan 2017                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor Icecast 2.3.x servers on Linux          |
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
# MA  02110-1301, USA.

import urllib2
import base64
import os

customers = (
    {'host': '127.0.0.1', 'port': '8000', 'mountpoint':'myradio.mp3', 'adminuser': 'admin', 'adminpass': 'verysecret1'},
    {'host': '127.0.0.1', 'port': '8000', 'mountpoint':'myradio.aac', 'adminuser': 'admin', 'adminpass': 'verysecret1'},
    {'host': '127.0.0.1', 'port': '8002', 'mountpoint':'transport.mp3', 'adminuser': 'admin', 'adminpass': 'verysecret2'},
	)

results = []
filelist = []


def downloadStatsfiles():
    for d in customers:
        url = "http://%s:%s/admin/stats?mount=/%s" % (d['host'], d['port'], d['mountpoint'])
        filename = "/tmp/icecast-%s-%s-%s" % (d['host'], d['port'], d['mountpoint'])
        request = urllib2.Request(url)
        base64string = base64.encodestring('%s:%s' % (d['adminuser'], d['adminpass'])).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        try:
            s = urllib2.urlopen(request)
            contents = s.read()
            file = open(filename, 'w')
            file.write(contents)
            file.close()
            filelist.append({'port': d['port'], 'filename': filename, 'mountpoint': d['mountpoint']})
        except:
            pass


def parseStatFile(port, file, mountpoint):
    from xml.dom import minidom
    xmldoc = minidom.parse(file)
    totalsources = xmldoc.getElementsByTagName('sources')[0].firstChild.nodeValue
    if totalsources > 0:
    	status = 1
        for source in xmldoc.getElementsByTagName('source'):
            if source.hasAttribute('mount') and source.getAttribute('mount') == "/%s" % mountpoint:
                listenersElement = source.getElementsByTagName('listeners')
                listeners = listenersElement[0].firstChild.nodeValue
                peakListenerElement = source.getElementsByTagName('listener_peak')
                listenerPeak = peakListenerElement[0].firstChild.nodeValue
            else:
                listeners = 0
                listenerPeak = 0
    else:
    	status = 0
        listeners = 0
        listenerPeak = 0
    results.append((port, listeners, status, listenerPeak, mountpoint))


def parseStatFiles():
    for file in filelist:
    	parseStatFile(file['port'], file['filename'], file['mountpoint'])


def printResults():
    print('<<<icecast2>>>')
    for result in results:
        resultstr = ""
        for item in result:
            resultstr+=str(item) + " "
        print(resultstr)


def deleteUsedFiles():
	for file in filelist:
		os.remove(file['filename'])


def mainFunction():
    downloadStatsfiles()
    parseStatFiles()
    printResults()
    deleteUsedFiles()


mainFunction()
