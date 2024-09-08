#!/usr/bin/env python
import json
import os

INP = open( "010402-07-Б1_О_07-Численные_методы_газовой_динамики.json", "r", encoding = "utf-8" )
RP = json.load( INP )

OUT = open( "testChMGD.tex", "w", encoding = "utf-8" )

OUT.write("""
\\documentclass[a4paper,12pt]{article} %article %12
\\pagestyle{plain}
\\usepackage[utf8]{inputenc} % Включаем поддержку UTF8
\\usepackage[english,russian]{babel}  % Включаем пакет для поддержки русского языка
\\usepackage{cmap}
\\usepackage[T2A]{fontenc}
\\usepackage{graphicx}
\\usepackage{amsmath}
\\usepackage{alltt}
\\usepackage{tabularx}
\\usepackage{indentfirst}
\\usepackage{float}
\\usepackage{breqn}
\\usepackage{esint}
\\usepackage{enumitem}
\\usepackage{amssymb}
\\usepackage{fancybox}
\\usepackage[urlcolor=blue]{hyperref}
\\textwidth=17cm
\\oddsidemargin=0pt
\\topmargin=-2cm
\\topskip=0pt
\\textheight=27cm
\\renewcommand
\\baselinestretch{1.25} % полуторный интервал
\\graphicspath{{./images/}}\n\n
\\begin{document}\n
""")

OUT.write("\\section{Структура и содержание дисциплины}")
nt = 1
for theme in RP["StructureAndContents"]:
  OUT.write("\n\nТема %i. " %(nt) + theme["ThemeTitle"] )
  ns = 1
  for sec in theme["Sections"]:
    OUT.write("\n\nРаздел %i.%i " %(nt, ns) + sec )
    ns += 1
  nt += 1

OUT.write("\\section{Вопросы к экзамену}")
for sem in RP["ExamQuestions"]:
  OUT.write("\n\\begin{center} Семестр %i\\end{center}\n" %(sem["Semester"]) )
  n = 1
  for t in sem["Questions"]:
    OUT.write("\n\n%i. " %(n) + t )
    n += 1

OUT.write("\\section{Билеты к экзамену}")
for sem in RP["ExamTickets"]:
  OUT.write("\n\\begin{center} Семестр %i\\end{center}\n" %(sem["Semester"]) )
  n = 1
  for t in sem["Tickets"]:
    OUT.write("\n\n%i. " %(n) + t )
    n += 1
    
OUT.write("\\section{Упражнения}")
for i in range( len( RP["Exersizes"] ) ):
  OUT.write("\n\n%i. " %(i+1) + RP["Exersizes"][i] )

OUT.write("\\section{Курсовые работы}")
for i in range( len( RP["CourseWork"] ) ):
  OUT.write("\n\n%i. " %(i+1) + RP["CourseWork"][i] )
  

OUT.write("\\end{document}\n")  
