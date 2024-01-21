class Student:
    #Constructor for the student class
    def __init__(self, studentName, studentID, studentGPA, studentMajor):
        self.studentName  = studentName
        self.studentID    = studentID
        self.studentGPA   = studentGPA
        self.studentMajor = studentMajor
        self.studentCourses      = []

    #This is being used to COMPARE the student to other student objects to determine if they match
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.studentName == other.studentName
        return False        

    #Getters and setters
    def get_studentName(self):
        return self.studentName

    def set_studentName(self, value):
        self.studentName = value

    def get_studentID(self):
        return self.studentID

    def set_studentID(self, value):
        self.studentID = value

    def get_studentGPA(self):
        return self.studentGPA

    def set_studentGPA(self, value):
        self.studentGPA = value

    def get_studentMajor(self):
        return self.studentMajor

    def set_studentMajor(self, value):
        self.studentMajor = value

    def get_studentCourses(self):
        return self.studentCourses

    def set_studentCourses(self, value):
        self.studentCourses = value        

    def get_studentCourseHistory(self):
        return self.studentCourseHistory

    def set_studentCourseHistory(self, value):
        self.studentCourseHistory = value

    #toString method()
    def to_string(self):
        print(f"\nStudent Name: {self.studentName}" +
              f"\nStudent ID#: {self.studentID}" +
              f"\nStudentGPA: {self.studentGPA}" +
              f"\nStudent Major: {self.studentMajor}\n")

    #prints a list of courses the student is enrolled in    
    def get_courses(self):
        print(f"\n{self.studentName} Course List")
        print("===================")
        for course in self.studentCourses:
            print(course.courseName,
              course.courseNumber,
              course.numCredits, end="\n")

    #prints the sum of the student's course credits
    def get_total_credits(self):
        creditCount = 0
        for course in self.studentCourses:
            creditCount += course.numCredits
        print(creditCount)
        return creditCount

    #enrolls the student in a course and prints confirmation to console
    def add_course(self, courseInput):
        if(self not in courseInput.courseRoster):
            self.studentCourses.append(courseInput)

class Course:
    #Constructor for the Course class
    def __init__(self, courseName, courseNumber, numCredits):
        self.courseName = courseName
        self.courseNumber = courseNumber
        self.numCredits = numCredits
        self.courseRoster = []

    #This is being used to COMPARE the student to other course objects to determine if they match
    def __eq__(self, other):
        if isinstance(other, Course):
            return self.courseName == other.courseName
        return False

    #I don't understand this but I am seeing if it works
    def __hash__(self):
        return hash(self.courseName)

    def get_courseName(self):
        return self.courseName

    def set_courseName(self, value):
        self.courseName = value

    def get_courseNumber(self):
        return self.courseNumber

    def set_courseNumber(self, value):
        self.courseNumber = value

    def get_numCredits(self):
        return self.numCredits

    def set_numCredits(self, value):
        self.numCredits = value

    def get_courseList(self):
        return self.courseList

    def set_courseList(self, value):
        self.courseList = value        

    def get_courseRoster(self):
        return self.courseRoster

    def set_courseRoster(self, value):
        self.courseRoster = value  

    #Adds a student to the course's student List/roster
    def add_new_student(self, newStudent):
        if(newStudent not in self.courseRoster):
            self.courseRoster.append(newStudent)
        newStudent.studentCourseHistory[self] = 89
        print(f"Successfully enrolled {newStudent.studentName} in {self.courseName}")

    #Prints the course details to the console
    def to_string(self):
        print(f"\nCourse Name: {self.courseName}" +
              f"\nCourse #: {self.courseNumber}" +
              f"\nNumber Credits: {self.numCredits}\n")        

    #Prints the currently enrolled students to the console
    def course_roster_to_string(self):
        print("\n Name\t ID\t GPA\t Major ", end="\n==============================\n") 
        for student in self.courseRoster:
            print(student.studentName,
                  student.studentID,
                  student.studentGPA,
                  student.studentMajor, end="\n")

