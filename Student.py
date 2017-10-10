class Student(object):

    def __init__(self, name, grade):
        self.name = name;
        self.grade = grade;

    def printStudent(self):
        print ("Name: %s Grade %s" %(self.name, self.grade))


stuA = Student("Abc", "12");
stuA.name = "Garima"
stuA.grade = "pre-K"
stuA.printStudent();

# inheritance
class MathStudent(Student):

    def __init__(self, name, grade, mathScore):
        super(MathStudent,self).__init__(name, grade)
        self.mathScore = mathScore

stuM = MathStudent("Geek", "5", "98")
stuM.printStudent()
print("MathScore: %s" %stuM.mathScore)