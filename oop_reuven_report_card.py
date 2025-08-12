# class ReportCard:
#     def __init__(self, name, **kwargs):
#         self.name = name
#         self.grades = kwargs
#
#     def get_grade(self, subject_name):
#         if subject_name in self.grades:
#             return self.grades[subject_name]
#         return f'No such subject found: {subject_name}'
#
#     def print_all_grades(self):
#         for subject, grade in self.grades.items():
#             print(f'{subject}: {grade}')
#
#     def gpa(self):
#         return sum(self.grades.values()) / len(self.grades) if self.grades else 0
#
# rc = ReportCard('Reuven', English=90, Math=85, Science=95) # here we are passing arguments, this is our hash
# print(rc.get_grade('English'))  # Output: 90
# print(rc.gpa())  # Output: 90.0

class ReportCard:
    def __init__(self, name, **kwargs):
        self.name = name
        self.grades = kwargs

    def get_grade(self, subject_name):
        if subject_name in self.grades:
            return self.grades[subject_name]
        return f'No such subject found: {subject_name}'

    def __repr__(self):
        return '\n'.join([f'{key}: {value}' for key, value in self.grades.items()]) # more concise

    # def __repr__(self):
    #     output = ''
    #     for key, value in self.grades.items():
    #         output += f'{key}: {value}\n'
    #     return output # this method will be called when we print an object of this class

    # def print_all_grades(self):
    #     for subject, grade in self.grades.items():
    #         print(f'{subject}: {grade}')

    def gpa(self):
        return sum(self.grades.values()) / len(self.grades) if self.grades else 0



rc = ReportCard('Reuven', English=90, Math=85, Science=95) # here we are passing arguments, this is our hash
print(rc)
print(rc.get_grade('English'))  # Output: 90
print(rc.gpa())  # Output: 90.0

print('---')
class LetterReportCard(ReportCard):
        def __init__(self, name, **kwargs):
            self.name = name
            self.grades = {}

            for subject, number_grade in kwargs.items():
                letter_grade = 'F'
                if number_grade < 70:
                    letter_grade = 'D'
                elif number_grade < 80:
                    letter_grade = 'C'
                elif number_grade < 90:
                    letter_grade = 'B'
                elif number_grade <= 100:
                    letter_grade = 'A'
                self.grades[subject] = letter_grade


        def get_grade(self, subject_name):
            print(self.grades)
            if subject_name in self.grades:
                return self.grades[subject_name]
            return f'No such subject found: {subject_name}'

        def __repr__(self):
            return '\n'.join([f'{key}: {value}' for key, value in self.grades.items()]) # more concise

        # def print_all_grades(self):
        #     for subject, grade in self.grades.items():
        #         print(f'{subject}: {grade}')

        def gpa(self):
            return sum(self.grades.values()) / len(self.grades) if self.grades else 0


rlc = LetterReportCard('Reuven', English=90, Math=85, Science=95)
print(rlc.get_grade('English'))  # Output: A
print(rlc)
# print(rlc.gpa())
