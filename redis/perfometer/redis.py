#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |                    _ _                                              |
# |       _ __ ___  __| (_)___       ___  ___ _ ____   _____ _ __       |
# |      | '__/ _ \/ _` | / __|_____/ __|/ _ \ '__\ \ / / _ \ '__|      |
# |      | | |  __/ (_| | \__ \_____\__ \  __/ |   \ V /  __/ |         |
# |      |_|  \___|\__,_|_|___/     |___/\___|_|    \_/ \___|_|         |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor redis-server on Debian systems          |
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

def perfometer_redis_info(row, check_command, perf_data):
    return '', ''


def perfometer_redis_status(row, check_command, perf_data):
    return '', ''


def perfometer_redis_process(row, check_command, perf_data):
    return '', ''


def perfometer_redis_cpu(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    if perf_data[0][0] == "lru_clock":
        value = int(perf_data[0][1])
        return "%d" % value, perfometer_logarithmic(value, 100, 5, color)
    else:
        value = float(perf_data[0][1])
        return "%.0f%%" % value, perfometer_linear(value, color)


def perfometer_redis_memory(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    if perf_data[0][0] == "mem_fragmentation_ratio":
        value = float(perf_data[0][1])
        return "%.0f%%" % value, perfometer_linear(value, color)
    else:
        value = int(perf_data[0][1])
        return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


def perfometer_redis_connections(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


def perfometer_redis_keys(row, check_command, perf_data):
    color = {0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2"}[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


perfometers["check_mk-redis.info"] = perfometer_redis_info
perfometers["check_mk-redis.status"] = perfometer_redis_status
perfometers["check_mk-redis.process"] = perfometer_redis_process
perfometers["check_mk-redis.cpu"] = perfometer_redis_cpu
perfometers["check_mk-redis.memory"] = perfometer_redis_memory
perfometers["check_mk-redis.connections"] = perfometer_redis_connections
perfometers["check_mk-redis.keys"] = perfometer_redis_keys