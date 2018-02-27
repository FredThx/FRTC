# FRTC : DS1302 RTC AND NTP

Simple Python module (based on rpi.rtc) to sync date and time on a Raspberry Pi with DS1302 and/or NTP
	
## Hardware
		- Raspberry Pi
		- DS1302
	
## Dependances
* rpi.rtc	https://github.com/sourceperl/rpi.rtc
* ntpstat
* FUTIL		https://github.com/FredThx/FUTIL

## Installation

 apt-get install ntpstat
 
 git clone https://github.com/sourceperl/rpi.rtc
 
 cd rpi.rtc
 
 sudo python setup.py install
 
 cd ..
 
 git clone https://github.com/FredThx/FUTIL
 
 cd FUTIL
 
 sudo python setup.py install
 
 git clone https://github.com/FredThx/FRTC
 
 cd FRTC
 
 sudo python setup.py install
 

	 
## Usage
	
		sudo crontab -e -u root
	
	add "42 * * * * /usr/local/bin/ds1302_ntp_sync"
	(check time every hour, at minute 42)
	 	 
	 

