from itranslit.transliterate import Translit

trans = Translit('bn')

res = trans.predict('ami')
print(res)