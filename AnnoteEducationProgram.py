import os
import json

def StrOfInt(i):
  if i == 0:
    return ""
  else:
    return ( "%i" %( i ) )

def TitlePageString( disfilename ):
  INP = open( disfilename, "r", encoding = "utf-8" )
  dis = json.load( INP )
  return """\\documentclass[a4paper,12pt]{article}
\\pagestyle{plain}
\\usepackage[pdftex,unicode]{hyperref}
\\usepackage{mathtext}
\\usepackage[T2A]{fontenc}
\\usepackage[utf8]{inputenc}
\\usepackage[russian]{babel}
\\usepackage{amsmath,amssymb}
\\usepackage{amsxtra}
\\usepackage{color}
\\usepackage{array}
\\usepackage{verbatim}
\\usepackage{appendix}
\\usepackage{rotating}
\\usepackage{longtable}
\\textheight=24cm
\\textwidth=16.5cm
\\topmargin=-1cm
\\oddsidemargin=0cm
\\makeatletter
\\renewcommand\\thesubsection{}
\\makeatother
\\setcounter{secnumdepth}{0}
\\begin{document}
\\renewcommand{\\contentsname}{Оглавление}

\\thispagestyle{empty}
\\phantom{,}\\vskip-1cm\\hskip-1cm
\\parbox{18cm}{
\\begin{center}
МИНИСТЕРСТВО НАУКИ И ВЫСШЕГО ОБРАЗОВАНИЯ РОССИЙСКОЙ ФЕДЕРАЦИИ\\\\
ФЕДЕРАЛЬНОЕ ГОСУДАРСТВЕННОЕ АВТОНОМНОЕ ОБРАЗОВАТЕЛЬНОЕ\\\\
УЧРЕЖДЕНИЕ ВЫСШЕГО ОБРАЗОВАНИЯ\\\\
<<Национальный исследовательский ядерный университет <<МИФИ>>\\\\
{\\bf Саровский физико-технический институт --}\\\\
филиал федерального государственного автономного образовательного учреждения высшего\\\\
образования <<Национальный исследовательский ядерный университет <<МИФИ>>\\\\
({\\bf СарФТИ НИЯУ МИФИ})\\\\[2cm]
{\\bf ФИЗИКО-ТЕХНИЧЕСКИЙ ФАКУЛЬТЕТ}\\\\[2cm]
{\\bf АННОТАЦИИ К РАБОЧИМ ПРОГРАММАМ}
\\end{center}
}

\\vfill
\\hskip-1cm
\\parbox{18cm}{
\\begin{tabular}{p{0.5\\textwidth}p{0.5\\textwidth}}
\\begin{flushleft}Направление подготовки (специальность)\\end{flushleft}& \\begin{flushleft}%s\\end{flushleft}\\\\[-5mm]\\cline{2-2}
&\\\\[-5mm]
\\begin{flushleft}Наименование образовательной программы\\end{flushleft}&\\begin{flushleft}%s\\end{flushleft} \\\\[-5mm]\\cline{2-2}
&\\\\[-5mm]
\\begin{flushleft}Квалификация (степень) выпускника\\end{flushleft} &\\begin{flushleft} %s \\end{flushleft}\\\\[-5mm]\\cline{2-2}
&\\\\[-5mm]
\\begin{flushleft}Форма обучения\\end{flushleft} & \\begin{flushleft}очная\\end{flushleft}\\\\[-5mm]\\cline{2-2}
\\end{tabular}
}
\\vfill

\\centerline{г.~Саров, 2022 г.}
\\newpage

\\tableofcontents
\\newpage
""" %(dis["TrainingDirection"], dis["EducationProgram"], dis["Degree"])

