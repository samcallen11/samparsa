from googletrans import Translator
s = Translator()
x= 'what are you doing now'
print('is calculating')


res = s.translate( x , dest = 'fr', src = 'en')
res = res.text


# for displace the result
res = res.split()
m = ''
l = len(res)

for i in range(l ):
    m += res[l - 1 - i] + ' '
   
    


print(m)

