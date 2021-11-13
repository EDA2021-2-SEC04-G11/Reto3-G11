import config as cf
import model
import csv

# FOR SMALL FILE:
#TOTAL UFOS = 803
#cities keys = 679
#durations keys = 58
#time keys = 249
#date keys = 750
#longitude keys = 632
#latitude max count amougnst keys = 8

# FOR LARGE FILE:
#TOTAL UFOS = 80332
#cities keys = 19900
#duration keys = 533
#time keys = 1390
#date keys = 10525
#longitude keys = 6977
#latitude max count amougnst keys = 614

# EMPTY analyzer

def initanalyzer():
  return model.initanalyzer()

# LOAD DATA

def loaddata(analyzer):
  load(analyzer)

def load(analyzer):
  filedir = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
  file = csv.DictReader(open(filedir, encoding='utf-8'))
  for ufo in file:
    model.add(analyzer,ufo)

# REQUIREMENTS

def req1(analyzer,city):
  return model.req1(analyzer,city)

def req2(analyzer):
  return model.req2(analyzer)

def req3(analyzer,ti,tf):
  return model.req3(analyzer,ti,tf)

def req4(analyzer,di,df):
  return model.req4(analyzer,di,df)

def req5(analyzer,longi,longf,lati,latf):
  return model.req5(analyzer,longi,longf,lati,latf)