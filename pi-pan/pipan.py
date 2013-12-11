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

# servo definitions (for current board).
S4 = 0
S5 = 1
#

class PiPan:
    ServoBlaster = 0
    y = 0

    def __init__(self):
        global ServoBlaster
        try:
            ServoBlaster = open('/dev/servoblaster', 'w')
        except (IOError):
            print "*** ERROR ***"
            print "Unable to open the device, check that servod is running"
            print "To start servod, run: sudo /etc/init.d/servoblaster.sh start"
            exit()

    def pwm(self, pin, angle):
        #print "servo[" + str(pin) + "][" + str(angle) + "]"
        ServoBlaster.write(str(pin)+'=' + str(int(angle)) + '\n')
        ServoBlaster.flush()

    # bring the pan servo to neutral position
    def neutral_pan(self):
        self.pwm (S4, int(150))

    # bring the tilt servo to neutral position
    def neutral_tilt(self):
        self.pwm (S5, int(150))

    # pan movement
    def do_pan(self, x):
        if ( x > 250 ):
            x = 250
        if ( x < 50 ):
            x = 50
        self.pwm (S4, int(x))

    # tilt movement
    def do_tilt(self, y):
        # limit tilt between 80 and 220
        if ( y > 220 ):
            y = 220
        if ( y < 80 ):
            y = 80
        self.pwm (S5, int(y))


