#!/usr/bin/env python
import json
import os

def FindAbsentDiscipline( lecturerFile : str, disciplinesFolder : str ) -> None:
# READING THE DISCIPLINES LIST WITH WORKPROGRAM
  rpnames = os.listdir( "./" + disciplinesFolder )
  RP = []
  for r in rpnames:
    rpname = "./" + disciplinesFolder + "/" + r
    if r.count( ".json" ) > 0:
      INP2 = open( rpname, "r", encoding = "utf-8" )
      rr = json.load( INP2 )
      RP.append( rr["Name"] )
#CHECK IF DISCIPLINES ARE IN THE LIST
  INP1 = open( "./" + lecturerFile, "r", encoding = "utf-8" )
  dis = json.load( INP1 )
  for i in range( len( dis["Disciplines"] ) ):
    dd = dis["Disciplines"][i]["Name"]
    if dd not in RP:
      print( dd )
  
if __name__ == '__main__':
  FindAbsentDiscipline( "lecturer.json", "JSON010402" )  

