#li = [-9,-1,-8,2,7,3,6,4,5]
#tup = [9,1,8,2,7,3,6,4,5]

#s_tup=sorted(tup)

#print('sorted tuple',s_tup)

#s_li=sorted(li,key=abs)
#print('sorted list',s_li)


#li.sort(reverse=True)
#print('original variable{}'.format(li))

class Employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary

    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1=Employee('carl',37,70000)
e2=Employee('sarah',29,80000)
e3=Employee('jj',43,90000)
def e_sort(emp):
    return emp.salary

employees=[e1,e2,e3]
s_employees=sorted(employees,key=e_sort,reverse=True)
print(s_employees)
