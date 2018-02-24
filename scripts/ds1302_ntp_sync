#!/usr/bin/env python
# -*- coding:utf-8 -*

from FRTC.frtc import *
try:
	from FUTIL.my_logging import *
	my_logging(console_level = DEBUG, logfile_level = INFO, details = False)
except:
	import logging

rtc = frtc(clk_pin=37, data_pin=40, ce_pin=38)
rtc.write_ntp()
