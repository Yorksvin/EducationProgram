import os
import json
import MdRPD

disfiles = ["JSON010302/010302-10-Б1_О_10-Дифференциальные_уравнения.json", "JSON010302/010302-40-Б1_В_09-Элементы_прикладной_математики__введение_в_специальность.json", "JSON010302/010302-26-Б1_О_ДВ_01_01-Введение_в_теорию_алгоритмов.json","JSON010302/010302-11-Б1_О_11-Теория_вероятностей_и_математическая_статистика.json",
"JSON010302/010302-27-Б1_О_ДВ_01_02-Элементы_теории_графов.json"]

compfile = "competence010302.json"

for f in disfiles:
  g = f.replace("JSON010302","res").replace(".json", ".md" )
  OUT = open(g,"w",encoding='utf-8')
  OUT.write( MdRPD.StringForDisc( f, compfile ) )
  OUT.close()

