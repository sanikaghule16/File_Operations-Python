#----------------using for loop----------------
file=open('Text.txt','r')
for each in file:
    print(each)

#--------------without for loop--------------
    
file=open('Text.txt','r')
print(file)

    
#-------------------------------------
print("------------------------------------------------------------")
file1=open('myfile.txt','w')
L=["This is Delhi \n","This is paris \n","this is sangamner \n"]
file1.write("hello\n")
file1.writelines(L)
file1.close()
file1=open("myfile.txt","r+")
print("output of read function is:")
print(file1.read())
print()

#---------------------------------------
file1.seek(0)
print("output of readline function is:")
print(file1.readline())
print()
file1.seek(0)

#diff betn read and readline

print("output of read(9)")
print(file1.read(9))
print()
file1.seek(0)

print("output of readline(9)")
print(file1.readline(9))
print()
file1.seek(0)
file1.close()
print("-----------------------------------------------------------")

L=["This is Delhi \n","This is Sangamner \n ","This is London \n"]
with open("myfile.txt","w")as file1:
    #writing data to a file
    file1.write("Hello\n")
    file1.writelines(L)
    #reading data to file
with open("myfile.txt","r+") as file1:
    #reading from a file
    print(file1.read())
