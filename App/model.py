from io import TextIOBase
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

class ufo:
  def __init__(self,pack,analyzer):
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
  global analyzer
  analyzer = {}
  # EXHIBITION
  analyzer['exhibition'] = {'total':0,'list':lt.newList()}
  # CITY
  analyzer['cities map'] = mp.newMap(19900,loadfactor = 1, maptype = 'CHAINING')
  analyzer['best city'] = {'best':None,'count':0}
  # DURATION
  analyzer['duration rbt'] = rbt.newMap(cmpduration) 
  analyzer['best duration'] = {'best':None,'count':0}
  # TIME
  analyzer['time rbt'] = rbt.newMap(cmptime)
  analyzer['best time'] = {'best':None,'count':0} 
  analyzer['time prints'] = {'count':0,'ufos':rbt.newMap(cmptimedate)}
  # DATE
  analyzer['date map'] = mp.newMap(numelements = 10525, maptype = 'CHAINING', loadfactor = 1) 
  analyzer['best date'] = {'best':None,'count':0} 
  analyzer['date lst'] = lt.newList(datastructure = 'ARRAY_LIST',cmpfunction = cmpdate) 
  analyzer['date prints'] = {'count':0,'ufos':rbt.newMap(cmpdatetime)}
  analyzer['date rbt'] = rbt.newMap(cmpdate)
  # LONGITUDE AND LATITUDE
  analyzer['longitude map'] = mp.newMap(numelements = 6977, maptype = 'CHAINING', loadfactor = 1) 
  analyzer['longitude lst'] = lt.newList(datastructure = 'ARRAY_LIST',cmpfunction = cmplongitude)

  analyzer['ufos'] = lt.newList(datastructure = 'ARRAY_LIST') # TODO
  return analyzer

######### DEFAULTS #########

def exhibition(analyzer,ufo):
    if analyzer['exhibition']['total'] < 10:
        lt.addLast(analyzer['exhibition']['list'],ufo)
    elif analyzer['exhibition']['total'] >= 10:
        lt.deleteElement(analyzer['exhibition']['list'],6)
        lt.addLast(analyzer['exhibition']['list'],ufo)
    analyzer['exhibition']['total']+=1

def citydefault(analyzer,ufo):
  # CITY 
  new = {}
  new['count'] = 1
  new['ufos'] = rbt.newMap(cmpdatetime)
  rbt.put(new['ufos'],ufo,None)
  mp.put(analyzer['cities map'],ufo.city,new)
def datedefault(analyzer,ufo):
  # DATE
  new = {}
  new['count'] = 1
  new['ufos'] = rbt.newMap(cmpdatetime)
  new['position'] = lt.size(analyzer['date lst']) + 1
  rbt.put(new['ufos'],ufo,None)
  mp.put(analyzer['date map'],ufo.date,new)
def datedefaultrbt(analyzer,ufo):
  # DATE
  new = {}
  new['count'] = 1
  new['ufos'] = rbt.newMap(cmpdatetime)
  rbt.put(new['ufos'],ufo,None)
  rbt.put(analyzer['date rbt'],ufo.date,new)
def timedefault(analyzer,ufo):
  # TIME
  new = {}
  new['count'] = 1
  new['ufos'] = rbt.newMap(cmptimedate)
  rbt.put(new['ufos'],ufo,None)
  rbt.put(analyzer['time rbt'],ufo.time,new)
############################


######### GET THE BEST FOR EACH KEY #########
def bestcity(analyzer,ufo):
  count = analyzer['best city']['count']
  current = me.getValue(mp.get(analyzer['cities map'],ufo.city))['count']
  if current > count:
    analyzer['best city']['count'] = current
    analyzer['best city']['best'] = ufo.city
