# List
thisList = ["SI", "TI", "MI", "SK", "IA"]

#tuple
thistuple = ("SI", "TI", "MI", "SK", "IA")

#sets
thisSets = {"SI", "TI", "MI", "SK", "IA"}

#Nested Dictionary
student = {
    "student1" : {
        "name" : "Raindeca",
        "year" : "1998"
    },

    "student2" : {
        "name" : "Maya",
        "year" : "2032"
    },

    "student3" : {
        "name" : "Iona",
        "year" : "1991"
    }
}

# Loops

for x in range(0,6):
    print("CARNIVAL DAYO! ")

print("\n")

for X in thisList:
    print(X)

print("\n")

for x in thisSets:
    print(x)

print("\n")

for x, y in student.items():
    print(x,y)

print("\n")
