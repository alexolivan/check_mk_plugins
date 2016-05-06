#!/usr/bin/python
##### NICE ELASTICSEARCH HEAD WITH GPL STUFF #####

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

