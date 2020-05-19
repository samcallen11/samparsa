import os
class Sclass:
    def __init__(self, studentn, teachers, news, sessions, name, repeatation, Sclass):
        
        self.StudentNumber = studentn
        self.Teachers = teachers
        self.News = news
        self.Sessions = sessions
        self.Name = name
        self.Repeatation = repeatation
        self.Sclass = Sclass
file_path = os.path.join("/home/sami/Documents/h3school/Computer/pajoheshi/pss-master/class/" ,"class_info.txt")
file = open(file_path, 'r')
lines = file.readlines()
classess = {}
def sam_split(x):
    nat = x
    t = -1
    for i in x:
        t += 1
        if i == "'":
            nat = nat[:t] + nat[t+1:]
            
            t -= 1

    
    nat = nat.split(',')
    return nat
            

for i in lines:
    i = i.split()
    
    if i != []:
        if not i[0] in classess:
            classess[i[0]] = []
        i[5] = sam_split(i[5])[0]
        
        if not os.path.exists('/home/sami/Documents/h3school/Computer/pajoheshi/pss-master/classess/school_class/' + i[5]) and i[5] != "'-'" and i[5] != "'":
            os.mkdir('/home/sami/Documents/h3school/Computer/pajoheshi/pss-master/classess/school_class/' + i[5])


        for c in i[4]:
            c = c.split(':')
            
            if not os.path.exists('/home/sami/Documents/h3school/Computer/pajoheshi/pss-master/classess/school_class/' + c[0]):
                os.mkdir('/home/sami/Documents/h3school/Computer/pajoheshi/pss-master/classess/school_class/' + c[0])
            
            
        

        
        classess[i[0]] += [Sclass(i[1], sam_split(i[2]), i[3], i[4], i[5], sam_split(i[6]), 'school_class')]



        





'''
Math = Sclass(0, ['Mr rasoli'], '', '', 'Math')

Quran = Sclass(0, [''], '', '', 'Quran')

Maaref_takmily = Sclass(0, [''], '', '', 'Maaaref_takmily')

Computer = Sclass(0, ['Mr mohhamady', 'Mr mahdavi'], '', '', 'Computer')
English = Sclass(0, ['Mr Fatemi'], '', '', 'English')
Physic = Sclass(0, ['Mr Ostad azim'], '', '', 'Physic')
Work = Sclass(0, ['Mr Givechian'], '', '', 'Work')
About_science = Sclass(0, ['Mr tahmasebi'], '', '', 'About_science')
Laboratory = Sclass(0, [''], '', '', 'Laboratory')
Chemistry = Sclass(0, [''], '', '', 'Chemistry')
Sport = Sclass(0, [''], '', '', 'Sport')
Literature = Sclass(0, [''], '', '', 'Literature')
Arabic = Sclass(0, [''], '', '', 'Arabic')
History = Sclass(0, [''], '', '', 'History')
Writing = Sclass(0, [''], '', '', 'Writing')
Biology = Sclass(0, [''], '', '', 'Biology')
Advice = Sclass(0, [''], '', '', 'Advice')
Art = Sclass(0, [''], '', '', 'Art')
Research_Class = Sclass(0, [''], '', '', 'Research_Class')
Education = Sclass(0, [''], '', '', 'Education')
Scaning = Sclass(0, [''], '', '', 'Scaning')
Social_Studies = Sclass(0, [''], '', '', 'Social_Studies')
O = Sclass(0, [''], '', '', '-')
'''
