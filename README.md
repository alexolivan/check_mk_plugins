# check_mk_plugins
### Nagios Check_MK PLugins

A set of self made Check_mk plugins.
They probably need serious refactoring, and code isn't probably nice (I'm not comfortable with python).
Although I try to stick to recommended practices at developing check_mk modules, this work may not work to everyoone...
They but work for me, I just want to share the code, just in case someone is interested.
The main flaw is that for that reason, the plugins are meant to run on linux, and more precissely, debian Linux, so the agents may be completely unuseful in different scenarios.


##### List of plugins:
- elasticsearch (tested with elasticsearch 1.4)
- logstash (tested with elasticsearch 1.5)
- Redis-Server
- PROXMOX PVE (tested with 3.x)
- SHOUTCast DNAS 1.9.8
- SHOUTCast DNAS 2.x
- Icecast2 (Only newer than 2.4.1 with json xsl stats enabled)
- Centovacast (tested with CentovaCast 3.2.x)
- WowzaStreamEngine (tested with 4.3.0 VHosts)
- OpenVPN (Multiple instances, so relies on certain Debian9-style folder tree)
- Resque Web failed Queues (For Rails apps... tested on Reque v1.25.2)
 
