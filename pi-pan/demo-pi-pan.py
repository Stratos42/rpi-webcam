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
# 08/22/13  Deepak      Initial authoring.
#

import time
import os, sys
import pipan

print "pi-pan pan/tilt demo"

p = pipan.PiPan()

x = 128
y = 140
p.do_tilt (int(y))
p.do_pan (int(x))

def head_up_down(y):
    # move head down
    while y > 80:
        p.do_tilt (int(y))
        time.sleep(0.1)
        y -= 2

    # move head up
    while y < 180:
        p.do_tilt (int(y))
        time.sleep(0.1)
        y += 2

    # level the head to look in front
    while y > 140:
        p.do_tilt (int(y))
        time.sleep(0.1)
        y -= 2


while 1:
    # move head to right
    while x < 200:
        p.do_pan (int(x))
        time.sleep(0.1)
        x += 2

    head_up_down(y)

    # move head to left
    while x > 50:
        p.do_pan (int(x))
        time.sleep(0.1)
        x -= 2

    head_up_down(y)

