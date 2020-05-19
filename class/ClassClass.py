import sys
from  Classes import classess
sys.path.append('/home/sami/Documents/h3school/Computer/pajoheshi/pss-master/class/')
def clear_class(x):
    t = -1
    for i in x:
        t += 1
        if i == '':
            del x[t]
    return x

def defualt_class():
    x = []
    for i in range(6):
        x += [[0] * 6]
    
    return x

'''
c202 =      ([Quran, Math, Maaref_takmily, Math, Computer, Computer],
             [English, English, Physic, Work, Physic, About_science],
             [Math, Laboratory, Math, Chemistry, Math, Work],
             [Sport, Sport, Literature, Literature, Arabic, History],
             [Writing, Biology, Advice, Art, Research_Class, Research_Class],
             [Education, Scaning, Social_Studies, Scaning, O, O]

                  )


c201 =     ([Math, Maaref_takmily, Computer, Computer, Math, Quran],
            [English, English, Work, Physic, About_science, Physic],
            [Laboratory, Math, Chemistry, Math, Work, Math],
            [Literature, Literature, Sport, Sport, History, Arabic],
            [Biology, Writing, Art, Advice, Research_Class, Research_Class],
            [Scaning, Education, Scaning, Social_Studies, O, O]

            )
'''
Classes = {}
for i in classess:
    if not i in Classes:
        Classes[i] = defualt_class()
     
    for c in classess[i]:
        
             
        for d in clear_class(c.Repeatation):
            d = d.split('-')
            
            Classes[i][int(d[0]) - 1][int(d[1]) - 1] = c
       




