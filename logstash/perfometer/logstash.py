#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |               _                 _            _                      |
# |              | | ___   __ _ ___| |_ __ _ ___| |__                   |
# |              | |/ _ \ / _` / __| __/ _` / __| '_ \                  |
# |              | | (_) | (_| \__ \ || (_| \__ \ | | |                 |
# |              |_|\___/ \__, |___/\__\__,_|___/_| |_|                 |
# |                       |___/                                         |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk plugin to monitor logstash 1.5 on Debian systems         |
# | This file contains the check definition / inventory code.           |
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


def perfometer_logstash_processes(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    if perf_data[0][0] == "total_processes":
        value = int(perf_data[0][1])
        return "%d" % value, perfometer_logarithmic(value, 100, 5, color)
    else:
        return '', ''


def perfometer_logstash_redis(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


def perfometer_logstash_memory(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]

    if perf_data[0][0] == "memory_usage":
        value = float(perf_data[0][1])
        return "%.0f%%" % value, perfometer_linear(value, color)
    else:
        value = int(perf_data[0][1])
        return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


def perfometer_logstash_cpu(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    if perf_data[0][0] == "cpu_usage":
        value = float(perf_data[0][1])
        return "%.0f%%" % value, perfometer_linear(value, color)
    else:
        return '', ''


perfometers['check_mk-logstash.processes'] = perfometer_logstash_processes
perfometers['check_mk-logstash.redis'] = perfometer_logstash_redis
perfometers['check_mk-logstash.memory'] = perfometer_logstash_memory
perfometers['check_mk-logstash.cpu'] = perfometer_logstash_cpu
