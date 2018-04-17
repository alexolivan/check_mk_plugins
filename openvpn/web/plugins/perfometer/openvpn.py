#!/bin/bash
# +---------------------------------------------------------------------+
# |     ___                __     ______  _   _                         |
# |    / _ \ _ __   ___ _ _\ \   / /  _ \| \ | |                        |
# |   | | | | '_ \ / _ \ '_ \ \ / /| |_) |  \| |                        |
# |   | |_| | |_) |  __/ | | \ V / |  __/| |\  |                        |
# |    \___/| .__/ \___|_| |_|\_/  |_|   |_| \_|                        |
# |         |_|                                                         |
# |                                                                     |
# | Copyright Alejandro Olivan 2018                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor OpenVPN Remote Access servers on Linux  |
# | This file contains plugin agent definition.                         |
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

def perfometer_openvpn(row, check_command, perf_data):
    uptime = perf_data[2][1]
    return "%d days" % uptime, '<table><tr>' \
    				+ perfometer_logarithmic(uptime, 30, 2, '#0f0') \
                            	+ '</tr></table>'


perfometers['check_mk-openvpn.clients'] = perfometer_openvpn
