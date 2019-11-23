
class Employee:
    num_of_emps=0
    raise_amount=1.04
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+last+'@company.com'
        Employee.num_of_emps+=1
    def fullname(self):
        return ('{} {}'.format(self.first,self.last))

    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay=emp_str.split('-')
        return cls(first,last,pay)

emp_1=Employee("imran","khan",100000)
emp_2=Employee("naveed","ur rehman",100000)

#
# emp_str_1='john-doe-7000'
#
# new_emp_1=Employee.from_string(emp_str_1)
#
# print(new_emp_1.email)
# print(new_emp_1.pay)
