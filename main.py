class Student:
    def __init__(self, name, age, gender, gpa):
        self.name = name
        self.age = age
        self.gender = gender
        self.gap = gpa

    def updateName(self, newName):
        self.name = newName

    def updateAge(self, newAge):
        self.age = newAge

    def updateGpa(self, newGpa):
        self.Gpa = newGpa

class List:
    def printOptions(options):
        for optionNum in options:
            print('{}. {}'.format(optionNum, options[optionNum]))
        print('\nWhat do you want to do:')

    def printStudents(students):
        for student in students:
            print('{}. {}'.format(student, students[student].name))
        print("")

def main():
    students = {}
    options = {0: 'List all students', 1: 'Add a new student', 2: 'Remove a student', 3: 'Remove all students', 4: 'Quit'}
    quit = False

    while not quit:
        List.printOptions(options)
        user = input('> ')

        if(user == '0'):
            if(not students):
                print("\nThere are no students to show.\n")
            else:
                print("")
                List.printStudents(students)
        elif(user == '1'):

            name = input("\nEnter the student's first and last name: ")
            while True:
                try:
                    age = int(input("Enter the student's age: "))
                except:
                    print("\nPlease enter a whole number.\n")
                else:
                    break
            gender = input("Enter the student's gender: ")
            while True:
                try:    
                    gpa = float(input("Enter the student's GPA: "))
                except:
                    print("\nPlease enter a number.\n")
                else:
                    break

            students[len(students)] = Student(name, age, gender, gpa)
            print("")

        elif(user == '2'):
            List.printStudents(students)
            print("Which student do you want to remove: ")

            while True:
                user = int(input("> "))

                if user == 'quit' or user == 'q':
                    break
                elif students[user]:
                    del(students[user])
                    print("\nStudent was removed.\n")
                    break
                else:
                    print("That student is not in the system")
        elif(user == '3'):
            students = {}
            print("All students deleted.")
        elif(user == '4'):
            quit = True
        else:
            print("Please enter a number between 1 to 4.")

if __name__ == '__main__':
    main()
