import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
from DISClib.DataStructures import rbt
from DISClib.ADT import map as mp
assert cf

default_limit = 1000
sys.setrecursionlimit(default_limit*10)

def printMenu():
  print("<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
  print("Welcome")
  print("1- REQ 1")
  print("2- REQ 2")
  print("3- REQ 3")
  print("4- REQ 4")
  print("5- REQ 5")
  print("6- REQ 6")
  print("7- EXIT")

def charge():
  start_time = time.process_time()
  print('\n\n ... LOADING DATA ...\n\n')
  analyzer = initanalyzer()
  loaddata(analyzer)
  print('\n\n ... DATA LOADED ...\n\n')
  stop_time = time.process_time()
  elapsed_time_mseg = round((stop_time - start_time)*1000,2)
  print(f"Total UFO loaded: {analyzer['exhibition']['total']}")
  print(f"First 5 and last 5:")
  for i in lt.iterator(analyzer['exhibition']['list']):
    i.printufo()
  print(f"TIME : {round(elapsed_time_mseg,2)}")
  input('\nPRESS ENTER TO CONTINUE')
  return analyzer

def initanalyzer():
  return controller.initanalyzer()

def loaddata(analyzer):
  controller.loaddata(analyzer)

def req1(analyzer):
  print('+-+-+-+-+-+-+-+-+ REQ 1 +-+-+-+-+-+-+-+-+\n')
  # INPUTS
  city = input('City?\n').strip()
  if city == 'test':
    city = 'las vegas'
  # DATA
  start_time = time.process_time()
  target = controller.req1(analyzer,city)
  stop_time = time.process_time()
  timef = round((stop_time - start_time)*1000,2)
  # PRINT
  print('\n')
  print(f"The best city so far is {analyzer['best city']['best']}, with {analyzer['best city']['count']} UFO's.")
  print(f"We've found {target['count']} UFO's in the city {city}.")
  print('The last 3 and first 3 UFO found in this city are:')
  for i in lt.iterator(rbt.keySet(target['ufos'])):
    i.printufo()
  print(f"TIME REQUIRED : {timef}")

def req2(analyzer):
  return
  print('+-+-+-+-+-+-+-+-+ REQ 2 +-+-+-+-+-+-+-+-+\n')
  # INPUTS
  # DATA
  start_time = time.process_time()
  pack = controller.req2()
  stop_time = time.process_time()
  timef = round((stop_time - start_time)*1000,2)
  # PRINT
  print(f"TIME REQUIRED : {timef}")

def req3(analyzer):
  # 20:45  23:15
  print('+-+-+-+-+-+-+-+-+ REQ 3 +-+-+-+-+-+-+-+-+\n')
  # INPUTS
  ti = input('Initial time?\n').strip()
  if ti == 'test':
    ti = '20:45'
    tf = '23:15'
    print(ti,tf)
  else:
    tf = input('final time?\n').strip()
  # DATA
  start_time = time.process_time()
  controller.req3(analyzer,ti,tf)
  stop_time = time.process_time()
  timef = round((stop_time - start_time)*1000,2)
  # PRINT
  lst = rbt.keySet(analyzer['time prints']['ufos'])
  count = analyzer['time prints']['count']
  print(f"Lastest time: {analyzer['best time']['best']} count: {analyzer['best time']['count']}")
  print(f"There are {count} UFO's reported in that range of time.")
  print(f"Last 3 and first 3 are:")
  for i in lt.iterator(lst):
    i.printufo()
  print(f"TIME REQUIRED : {timef}")

def req4(analyzer):
  # 1945-08-06      1984-11-15
  print('+-+-+-+-+-+-+-+-+ REQ 4 +-+-+-+-+-+-+-+-+\n')
  # INPUTS
  di = input('Initial date?\n').strip()
  if di == 'test':
    di = '1945-08-06'
    df = '1984-11-15'
    print(di,' || ',df)
  else:
    df = input('End date?\n').strip()
  # DATA
  start_time = time.process_time()
  controller.req4(analyzer,di,df)
  stop_time = time.process_time()
  timef = round((stop_time - start_time)*1000,2)
  # PRINT
  lst = rbt.keySet(analyzer['date prints']['ufos'])
  count = analyzer['date prints']['count']
  print(f"Worst date: {analyzer['best date']['best']} count: {analyzer['best date']['count']}")
  print(f"There are {count} UFO's reported in that range of date.")
  print(f"Last 3 and first 3 are:")
  for i in lt.iterator(lst):
    i.printufo()
  print(f"TIME REQUIRED : {timef}")

def req5(analyzer):
  return
  # -103.00 a -109.05 y una latitud desde 31.33 a 37.00
  print('+-+-+-+-+-+-+-+-+ REQ 5 +-+-+-+-+-+-+-+-+\n')
  # INPUTS
  longi = float(input('Min longitude?\n').strip())
  longf = float(input('Max longitude?\n').strip())
  lati = float(input('Min latitude?\n').strip())
  latf = float(input('Max latitude?\n').strip())
  # DATA
  start_time = time.process_time()
  pack = controller.req5(analyzer,longi,longf,lati,latf)
  stop_time = time.process_time()
  timef = round((stop_time - start_time)*1000,2)
  # PRINT
  print(f"TIME REQUIRED : {timef}")

def req6(analyzer):
  return
  print('+-+-+-+-+-+-+-+-+ REQ 6 +-+-+-+-+-+-+-+-+\n')
  # INPUTS
  # DATA
  start_time = time.process_time()
  pack = controller.req6()
  stop_time = time.process_time()
  timef = round((stop_time - start_time)*1000,2)
  # PRINT
  print(f"TIME REQUIRED : {timef}")

"""
Main menu
"""
analyzer = charge()
while True:
  printMenu()
  while True:
    try:
      option = int(input('Choose an option to continue\n').strip()[0])
      print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>')
      break
    except:
      continue
  if option == 1:
    req1(analyzer)
  elif option == 2:
    req2(analyzer)
  elif option == 3:
    req3(analyzer)
  elif option == 4:
    req4(analyzer)
  elif option == 5:
    req5(analyzer)
  elif option == 6:
    req6(analyzer)
  elif option == 7:
    sys.exit(0)
  input('\nPRESS ENTER TO CONTINUE')
sys.exit(0)