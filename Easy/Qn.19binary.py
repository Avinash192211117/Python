def largest_binary_number(num1, num2, num3):
    num1_dec = int(num1, 2)
    num2_dec = int(num2, 2)
    num3_dec = int(num3, 2)
    max_dec = max(num1_dec, num2_dec, num3_dec)
    max_bin = bin(max_dec)[2:]
    return max_bin
binary1 = "1010"
binary2 = "1101"
binary3 = "1001"
print("The largest binary number is:", largest_binary_number(binary1, binary2, binary3))
