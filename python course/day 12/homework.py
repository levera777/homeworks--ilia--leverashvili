budget= int(input("what is your budget:"))
cost=int(input("please enter cost:"))

if budget>= cost:
    print("you have enough money")
else:
    print("you dont have enough money")

#2
registred_password ="lever4"
password= input("please enter your password:")

while password != registred_password:
    password= input("please enter your password again:")
    if password== registred_password:
        print("you have accses on your account")
    else:
        print("you have entered your password wrong, try again")


#3
        start = int(input("please enter starting value:"))
        end= int(input("please enter ending value:"))
        step=int(input("please enter step value"))


        for i in range( start,end ,step):
            print(i)


#4
    s1=int(input("please enter first side:"))       
    s2=int(input("please enter secont side: "))
    s3=int(input("please enter third side:"))
is_valid= (s1+s2>s3) and (s2+s3>s1) and (s3+s1>s2)

while is_valid != True:
    s1= int(input("please enter first side:"))
    s2=int(input("please enter secont side:"))
    s3=int(input("please enter third side"))

is_valid= s1+s2>s3




