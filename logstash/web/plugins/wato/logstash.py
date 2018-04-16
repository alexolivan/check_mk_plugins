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
    "logstash_redis",
    _("logstash established connections to redis server"),
    Dictionary(
        elements = [
            ("redis-connections",
                Tuple(
                    title = _("Redis output connections"),
                    help = _("Number of connections to redis through redis output"),
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
        ]
   ),
   TextAscii( title=_("Logstash instance Connections limits"),
   help=_("Leave blank to apply limits to all logstash instances, or specify an specicfic instance  to set limit values only to it.")),
   "dict"
)

register_check_parameters(
    subgroup_applications,
    "logstash_memory",
    _("logstash virtual memory"),
    Dictionary(
        elements = [
            ("virtual_memory",
                Tuple(
                    title = _("Total virtual memory used"),
                    help = _("total number of bytes allocated by Logstash"),
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
            ("resident_memory",
                Tuple(
                    title = _("Total resident memory used"),
                    help = _("total number of bytes allocated by Logstash"),
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
            ("shared_memory",
                Tuple(
                    title = _("Total shared memory used"),
                    help = _("total number of bytes allocated by Logstash"),
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
            ("memory_usage",
                Tuple(
                    title = _("Memory usage"),
                    help = _("Percentage of total system memory used"),
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
   TextAscii( title=_("Logstash instance Memory limits"),
   help=_("Leave blank to apply limits to all resellers, or specify an specicfic reseller to set limit values only to it.")),
   "dict"
)

register_check_parameters(
    subgroup_applications,
    "logstash_cpu",
    _("logstash CPU usage"),
    Dictionary(
        elements = [
            ("cpu_usage",
                Tuple(
                    title = _("CPU usage"),
                    help = _("Percentage of total system CPU used"),
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
   TextAscii( title=_("Logstash instance CPU limits"),
   help=_("Leave blank to apply limits to all instances, or specify an specicfic instance to set limit values only to it.")),
   "dict"
)
