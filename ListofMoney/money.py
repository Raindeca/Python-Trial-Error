#Student

class Student():
    def __init__(self, fullname, npm, jurusan, angkatan):
        self.fullname = fullname
        self.npm = npm
        self.jurusan = jurusan
        self.angkatan = angkatan

    @staticmethod
    def fetchData():
        #StudentList
        list = []
        n = int(input("Dataset\t: "))

        for index in n:
            print("Dataset-"+(n+1))
            fName = input("Front name\t: ")
            lName = input("Last Name\t: ")
            fullname = fName+" "+lName
            npm = input("Student ID\t: ")
            major = jurusan(npm)
            angkatan = npm[3:5]

            list.append( Student(fullname, npm, major, angkatan))
    
    @staticmethod
    def jurusan(npm):
        temp = npm[0:3]

        if temp =="110":
            major = "SI"
        elif temp =="510":
            major = "TI"
        elif temp == "111":
            major  = "MI"
        elif temp == "310":
            major = "SK"
        elif temp == "311":
            major = "TK"
        else:
            major = "N/A"
        
        return major

for index in Student.fetchData:
    pass