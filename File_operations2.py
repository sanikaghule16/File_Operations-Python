count=0
with open("people-100.csv","r")as f:
    next(f)#skip header
    for line in f:
        count+=1
print("total Records:",count)


with open("people-100.csv","r")as f:
    for i in range(7):
        print(f.readline())

with open("people-100.csv","r")as f:
    next(f)
    for line in f:
        data=line.strip().split(",")
        email=data[7]
        print(email)


with open("people-100.csv","r")as f,open("emails.text","w")as out:
    next(f)
    for line in f:
        email=line.strip().split(",")[5]
        out.write(email + "\n")
        


with open("organizations-100.csv","r")as f:
    for i in range(5):
        print(f.readline())
