#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |         ____           _                   ____          _          |
# |        / ___|___ _ __ | |_ _____   ____ _ / ___|__ _ ___| |_        |
# |       | |   / _ \ '_ \| __/ _ \ \ / / _` | |   / _` / __| __|       |
# |       | |__|  __/ | | | || (_) \ V / (_| | |__| (_| \__ \ |_        |
# |        \____\___|_| |_|\__\___/ \_/ \__,_|\____\__,_|___/\__|       |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor CentovaCast server panel on Linux       |
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


def perfometer_centovacast(row, check_command, perf_data):
    diskquota = int(perf_data[0][6])
    diskused = int(perf_data[0][1])
    diskusage = 0
    if not diskquota <= 0:
        diskusage = int(diskused / float(diskquota) * 100)
    quotawarn = int(perf_data[0][3])
    quotacrit = int(perf_data[0][4])
    transfermax = int(perf_data[1][6])
    transferused = int(perf_data[1][1])
    transferusage = 0
    if not transfermax <= 0:
        transferusage = int(transferused / float(transfermax) * 100)
    transferwarn = int(perf_data[1][3])
    transfercrit = int(perf_data[1][4])

    if diskusage > quotacrit:
        diskcolor = "#f00"
    elif diskusage > quotawarn:
        diskcolor = "#ff0"
    else:
        diskcolor = "#0f0"

    if transferusage > transfercrit:
        transfercolor = "#f00"
    elif transferusage > transferwarn:
        transfercolor = "#ff0"
    else:
        transfercolor = "#0f0"

    td_disk_usage = int(diskusage / 2)
    td_disk_usage_to_50 = 50 - td_disk_usage
    td_transfer_usage = int(transferusage / 2)
    td_transfer_usage_to_100 = 50 - td_transfer_usage

    return "%d%% %d%%" % (diskusage, transferusage), '<table><tr>' \
                               + perfometer_td(td_disk_usage, diskcolor) \
                               + perfometer_td(td_disk_usage_to_50, '#fff') \
                               + perfometer_td(td_transfer_usage, transfercolor) \
                               + perfometer_td(td_transfer_usage_to_100, '#fff') \
                               + '</tr></table>'


perfometers['check_mk-centovacast.resellers'] = perfometer_centovacast
perfometers['check_mk-centovacast.accounts'] = perfometer_centovacast