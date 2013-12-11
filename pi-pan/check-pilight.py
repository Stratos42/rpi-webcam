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

import time
import os, sys
import pilight

print "Check that Pi-Light is working correctly"

pl = pilight.PILIGHT()

pl.createPiLight(255,255,255)
time.sleep(1)

pl.createPiLight(255, 0, 0)
time.sleep(1)

pl.createPiLight(0, 255, 0)
time.sleep(1)

pl.createPiLight(0, 0, 255)
time.sleep(1)

pl.createPiLight(255,255,255)
time.sleep(1)

pl.createPiLight(0, 0, 0)
