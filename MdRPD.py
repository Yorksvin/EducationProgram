import os
import json

def StrOfInt(i):
  if i == 0:
    return ""
  else:
    return ( "%i" %( i ) )

def BoldStrOfInt(i):
  if i == 0:
    return ""
  else:
    return ( "**%i**" %( i ) )

def Interval( beg, length ):
  if length == 1:
    return str( beg )
  return str(beg)+ "-" + str( beg + length - 1 )

def TitlePageString( distitle, direction, program, qualification ):
  return r"""
### МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ
### ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ АВТОНОМНОЕ ОБРАЗОВАТЕЛЬНОЕ
### УЧРЕЖДЕНИЕ ВЫСШЕГО ОБРАЗОВАНИЯ
### «Национальный исследовательский ядерный университет «МИФИ»
### Саровский физико-технический институт -
### филиал федерального государственного автономного образовательного учреждения высшего
### образования «Национальный исследовательский ядерный университет «МИФИ»
### (СарФТИ НИЯУ МИФИ)

### ФИЗИКО-ТЕХНИЧЕСКИЙ ФАКУЛЬТЕТ
### Кафедра прикладной математики

|               | УТВЕРЖДАЮ                 |
|---------------|---------------------------|
|               |Декан физико-технического  |
|               |факультета СарФТИ НИЯУ МИФИ|
|               |_____________ А.К.Чернышев |
|               |_____________ 20__ г.  |

### РАБОЧАЯ ПРОГРАММА ДИСЦИПЛИНЫ 
### %s
(наименование дисциплины)

| | |
|----------------------------------------|----------------------------------------------------|
| Направление подготовки (специальность) | %s |
| Наименование образовательной программы | %s |
| Квалификация выпускника                | %s |
| Форма обучения                         | очная                                              |

г. Саров, 2026 г.
""" %(distitle, direction, program, qualification)

def TableHours( dis ):
  s = r"""
|Семестр | В форме практической подготовки | Трудоемкость, кред.| Общий объем курса, час. | Лекции, час. | Практич. занятия, час.| Лаборат. работы, час. | СРС, час. | КР/ КП | Форма(ы) контроля, Экз/Зач/ЗсО |
|--------|--------------|---------------|-----------|------------|----------------|-------------|---------------|-------------|--------------|
"""
  itogo = []
  semm = dis["Semester"]
  for i in range( len( semm ) ):
    sem = semm[i]
    if i == 0:
      itogo.append( sem["ZET"] )
      itogo.append( sem["VolumeHours"] )
      itogo.append( sem["LecturesHours"] )
      itogo.append( sem["PracticeHours"] )
      itogo.append( sem["LaboratoryHours"] )
      itogo.append( sem["SelfWork"] )
    else:
      itogo[0] += sem["ZET"]
      itogo[1] += sem["VolumeHours"]
      itogo[2] += sem["LecturesHours"]
      itogo[3] += sem["PracticeHours"]
      itogo[4] += sem["LaboratoryHours"]
      itogo[5] += sem["SelfWork"]
    s += "|%i | |" %( sem["Id"] )
    s += "%s|" %( StrOfInt( sem["ZET"] ) )
    s += "%s|" %( StrOfInt( sem["VolumeHours"] ) )
    s += "%s|" %( StrOfInt( sem["LecturesHours"] ) )
    s += "%s|" %( StrOfInt( sem["PracticeHours"] ) )
    s += "%s|" %( StrOfInt( sem["LaboratoryHours"] ) )
    s += "%s| |" %( StrOfInt( sem["SelfWork"] ) )
    s += "%s|\n" %( sem["ControlForm"][0:3] )
  s += "|**ИТОГО**| |%s| " %( BoldStrOfInt( itogo[0] ) )
  s += "%s| " %( BoldStrOfInt( itogo[1]  ) )
  s += "%s| " %( BoldStrOfInt( itogo[2]  ) )
  s += "%s| " %( BoldStrOfInt( itogo[3]  ) )
  s += "%s|" %( BoldStrOfInt( itogo[4]  ) )
  s += "%s| |" %( BoldStrOfInt( itogo[5]  ) )
  return s

