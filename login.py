#check if the user is greater than 18 
age = input ("please enter your age :")
legal_age = 18
if (float(age) >=50):
    print ("you can order your beer ...")
elif(float(age)>=legal_age):
    print ("you are too old for a beer..")
else:
    print("too young to order a beer ")
