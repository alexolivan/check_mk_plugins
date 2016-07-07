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
# | This file contains plugin WATO parameters definition.               |
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

group = "checkparams"
subgroup_applications = _("Applications, Processes & Services")

register_check_parameters(
    subgroup_applications,
    "redis_cpu",
    _("redis-server cpu and LRU clock"),
    Dictionary(
        elements = [
            ("lru_clock",
                Tuple(
                    title = _("LRU Clock"),
                    help = _("Clock incrementing every minute, for LRU management"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("minutes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("minutes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("used_cpu_sys",
                Tuple(
                    title = _("CPU sys"),
                    help = _("System CPU consumed by the Redis server"),
                    elements = [
                        Percentage(
                            title = _("Warning if below"),
                            unit = _("percent"),
                            default_value = 50                            
                        ),
                        Percentage(
                            title = _("Critical if below"),
                            unit = _("percent"),
                            default_value = 75                            
                        ),
                    ]
                )
            ),
            ("used_cpu_user",
                Tuple(
                    title = _("CPU user"),
                    help = _("User CPU consumed by the Redis server"),
                    elements = [
                        Percentage(
                            title = _("Warning if below"),
                            unit = _("percent"),
                            default_value = 50                            
                        ),
                        Percentage(
                            title = _("Critical if below"),
                            unit = _("percent"),
                            default_value = 75                            
                        ),
                    ]
                )
            ),
            ("used_cpu_sys_children",
                Tuple(
                    title = _("CPU children sys"),
                    help = _("System CPU consumed by the background processes"),
                    elements = [
                        Percentage(
                            title = _("Warning if below"),
                            unit = _("percent"),
                            default_value = 50                            
                        ),
                        Percentage(
                            title = _("Critical if below"),
                            unit = _("percent"),
                            default_value = 75                            
                        ),
                    ]
                )
            ),
            ("used_cpu_user_children",
                Tuple(
                    title = _("CPU children user"),
                    help = _("User CPU consumed by the background processes"),
                    elements = [
                        Percentage(
                            title = _("Warning if below"),
                            unit = _("percent"),
                            default_value = 50                            
                        ),
                        Percentage(
                            title = _("Critical if below"),
                            unit = _("percent"),
                            default_value = 75                            
                        ),
                    ]
                )
            ),           
       ]
   ),
   TextAscii( title=_("Redis server CPU limits"),
   help=_("Leave blank to apply limits to all redis servers, or specify an specicfic server to set limit values only to it.")),
   "first"
)

register_check_parameters(
    subgroup_applications,
    "redis_memory",
    _("redis server memory"),
    Dictionary(
        elements = [
            ("used_memory",
                Tuple(
                    title = _("Total Memory"),
                    help = _("total number of bytes allocated by Redis using its allocator"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("Bytes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("Bytes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("used_memory_rss",
                Tuple(
                    title = _("RSS Memory"),
                    help = _(" Number of bytes that Redis allocated as seen by the operating system"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("Bytes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("Bytes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("used_memory_peak",
                Tuple(
                    title = _("Peak Memory"),
                    help = _("Peak memory consumed by Redis"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("Bytes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("Bytes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("mem_fragmentation_ratio",
                Tuple(
                    title = _("Memory fragmentation Ratio"),
                    help = _("Ratio between used_memory_rss and used_memory"),
                    elements = [
                        Percentage(
                            title = _("Warning if below"),
                            unit = _("percent"),
                            default_value = 50                            
                        ),
                        Percentage(
                            title = _("Critical if below"),
                            unit = _("percent"),
                            default_value = 75                            
                        ),
                    ]
                )
            ),
       ]
   ),
   TextAscii( title=_("Redis server memory limits"),
   help=_("Leave blank to apply limits to all servers, or specify an specicfic server to set limit values only to it.")),
   "first"
)

register_check_parameters(
    subgroup_applications,
    "redis_connections",
    _("redis-server connections"),
    Dictionary(
        elements = [
            ("connected_clients",
                Tuple(
                    title = _("Client connections"),
                    help = _("Number of client connections"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("connections"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("connections"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("connected_slaves",
                Tuple(
                    title = _("Slaves connections"),
                    help = _("Number of slave servers connections"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("connections"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("connections"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("client_longest_output_list",
                Tuple(
                    title = _("Client longest output list"),
                    help = _("longest output list among current client connections"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            default_value = 0                            
                            ),
                        Integer(
                            title = _("Critical if below"),
                            default_value = 0                            
                            ),
                    ]
                )
            ),
            ("client_biggest_input_buf",
                Tuple(
                    title = _("Client biggest input buffer"),
                    help = _("biggest input buffer among current client connections"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            default_value = 0                            
                            ),
                        Integer(
                            title = _("Critical if below"),
                            default_value = 0                            
                            ),
                    ]
                )
            ),
            ("blocked_clients",
                Tuple(
                    title = _("Blocked clients"),
                    help = _("Number of clients pending on a blocking call"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("blocks"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("blocks"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("total_connections_received",
                Tuple(
                    title = _("Total Received Connections"),
                    help = _("Total number of connections accepted by the server"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("connections"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("connections"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("total_commands_processed",
                Tuple(
                    title = _("Total Processed commands"),
                    help = _("Total number of commands processed by the server"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("commands"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("commands"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
       ]
   ),
   TextAscii( title=_("Redis server connection limits"),
   help=_("Leave blank to apply limits to all servers, or specify an specicfic server to set limit values only to it.")),
   "first"
)


register_check_parameters(
    subgroup_applications,
    "redis_keys",
    _("redis-server keys"),
    Dictionary(
        elements = [
            ("expired_keys",
                Tuple(
                    title = _("Expired Keys"),
                    help = _("Total number of key expiration events"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("keys"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("keys"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("evicted_keys",
                Tuple(
                    title = _("Evicted keys"),
                    help = _("Number of evicted keys due to maxmemory limit"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("keys"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("keys"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("keyspace_hits",
                Tuple(
                    title = _("Total Keyspace hits"),
                    help = _("Number of successful lookup of keys in the main dictionary"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("hits"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("hits"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("keyspace_misses",
                Tuple(
                    title = _("Total Keyspace misses"),
                    help = _("Number of failed lookup of keys in the main dictionary"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("misses"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("misses"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
       ]
   ),
   TextAscii( title=_("Redis server keys limits"),
   help=_("Leave blank to apply limits to all servers, or specify an specicfic server to set limit values only to it.")),
   "first"
)