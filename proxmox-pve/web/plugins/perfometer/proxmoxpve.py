#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |     ____  ____   _____  ____  __  _____  __                         |
# |    |  _ \|  _ \ / _ \ \/ /  \/  |/ _ \ \/ /     _ ____   _____      |
# |    | |_) | |_) | | | \  /| |\/| | | | \  /_____| '_ \ \ / / _ \     |
# |    |  __/|  _ <| |_| /  \| |  | | |_| /  \_____| |_) \ V /  __/     |
# |    |_|   |_| \_\\___/_/\_\_|  |_|\___/_/\_\    | .__/ \_/ \___|     |
# |                                                |_|                  |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor PROXMOX PVE Hypervisor systems          |
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


def perfometer_proxmoxpve_pveversion(row, check_command, perf_data):
    return '', ''


def perfometer_proxmoxpve_clusterinfo(row, check_command, perf_data):
    return '', ''


def perfometer_proxmoxpve_clusterstatus(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


def perfometer_proxmoxpve_localstatus(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


perfometers["check_mk-proxmoxpve.pveversion"] = perfometer_proxmoxpve_pveversion
perfometers["check_mk-proxmoxpve.clusterinfo"] = perfometer_proxmoxpve_clusterinfo
perfometers["check_mk-proxmoxpve.clusterstatus"] = perfometer_proxmoxpve_clusterstatus
perfometers["check_mk-proxmoxpve.localstatus"] = perfometer_proxmoxpve_localstatus   