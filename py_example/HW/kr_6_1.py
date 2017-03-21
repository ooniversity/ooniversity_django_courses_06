
class Student:
    # name = ''
    # # lub_max & lab_num
    # config = {}
    # labs = []

    def __init__(self,name,config):
        self.name = name
        self.lab_max = config['lab_max']
        self.lab_num = config['lab_num']
        self.labs = [0] * self.lab_num


    def set_lab(self,score,number = None):
        # Add  None  checker  .....Проверку  на None a после проверку на оценку
        tmp_score = 0
        if score > self.lab_max:
            tmp_score = self.lab_max
        else:
            tmp_score = score
        if number == None:
            checker = True
            for i in range(self.lab_num):
                if self.labs[i] == 0:
                    self.labs[i] = tmp_score
                    checker = False
                    break
            if checker:
                return 'error'
        elif number> self.lab_num -1:
            return 'error'
        elif number != None:
            self.labs[number] = tmp_score

    def average_score(self):
        res = 0
        for item in  self.labs:
            res +=item
        res  = res / len(self.labs)
        res = round(res, 1)
        return res


ivan = Student("Ivan", {"lab_max": 5, "lab_num": 4})
print(ivan.name)
print(ivan.labs)
ivan.set_lab(4, 1)
print(ivan.labs)
ivan.set_lab(5)
print(ivan.labs)
print(ivan.average_score())
ivan.set_lab(5, 6)
ivan.set_lab(8, 2)
print(ivan.labs)
ivan.set_lab(3)
print(ivan.labs)
ivan.set_lab(5)
print(ivan.average_score())

# ivan = Student("Ivan", {"lab_max": 5, "lab_num": 4})
# ivan.name =>'Ivan'
# ivan.labs => [0, 0, 0, 0]
# ivan.set_lab(4, 1)
# ivan.labs => [0, 4, 0, 0]
# ivan.set_lab(5)
# ivan.labs => [5, 4, 0, 0]
# ivan.average_score() => 2.3
# ivan.set_lab(5, 6) => 'error'
# ivan.set_lab(8, 2)
# ivan.labs => [5, 4, 5, 0]
# ivan.set_lab(3)
# ivan.labs => [5, 4, 5, 3]
# ivan.set_lab(5) => 'error'
# ivan.average_score() => 4.3