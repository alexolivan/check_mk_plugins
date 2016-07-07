#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |         ___                       _   ____   _  _                   |
# |        |_ _|___ ___  ___ __ _ ___| |_|___ \ | || |  __  __          |
# |         | |/ __/ _ \/ __/ _` / __| __| __) || || |_ \ \/ /          |
# |         | | (_|  __/ (_| (_| \__ \ |_ / __/ |__   _| >  <           |
# |        |___\___\___|\___\__,_|___/\__|_____(_) |_|(_)_/\_\          | 
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor Icecast 2.4.x servers on Linux          |
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



group = "checkparams"
subgroup_applications = _("Applications, Processes & Services")

register_check_parameters(
    subgroup_applications,
    "icecast2",
    _("Icecast 2.4.x streaming server"),
    Dictionary(
        elements = [
            ("currentlisteners",
                Tuple(
                    title = _("Current listeners"),
                    help = _("total number of connected listeners to the server"),
                    elements = [
                        Integer(
                        	title = _("Warning if below"),
                        	unit = _("Listeners"),
                        	default_value = 2
                        ),
                        Integer(
                        	title = _("Critical if below"),
                        	unit = _("Listeners"),
                        	default_value = 1
                        ),
                    ]
                )
            ),
            ("status",
                Tuple(
                    title = _("Server Status"),
                    help = _("Server source up or down status."),
                    elements = [
                        Integer(
                        	title = _("Warning if below"),
                        	default_value = 1
                        ),
                        Integer(
                        	title = _("Critical if below"),
                        	default_value = 1
                        ),
                    ]
                )
            ),            
            ("peaklisteners",
                Tuple(
                    title = _("Peak listeners"),
                    help = _("Maximum number of connected listeners to the server"),
                    elements = [
                        Integer(
                        	title = _("Warning if over"),
                        	unit = _("Listeners"),
                        	default_value = 0
                        ),
                        Integer(
                        	title = _("Critical if over"),
                        	unit = _("Listeners"),
                        	default_value = 0
                        ),
                    ]
                )
            ),
            ("maxlisteners",
                Tuple(
                    title = _("Server slots"),
                    help = _("Max number of connections configured in the server"),
                    elements = [
                        Integer(
                        	title = _("Available slots"),
                        	unit = _("Slots"),
                        	default_value = 1024
                        ),
                    ]
                )
            )
        ]
   ),
   TextAscii( title=_("Icecast2 server instance limits"),
   help=_("Leave blank to apply limits to all servers, or specify an specicfic server listen PORT to set limit values only to it.")),
   "first"
) 