def TableHours( dis ):
  s = """\\begin{tabular}{|p{1.5cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|p{1.15cm}|}\\hline
\\rotatebox{90}{Семестр}&
\\rotatebox{90}{\\parbox[c]{4.5cm}{В форме практической\\\\подготовки}}&
\\rotatebox{90}{Трудоемкость, кред.}&
\\rotatebox{90}{\\parbox[c]{4.5cm}{Общий объем курса,\\\\час.}}&
\\rotatebox{90}{Лекции, час.}&
\\rotatebox{90}{Практич. занятия, час.}&
\\rotatebox{90}{Лаборат. работы, час.}&
\\rotatebox{90}{СРС, час.}&
\\rotatebox{90}{КР/ КП}&
\\rotatebox{90}{\\parbox[c]{4.5cm}{Форма(ы) контроля,\\\\Экз/Зач/ЗсО/}}\\\\\\hline\n"""
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
      itogo.append( sem["PrivateWork"] )
    else:
      itogo[0] += sem["ZET"]
      itogo[1] += sem["VolumeHours"]
      itogo[2] += sem["LecturesHours"]
      itogo[3] += sem["PracticeHours"]
      itogo[4] += sem["LaboratoryHours"]
      itogo[5] += sem["PrivateWork"]
    s += "%i&&" %( sem["Id"] )
    s += "%s&" %( StrOfInt( sem["ZET"] ) )
    s += "%s&" %( StrOfInt( sem["VolumeHours"] ) )
    s += "%s&" %( StrOfInt( sem["LecturesHours"] ) )
    s += "%s&" %( StrOfInt( sem["PracticeHours"] ) )
    s += "%s&" %( StrOfInt( sem["LaboratoryHours"] ) )
    s += "%s&&" %( StrOfInt( sem["PrivateWork"] ) )
    s += "%s\\\\\\hline\n" %( sem["ControlForm"][0:3] )
  s += "{\\bf ИТОГО}&&{\\bf %s}&" %( StrOfInt( itogo[0] ) )
  s += "{\\bf %s}&" %( StrOfInt( itogo[1]  ) )
  s += "{\\bf %s}&" %( StrOfInt( itogo[2]  ) )
  s += "{\\bf %s}&" %( StrOfInt( itogo[3]  ) )
  s += "{\\bf %s}&" %( StrOfInt( itogo[4]  ) )
  s += "{\\bf %s}&&" %( StrOfInt( itogo[5]  ) )
  s += "\\\\\\hline\\end{tabular}\n\n\\bigskip\n"
  return s

def UniversalCompetenceNum( discomplist, UC ):
  res = []
  for d in discomplist:
    for i in range( len( UC ) ):
      if d == UC[i]["Id"]:
        res.append( i )
  return res

def ProfessionalCompetenceNum( discomplist, PC ):
  res = []
  for P in PC:
    res.append([])
    for d in discomplist:
      for i in range( len( P["Competence"] ) ):
        if d == P["Competence"][i]["Id"]:
          res[ len(res) - 1 ].append( i )
  return res

def TableUniversalCompetence( discomplist, UC ):
  s = ""
  u = UniversalCompetenceNum( discomplist, UC )
  for i in u:
    if s == "":
      s += """\\begin{center}Универсальные и общепрофессиональные компетенции:\\end{center}
\\begin{longtable}{|p{0.45\\textwidth}|p{0.5\\textwidth}|}\\hline
Код и наименование компетенции& Код и наименование индикатора достижения компетенции\\\\\\hline\n"""
    s += UC[i]["Id"] + " " + UC[i]["Contents"]
    s += "&" + UC[i]["Knowledge"]["Id"] + " " + UC[i]["Knowledge"]["Contents"]
    s += "; " + UC[i]["Ability"]["Id"] + " " + UC[i]["Ability"]["Contents"]
    s += "; " + UC[i]["Skill"]["Id"] + " " + UC[i]["Skill"]["Contents"] + "\\\\\\hline\n"
  if s != "":
    s += "\\end{longtable}\n\n"
  return s

