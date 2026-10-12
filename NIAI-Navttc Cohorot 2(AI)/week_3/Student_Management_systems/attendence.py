# how student_attendence module will work here
# student will check his/her attendence status 
# status will be present or absent
# student_name or id can be used for identity_verification
# It will obtain by students using input funntion 
# have to match both things id and name by using and(&) operator then will display status


i = input("enter ur id")
n= input("enter ur name")
class Attendence:
    information = [
        {"id": 1 , "Name": "Moon"},
        {"id": 2 , "Name": "Ali"},
        {"id": 3 , "Name": "Zafar"}
    ]
    def verification(id , name):
       pass


obj= Attendence()
obj.verification("i", "n")









