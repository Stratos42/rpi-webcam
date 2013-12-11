#!/usr/bin/env python
#
# Copyright (c) 2013 OpenElectrons.com
# Pi-Pan isntallation script.
# for more information about Pi-Pan and PiLight,  please visit:
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
# 09/15/13    Nitin Patil    Initial authoring.
#
# this is driver for the driveing Openelectrons.com PiLight with any RGB values 

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.


from Adafruit_I2C import Adafruit_I2C
import sys
import time

class PILIGHT(Adafruit_I2C):

    # Minimal constants required by library
    
    PILIGHT_ADDRESS = (0x30 >> 1)  
    
    PILIGHT_WHO_AM_I    =  0x10
    PILIGHT_VERSION    =  0x00
    PILIGHT_VENDOR    =  0x08
    
    PILIGHT_RED  = 0x42
    PILIGHT_GREEN  =  0x43
    PILIGHT_BLUE   =  0x44
    
    def __init__(self, busnum=-1, debug=False, hires=False):

        #define the pilight address
        self.pilight = Adafruit_I2C(self.PILIGHT_ADDRESS, busnum, debug)
        

    def readPiLight(self):
        # read  the piLight RGB values
        list = self.pilight.readList(self.PILIGHT_RED, 3)
        return list    
        
    def setTimeout(self, timeoutValue):
        # write the piLight
        list = [] 
        list.append(0)
        list.append(0)
        list.append(0)
        list.append(timeoutValue)
        self.pilight.writeList(self.PILIGHT_RED, list)

    def createPiLight(self, red, green, blue):
        # write the piLight
        list = [] 
        list.append(red)
        list.append(green)
        list.append(blue)
        self.pilight.writeList(self.PILIGHT_RED, list)
        

    def GetFirmware(self):
        # Read the version
        list = self.pilight.readList(self.PILIGHT_VERSION, 8)
        return list
        
    def GetVendorID(self):
        # Read the version
        list = self.pilight.readList(self.PILIGHT_VENDOR, 8)
        return list    
        
    def GetDeviceID(self):
        # Read the version
        list = self.pilight.readList(self.PILIGHT_WHO_AM_I, 8)
        return list


# Simple example to  to set RGB values of PiLight from command line
if __name__ == '__main__':

    from time import sleep
    # Get the total number of args passed to the PiLight.py
    total = len(sys.argv)
    if total < 4 :
        print "insufficient parameters : PiLight R G B"
        sys.exit(1)
    # Get the arguments list 
    cmdargs = str(sys.argv)
        
    
    pilight = PILIGHT()
    print ''.join(chr(i) for i in pilight.GetFirmware())
    print ''.join(chr(i) for i in pilight.GetVendorID())
    print ''.join(chr(i) for i in pilight.GetDeviceID())
    pilight.createPiLight(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]))
    
