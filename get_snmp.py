"""Read router interface load and upload it to InfluxDB."""

import sys

import requests
from easysnmp import Session

import settings

session = Session(hostname=settings.HOST, community=settings.COMMUNITY, version=2)

in_octets = session.get(f"ifHCInOctets.{settings.IFINDEX}")
out_octets = session.get(f"ifHCOutOctets.{settings.IFINDEX}")

print(f"Octets in: {in_octets.value}")  # pylint: disable=no-member
print(f"Octets out: {out_octets.value}")  # pylint: disable=no-member

try:
    response = requests.post(
        url=settings.INFLUXDB_URL,
        headers={"Content-type": "text:plain"},
        data=f"octets,host={settings.HOST},interface=wan,direction=in value={in_octets.value}\n"  # pylint: disable=no-member
        f"octets,host={settings.HOST},interface=wan,direction=out value={out_octets.value}",  # pylint: disable=no-member
        auth=(settings.INFLUXDB_USER, settings.INFLUXDB_PASSWORD),
    )
except requests.exceptions.ConnectionError:
    print(f"[-] {sys.exc_info()[1]} <ConnectionError>")
    sys.exit()

if response.status_code != 204:
    print(
        f"[-] Http post operation to InfluxDB resulted in unexpected status code: "
        f"{response.status_code}"
    )
    sys.exit()

print(f"[+] Influx status code: {response.status_code}")
