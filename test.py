import json
import MdRPD

disfile = "JSON010302/010302-40-Б1_В_09-Элементы_прикладной_математики__введение_в_специальность.json"
disfile = "JSON010302/010302-10-Б1_О_10-Дифференциальные_уравнения.json"
compfile = "competence010302.json"

OUT = open("test.md","w",encoding='utf-8')
OUT.write( MdRPD.StringForDisc( disfile, compfile ) )
OUT.close()

