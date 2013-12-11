#!/bin/bash
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

#
#  check that user has required files.
#
if [ -e  servod ]
then
    sudo cp servod /usr/local/sbin
else
    echo "missing servod??"
    exit 1
fi

if [ -e  servoblaster.sh ]
then
    sudo cp servoblaster.sh /etc/init.d
else
    echo "missing servoblaster.sh??"
    exit 1
fi

#
# insert into startup scripts for subsequent use
#
sudo update-rc.d servoblaster.sh defaults 92 08

#
#  start the servoblaster for this time use
#
sudo /etc/init.d/servoblaster.sh start > /dev/null

echo "-----------------------------"
echo "Pi-Pan Install completed     "
echo "-----------------------------"