def bestdate(analyzer,ufo):
  if analyzer['best date']['best'] == None:
    analyzer['best date']['best'] = ufo.date
    analyzer['best date']['count'] = 1
  elif cmpdate(ufo.date,analyzer['best date']['best']) == 1:
    analyzer['best date']['best'] = ufo.date
    analyzer['best date']['count'] = 1
  elif cmpdate(ufo.date,analyzer['best date']['best']) == 0:
    analyzer['best date']['count'] += 1
def besttime(analyzer,ufo):
  if analyzer['best time']['best'] == None:
    analyzer['best time']['best'] = ufo.time
    analyzer['best time']['count'] = 1
  elif cmptime(ufo.time,analyzer['best time']['best']) == -1:
    analyzer['best time']['best'] = ufo.time
    analyzer['best time']['count'] = 1
  elif cmptime(ufo.time,analyzer['best time']['best']) == 0:
    analyzer['best time']['count'] += 1
######### ### ### #### ### #### ### #########

######### ADD #########
def add(analyzer,pack):
  new = ufo(pack,analyzer)
  exhibition(analyzer,new)
  lt.addLast(analyzer['ufos'],new)
  check = lambda key,mapkey : mp.get(analyzer[mapkey],key)
  # PUT UFO IN cities ############################
  mapkey = 'cities map'
  key = new.city
  check_ = check(key,mapkey)
  if check_ == None:
    citydefault(analyzer,new)
  else:
    target = me.getValue(check_)
    # ADD FIRST 3 AND LAST 3
    prints(target,new,cmpdatetime)
    target['count'] += 1
  bestcity(analyzer,new)
  # PUT UFO IN date ############################
  mapkey = 'date map'
  key = new.date
  check_ = check(key,mapkey)
  if check_ == None:
    datedefault(analyzer,new)
  else:
    target = me.getValue(check_)
    rbt.put(target['ufos'],new,None)
  lt.addLast(analyzer['date lst'],key)
  bestdate(analyzer,new)
  # PUT UFO IN date rbt ############################
  mapkey = 'date rbt'
  key = new.date
  check_ = rbt.get(analyzer[mapkey],key)
  if check_ == None:
    datedefaultrbt(analyzer,new)
  else:
    target = me.getValue(check_)
    target['count'] += 1
    rbt.put(target['ufos'],new,None)
  # PUT UFO IN time ############################
  mapkey = 'time rbt'
  key = new.time
  check_ = rbt.get(analyzer[mapkey],key)
  if check_ == None:
    timedefault(analyzer,new)
  else:
    target = me.getValue(check_)
    target['count'] += 1
    rbt.put(target['ufos'],new,None)
  besttime(analyzer,new)
######### ### #########

def prints(target,ufo,cmp):
  # ADD FIRST 3 AND LAST 3
  if target['count'] < 6:
    rbt.put(target['ufos'],ufo,None)
  if target['count'] >= 6:
    keys = rbt.keySet(target['ufos'])
    sixth = lt.getElement(keys,6)
    fifth = lt.getElement(keys,5)
    fourth = lt.getElement(keys,4)
    third = lt.getElement(keys,3)
    second = lt.getElement(keys,2)
    first = lt.getElement(keys,1)
    if cmp(ufo,sixth) == -1 or cmp(ufo,fifth) == -1 or cmp(ufo,fourth) == -1:
      rbt.remove(target['ufos'],third)
      rbt.put(target['ufos'],ufo,None)
      return
    keys = rbt.keySet(target['ufos'])
    sixth = lt.getElement(keys,6)
    fifth = lt.getElement(keys,5)
    fourth = lt.getElement(keys,4)
    third = lt.getElement(keys,3)
    second = lt.getElement(keys,2)
    first = lt.getElement(keys,1)
    if cmp(ufo,first) == 1 or cmp(ufo,second) == 1 or cmp(ufo,third) == 1:
      rbt.remove(target['ufos'],fourth)
      rbt.put(target['ufos'],ufo,None)
      return

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  AFTER LOADED  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def sort(analyzer):
  # CITIES
  # keys = mp.keySet(analyzer['cities map'])
  # for key in lt.iterator(keys):
  #   target = me.getValue(mp.get(analyzer['cities map'],key))
  #   lst = target['ufos']
  #   cmp = cmpdatetime
  #   mergesorting(lst,cmp)
  # LONGITUDE
  # DATE
  pass

