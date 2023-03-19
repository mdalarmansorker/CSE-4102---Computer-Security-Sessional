number = int(input("Integer input: "))
number = format(number, '06b')
print("Binary:",number)
s_box = [[2,12,4,1,7,10,11,6,8,5,3,15,13,0,14,9],
        [14,11,2,12,4,7,13,1,5,0,15,10,3,9,8,6],
        [4,2,1,11,10,13,7,8,15,9,12,5,6,3,0,14],
        [11,8,12,7,1,14,2,13,6,15,0,9,10,4,5,3]]

# for i in range(4):
#     print("Row", i, ":")
#     a = list(map(int, input().split(" ")))
#     s_box.append(a)

row = int(number[5]+number[0], 2)
column = int(number[4]+number[3]+number[2]+number[1], 2)
output = '{:04b}'.format(s_box[row][column])

print("Output:",output)