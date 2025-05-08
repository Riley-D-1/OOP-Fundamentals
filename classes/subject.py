class Subject:
    def __init__(self,name,yr_lvl,code,student_num):
        self.name =name
        self.yr_lvl=yr_lvl
        self.code =code
        self.student_num=student_num
    def info(self):
        print(self.name)
        print(self.yr_lvl)
        print(self.code)
        print(self.student_num)

