#Optional Extra Credit Assignment #7
#Bristol Community College, COMP 153
#Author: Lorelai Lyons, Date: 1/20/24

from ExtraCreditFunc import Student
from ExtraCreditFunc import Course
from ExtraCreditFunc import School
import json

class ProgramFuncs:
    def __init__(self, schoolInput):
        pass
    
    #Saving the school information to a binary file with JSON
    def save(self, schoolInput):
        print("Save this session to the current school database")

        #Using "with" closes the data stream when complete
        with open('schoolDetails.json', 'w', encoding="utf-8") as saveFile:
            #JSON works using key value pairs and so this is saving the information in that format
            data = {
                'courses': [
                    {'courseName': course.courseName,
                     'courseNumber': course.courseNumber,
                     'numCredits': course.numCredits}
                    for course in schoolInput.completeCourseList
                ],
                'students': [
                    {'studentName': student.studentName,
                     'studentID': student.studentID,
                     'studentGPA': student.studentGPA,
                     'studentMajor': student.studentMajor,
                     'enrolledCourses': [course.courseName for course in student.studentCourses]}
                    for student in schoolInput.completeStudentList
                ]
            }
            
            #Actually saving the bytestream to JSON
            json.dump(data, saveFile, indent=2)
        print("Information saved successfully!")

    #Loading the school information from a binary file using JSON
    def load(self, schoolInput):
        print("Load the records of another school")
        try:            
            with open('schoolDetails.json', encoding="utf-8") as saveFile:
                #Reading data from the save file
                read_data = json.load(saveFile)

                #Reading the course and student JSON objects
                courses = read_data['courses']
                students = read_data['students']

                #Loading JSON data into school registry
                schoolInput.completeCourseList = [Course(course['courseName'], course['courseNumber'], course['numCredits']) for course in courses]
                schoolInput.completeStudentList = [Student(student['studentName'], student['studentID'], student['studentGPA'], student['studentMajor']) for student in students]

                #Using JSON data to fetch student information and enroll them in the correct classes
                for student_data in students:
                    student = schoolInput.get_student_by_name(student_data['studentName'])
                    if student:
                        for course_name in student_data.get('enrolledCourses', []):
                            course = schoolInput.get_course_by_name(course_name)
                            if course:
                                student.add_course(course)
            #Confirms success
            print("Information loaded successfully!")
        except FileNotFoundError:
            print("File not found. Please make sure 'schoolDetails.json' exists.")
        except json.JSONDecodeError:
            print("Error decoding JSON. Please check the format of 'schoolDetails.json'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def main():
    #The school class contains a complete list of student and course objects

    ExampleSchool = School([],[])
    ExampleIO = ProgramFuncs(ExampleSchool)

    #This is the primary state machine that allows a user to interact with the console.
    inSesh = True
    ExampleSchool.display_banner()
    
    while inSesh:
        ExampleSchool.display_selection()
        match input("What would you like to do? ").lower():
            case 'a':
                ExampleSchool.register_a_new_student()
            case 'b':
                ExampleSchool.print_a_specific_student_courseload()
            case 'c':
                ExampleSchool.create_new_course()
            case 'd':
                ExampleSchool.completeCourseList_to_string()
            case 'e':
                ExampleSchool.add_course_to_a_student()                    
            case 'f':
                ExampleSchool.display_total_credits()
            case 'g':
                ExampleIO.save(ExampleSchool)
            case 'h':
                ExampleIO.load(ExampleSchool)                    
            case 'i':
                #Exiting the program
                print("Thanks for using the 'EnrollmentSim'")
                inSesh = False;
            case 'j':#This is an extra bonus kinda hid in the back end... k(bonus): A complete list of all students currently enrolled
                ExampleSchool.display_completeStudentList()
            case _:
                return "This indicates invalid input or an error"

if __name__ == '__main__':
    main()
