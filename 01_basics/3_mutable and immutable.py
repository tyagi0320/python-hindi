
#Everything iside python is an object.
#Once a reference is given to a variable in python's memory,
# it is immutable. It cannot be changed.
#We can add multiple references in a variable.But we can never change the variable itself because it is immutable.

#EXAMPLE:
#x=10,y=x
#print(x)=> 10
#print(y)=> 10
#Now, x=15
#print(x)=> 15
#print(y)=> 10


#Q. Why print(y) gives output as "10" instead "15"?
#Ans. Firstly, x->(refers to) 10
#     then y=x => This implies reference of y is same as that of x.
#     Hence, y-> (refers to) 10
#     Now, we update x, x->15
#     But meanwhile we never updated y. y->10 only even now.This
#     is happening because referencing of variables in python is immutable.


#Q.We have declared and a string "coffeeaurcode".Can we change it to "chaiaurcode"?
#Ans. NO, we cannot do any changes. We will be required to make a new string
#     which says "chaiaurcode".


#MUTABLE DATATYPES:
#1.List
#2.Set
#3.Dictionary
#4.Bytearray
#5.Array

#IMMUTABLE DATATYPES:
#1.Integers
#2.Float
#3.Boolean
#4.Strings
#5.Tuples
#6.Frozen set
#7.Bytes