"""
Comma ,

"Print these things separately."
So why does it LOOK like one sentence?

Because print() has a default behavior:

When you give it multiple arguments separated by commas, it prints them with a space between them.

print("Hello", name)

x = print("Name:", "Mamoona", "Age:", 25)
print(type(x))
<class 'NoneType'>

That's because print() prints the arguments; it doesn't create a string containing them.

Mainly useful when you're directly printing.

+

"Join these strings together."

message = "Hello " + name

Useful when you actually need to create a single string.

f-string
"Build a string using variables/expressions."

message = f"Hello {name}"

Usually the cleanest modern approach.

"""




name = "Mamoona"

message = "Hello", name 

print(message) # ('Hello', 'Mamoona')

# It creates a tuple:
x = print("Name:", "Mamoona", "Age:", 25)
print(type(x))


name = "Mamoona"

message = "Hello " + name

print(message) #Hello Mamoona

email = message + ", welcome to Python!"
print(type(email))
print(email)

# It is one string.

# That's something the comma doesn't do.

name = "Mamoona"
age = 25

print("Name:", name, "Age:", age)  #The result looks like one sentence, but they are separate values/arguments.


# f-string creates one string while allowing variables/expressions inside {}.

# course= "Artificial Intelligence"
# organization= "NETSOL"
course , organization , cohort= "Artificial Intelligence" , "NETSOL" , 2

print(course.upper())
print(len(course))
print(course[0:7])
print(f"f_strings are the modern to insert variables into text")
print(f"{course} and {organization} and {cohort}")

print("comparison")

# print( "course , +" and " organization")

print(course +  " and " +  organization)
print(course +  " and " +  organization + str(cohort))

name=Mamoona
age=24

print("My name is", name, "and I am", age)
print("My name is" + name + "and I am"+ str(age))
print(f"My name is {name} and I am {age}")

age = 25

print(f"I will be {age + 1} next year.")