import csv,os
from lib2to3.pgen2.token import LSQB
from tkinter import N
print("1) Login (Kindly login to save your progress) ")
print("2) Sign Up")
print("3) Start Quiz")
print("4) Show all Questions")
print("5) Add a Question ")
print("6) Remove a Question ")
print("7) Instructions")
print("8) Quit / Logout")
loginstatus=False
def conv(list):
    s = [str(i) for i in list]
    r = int("".join(s))
    return(r)
def one():
    global userid
    global userp
    userid=input("Enter your username")
    userp=input("Enter your password")
    x=open("credentials.csv",newline="")
    r=csv.reader(x)
    for a in r:
        #print(a)
        if a[0]==userid:
            #print(a[0])
            if a[1]==userp:
                global loginstatus
                print("Successfully Logged in")
                loginstatus=True
                break
            else:
                print("Password Incorrect")
                break
    #else:
     #   print("Username Incorrect")
    x.close()
def two():
    c1=input("Enter a username")
    x=open("credentials.csv","a+",newline="")
    r=csv.reader(x)
    r1=csv.writer(x)
    if c1 not in r:
        c2=input("Enter a password")
        data=[c1,c2,0,0]
        r1.writerow(data)
        x.close()
    else:
        print("Username not available")
        two()
def three():
    score=0
    qno=0
    print("Quiz starting in 1.....2.....3.....")
    x=open("questions.csv",newline="")
    y=open("choices.csv",newline="")
    z=open("answers.csv",newline="")
    x1=list(csv.reader(x))
    y1=list(csv.reader(y))
    z1=csv.reader(z)
    for i,j,k in zip(x1,y1,z1):
        print(i)
        for J in j:
            print(J)
        ans=int(input("Enter choice number (index starts from 1) "))
        if ans==conv(k):
            score+=1
            qno+=1
            print("That's correct")
        else:
            print("Better luck next time")
        
        leave=input("Wanna quit? Scared? dw if logged in your progress will be saved!")
        if leave=="y":
            break
    print("Your Score is ",score)
    if loginstatus==True:
        ls1=open("credentials.csv","r+",newline="")
        ls2=open("credentials1.csv","x",newline="")
        lsr=csv.reader(ls1)
        lsw=csv.writer(ls2)
        for qp in lsr:
            if qp[0]==userid:
                lsw.writerow([userid,userp,score,qno])
                print("Checkpoint saved successfully")
            else:
                lsw.writerow(qp)
        ls1.close()
        ls2.close()
        os.remove("credentials.csv")
        os.rename("credentials1.csv","credentials.csv")
def four():
    with open("questions.csv",newline="") as f:
        f1=csv.reader(f)
        c=0
        for i in f1:
            c+=1
            print(c," ",i)
def fifth():
    a1=str(input("Enter the question"))
    a2=[]
    for i in range(int(input("enter no of choices"))):
        a2.append(input("Option : "))
    a3=input("Enter the correct choice's index (Starts from 1)")
    with open ("questions.csv","a+",newline="") as f1:
        f11=csv.writer(f1)
        f11.writerow([a1])
    with open ("choices.csv","a+",newline="") as f2:
        f22=csv.writer(f2)
        f22.writerow(a2)
    with open ("answers.csv","a+",newline="") as f3:
        f33=csv.writer(f3)
        f33.writerow(a3)
def sixth():
    qr=int(input("Enter Qn index to remove"))
    f1= open ("questions.csv",newline="")
    f2= open ("questions1.csv","x",newline="")
    f2r=csv.writer(f2)
    dat1=csv.reader(f1)
    c=0
    for i in dat1:
        if any(i):
            c+=1
            if c!=qr:
                f2r.writerow(i)
    f1.close()
    f2.close()
    #
    f3= open("answers.csv",newline="")
    f4=open("answers1.csv","x",newline="")
    dat2=csv.reader(f3)
    f4r=csv.writer(f4)
    c=0
    for j in dat2:
        if any(j):
            c+=1
            if c!=qr:
                f4r.writerow(j)
            
    f3.close()
    f4.close()
    #
    f5=open("choices.csv",newline="")
    f6=open("choices1.csv","x",newline="")
    dat3=csv.reader(f5)
    c=0
    f6r=csv.writer(f6)
    for k in dat3:
        if any(k):
            c+=1
            if c!=qr:
                f6r.writerow(k)
    f5.close()
    f6.close()
    os.remove("answers.csv")
    os.remove("choices.csv")
    os.remove("questions.csv")
    os.rename("questions1.csv","questions.csv")
    os.rename("choices1.csv","choices.csv")
    os.rename("answers1.csv","answers.csv")

def seven():
    print("Each correct answer gives 1 mark and no negatives. Good Luck")
def eight():
    quit()
while True:
    c=int(input("Enter Your Choice (Number) "))
    if c==1:  
        one()    
    elif c==2:  
        two()
    elif c==3:
        three()
    elif c==4:
        four()
    elif c==5:
        fifth()
    elif c==6:
        sixth()
    elif c==7:
        seven()
    elif c==8:
        eight()

    ch=input("Wanna continue?  (y/n) ")
    if ch=="n":
        break
    a=input("Want to see choices again?  (y/n) ")
    if a=="y":
        print("1) Login (Kindly login to store your progress) ")
        print("2) Sign Up")
        print("3) Start Quiz")
        print("4) Show all Questions")
        print("5) Add a Question ")
        print("6) Remove a Question ")
        print("7) Instructions")
        print("8) Quit / Logout")