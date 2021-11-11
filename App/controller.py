import config as cf
import model
import csv

# EMPTY analyzer

def initanalyzer():
  return model.initanalyzer()

# LOAD DATA

def loaddata(analyzer):
  load(analyzer)
  sort(analyzer)
  #model.test(analyzer)

def load(analyzer):
  filedir = cf.data_dir + 'UFOS/UFOS-utf8-small.csv'
  file = csv.DictReader(open(filedir, encoding='utf-8'))
  for ufo in file:
    model.add(analyzer,ufo)

def sort(analyzer):
  model.sort(analyzer)
  
def changestate(analyzer):
  model.changestate(analyzer)

# REQUIREMENTS

def req1(analyzer,city):
  return model.req1(analyzer,city)

def req2(analyzer):
  return model.req2(analyzer)

def req3(analyzer,ti,tf):
  return model.req3(analyzer,ti,tf)

def req4(analyzer,di,df):
  return model.req4(analyzer,di,df)

def req6(analyzer):
  return model.req6(analyzer)

def req5(analyzer,longi,longf,lati,latf):
  return model.req5(analyzer,longi,longf,lati,latf)