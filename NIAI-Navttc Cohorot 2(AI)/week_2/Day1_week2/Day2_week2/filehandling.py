# a = append
# f = fatch
# read , write , append = r , w,,a
with open('notes.txt' ,'w') as f:
    f.write('hi')

# overwwrite

with open('notes.txt' ,'w') as f:
    f.write('Mamoona')

# show in the terminal

with open('notes.txt' ,'r') as f:
    content = f.read()
    print(content)


# The Python .write() method only accepts a single string argument at a time.
# task
with open('scores.txt' , 'w') as f:
    f.write("Computer\nMaths\nEnglish")  

subjects = ["Mathematics", "Computer Science", "Physics"]

with open("scores.txt", "w") as file:
    for subject in subjects:
        file.write(subject + "\n")

with open("scores.txt" , "r") as f:
    content = f.read()
    print(content)           