#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |         ____           _                   ____          _          |
# |        / ___|___ _ __ | |_ _____   ____ _ / ___|__ _ ___| |_        |
# |       | |   / _ \ '_ \| __/ _ \ \ / / _` | |   / _` / __| __|       |
# |       | |__|  __/ | | | || (_) \ V / (_| | |__| (_| \__ \ |_        |
# |        \____\___|_| |_|\__\___/ \_/ \__,_|\____\__,_|___/\__|       |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor CentovaCast server panel on Linux       |
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
    "centovacast_resellers",
    _("CentovaCast Reseller accounts"),
    Dictionary(
        elements = [
            ("diskquota",
                Tuple(
                    title = _("Disk quota usage"),
                    help = _("Percent usage of CentovaCast reseller assigned disk quota."),
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
            ("transferlimit",
                Tuple(
                    title = _("Transfer limit usage"),
                    help = _("Percent usage of tCentovacast reseller assigned transfer limit."),
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
   None,
   "dict"
)

register_check_parameters(
    subgroup_applications,
    "centovacast_accounts",
    _("Centovacast Server accounts"),
    Dictionary(
        elements = [
            ("diskquota",
                Tuple(
                    title = _("Disk quota usage"),
                    help = _("Percent usage of CentovaCast reseller assigned disk quota."),
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
            ("transferlimit",
                Tuple(
                    title = _("Transfer limit usage"),
                    help = _("Percent usage of tCentovacast reseller assigned transfer limit."),
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
   None,
   "dict"
)
