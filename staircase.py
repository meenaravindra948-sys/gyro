# def staircase(n):
#     for i in range(1,n+1):
#         for j in range(n-i):
#             print(" ",end="")
            
#         for j in range(i):
#             print("#",end="")
        
#         print()


# staircase(6)


# optimal 

def staircase(n):
    for i in range(1,n+1):
        print(" " * (n-i),"#"*i,sep="")

staircase(5)