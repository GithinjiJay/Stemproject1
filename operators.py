#logical operator
#g = 12
#h = 87
#if (h>g)
  #print (h+"is greater than")
h = input ("enter a number")
g = input ("enter another number")
#type (checks the variable data type)print
#results = print (type(h+g))
if (float(h) >= float (g)) :
    print ( f"{h}is greater than or equal to {g}")
else:
    print (f"{h}is equal to {g}")
    