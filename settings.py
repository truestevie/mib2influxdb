"""Retrieve settings from settings.ini"""

from decouple import config

HOST = config("HOST")
COMMUNITY = config("COMMUNITY")
IFINDEX = config("IFINDEX")

INFLUXDB_URL = config("INFLUXDB_URL")
INFLUXDB_USER = config("INFLUXDB_USER")
INFLUXDB_PASSWORD = config("INFLUXDB_PASSWORD")
