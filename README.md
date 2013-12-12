RPi-Webcam
===========

This project is based on django_twisted_chat (https://github.com/aausch/django_twisted_chat.git).

The video streaming use the program 'motion' with the configuration file modified by Robin Newman (http://rbnrpi.wordpress.com/).

For the movement, I'm using the Pi-Pan Kit, buy on OpenElectrons.com (http://openelectrons.com/index.php?module=pagemaster&PAGE_id=15).

*****

# INSTALL

This project is composed in 3 parts:
- Motion-mmal (for the stream)
- Django-website (website build with django to see and control the camera)
- Chatserver.py (Twisted server for the websocket)

## Dependencies

First, you need to install Python 2.7 (dev) and PiPan module (http://www.openelectrons.com/pages/24)

	sudo apt-get install python-dev
	cd /tmp
	wget http://openelectrons.com/files/documents/pi-pan.tar.gz
	tar -zxvf pi-pan.tar.gz
	cd pi-pan
	sudo ./install-pi-pan.bash

After, install the Twisted (branch websocket-4173-4)
	
	cd /tmp
	git clone https://github.com/twisted/twisted.git
	git checkout -b websocket origin/websocket-4173-4
	sudo python setup.py install

And finaly, Motion (See: http://rbnrpi.wordpress.com/project-list/setting-up-wireless-motion-detect-cam/)

## Twisted Server

Run the twisted server:

	twisted -n -y chatserver.py


## Motion-mmal

Run the motion server:

	cd mmal
	./motion-mmal -n -c motion-mmalcam.conf

## Django-website

In django-website/camera/templates/cameras/, modify the URL of your rpi for the video stream and the websocket in the 'camera_room.html' file
(Lines 19 and 20)

The directory django-website is django project.

	python manage.py syncdb
	python manage.py runserver 8080

Connect to your django website http://localhost:8080/admin and create a Camera Room.
Access to you Camera Room: http://localhost:8080/cameras/1

## TODO

- [x] PiPan control by websocket
- [x] Slider update when client change the value
- [ ] Repair http://localhost:8080/cameras/ (list Room)
- [ ] Make URL in camera_room.html linked to the database
