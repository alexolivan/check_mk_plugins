#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
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
# | This file contains plugin perfometer definition.                    |
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


def perfometer_icecast2(row, check_command, perf_data):
    current = int(perf_data[0][1])
    peak = int(perf_data[1][1])
    status = int(perf_data[2][1])
    maxim = int(perf_data[0][6])
    peak_warn = int(perf_data[1][3])
    peak_crit = int(perf_data[1][4])


    if row["service_state"] == 0:
        color = {0: "#0f0", 1: "#6f8"}
    elif row["service_state"] == 1:
        color = {0: "#ff0", 1: "#ff2"}
    elif row["service_state"] == 2:
        color = {0: "#f00", 1: "#f22"}
    else:
        color = {0: "#fa0", 1: "#fa2"}

    if peak_warn != 0 or peak_crit != 0:
        if peak > int(perf_data[1][4]):
    	    color[3] = "#f00"
        elif peak > int(perf_data[1][3]):
    	    color[3] = "#ff0"
        else:
    	    color[3] = "#0f0"
    else:
    	color[3] = "#0f0"

    usage = int(current / float(maxim) * 100)
    cur_to_peak = int((peak - usage) / float(maxim) * 100) - 1
    peak_to_max = int((maxim - peak) / float(maxim) * 100)

    return "%d%%" % usage, '<table><tr>' \
                               + perfometer_td(usage, color[0]) \
                               + perfometer_td(cur_to_peak, '#fff') \
                               + perfometer_td(2, color[3]) \
                               + perfometer_td(peak_to_max, '#fff') \
                               + '</tr></table>'

perfometers['check_mk-icecast2'] = perfometer_icecast2