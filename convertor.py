def binary_convertor(num):
    if num == 0:
        return "0"
    binary_str = ""
    while num > 0:
        remainder = num % 2
        binary_str = str(remainder) + binary_str
        num = num // 2
    return binary_str