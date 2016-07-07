#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |  ____  _   _  ___  _   _ _____ ____              _           ____   |
# | / ___|| | | |/ _ \| | | |_   _/ ___|___ __ _ ___| |_  __   _|___ \  |
# | \___ \| |_| | | | | | | | | || |   / __/ _` / __| __| \ \ / / __) | |
# |  ___) |  _  | |_| | |_| | | || |__| (_| (_| \__ \ |_   \ V / / __/  |
# | |____/|_| |_|\___/ \___/  |_| \____\___\__,_|___/\__|___\_/ |_____| |
# |                                                   |_____|           |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor Shoutcast 2.x servers on Linux          |
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
    "shoutcastv2",
    _("Shoutcast DNAS 2.x streaming server"),
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
                    help = _("Maximum percent usage of the server based alarm based in peaklisteners"),
                    elements = [
                        Integer(
                            title = _("Warning if over"),
                            unit = _("Percent"),
                            default_value = 80
                        ),
                        Integer(
                            title = _("Critical if over"),
                            unit = _("Percent"),
                            default_value = 90
                        ),
                    ]
                )
            ),
            ("uniquelisteners",
                Tuple(
                    title = _("Unique listeners"),
                    help = _("total number of connected  different IPs to the server"),
                    elements = [
                        Integer(
                        	title = _("Warning if below"),
                        	unit = _("Listeners"),
                        	default_value = 0
                        ),
                        Integer(
                        	title = _("Critical if below"),
                        	unit = _("Listeners"),
                        	default_value = 0
                        ),
                    ]
                )
            )
        ]
   ),
   TextAscii( title=_("SHOUTCast 2.x server limits"),
   help=_("Leave blank to apply limits to all servers, or specify an specicfic server PORT to set limit values only to it.")),
   "first"
)        