def UniversalCompetenceNum( dis, UC ):
  res = []
  for d in dis["Competence"]:
    for i in range( len( UC ) ):
      if d == UC[i]["Id"]:
        res.append( i )
  return res

def ProfessionalCompetenceNum( dis, PC ):
  res = []
  for P in PC:
    res.append([])
    for d in dis["Competence"]:
      for i in range( len( P["Competence"] ) ):
        if d == P["Competence"][i]["Id"]:
          res[ len(res) - 1 ].append( i )
  return res

def TableUniversalCompetence( dis, UC ):
  s = ""
  u = UniversalCompetenceNum( dis, UC )
  for i in u:
    if s == "":
      s += """|Код и наименование компетенции| Код и наименование индикатора достижения компетенции|
|------------------------------|-----------------------------------------------------|\n"""
    s += "|" + UC[i]["Id"] + " " + UC[i]["Contents"]
    s += "|" + UC[i]["Knowledge"]["Id"] + " " + UC[i]["Knowledge"]["Contents"]
    s += "; " + UC[i]["Ability"]["Id"] + " " + UC[i]["Ability"]["Contents"]
    s += "; " + UC[i]["Skill"]["Id"] + " " + UC[i]["Skill"]["Contents"] + "|\n"
  if s != "":
    s += "\n"
  return s

def TableProfessionalCompetence( dis, PC ):
  s = ""
  PP = ProfessionalCompetenceNum( dis, PC )
  for j in range( len( PP ) ):
    if len( PP[j] ):
      if s == "":
        s += """
|Задача профессиональной деятельности (ЗПД)| Объект или область знания|Код и наименование профессиональной компетенции|Код и наименование индикатора достижения профессиональной компетенции|
|---------------------------|------------------|----------------------|----------------------------------|\n"""
      s += "|  | " + PC[j]["TypeTaskPD"] +" |  |  |\n"
      s += "|" + PC[j]["TaskPD"] + "|" + PC[j]["ObjectField"] + "|"
      for i in range( len( PP[j] ) ):
        q = PC[j]["Competence"][PP[j][i]]
        if i:
          s += "| | |"
        s += q["Id"] + " " + q["Contents"] + " Основание: " + q["ProfStandard"] + "|"
        s += q["Knowledge"]["Id"] + " " + q["Knowledge"]["Contents"]
        s += "; " + q["Ability"]["Id"] + " " + q["Ability"]["Contents"]
        s += "; " + q["Skill"]["Id"] + " " + q["Skill"]["Contents"] + "|\n"
  if s != "":
    s += "\n\n"
  return s

def TableThemeInStructure( dis, p ):
  sec = dis["Section"][p-1]
  s = "|"
  s += str( p ) + "|" + sec["Title"] + "| | | | | | | |\n"
  numsub = 1
  for sub in sec["Subsection"]:
    s += "|" + str(p) + "." + str( numsub ) + "|" + sub["Title"] + "|" + Interval( sub["WeekBegin"], sub["Weeks"] ) + "|" + str( sub["LectureHours"] ) + "|" + str( sub["PracticeHours"] ) + "|"
    s += str( sub[ "LabHours" ] ) + "|" + str( sub["SelfWork" ] ) + "|" + sub["Control"] + "| "
    if sub["MaxBall"] != "": s += str( sub["MaxBall"] )
    s +=" |\n"
    numsub += 1
  return s

def TableThemeInSectionsLectures( dis, p ):
  sec = dis["Section"][p-1]
  s = "|"
  s += str( p ) + "|" + sec["Title"] + "| |\n"
  numsub = 1
  for sub in sec["Subsection"]:
    s += "|" + str(p) + "." + str( numsub ) + "|" + sub["Title"] + "|" + sub["LecturesContents"] + "|\n"
    numsub += 1
  return s
  
