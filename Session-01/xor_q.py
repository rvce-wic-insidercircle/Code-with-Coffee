def xor_all_bruteforce(n):
    xor_res=0
    for i in range(1,n+1):
        xor_res=xor_res^i
    #print("brute force solution- XOR:",xor_res,"\n")
    return xor_res
    
def xor_all_optimized(n):
    xor_res=0
    if n%4==0:
        xor_res=n
    elif n%4==1:
        xor_res=1
    elif n%4==2:
        xor_res=n+1
    elif n%4==3:
        xor_res=0
    #print("optimized solution- XOR:",xor_res,"\n")
    return xor_res
    
def xor_range_bruteforce(l,h):
    xor_res=0
    for i in range(l,h+1):
        xor_res=xor_res^i
    #print("brute force solution(range)- XOR:",xor_res,"\n")
    return xor_res
    
def xor_range_optimized(l,h):
    xor_res=xor_all_optimized(l-1)^xor_all_optimized(h)
    #print("optimized solution(range)- XOR:",xor_res,"\n")
    return xor_res
    

n=int(input("Please enter the value of n: \n"))
l=int(input("Please enetr the lower limit: \n"))
h=int(input("Please enetr the upper limit: \n"))

#print(n)
all_bf=xor_all_bruteforce(n)
all_o=xor_all_optimized(n)
range_bf=xor_range_bruteforce(l,h)
range_o=xor_range_optimized(l,h)

print("brute force solution- XOR:",all_bf,"\n")
print("optimized solution- XOR:",all_o,"\n")
print("brute force solution(range)- XOR:",range_bf,"\n")
print("optimized solution(range)- XOR:",range_o,"\n")
