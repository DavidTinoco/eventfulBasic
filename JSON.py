#-*- coding:utf-8 -*-

import requests
import json
import os

url_base = "http://api.eventful.com/json"
ciudad = raw_input("Ciudad: ")
busqueda = raw_input("Busqueda: ")
key = os.environ["key1"]
payload = {'app_key':key,'keywords':busqueda,'location':ciudad,'date':'Future'}
r=requests.get(url_base + '/events/search',params=payload)

if r.status_code == 200:
    print "Los eventos de la ciudad",ciudad,"son:"
    print ""
    doc = r.json()

    for a in doc["events"]["event"]:
    	cadtit = a["title"]
    	cadtit = cadtit.encode("utf-8")
        print "Evento",cadtit,":"
        cadrea = a["venue_address"]
        if cadrea == None:
        	cadrea = "Sin datos"w 
        else:
        	cadrea = cadrea.encode("utf8")
        cadurl = a["venue_url"]
        cadurl = cadurl.encode("utf8")
        print "Se realiza en",cadrea,". Podemos ver más información sobre este evento en",cadurl
        print ""
        
