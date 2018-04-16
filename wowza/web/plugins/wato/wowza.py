#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |       __        __                          ____  _____             |
# |       \ \      / /____      ________ _     / ___|| ____|            |
# |        \ \ /\ / / _ \ \ /\ / /_  / _` |____\___ \|  _|              |
# |         \ V  V / (_) \ V  V / / / (_| |_____|__) | |___             |
# |          \_/\_/ \___/ \_/\_/ /___\__,_|    |____/|_____|            |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor Wowza Stream Engine servers on Linux    |
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
    "wowza",
    _("Wowza Stream Engine server"),
    Dictionary(
        elements = [
            ("connections_current",
                Tuple(
                    title = _("Vhost current connections"),
                    help = _("Maximum percent usage of the VHost, alarm based in current connections"),
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
        ]
   ),
   TextAscii( title=_("Wowza Stream Engine VHosts usage."),
   help=_("Leave blank to apply limits to all VHosts, or specify an specicfic server VHost to set limit values only to it.")),
   "dict"
) 
