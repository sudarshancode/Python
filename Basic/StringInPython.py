'''
 Python String
    Program written by Sudarshan Chakraborty
'''
x="Hello I am Sudarshan Chakraborty"

#find length of this string
print("Length of the string:"+x)

#check sudarshan is present in string x

if "Sudarshan" in x:
    print("Yes, Sudarshan is present in this String.")
if "Rakesh" not in x:
    print("Yes, Rakesh is not present in this String")

for y in x:
    print(y)

#Slicing-----------------------------------------

name="Sudarshan chakraborty"
print("Substring of name: "+name[2:8])
#slice from start
print(name[:5])
#slice from end -Get the character from position 4
print(name[4:])

#Modify String-----------------------------------

course="  Bsc Computer Science  "
print("Upper Case:"+course.upper())
print("Lower Case:"+course.lower())
print("Remove White Space:"+course.strip())
#Split String
print(course.split())
st1,st2,st3=course.split()
print("First String:"+st1+" Second String:"+st2+" Third String:"+st3)

#Format String -----------------------------------
age=20
print(f"My age :{age}")

length=20
width=40
print(f"Area={length*width}",end=" ")
print("cm^2")



