#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
计算能最快到达高速路上着火点的消防站

数据：
    point(634886,224328)    着火点位置
    myfirestations@user1    消防站位置
    streets_wake            道路图
"""
import subprocess
import grass as maingrass
from grass.script import core as grass

#---------------------------------------------------
def _exit(status):
    if(status):
        sys.exit(status)
#===================================================
from grass.script import core as grass

try:
    # change the location and mapsets of workspace 
    gisenv = grass.gisenv()
    if 'nc_spm_08' == gisenv['LOCATION_NAME']:
        grass.pipe_command("g.gisenv", set='LOCATION_NAME=nc_spm_08')
    if 'user1' == gisenv['MAPSET']:
	grass.run_command("g.gisenv", set='MAPSET=user1')
	    
    # set current region
    grass.run_command("g.region", vect='streets_wake@user1')
	
    # 栅格化streets_wake矢量图
    grass.run_command("v.to.rast", overwrite=True, input="streets_wake",
    	                        output="streets_speed", use="attr",
                                attrcolumn="speed")
except OSError,err:
    print "没有相关命令!\n"
    print err.child_traceback
except ValueError,err:
    print "参数传入错误!\n"
    print err.child_traceback
#except CalledProcessError,warn:
#    print "执行结果不正确!\n"
#    print warn.child_traceback
else:
    pass
	
	
	     
