"""

    Fibonacci Sequence
    0,1,1,2,3,5...
"""

def fibo(n):

    a = 0 
    b = 1
    c = 0

    for i in range(1,n+1):
        print(c ,end=", ")
        c=a+b
        if i==2:
            c=1
        a,b=b,c

# def fiboR(n,a=0,b=1,c=0):
#     if n<=1:
#         print(c)
#         return
#     else:
#         print(c, end=", ")
#         c=a+b
#         a,b=b,c
#         if(a==1 & b==1):
#             c=1
#         fiboR(n-1,a,b,c)
#         return
# Python program to display the Fibonacci sequence

def fiboR(n):
   if n <= 1:
       print(n, end="")
       return n
   else:
       d1 = fiboR(n-1)
       d2 = fiboR(n-2)
       print((d1+d2), end=", ")
       return(d1+d2)

# Driver Program
limit = 5
fibo(limit)
print("\n=====================")
fiboR(limit)