def TableProfessionalCompetence( discomplist, PC ):
  s = ""
  PP = ProfessionalCompetenceNum( discomplist, PC )
  for j in range( len( PP ) ):
    if len( PP[j] ):
      if s == "":
        s += """\\begin{center}Профессиональные компетенции в соответствии с задачами и объектами (областями знаний) профессиональной деятельности:\\end{center}
\\begin{longtable}{|p{0.25\\textwidth}|p{0.25\\textwidth}|p{0.25\\textwidth}|p{0.25\\textwidth}|}\\hline
Задача профессиональной деятельности (ЗПД)& Объект или область знания&Код и наименование профессиональной компетенции&
Код и наименование индикатора достижения профессиональной компетенции\\\\\hline"""
      s += "\\multicolumn{4}{|c|}{" + PC[j]["TypeTaskPD"] +"}\\\\\\hline\n"
      s += PC[j]["TaskPD"] + "&" + PC[j]["ObjectField"] + "&"
      for i in range( len( PP[j] ) ):
        q = PC[j]["Competence"][PP[j][i]]
        if i:
          s += "\n&&"
        s += q["Id"] + " " + q["Contents"] + " Основание: " + q["ProfStandard"] + "&"
        s += q["Knowledge"]["Id"] + " " + q["Knowledge"]["Contents"]
        s += "; " + q["Ability"]["Id"] + " " + q["Ability"]["Contents"]
        s += "; " + q["Skill"]["Id"] + " " + q["Skill"]["Contents"] + "\\\\\\hline\n"
  if s != "":
    s += "\\end{longtable}\n\n"
  return s

def StringForDisc( disfilename, compfilename, planfilename ):
  INP1 = open( disfilename, "r", encoding = "utf-8" )
  dis = json.load( INP1 )
  INP2 = open( compfilename, "r", encoding = "utf-8" )
  comp = json.load( INP2 )
  INP3 = open( planfilename, "r", encoding = "utf-8" )
  plan = json.load( INP3 )
  numdis = -1
  for i in range( len( plan["Disciplines"] ) ):
    if dis["Name"] == plan["Disciplines"][i]["Name"]:
      numdis = i
  if numdis == -1:
    print( "Discipline " + dis["Name"] + "  not found in " + planfilename )
    return ""      
  res = ""
  #TITLE
#  res += ("\\section*{%s}\\addcontentsline{toc}{section}{%s}" %( dis["Name"].upper(), dis["Name"].upper() ) )
  res += ("\\subsection{%s}" %( dis["Name"].upper() ) )
  #TABLE WITH HOURS
  res += TableHours( dis )
  #ANNOTE
  res += ( "\\noindent" + dis["Annote"] )
  #AIMS
  res += ( "\n\\bigskip\n\n\\noindent{\\bf ЦЕЛИ И ЗАДАЧИ ОСВОЕНИЯ УЧЕБНОЙ ДИСЦИПЛИНЫ}\\\\" )
  res += ( dis["Aims"] )
  #PLACE IN STRUCTURE
  res += ("\n\\bigskip\n\n\\noindent{\\bf МЕСТО УЧЕБНОЙ ДИСЦИПЛИНЫ В СТРУКТУРЕ ООП ВО}\\\\" )
#  res += ( "Дисциплина <<" + dis["Name"] + ">> "+ dis["PlaceInStructure"] + " "+ dis["TrainingDirection"] )
  res += dis["PlaceInStructure"]
  res += ("\n\\newpage\\noindent{\\bf ФОРМИРУЕМЫЕ КОМПЕТЕНЦИИ И ПЛАНИРУЕМЫЕ РЕЗУЛЬТАТЫ ОБУЧЕНИЯ}\n" )
  #UNIVERSAL COMPETENCE
  uc = TableUniversalCompetence( plan["Disciplines"][numdis]["Competence"], comp["UniversalCompetence"] )
  res += ( uc )
  if uc != "":
    res += ("\n\\newpage")
  pc = TableProfessionalCompetence( plan["Disciplines"][numdis]["Competence"], comp["ProfessionalCompetence"] )
  res += ( pc )
  if pc != "":
    res += ("\n\\newpage")
  return res

def WriteProgram( disfoldername, compfilename, planfilename, resfilename ):
  disnames = os.listdir( "./" + disfoldername )
  disnames.sort()
  OUT = open( resfilename ,"w", encoding = "utf-8")
  OUT.write( TitlePageString( "./" + disfoldername + "/" + disnames[0] ) )
  for d in disnames:
    dname = "./" + disfoldername + "/" + d
    OUT.write( StringForDisc( dname, compfilename, planfilename ) )
  OUT.write("\n\\end{document}")
  return

if __name__ == '__main__':
#WriteProgram( "JSON010302", "competence010302.json","annot010302.tex" )
  WriteProgram( "JSON010402", "competence010402Logos.json","010402_plan_csv.json","annot010402.tex" )
