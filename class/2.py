class student:
    def __init__(self,uname,pword):
        self.username = uname
        self.password = pword
students_list = {}
#uname = input()
#pword = input()
#Rpword = input()
#print('your re-enter password is incorect')
#while pword != Rpword:
#    word = input()
#    Rpword = input()
uname = 'sami'
pword = '1384'
x = student( uname ,pword)
students_list[uname , pword] = x


uname = 'sami1'
pword = '13841'
x = student(uname,pword)
students_list[uname , pword] = x





uname = input()
pword = input()
while not (uname ,pword)  in students_list:
    print('your username or password is incorect')
    
    uname = input()
    pword = input()
me = students_list[uname,pword]
print('Welcome' , me.username)
