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
