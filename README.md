# Bongo coding test 2 solution

## Question no 4
Getting oldest employee from each department

    class Department(models.Model):
        name = models.CharField(max_length=255)
    
        def __str__(self):
            return "{} {}".format(self.id, self.name)
    
        class Meta:
            db_table = 'departments'
    
    
    class Employee(models.Model):
        employee_name = models.CharField(max_length=255)
        birthdate = models.DateField()
        department = models.ForeignKey(Department, on_delete=models.CASCADE)
    
        def __str__(self):
            return "{} {}".format(self.id, self.employee_name)
    
        class Meta:
            db_table = 'employees'

        @staticmethod
        def get_oldest_employee_from_each_department():
            """
            if db backend is postgres you can use do the following:
            return Employee.objects.all().order_by('department','birthdate').distinct('department')
            :return:
            """
            employees = Employee.objects.raw(
                "SELECT * FROM employees where birthdate in ( SELECT MIN(birthdate) from employees GROUP BY department_id)")
            for employee in employees:
                print("name={}, birthdate={}, department={}".format(employee.employee_name, employee.birthdate, employee.department.name))
            return list(employees)
            
 Working project: (core.models)
 > https://github.com/hackerbin/bgdjango

## Question no 5
### Execution
`$ python3 problem5.py`

### Unit Test
`$ python3 test_problem5.py`

### Time complexity:  
> Its a greedy algorithm.  
> Time complexity is O(N^2) where N is the number of persons

## Question no 6
### Execution
`$ python3 problem6.py`

### Unit Test
`$ python3 test_problem6.py`

### Time complexity:  
> O(N) as we are traversing each cell just once and marking it with 3 as visited  
> In worst case scenario complexity is O(N^2)


### Run all unittest at once
In project root run following command
> `$ python3 -m unittest discover .`

