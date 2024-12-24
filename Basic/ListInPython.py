#List ------------
mylist = ["apple", 20, "cherry",30.4]

print(mylist)
print(type(mylist))

#List another way ---------

myDevice=list(("Laptop","Desktop","AndroidPhone","Printer"))
print(myDevice)

myDevice[1]="Windows Desktop"
myDevice[0]="Linux Laptop"
print(myDevice)

#Insert new item in the list
mylist.append("Orange")
print(mylist)
mylist.insert(4,"Banana")
print(mylist)

#Remove item from list

myDevice.remove("AndroidPhone")
print(myDevice)

mylist.pop(2)
print(mylist) #Remove cherry from mylist

#Loop List ---------

for i in range(len(mylist)): #using for loop
    print(mylist[i])
print("--------------------------")
x=0
while x< len(mylist):
    print(mylist[x])
    x=x+1


