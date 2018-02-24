#!/usr/bin/env python
# -*- coding:utf-8 -*

'''

Gestion d'une horloge temps réel DS1302 pour Raspberry pi

Basée sur 
	- lib python rpi.rtc (https://github.com/sourceperl/rpi.rtc)
	- ntpstat
	
Objectifs
	- en plus de la lecture et ecriture du temps dans le ds1302,
		créer un deamon qui si un serveur ntp est ok, met à jour le ds1302
	
'''

import pyRPiRTC
import subprocess
import datetime
import logging

class frtc(pyRPiRTC.DS1302):
	''' ds1302 device
	'''
	def write_ntp(self):
		''' Check ntp status and write ds1302 if ntp is ok
		'''
		ntpstat = subprocess.Popen("ntpstat")
		if ntpstat.returncode == 0:
			now = datetime.datetime.utcnow()
			self.write_datetime(now)
			logging.info("NTP status : Ok. %s writed to DS1302."%(now))
		else:
			logging.info("NTP status : Down.")