import json
import MdRPD
import TeXRPD

def TestJSON( f ):
  INP1 = open( f, "r", encoding = "utf-8" )
  dis = json.load( INP1 )
  print( "File " + f + " for \ndiscipline \"" + dis["Name"] + "\" read.\nJSON seems to be correct\n" )
  return

def FOS_JSON2TEX( f ):
  OUT = open("test_FOS.tex","w",encoding='utf-8')
  OUT.write( TeXRPD.StringForFOS( f ) )
  OUT.close()

f = "JSON010302/010302-11-Б1_О_11-Теория_вероятностей_и_математическая_статистика.json"

### ПРОТЕСТИРОВАТЬ JSON:
TestJSON( f )

### СДЕЛАТЬ ТЕХ-ФАЙЛ С ЭЛЕМЕНТАМИ ФОНДА ОЦЕНОЧНЫХ СРЕДСТВ
### (ДЛЯ РАБОТЫ НЕОБХОДИМО, ЧТОБ JSON БЫЛ КОРРЕКТНЫМ)
# FOS_JSON2TEX( f )

