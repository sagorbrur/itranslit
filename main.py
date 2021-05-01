from itranslit.transliterate import Translit

trans = Translit('ta')

res = trans.predict('ami')
print(res)