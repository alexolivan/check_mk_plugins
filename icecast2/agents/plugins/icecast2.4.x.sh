#!/bin/bash
# +---------------------------------------------------------------------+
# |         ___                       _   ____   _  _                   |
# |        |_ _|___ ___  ___ __ _ ___| |_|___ \ | || |  __  __          |
# |         | |/ __/ _ \/ __/ _` / __| __| __) || || |_ \ \/ /          |
# |         | | (_|  __/ (_| (_| \__ \ |_ / __/ |__   _| >  <           |
# |        |___\___\___|\___\__,_|___/\__|_____(_) |_|(_)_/\_\          | 
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
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
# MA  02110-1301, USA.

#Environment
STARTPORT=6000
ENDPORT=10000

function jsonval {
    temp=`echo $RESULT | sed 's/\\\\\//\//g' | 
sed 's/[{}]//g' | awk -v k="text" '{n=split($0,a,","); for (i=1; i<=n; i++) print a[i]}' | 
sed 's/\"\:\"/\|/g' | sed 's/[\,]/ /g' | sed 's/\"//g' | grep -w $TARGETPROP | cut -d ":" -f 2`
    echo ${temp##*|}
}

CANDIDATEPORTS=()
POSSIBLEPORTS=`netstat -tnl | awk '{print $4}' | grep ':' | cut -d ":" -f 2 | sort | uniq`
while read line ; do
    if [ ${line:-0} -ge $STARTPORT ] && [ ${line:-0} -le $ENDPORT ] && [ ${line:-0} -ne 6556 ]; then
        CANDIDATEPORTS+=($line)
    fi
done <<<"$POSSIBLEPORTS"

echo "<<<icecast2>>>"

for PORT in "${CANDIDATEPORTS[@]}"
do
    LISTENIP=`netstat -tnl | grep ${PORT} | awk '{print $4}' | cut -d ":" -f 1`
    if [ $LISTENIP == "0.0.0.0" ]; then
        LISTENIP="127.0.0.1"
    fi
    RESULT=`curl http://${LISTENIP}:${PORT}/status-json.xsl -A Mozilla/4.0 -s -I | grep Icecast`
    if [[ ! $(tr -d "\r\n" <<< $RESULT | wc -c) -eq 0 ]]; then
        RESULT=`curl http://${LISTENIP}:${PORT}/status-json.xsl -A Mozilla/4.0 -s`
        TARGETPROP='listener_peak'
        STREAMSTATUS=`jsonval`
        if [ -z "${STREAMSTATUS}" ]; then
            STREAMSTATUS=0
            CURRENTLISTENERS=0
            PEAKLISTENERS=0
        else
            STREAMSTATUS=1
            TARGETPROP='listeners'
            CURRENTLISTENERS=`jsonval`
            TARGETPROP='listener_peak'
            PEAKLISTENERS=`jsonval`
        fi
        RESULT="${CURRENTLISTENERS} ${STREAMSTATUS} ${PEAKLISTENERS}"
        if [ $(wc -w <<< $RESULT) -eq 3 ]; then
            echo "${PORT} ${RESULT}"
        fi
    fi
done