def TableThemeInSectionsPractice( dis, p ):
  sec = dis["Section"][p-1]
  s = "|"
  s += str( p ) + "|" + sec["Title"] + "| |\n"
  numsub = 1
  for sub in sec["Subsection"]:
    l = sub["PracticeContents"]
    if l == "":
      l = sub["LecturesContents"]
    s += "|" + str(p) + "." + str( numsub ) + "|" + sub["Title"] + "|" + l + "|\n"
    numsub += 1
  return s

def TableStructure( dis ):
  s = """|№ п/п|Наименование раздела/темы дисциплины |№ недели | Виды учебной работы | | | |Текущий контроль (форма)*|Максимальный балл |
|----|----|----|----|----|----|----|----|----|
| | | |**Лекции** |**Практ. занятия/семинары** |**Лаб. работы** |**СРС** | | |
"""
  hours = []
  semm = dis["Semester"]
  for i in range( len( semm ) ):
    sem = semm[i]
    if i == 0:
      hours.append( sem["LecturesHours"] )
      hours.append( sem["PracticeHours"] )
      hours.append( sem["LaboratoryHours"] )
      hours.append( sem["SelfWork"] )
    else:
      hours[0] += sem["LecturesHours"]
      hours[1] += sem["PracticeHours"]
      hours[2] += sem["LaboratoryHours"]
      hours[3] += sem["SelfWork"]
  s += "| | | |" 
  s += "%s| " %( BoldStrOfInt( hours[0]  ) )
  s += "%s| " %( BoldStrOfInt( hours[1]  ) )
  s += "%s| " %( BoldStrOfInt( hours[2]  ) )
  s += "%s| | |\n" %( BoldStrOfInt( hours[3] ) )
  plan = dis["Structure"]
  for p in plan:
    if isinstance( p, str ):
      s += "| |" + p + " | | | | | | | |\n"
    elif isinstance( p, list ):
      s += "| |" + p[0]["Control"] + "|"+ str( p[1]["How"]["Week"] ) + "| | | | |" + p[1]["How"]["Form"] + "|"+str(p[1]["How"]["MaxBall"]) + "| \n"
    elif isinstance( p, int ):
      s += TableThemeInStructure( dis, p )
  return s

def TableSectionsLectures( dis ):
  s = """|№ |Наименование раздела/темы дисциплины | Содержание |
|----|----|----|
"""
  plan = dis["Structure"]
  for p in plan:
    if isinstance( p, int ):
      s += TableThemeInSectionsLectures( dis, p )
  return s

def TableSectionsPractice( dis ):
  s = """|№ |Наименование раздела/темы дисциплины | Содержание |
|----|----|----|
"""
  plan = dis["Structure"]
  for p in plan:
    if isinstance( p, int ):
      s += TableThemeInSectionsPractice( dis, p )
  return s

def ZUN( dis, comp ):
  s = ""
  u = UniversalCompetenceNum( dis, comp["UniversalCompetence"] )
  for i in u:
    U = comp["UniversalCompetence"][i]
    if s != "": s += "; "
    s += U["Knowledge"]["Id"]+ "; " + U["Ability"]["Id"] + "; " + U["Skill"]["Id"]
  PC = comp["ProfessionalCompetence"]
  PP = ProfessionalCompetenceNum( dis, PC )
  for j in range( len( PP ) ):
    if len( PP[j] ):
      for i in range( len( PP[j] ) ):
        if s != "": s += "; "
        q = PC[j]["Competence"][PP[j][i]]
        s += q["Knowledge"]["Id"]+ "; " + q["Ability"]["Id"] + "; " + q["Skill"]["Id"]
  return s

def TableThemeInFOS( dis, p, compdis, zun ):
  sec = dis["Section"][p-1]
  s = "|" + str( p ) + "|" + sec["Title"] + "| | | |\n"
  numsub = 1
  for sub in sec["Subsection"]:
    s += "|" + str(p) + "." + str( numsub ) + "|" + sub["Title"] + "|" + compdis + "|" + zun + "| "
    if sub["Control"] != "": s += sub["Control"] + ", " + Interval( sub["WeekBegin"],sub["Weeks"] )
    s +="|\n"
  return s

