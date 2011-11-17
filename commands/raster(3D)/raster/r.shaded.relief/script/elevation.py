#!c:\Python25\python.exe
# -*- encoding=utf8 -*-
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

# system enviroment varibles
#---------------------------------------------------
def _exit(status):
    if(status):
        sys.exit(status)
#===================================================
from grass.script import core as grass

# change the location and mapsets of workspace 
gisenv = grass.gisenv()
if 'nc_spm_08' == gisenv['LOCATION_NAME']:
    ret=grass.run_command("g.gisenv", set='LOCATION_NAME=nc_spm_08')
    _exit(ret)
    if 'user1' == gisenv['MAPSET']:
        ret=grass.run_command("g.gisenv", set='MAPSET=user1')
        _exit(ret)
    
# set current region
ret = grass.run_command("g.region", rast='elevation')
_exit(ret)

ret = grass.run_command("r.shaded.relief.py", overwrite=True, input='elevation',output='myenv_shaded',azimuth=90, altitude=50,zmult=3, scale=2)
_exit(ret)

# display the result
monitor = 'png'
grass.run_command("d.mon", start=monitor, output='elevation_shaded')

grass.run_command("d.rast", map='myenv_shaded')

grass.run_command("d.his", h_map='elevation', i_map='myenv_shaded',brighten=30)

# close display monitor
grass.run_command("d.mon", stop=monitor)



