#!/usr/bin/env python
# -*- conding=utf8 -*-
#
############################################################################
#
# EXAMPLE:	evelation.py 
# AUTHOR(S):	zzpwelkin
# PURPOSE:	create the shaded map of nc_spm_80@evelation and display
# COPYRIGHT:	(C) 2004,2008 by the GRASS Development Team
#
#		This program is free software under the GNU General Public
#		License (>=v2). Read the file COPYING that comes with GRASS
#		for details.
#
#############################################################################

import os
import sys

# 系统环境设置
os.altsep="\\"
sys.path.append('D:\\OSGeo4W\\apps\\grass\\grass-7.0.svn\\etc\\python')

#---------------------------------------------------
def _exit(status):
    if(status):
        sys.exit(status)
#===================================================
from grass.script import core as grass

# change the location and mapsets of workspace 
ret=grass.run_command("g.gisenv", set='LOCATION_NAME=nc_spm_08')
_exit(ret)
ret=grass.run_command("g.gisenv", set='MAPSET=user1')
_exit(ret)
    
# set current region
ret = grass.run_command("g.region", rast='evelation')
_exit(ret)

ret = grass.run_command("r.shaded.relief", input='elevation',output='myenv_shaded',azimuth=90, altitude=50,zmult=3, scale=2)
_exit(ret)

# display the result
ret = grass.run_command("d.mon", start='wx0')
_exit(ret)
ret = grass.run_command("d.rast", map='myenv_shaded')
_exit(ret)
ret = grass.run_command("d.his", h_map='elevation', i_map='myenv_shaded',brighten=30)
sys.exit(status)

