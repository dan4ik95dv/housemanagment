#!/usr/bin/bash
set -x
./manage.py makemigrations &&
	./manage.py migrate &&
	./manage.py loaddata initial companies srvprov arbitrary meter_types