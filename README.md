# ADS79xx_RPI_Python_Driver
Raspberry Pi Python Library for Texas Instruments ADS7950, ADS7951, ADS7952, ADS7953, ADS7954, ADS7955 ADS7956, ADS7957, ADS7958, ADS7959, ADS7960, ADS7961 Analog to Digital Converter Modules.

Raspberry Pi Preparation.

P1 HEADER PIN	FUNCTION
19	MOSI – master output slave input
21	MISO – master input slave output
23	SCLK – clock
24	CE0 – chip enable 0

Enable SPI on the Raspberry Pi
1.In your Pi’s terminal, run
 sudo raspi-config
2.Go to Advanced Options > SPI
Choose “Yes” for both questions then select Finish to exit raspi-config
3.Reboot your Pi

Install spidev
Spidev is a python module that allows us to interface with the Pi’s SPI bus.Watch movie online The Transporter Refueled (2015)

sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python-dev python3-dev
cd ~
git clone https://github.com/doceme/py-spidev.git
cd py-spidev
make
sudo make install

SPEED	SPI.MAX_SPEED_HZ VALUE
125.0 MHz	125000000
62.5 MHz	62500000
31.2 MHz	31200000
15.6 MHz	15600000
7.8 MHz	7800000
3.9 MHz	3900000
1953 kHz	1953000
976 kHz	976000
488 kHz	488000
244 kHz	244000
122 kHz	122000
61 kHz	61000
30.5 kHz	30500
15.2 kHz	15200
7629 Hz	7629
