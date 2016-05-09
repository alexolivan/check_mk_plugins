#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |          _           _   _                              _           |
# |      ___| | __ _ ___| |_(_) ___ ___  ___  __ _ _ __ ___| |__        |
# |     / _ \ |/ _` / __| __| |/ __/ __|/ _ \/ _` | '__/ __| '_ \       |
# |    |  __/ | (_| \__ \ |_| | (__\__ \  __/ (_| | | | (__| | | |      |
# |     \___|_|\__,_|___/\__|_|\___|___/\___|\__,_|_|  \___|_| |_|      |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk plugin to monitor elasticsearch 1.5 on Debian systems    |
# | This file contains plugin perfometer definition  .                  |
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

def perfometer_elasticsearch_cluster_name(row, check_command, perf_data):
    return '', ''

def perfometer_elasticsearch_status(row, check_command, perf_data):
    return '', ''

def perfometer_elasticsearch_nodes(row, check_command, perf_data):
    color = { 0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)

def perfometer_elasticsearch_shards(row, check_command, perf_data):
    color = { 0: "#6f8", 1: "#ff2", 2: "#f22", 3: "#fa2" }[row["service_state"]]
    value = int(perf_data[0][1])
    return "%d" % value, perfometer_logarithmic(value, 100, 5, color)


perfometers['check_mk-elasticsearch.cluster_name'] = perfometer_elasticsearch_cluster_name
perfometers['check_mk-elasticsearch.status'] = perfometer_elasticsearch_status
perfometers['check_mk-elasticsearch.nodes'] = perfometer_elasticsearch_nodes
perfometers['check_mk-elasticsearch.shards'] = perfometer_elasticsearch_shards