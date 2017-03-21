from datetime import datetime
import csv


class Person:
    def __init__(self,surname,first_name, birth_date,nickname = None):
        self.surname = surname
        self.first_name = first_name
        if nickname is None:
            self.nickname = self.surname
        else:
            self.nickname = nickname
        birth_date_tmp = datetime.strptime(birth_date,"%Y-%m-%d")
        self.birth_date = birth_date_tmp.date()
    def get_age(self,):
         now_date = datetime.now().date()
         birthday = self.birth_date
         delta = now_date.year- birthday.year
         if now_date.month < birthday.month :
            delta -=1
         return delta
    def get_fullname(self):
        return self.surname+' '+self.first_name

def find_oldest_person(filename):
    fp = open(filename,'r')
    tmp_csv = csv.reader(fp)
    d = []
    tmp_dict = {}
    for item in tmp_csv:
        d.append(item)
    for item in d[1:]:
        l = len(item)
        if len(item) > 3:
            person = Person(item[0], item[1], item[2], item[3])
        else:
            person = Person(item[0], item[1], item[2])
        person_age = person.get_age()
        person_fulname = person.get_fullname()
        tmp_dict[person_age]=person_fulname
    oldest = max(tmp_dict)
    oldest_person = tmp_dict[oldest]
    return oldest_person

print(find_oldest_person('persons2.csv'))
