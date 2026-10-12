class Attendence:
    information = [
        {"id": 1, "Name": "Moon", "status": "Present"},
        {"id": 2, "Name": "Ali", "status": "Absent"},
        {"id": 3, "Name": "Zafar", "status": "Present"}
    ]

    def verification(self, id, name):
        for student in self.information:
            if student["id"] == id and student["Name"].lower() == name.lower():
                print(f"Status: {student['status']}")
                return
        print("Student not found. Check your ID and name.")


i = int(input("enter ur id: "))
n = input("enter ur name: ")

obj = Attendence()
obj.verification(i, n)

