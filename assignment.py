# #write a loop that makes seven calls to print().so we get output in triangle
for n in range(0,7):
     for m in range(0,n+1):
             print("# ", end="")
     print()
#program to check whether a number is prime or not
a =int(input("Enter number"))
if a > 1:
    for i in range(2, (a//2)+1):
        
        if (a% i) == 0:
            print(a, "is not a prime number")
            break
    else:
        print(a, "is a prime number")
else:
    print(a, "is not a prime number")
#check a year is leap year or not
year=int(input("Enter year"))
if(year%400==0)or(year%100!=0)and(year%4==0):
     print("Given year is leap")
else:
     print("Given year is not leap")
#use and operator to check if on is found in both python and dragon then print true
print('on' in 'python' and 'on' in 'dragon')
#program to check number is divisible by 7 or not
g=int(input("Enter a number"))
if (g%7==0):
    print(g," is divisible by 7")
else:
    print(g,"is not divisible by 7")
#find the length of python and convert the value in float  and convert in in to string
h = "python"
j = len(h)
print(j)
print(type(j))
k=float(j)
print(k)
print(type(k))
o=str(k)
print(o)
print(type(o))