def TableFOS( dis, comp ):
  s = """
|№ |Темы |Компетенция | Индикаторы освоения | Текущий контроль, неделя |
|----|----|----|----|----|
"""
  plan = dis["Structure"]
  compdis = ""
  for c in dis["Competence"]:
    if compdis != "": compdis += " "
    compdis += c
  zun = ZUN( dis, comp )
  for p in plan:
    if isinstance( p, str ):
      s += "| |" + p + " | | | |\n"
    elif isinstance( p, list ) and p[0]["Control"].count("Посещаемость") == 0:
      s += "| |" + p[0]["Control"] + "|"+ compdis + "| " + zun + " | " + p[1]["How"]["Form"]
      week = str( p[1]["How"]["Week"] )
      if week != "": s += ", " + week
      s += "|\n"
    elif isinstance( p, int ):
      s += TableThemeInFOS( dis, p, compdis, zun )
  return s

def FOSElementString( f ):
  res = ""
  if isinstance( f["List"][0], str ):
    for i in range( len( f["List"] ) ):
      res += str( i + 1 ) + ". " + f["List"][i] + "\n"
  elif isinstance( f["List"][0], list ) and isinstance( f["List"][0][1], str ):
# БИЛЕТЫ К ЭКЗАМЕНУ
    for i in range( len( f["List"] ) ):
      if f["Unit"] != "": res += f["Unit"] + " № " + str( i + 1 ) + "\n\n"
      for j in range( len( f["List"][i] ) ):
        res += str( j + 1 ) + ". " + f["List"][i][j] + "\n\n"
  elif isinstance( f["List"][0], list ) and isinstance( f["List"][0][1], list ):
# ВАРИАНТЫ КОНТРОЛЬНЫХ
    for i in range( len( f["List"] ) ):
      res += "#### " + f["List"][i][0] + "\n"
      for j in range( 1, len( f["List"][i] ) ):
        if f["Unit"] != "": res += f["Unit"] + " № " + str( j ) + "\n"
        for k in range( len( f["List"][i][j] ) ):
          res += str( k + 1 ) + ". " + f["List"][i][j][k] + "\n"
        res += "\n"
  return res

