from googletrans import Translator
s = Translator()
srclanguage=input("src:")
destlanguage=input("dest:")
dest=destlanguage[0]+destlanguage[1]
dest=dest.lower()
#to become it unCapslock
src=srclanguage[0]+srclanguage[1]
src=src.lower()
x= input()
print('is calculating')
res = s.translate( x , dest = dest, src = src)
res = res.text
print(res)
