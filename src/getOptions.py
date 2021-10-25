# optionName="" もしくはoptionName=''もしくはoptionName=○○もしくはoptionNameで定義された入力オプションを検出して辞書化する

def _trim(string):
  if len(string) == 0:
    return ''
  elif string[0] == '\'' or string[0] == '\"':
    return string[1:-1]
  else:
    return string


def getDict(args, dict={}):
  for arg in args:
    eqindex = arg.find('=')
    if eqindex == -1:
      dict[arg] = True
    else:
      dict[arg[:eqindex]] = _trim(arg[eqindex + 1:])
  return dict


def toInt(dictionary, optionName):
  if type(dictionary[optionName]) is not int:
    dictionary[optionName] = int(dictionary[optionName])