def StringForDisc( disfilename, compfilename ):
  INP1 = open( disfilename, "r", encoding = "utf-8" )
  dis = json.load( INP1 )
  INP2 = open( compfilename, "r", encoding = "utf-8")
  comp = json.load( INP2 )
  res = ""
  #TITLE
  res += TitlePageString( dis["Name"], dis["TrainingDirection"], dis["EducationProgram"], dis["Degree"] )
  #TABLE WITH HOURS
  res += TableHours( dis )
  #ANNOTE
  res += ( "\n\n# АННОТАЦИЯ\n\n" + dis["Annote"] )
  #AIMS
  res += ( "\n\n# 1. ЦЕЛИ И ЗАДАЧИ ОСВОЕНИЯ УЧЕБНОЙ ДИСЦИПЛИНЫ\n" )
  res += ( dis["Aims"] )
  #PLACE IN STRUCTURE
  res += ("\n\n# 2. МЕСТО УЧЕБНОЙ ДИСЦИПЛИНЫ В СТРУКТУРЕ ООП ВО\n" )
  res += dis["PlaceInStructure"]  
  res += "\n\nИзучение дисциплины предполагает у студентов владение материалом дисциплин:\n"
  res += dis["Background"].replace( "--", "-" )
  res += ("\n\n# 3. ФОРМИРУЕМЫЕ КОМПЕТЕНЦИИ И ПЛАНИРУЕМЫЕ РЕЗУЛЬТАТЫ ОБУЧЕНИЯ\n" )
  #UNIVERSAL COMPETENCE
  res += ("\n\n## 3.1 Универсальные и общепрофессиональные компетенции\n" )
  res += ( TableUniversalCompetence( dis, comp["UniversalCompetence"] ) )
  #PROFESSIONAL COMPETENCE
  res += "\n\n## 3.2 Профессиональные компетенции в соответствии с задачами и объектами (областями знаний) профессиональной деятельности\n"
  res += TableProfessionalCompetence( dis, comp["ProfessionalCompetence"] )
  #STRUCTURE AND CONTENTS
  res += "\n\n# 4. СТРУКТУРА И СОДЕРЖАНИЕ УЧЕБНОЙ ДИСЦИПЛИНЫ\n"
  res += "## 4.1 Структура учебной дисциплины\n"
  res += TableStructure( dis )
  res += "\n**\\*Сокращение наименований форм текущего, рубежного и промежуточного контроля:**\n\n" 
  res += dis["AbbreviationsForControl"]
  res += "\n\n## 4.2 Содержание дисциплины, структурированное по разделам (темам)\n"
  res += "### 4.2.1 Лекционный курс\n"
  res += TableSectionsLectures( dis )
  res += "\n### 4.2.2 Практические/семинарские занятия\n"
  res += TableSectionsPractice( dis )
  #FOS PASSPORT
  res += "# 5. ОЦЕНОЧНЫЕ СРЕДСТВА ДЛЯ ТЕКУЩЕГО КОНТРОЛЯ УСПЕВАЕМОСТИ, ПРОМЕЖУТОЧНОЙ АТТЕСТАЦИИ ПО ИТОГАМ ОСВОЕНИЯ ДИСЦИПЛИНЫ\n"
  res += dis["FOSAnnote"]
  res += "\n## 5.1 Паспорт фонда оценочных средств по дисциплине\n"
  res += "Связь между формируемыми компетенциями и формами контроля их освоения представлена в следующей таблице:\n"
  res += TableFOS( dis, comp )
  res += "\n\n## 5.2. Типовые контрольные задания или иные материалы, необходимые для оценки знаний, умений, навыков и (или) опыта деятельности, характеризующие этапы формирования компетенций в процессе освоения образовательной программы\n"
  n = 1
  for f in dis["FOS"]:
    res += "### 5.2." + str(n) + ". " + f["Title"] + "\n\n"  
    res += FOSElementString( f )
    if f["Criteria"] != "" and f["Scale"] != "":
      res += "#### 5.2." + str(n) + ".1. Критерии оценивания\n"
      res += f["Criteria"]
      res += "\n#### 5.2." + str(n) + ".2. Шкалы оценивания\n"
      res += f["Scale"]+"\n\n"
    n += 1
  res += "# 6. УЧЕБНО-МЕТОДИЧЕСКОЕ И ИНФОРМАЦИОННОЕ ОБЕСПЕЧЕНИЕ УЧЕБНОЙ ДИСЦИПЛИНЫ\n"
  n = 1
  for p in dis["MethodicalSupport"]:
    res += "## 6." + str( n ) + ". " + p["Title"] + "\n"
    res += p["Contents"] + "\n"
    n += 1
  res += "# 7. МАТЕРИАЛЬНО-ТЕХНИЧЕСКОЕ ОБЕСПЕЧЕНИЕ УЧЕБНОЙ ДИСЦИПЛИНЫ\n"
  res += dis["MaterialSupport"] + "\n"
  res += "# 8. ОБРАЗОВАТЕЛЬНЫЕ ТЕХНОЛОГИИ\n"
  res += dis["EducationalTechnologies"] + "\n"
  res += "# 9. МЕТОДИЧЕСКИЕ РЕКОМЕНДАЦИИ СТУДЕНТАМ ПО ОРГАНИЗАЦИИ ИЗУЧЕНИЯ ДИСЦИПЛИНЫ\n"
  res += dis["MethodicalRecomendations"] + "\n\n"
  res += "Программа составлена в соответствии с требованиями ОС ВО НИЯУ МИФИ к обязательному минимуму содержания основной образовательной программы по направлению подготовки " + dis["TrainingDirection"] + "\n\n"
  res += "Автор(ы): " + dis["Author"] + "\n"
  return res

#WriteProgram( "JSON010302", "competence010302.json","annot010302.tex" )
#WriteProgram( "JSON010402", "competence010402Logos.json","annot010402.tex" )

