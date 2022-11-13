#Maximum value in the list
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    ele = int(input()) 
    list.append(ele)
max_val = None
for i in list:
    if(max_val is None or i > max_val):
        max_val = i
print("max_val :",max_val)
    
