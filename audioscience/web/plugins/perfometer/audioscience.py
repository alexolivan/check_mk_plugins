#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |        _             _ _      ____       _                          |
# |       / \  _   _  __| (_) ___/ ___|  ___(_) ___ _ __   ___ ___      |
# |      / _ \| | | |/ _` | |/ _ \___ \ / __| |/ _ \ '_ \ / __/ _ \     |
# |     / ___ \ |_| | (_| | | (_) |__) | (__| |  __/ | | | (_|  __/     |
# |    /_/   \_\__,_|\__,_|_|\___/____/ \___|_|\___|_| |_|\___\___|     |
# |                                                                     |
# | Copyright Alejandro Olivan 2018                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor AudioScience cards on Debian systems    |
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


def perfometer_audioscience_info(row, check_command, perf_data):
    return '', ''


def perfometer_audioscience_dspload(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d%%" % value, perfometer_linear(value, color)


def perfometer_audioscience_temperature(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = float(perf_data[0][1])
    return "%.0f%ºC" % value, perfometer_linear(value, color)


perfometers["check_mk-audioscience.info"] = perfometer_audioscience_info
perfometers["check_mk-audioscience.temperature"] = perfometer_audioscience_temperature
perfometers["check_mk-audioscience.dspload"] = perfometer_audioscience_dspload
