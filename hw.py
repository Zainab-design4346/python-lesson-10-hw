num = 10
if num== 0:
    print(0)
binary_num = "" 
while num > 0:
    binary_num = str(num % 2) + binary_num
    num = num // 2
print(binary_num)