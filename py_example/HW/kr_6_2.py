import csv
class Student:

    def __init__(self,name,config):
        self.name = name
        self.lab_max = config['lab_max']
        self.lab_num = config['lab_num']
        self.labs = [0] * self.lab_num


    def set_lab(self,score,number = None):
        # Add  None  checker  .....Проверку  на None
        if number == None:
            checker = True
            for i in range(self.lab_num):
                if self.labs[i] == 0:
                    self.labs[i] = score
                    checker = False
                    break
            if checker:
                return 'error'
        elif number > self.lab_num -1:
            return 'error'
        elif number != None:
            if score < self.lab_max:
                self.labs[number] = score
            else:
                self.labs[number] = self.lab_max
    def average_score(self):
        res = 0
        for item in  self.labs:
            res +=item
        res  = res / len(self.labs)
        res = round(res, 1)
        return res

def find_best_student(filename):
    fp = open(filename,'r')
    tmp_csv =  csv.reader(fp)
    tmp_list = []
    students_tmp = []
    lab_tmp =[]
    d_study = {}
    for item  in  tmp_csv:
        tmp_list.append(item)
    print(tmp_list[1:])
    for i in tmp_list[1:] :
        students_tmp = i[:3]
        student = Student(students_tmp[0],{'lab_max':int(students_tmp[1]),'lab_num':int(students_tmp[2])})
        lab_tmp = i[3:]
        for index,z in  enumerate(lab_tmp):
            z = int(z)
            if z == 0:
                continue
            student.set_lab(z,index)
        d_study[student.name] = student.average_score()
    g = max(d_study, key=d_study.get)
    return g
find_best_student('students.csv')