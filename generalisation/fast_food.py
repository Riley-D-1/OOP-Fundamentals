import datetime

class Employee:
    def __init__(self,name,employee_id,hourly_wage,shift_hours):
        self.name = name
        self.employee_id = employee_id
        self.hourly_wage = hourly_wage
        self.shift_hours = shift_hours
    def clock_in(self):
        print(f'Shif started at {datetime.datetime.now()}')
        return datetime.datetime.now()
    def clock_out(self,start_time):
        end_time = datetime.datetime.now()
        total_hours = start_time - end_time 
        print(f"Total Hours:{total_hours}")
    def get_pay(self):
        self.shift_hours * self.hourly_wage

class Cashier(Employee):
    def __init__(self,name,employee_id,hourly_wage,shift_hours):
        super().__init__(name,employee_id,hourly_wage,shift_hours)
        self.transactions = 0
    def add_transaction(self):
        self.transactions +1

class Cook(Employee):
    def __init__(self,name,employee_id,hourly_wage,shift_hours):
        super().__init__(name,employee_id,hourly_wage,shift_hours)
        self.meals_made = 0
    def add_meal(self):
        self.meals_made +1

class Cleaner(Employee):
    def __init__(self,name,employee_id,hourly_wage,shift_hours,cleaning_area):
        super().__init__(name,employee_id,hourly_wage,shift_hours)
        self.cleaning_area = cleaning_area
    def check_area(self):
        print(self.cleaning_area)

class drive_thru_Cashier(Employee):
    def __init__(self,name,employee_id,hourly_wage,shift_hours,drive_thru_lane):
        super().__init__(name,employee_id,hourly_wage,shift_hours)
        self.lane = drive_thru_lane
    def check_lane(self):
        print(self.lane)