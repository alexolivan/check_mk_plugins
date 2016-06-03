#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +---------------------------------------------------------------------+
# |     ____  ____   _____  ____  __  _____  __                         |
# |    |  _ \|  _ \ / _ \ \/ /  \/  |/ _ \ \/ /     _ ____   _____      |
# |    | |_) | |_) | | | \  /| |\/| | | | \  /_____| '_ \ \ / / _ \     |
# |    |  __/|  _ <| |_| /  \| |  | | |_| /  \_____| |_) \ V /  __/     |
# |    |_|   |_| \_\\___/_/\_\_|  |_|\___/_/\_\    | .__/ \_/ \___|     |
# |                                                |_|                  |
# |                                                                     |
# | Copyright Alejandro Olivan 2016                 alex@alexolivan.com |
# +---------------------------------------------------------------------+
# | A Check_mk agent to monitor PROXMOX PVE Hypervisor systems          |
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
    "pve_cluster_status",
    _("Proxmox PVE Cluster Status"),
    Dictionary(
        elements = [
            ("Nodes",
                Tuple(
                    title = _("Cluster Nodes"),
                    help = _("Total number of HN nodes belonging to this PVE Cluster"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("nodes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("nodes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("Expected-votes",
                Tuple(
                    title = _("Expected Votes"),
                    help = _("Total expected number of votes participating in the cluster"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("votes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("votes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("Total-votes",
                Tuple(
                    title = _("Total Votes"),
                    help = _("Actual number of votes really participating in the cluster"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("votes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("votes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("Node-votes",
                Tuple(
                    title = _("Node Votes"),
                    help = _("Total votes of this node in the cluster"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("votes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("votes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),            
            ("Quorum",
                Tuple(
                    title = _("Cluster Quorum"),
                    help = _("Total number of HN nodes that conform the cluster Quorum"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("nodes"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("nodes"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),            
            ("Active-subsystems",
                Tuple(
                    title = _("Active Subsystems"),
                    help = _("Total number of Active subsystems in the cluster"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("systems"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("systems"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
       ]
   ),
   None,
   "dict",
)

register_check_parameters(
    subgroup_applications,
    "pve_local_status",
    _("Proxmox PVE local running instances status"),
    Dictionary(
        elements = [
            ("stopped-vms",
                Tuple(
                    title = _("Stopped VMs"),
                    help = _("Total stopped Qemu Virtual Machines in this node"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("running-vms",
                Tuple(
                    title = _("Running VMs"),
                    help = _("Total running Qemu Virtual Machines in this node"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("stopped-vzs",
                Tuple(
                    title = _("Stopped VZs"),
                    help = _("Total stopped OpenVZ Containers in this node"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("running-vzs",
                Tuple(
                    title = _("Running VZs"),
                    help = _("Total running OpenVZ Containers in this node"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("stopped-lxcs",
                Tuple(
                    title = _("Stopped LXCs"),
                    help = _("Total stopped LXC Containers in this node"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),
            ("running-lxcs",
                Tuple(
                    title = _("Running LXCs"),
                    help = _("Total running LXC Containers in this node"),
                    elements = [
                        Integer(
                            title = _("Warning if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                        Integer(
                            title = _("Critical if below"),
                            unit = _("instances"),
                            default_value = 0                            
                        ),
                    ]
                )
            ),            
       ]
   ),
   None,
   "dict",
) 