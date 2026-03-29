import json
import MdRPD

disfile = "JSON010302/010302-10-Б1_О_10-Дифференциальные_уравнения.json"
disfile = "JSON010302/010302-26-Б1_О_ДВ_01_01-Введение_в_теорию_алгоритмов.json"
disfile = "JSON010302/010302-40-Б1_В_09-Элементы_прикладной_математики__введение_в_специальность.json"
compfile = "competence010302.json"

OUT = open("test.md","w",encoding='utf-8')
OUT.write( MdRPD.StringForDisc( disfile, compfile ) )
OUT.close()