class School:
    #Constructor for the school class
    def __init__(self, courseList, studentList):
        self.completeStudentList = []        
        self.completeCourseList = []

    #Getters and setters
    def get_completeStudentList(self):
        return self.completeStudentList

    def set_completeStudentList(self, value):
        self.completeStudentList = value     

    def get_completeCourseList(self):
        return self.completeCourseList

    def set_completeCourseList(self, value):
        self.completeCourseList = value

    #Displays welcome message once upon opening the program
    def display_banner(self):
        welcomeBanner = '''
            =========================================================
              ========= WELCOME TO THE ENROLLMENTSIM!!!! ==========
            =========================================================
        '''        
        print(welcomeBanner)

    #prints a list of options to the user
    def display_selection(self):
        pleaseSelect = '''
            Please select one of the following:
            a: Add a new student to our prestigious institution
            b: Display a particular student's personal information
            c: Create a new course
            d: Display all available courses
            e: Add a course to a student's schedule
            f: Display the number of credits a student has accumulated
            g: Save all information
            h: Load information
            j(bonus): See individual course loads by student name
            i: Exit
            '''
        print(pleaseSelect)
        
        
    #Gets a student object from the completeStudentList
    def get_student_by_name(self, studentName):
        for student in self.completeStudentList:
            if student.get_studentName() == studentName:
                return student
        return None

    #Gets a course object from the completeCourseList
    def get_course_by_name(self, courseName):
        for course in self.completeCourseList:
            if course.get_courseName() == courseName:
                return course
        return None

    #Prints complete course catalog to console
    def completeCourseList_to_string(self):
        print("\nCourse Name \t Course #  Course Credit", end="\n========================================\n")
        for course in self.completeCourseList:
            print(course.courseName, "\t",
              course.courseNumber, "\t",
              course.numCredits)

    #Function to place a new student into the student directory
    def register_a_new_student(self):
        print("Okay, you'd like to accept a new student.")
        while True:
            newStudent = Student("", 0, 0, "")
            
            #Taking input for new student credentials
            newStudent.studentName = input("Please enter their FULL name: ")
            newStudent.studentID = int(input("Please enter the student's ID: "))
            newStudent.studentGPA = float(input("Please enter the student's GPA: "))
            newStudent.studentMajor = input("Please enter the student's major: ")

            #printing out the student details to the console for confirmation
            newStudent.to_string()
            
            returnInput = input("Do these details look correct? (y/n) ").lower()
            match returnInput:
                case 'y':
                    print(f"Rad, we added {newStudent.studentName} to our student list.")
                    self.completeStudentList.append(newStudent)
                    break
                case 'n':
                    print("Okay, please re enter input.")
                case _:
                    print("Invalid input, no student will be added.")
                    
    #Creates a new course object and adds it to the school's catalog
    def create_new_course(self):
        newCourse = Course("", "", 0)
        print("Okay, you'd like to create a new course.")
        newCourse.courseName = input("Please enter the course name: ")
        newCourse.courseNumber = input("Please enter the course number: ")
        newCourse.numCredits = int(input("Please enter the number of credits: "))
        self.completeCourseList.append(newCourse);
        print("Now all the available classes to enroll students in are: ")
        self.completeCourseList_to_string()

    #This function uses the previously created functions to add a course to a student's courseList
    def add_course_to_a_student(self):
        studentName = input("Which student do you want to register in a course (name): ")
        student = self.get_student_by_name(studentName)
        if student:
            courseName = input("What course would you like to register them in (course name)? ")
            course = self.get_course_by_name(courseName)
            if course:
                print(f"\nBefore enrollment:")
                student.get_courses()
                student.add_course(course)
                print(f"\nAfter enrollment: ")
                student.get_courses()
            else:
                print("That is not a class currently.")
            print(f"Successfully enrolled {student.studentName} in {course.courseName}!")                
        else:
            print("This student was not found")

    #Prints the sum of a specific students current credits to the console
    def display_total_credits(self):
        studentName = input("Which student's details do you need to see? ")
        student = self.get_student_by_name(studentName)
        if student:
            print(f"{student.studentName} has {student.get_total_credits()} credits currently")
        else:
            print("This student was not found")

    #Lets you choose one student to see the courses they are enrolled in
    def print_a_specific_student_courseload(self):
        studentName = input("Which student's courses do you wish to see?")
        student = self.get_student_by_name(studentName)
        if student:
            student.get_courses()
        else:
            print("This student was not found")

    #This is a bonus function that is just in the back end and hidden from users (full student list)
    def display_completeStudentList(self):
        for student in self.completeStudentList:
            print(f"\nStudent Name: {student.studentName}" +
                  f"\nStudent ID#: {student.studentID}" +
                  f"\nStudentGPA: {student.studentGPA}" +
                  f"\nStudent Major: {student.studentMajor}\n")
            
