import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import rbt
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.Algorithms.Sorting import quicksort as quick
import datetime
import sys
import time
from math import floor
assert cf
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  DATA  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

class newufo:
  def __init__(self,pack):
    date_time = pack['datetime'][:16].strip()
    date_ = datetime.date.fromisoformat(pack['datetime'][:16].strip()[:-6])
    time_ = pack['datetime'][:16].strip()[-5:] # ex: '3/10/2004 23:00'
    country = pack['country'].strip()
    city = pack['city'].strip()
    try:
      duration = round(float(pack['duration (seconds)'].strip()),2)
    except:
      duration = None
    shape = pack['shape'].strip()
    try:
      latitude = round(float(pack['latitude'].strip()),2)
    except:
      latitude = None
    try:
      longitude = round(float(pack['longitude'].strip()),2)
    except:
      longitude = None
    self.datetime = date_time
    self.date = date_
    self.time = time_
    self.country = country
    self.city = city
    self.duration = duration
    self.shape = shape
    self.latitude = latitude
    self.longitude = longitude

  def gettime(self):
    try:
      secs = round(float(self.time[-2:])*60,2)
      secs += round(float(self.time[:2])*3600,2)
    except:
      secs = None
    return secs

  def printufo(self):
    print('___________________________________________________________________________________________')
    print(f"| datetime: {self.datetime} | date: {self.date} | time: {self.time} | country: {self.country} |")
    print(f"| city: {self.city} | duration: {self.duration} | shape: {self.shape} | latitude: {self.latitude} | longitude: {self.longitude} |")
    print('___________________________________________________________________________________________')

def initanalyzer():
  analyzer = {}
  # EXHIBITION
  analyzer['exhibition'] = {'total':0,'list':lt.newList()}
  # CITY
  # DURATION
  # TIME
  # DATE
  # LONGITUDE AND LATITUDE
  return analyzer

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  ADD  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def exhibition(analyzer,ufo):
    if analyzer['exhibition']['total'] < 10:
        lt.addLast(analyzer['exhibition']['list'],ufo)
    elif analyzer['exhibition']['total'] >= 10:
        lt.deleteElement(analyzer['exhibition']['list'],6)
        lt.addLast(analyzer['exhibition']['list'],ufo)
    analyzer['exhibition']['total']+=1

def everything(analyzer,pack):
    ufo = newufo(pack)
    exhibition(analyzer,ufo)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  AFTER LOADED  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  CMP  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$



#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  REQS  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def req1(analyzer,city):
  pass
def req2(analyzer):
  pass
def req3(analyzer,ti,tf):
  pass
def req4(analyzer,datei,datef):
  pass
def req5(analyzer,longi,longf,lati,latf):
  pass