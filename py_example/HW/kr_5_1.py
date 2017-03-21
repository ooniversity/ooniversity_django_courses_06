from datetime import datetime
from datetime import date


class Person:

    def __init__(self,surname,first_name, birth_date,nickname = None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        if  nickname is  None :
            surname
        birth_date_tmp = datetime.strptime(birth_date,"%Y-%m-%d")
        self.birth_date = birth_date_tmp.date()

    def get_age(self,):

         now_date = datetime.now().date()
         birthday = self.birth_date
         delta = now_date.year- birthday.year
         print(self.birth_date)
         print(now_date.month)
         print(birthday.month)
         if now_date.month < birthday.month :
            delta -=1
         return delta
    def get_fullname(self):
        return self.surname+' '+self.first_name

petroff = Person("Petrov", "Petro", "1952-01-02")
print(petroff.get_age())
print(datetime.now())
print(petroff.birth_date)
# datetime.date(2000, 10, 20)