def mergesorting(lst, cmp):
  start_time = time.process_time()
  sortedL = merge.sort(lst, cmp)
  stop_time = time.process_time()
  elapsed_time_mseg = (stop_time - start_time)*1000
  return (sortedL, f'time: {elapsed_time_mseg}')
     
def quicksorting(lst, cmp):
  start_time = time.process_time()
  sortedL = quick.sort(lst, cmp)
  stop_time = time.process_time()
  elapsed_time_mseg = (stop_time - start_time)*1000
  return (sortedL, f'time: {elapsed_time_mseg}')


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  CMP  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$


# CMP FUNCTIONS F0R MAP KEYS

def cmpcity(cityi: ufo, cityj: ufo):
  indi = 0
  indj = 0
  while indi < len(cityi) and indj < len(cityj):
    i = cityi[indi]
    j = cityj[indj]
    if i == j:
      indi += 1
      indj += 1
      continue
    if ord(i) < ord(j):
      return 1
    else:
      return -1
  return 0
def cmpduration(durationi: ufo, durationj: ufo):
  if durationi < durationj:
    return 1
  elif durationi > durationj:
    return -1
  return 0
def cmptime(timei: ufo, timej: ufo):
  if timei < timej:
    return 1
  elif timei > timej:
    return -1
  return 0
def cmptimerbt(ufoi,ufoj):
  ti = ufoi.gettime()
  tj = ufoj.gettime()
  return cmptime(ti,tj)
def cmpdate(datei, datej):
  if datei < datej:
    return 1
  elif datei > datej:
    return -1
  return 0
def cmplongitude(longitudei: ufo, longitudej: ufo):
  if longitudei < longitudej:
    return 1
  elif longitudei > longitudej:
    return -1
  return 0
def cmpdurationcountrycity(ufoi: ufo, ufoj: ufo):
  return
def cmpdatetime(ufoi: ufo, ufoj: ufo):
  if ufoi.date == ufoj.date:
    return cmptime(ufoi.time, ufoj.time)
  else:
    return cmpdate(ufoi.date,ufoj.date)
def cmplatitude(latitudei: ufo, latitudej: ufo):
  if latitudei < latitudej:
      return 1
  elif latitudei > latitudej:
      return -1
  return 0
def cmptimedate(ufoi: ufo, ufoj: ufo):
  if ufoi.gettime() == ufoj.gettime():
    return cmpdate(ufoi.date,ufoj.date)
  else:
    return cmptime(ufoi.time,ufoj.time)

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  REQS  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

def req1(analyzer,city):
  check = mp.get(analyzer['cities map'],city)
  if check == None:
    return 0
  else:
    target = me.getValue(check)
    return target

def req2(analyzer):
  pass

def req3(analyzer,ti,tf):
  defaultvalues = rbt.values(analyzer['time rbt'],tf,ti)
  for default in lt.iterator(defaultvalues):
    for ufo in lt.iterator(rbt.keySet(default['ufos'])):
      prints(analyzer['time prints'],ufo,cmptimedate)
      analyzer['time prints']['count'] += 1

def req4(analyzer,datei,datef):
  datei = datetime.date.fromisoformat(datei)
  datef = datetime.date.fromisoformat(datef)
  defaultvalues = rbt.values(analyzer['date rbt'],datef,datei)
  for default in lt.iterator(defaultvalues):
    for ufo in lt.iterator(rbt.keySet(default['ufos'])):
      prints(analyzer['date prints'],ufo,cmpdatetime)
      analyzer['date prints']['count'] += 1

def req5(analyzer,longi,longf,lati,latf):
  # -103.00 a -109.05 y una latitud desde 31.33 a 37.00
  return