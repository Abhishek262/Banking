import pickle
class Student :
    def __init__(self ,rno = 0, name = ''):
        self.rno = rno
        self.name = name
    def ww(self):
        print self.rno ,self.name
        
##s = Student(5665,"reddy")
##f = file('b','wb')
##pickle.dump(s,f)
m = file('b','rb')
try:
    y = pickle.load(m)
except EOFError :
    m.close()

y.ww()
