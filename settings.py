"""Retrieve settings from settings.ini"""

from decouple import config

IFHCINOCTETS = ".1.3.6.1.2.1.31.1.1.1.6"
IFHCOUTOCTETS = ".1.3.6.1.2.1.31.1.1.1.10"

HOST = config("HOST")
COMMUNITY = config("COMMUNITY")
IFINDEX = config("IFINDEX")

INFLUXDB_URL = config("INFLUXDB_URL")
INFLUXDB_USER = config("INFLUXDB_USER")
INFLUXDB_PASSWORD = config("INFLUXDB_PASSWORD")
