#!/usr/bin/python3
#
# Monitoring plugin for CCS811 sensor
# Based on https://learn.adafruit.com/adafruit-ccs811-air-quality-sensor/raspberry-pi-wiring-test
#
# Licence : GNU General Public Licence (GPL) http://www.gnu.org/
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#
#
# Copyright (c) 2019 Claudio Kuenzler


import time
import board
import busio
import adafruit_ccs811
i2c_bus = busio.I2C(board.SCL, board.SDA)
ccs811 = adafruit_ccs811.CCS811(i2c_bus)

# Wait for the sensor to be ready and calibrate the thermistor
while not ccs811.data_ready:
    print("CCS811 CRITICAL - Sensor not ready")
#temp = ccs811.temperature
#ccs811.temp_offset = temp - 25.0


# Before we output the plugin data, retrieve several values from sensor to wake it up
i = 0
while i < 10:
  ccs811.eco2
  ccs811.tvoc
  ccs811.temperature
  i += 1


print("CCS811 OK - CO2: {} PPM, TVOC: {} PPB, Temp: {} C|co2={};;; tvoc={};;; temp={};;;"
          .format(ccs811.eco2, ccs811.tvoc, ccs811.temperature, ccs811.eco2, ccs811.tvoc, ccs811.temperature))
