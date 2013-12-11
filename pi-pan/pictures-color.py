#!/usr/bin/env python
#
# Copyright (c) 2013 OpenElectrons.com
# Pi-Pan isntallation script.
# for more information about Pi-Pan,  please visit:
# http://www.openelectrons.com/Pi-Pan
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.
#
# History:
# Date      Author      Comments
# 09/18/13  Deepak      Initial authoring.
#

# this program takes pictures, with various settings of light on Pi-Light
# and puts them in /var/tmp folder.

# at the beginning it centers the camera and waits
# for 5 seconds for you to align the camera

# to run this script when pi boots up:
# insert this script in /etc/init.d/servoblaster.sh
# (in do_start function) as follows:

#  do_start () {
#	   /usr/local/sbin/servod --idle-timeout=2000 --p1pins=16,18 >/dev/null
#      sleep 2
#      python ~pi/pi-pan/YOUR-PROGRAM-HERE.
#  }



import time
import os, sys
import pipan
import subprocess
import pilight


def light_and_capture (R, G, B):
    pl.createPiLight(R,G,B)
    cmdstr = "/var/tmp/pic_" + str(idx) + "_" + str(R) + "_" + str(G) +"_"+str(B)+ ".jpg"
    print cmdstr
    f.write(cmdstr)
    f.write("\n")
    subprocess.call(["raspistill", "-o", cmdstr, "-rot", "180"])
    print "done taking picture"

def head_up_down(y):
    # move head up
    while y > 80:
        p.do_tilt (int(y))
        time.sleep(0.1)
        y -= 2

    # move head down
    while y < 180:
        p.do_tilt (int(y))
        time.sleep(0.1)
        y += 2

    # level the head to look in front
    while y > 140:
        p.do_tilt (int(y))
        time.sleep(0.1)
        y -= 2

print "Taking two pictures, file names as follows:"

# create PiPan object
p = pipan.PiPan()

# neutral the servos
p.neutral_pan()
p.neutral_tilt()

# allow time for user to setup his camera position.
time.sleep (5)
global idx

idx = 0
# create a unique log file to write all the picture names.
for fidx in xrange (10, 90, 1):
    fname = "/var/tmp/light_log_" + str(fidx) + ".txt"
    if not os.path.exists(fname):
        idx = fidx
        break

f = open(fname, 'a')

pl = pilight.PILIGHT()

light_and_capture(255, 255, 255)
light_and_capture(0, 0, 255)
light_and_capture(255, 0, 0)
light_and_capture(0, 255, 0)
light_and_capture(0, 0, 0)


f.close();
# sync the buffers.
subprocess.call(["sync"])
# move head up down to indicate that it has finished taking pictures
head_up_down(200)

