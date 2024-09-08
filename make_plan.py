import sys

def MakePlan( filein : str )-> str:
  INP = open( filein, "r", encoding = "utf_8" )
  OUT = open( filein.replace(".","_")+".json", "w", encoding = "utf_8" )
  OUT.write("""{
  \"Disciplines\" : [
""")
  numdis = 0
  for s in INP:
    ss = s.replace( "\\","").split("&")
    if len( ss ) >= 5:
      if numdis > 0:
        OUT.write(",\n")
      OUT.write("  {\n")
      OUT.write("    \"Id\" : \"%s\",\n" % ( ss[0].replace(" ","") ) )
      OUT.write("    \"Name\" : \"%s\",\n" % ( ss[1] ) )
      comp = ss[4].replace(" ","").replace("\n","").split(";")
      OUT.write("    \"Competence\" : [" )
      for i in range(len(comp)):
        if i != 0:
          OUT.write(",")
        OUT.write( "\"%s\"" %(comp[i]) )
      OUT.write( "],\n" )            
      OUT.write("    \"Lecturer\" : \"%s\",\n" % ( ss[2] ) )
      OUT.write("    \"Seminarian\" : \"%s\"\n" % ( ss[3] ) )
      OUT.write("  }")
      numdis += 1
  OUT.write("""
  ]
}""")

if __name__ == '__main__':
  MakePlan( sys.argv[1] )


    
