import json

"""
№[0]    Наименование раздела /темы дисциплины[1]    Содержание лекций[2]    Содержание семинаров[3]    № первой недели[4]    Число недель[5]    Часов лекций[6]    Часов семинаров[7]    Часов лабораторных[8]    Часов самостоятельной работы[9]    Текущий контроль (форма)[10] Максимальный балл[11]
"""

def CSV2JSON( csvname ):
  jsonname = csvname.replace(".","_") + ".json"
  INP = open(csvname,"r",encoding="utf-8")
  OUT = open(jsonname,"w", encoding = "utf-8")
  OUT.write( "  \"Section\":[\n" )
  for s in INP:
    ss = s.split('&')
    if ss[2] == "":
      OUT.write("    {\"Title\":\""+ss[1] + "\",\n      \"Subsection\":[\n")
    elif len(ss) >= 11:
      OUT.write("        {\n          \"Title\":\""+ss[1] + "\",\n" )
      OUT.write("          \"LectureHours\":"+str(int(ss[6]) ) +", ")
      OUT.write("\"PracticeHours\":"+str(int(ss[7] ) ) + ", " )
      OUT.write("\"LabHours\":" + str(int(ss[8] ) ) + ", " )
      OUT.write("\"SelfWork\":" + str(int(ss[9] ) ) + ", " )
      OUT.write("\"WeekBegin\":" + str(int(ss[4] ) ) + ", " )
      OUT.write("\"Weeks\":" + str(int(ss[5] ) ) + ", " )
      OUT.write("\"Control\":\"" + ss[10] + "\", " )
      if len(ss) >= 12: OUT.write("\"MaxBall\":\"" + ss[11].replace("\n","") + "\",\n" )
      else: OUT.write("\"MaxBall\":\"\",\n" )
      OUT.write( "          \"LecturesContents\":\"" + ss[2] + "\", " )
      OUT.write( "\"PracticeContents\":\"" + ss[3] + "\"\n        },\n" )
  OUT.write("  ]\n" )
  INP.close()
  OUT.close()
  return

def JSON2CSV( jsonname ):
  INP = open(jsonname,"r",encoding="utf-8")
  dis = json.load( INP )
  csvname = jsonname.replace(".","_") + ".csv"  
  OUT = open(csvname,"w", encoding = "utf-8")
  OUT.write( "№&Наименование раздела /темы дисциплины&Содержание лекций&Содержание семинаров&№ первой недели&Число недель&Часов лекций&Часов семинаров&Часов лабораторных&Часов самостоятельной работы&Текущий контроль (форма)&Максимальный балл\n")
  sec = dis["Section"]
  numsec = 1
  for s in sec:
    OUT.write( str(numsec) + ".&" + s["Title"] + "\n" )
    numsubsec = 1
    for ss in s["Subsection"]:
      OUT.write( str(numsec) + "." + str(numsubsec) + ".&" + ss["Title"] + "&" + ss["LecturesContents"] + "&" + ss["PracticeContents"] + "&" + str( ss["WeekBegin"] ) + "&" + str( ss["Weeks"] )+ "&" + str( ss["LectureHours"] )+ "&" + str( ss["PracticeHours"] )+ "&" + str( ss["LabHours"] )+ "&" + str( ss["SelfWork"] )+ "&" + ss["Control"] + "&" + str( ss["MaxBall"] )+"\n" )
      numsubsec += 1
    numsec += 1
  INP.close()
  OUT.close()
  return

fjson = "JSON010302/010302-11-Б1_О_11-Теория_вероятностей_и_математическая_статистика.json"
JSON2CSV( fjson )

