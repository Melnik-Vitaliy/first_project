class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, diff_day):
        self.remaining_vacation_days -= diff_day
        Employee.vacation_days = self.remaining_vacation_days

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {employee.vacation_days}.'


employee = Employee(first_name='Роберт', second_name='Крузо', gender='м')

employee.consume_vacation(7)
print(employee.get_vacation_details())
