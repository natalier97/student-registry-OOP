import re

class Student:

    def __init__(self, name, age=13, grade='12th'):
        self._name = name
        self._age = age
        self._grade = grade
    
    @property
    def get_name(self):
        return self._name
    
    @property
    def get_age(self):
        return self._age
    
    @property
    def get_grade(self):
        return self._grade
    
    @get_name.setter
    def set_name(self, new_name):
        pattern = r'^[a-zA-Z]+$'
        if isinstance(new_name, str) and len(new_name) > 3 and re.match(pattern, new_name) and new_name == new_name.title():
            self._name = new_name
        else:
            print("Name must be 3 characters or more, have no spaces or special characters, and be in title format")
        
    @get_age.setter
    def set_age(self, new_age):
        if isinstance(new_age, int) and new_age < 18 and new_age > 11:
             self._age = new_age
        else:
            print("student needs to be between the ages of 11 and 18")
             

    @get_grade.setter
    def set_grade(self,new_grade): 
        if isinstance(new_grade, str) and new_grade == '9th' or new_grade == '10th' or new_grade == '11th' or new_grade == '12th':
            self._grade = new_grade
        else:
            print('not a valid grade')
        
    def __str__(self):
        return f"Name: {self._name}, Age: {self._age}, Grade: {self._grade}"    
    



student1 = Student('Roger', 17, "9th")
student2 = Student('Natalie', 15, "9th")

# student1.set_grade=('12th')
# student1.set_age=(13)
# student1.set_name='Rogerrrr'

print(student1.__str__())
