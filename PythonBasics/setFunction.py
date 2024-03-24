# 1. Take the number of elements to be stored in the list as input
# 2. Use a for loop to input elements into the list
# 3. Calculate the total sum of elements in the list
# 4. Divide the sum by total number of elements in the list
# 5. Exit

# n = int(input("Enter the number of elements to be inserted: "))
# a=[] #empty list
# for i in range(0,n):
#     elem = int(input("Enter Element: "))
#     a.append(elem)
# avg = sum(a)/n
# print("Average of elements in the list", round(avg,2))

a = {11,2,3,6,8,9,10,4,5}
a.update((12,60))
print(a)
a.discard(9)
print(a)