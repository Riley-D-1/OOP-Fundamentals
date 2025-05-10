class Subject:
    def __init__(self, name, year_lvl, class_code, student_num):
        self.name = name
        self.year_level = year_lvl
        self.class_code = class_code
        self.student_num = student_num
    def info(self):
        return(self.name,self.year_level,self.class_code,self.student_num)
