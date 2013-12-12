from django.db import models

class CameraRoom(models.Model):
    name = models.CharField(max_length=200)
    cam_ip1 = models.IPAddressField(max_length=200)
    cam_port1 = models.IntegerField()
    cam_ip2 = models.IPAddressField(max_length=200)
    cam_port2 = models.IntegerField()
    socket_ip1 = models.IPAddressField(max_length=200)
    socket_port1 = models.IntegerField()
    socket_ip2 = models.IPAddressField(max_length=200)
    socket_port2 = models.IntegerField()

    def __unicode__(self):
	return self.name
