#!/usr/bin/env python
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

import sys
from grass.script import core as grass

# change the location and mapsets of workspace
ret=grass.run_command("g.gisenv", set="GISDBASE=F:\workstation\grass\grassdata",
                  set="LOCATION_NAME=nc_spm_08",
                  set="MAPSET=user1")
_exit(ret)
# set current region
ret = grass.run_command("g.region", rast=evelation)
_exit(ret)

ret = grass.run_command("r.shaded.relief", flags='--o',input=elevation,
                        output=myenv_shaded,azimuth=90, altitude=50, zmult=3, scale=2)
_exit(ret)

# display the result
ret = grass.run_command("d.mon", start=wx3)
_exit(ret)
ret = grass.run_command("d.rast", map=myenv_shaded)
_exit(ret)
ret = grass.run_command("d.hsi", h_map=evelation, i_map=myenv_shaded, brighten=30)
sys.exit(status)

def _exit(status):
    if(status):
        sys.exit(status)
