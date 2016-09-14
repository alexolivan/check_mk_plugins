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

def perfometer_wowza(row, check_command, perf_data):
    current = int(perf_data[0][1])   
    maxim = int(perf_data[0][6])
    peak_warn = int(perf_data[0][3])
    peak_crit = int(perf_data[0][4])


    if row["service_state"] == 0:
        color = "#0f0"
    elif row["service_state"] == 1:
        color = "#ff0"
    elif row["service_state"] == 2:
        color = "#f00"
    else:
        color = "#fa0"

    usage = int(current / float(maxim) * 100)
    usage_to_max = int((maxim - usage) / float(maxim) * 100)

    return "%d%%" % usage, '<table><tr>' \
                               + perfometer_td(usage, color) \
                               + perfometer_td(usage_to_max, '#fff') \
                               + '</tr></table>'

perfometers['check_mk-wowza'] = perfometer_wowza