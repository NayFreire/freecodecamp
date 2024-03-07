cpf = '111.777.222-33'
cpf_translated = str.maketrans({'.':'', '-':''})
cpf = cpf.translate(cpf_translated)
digits = [int(digit) for digit in cpf]
multipliers = [mult for mult in range(1, 11)]
print(cpf, digits, digits[0:9])

if len(cpf) == 9:
    total_sum_1 = 0
    for digit, number in zip(digits[0:9], reversed(multipliers)):
        verification_1 = digit * number
        #print(f'{digit}x{number}={verification_1}')
        total_sum_1 += verification_1

    digit_1 = total_sum_1 % 11

    print(digit_1)
    if digit_1 in [0, 1]:
        digit_1 = 0
    elif digit_1 in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        digit_1 = 11 - digit_1

    print(digit_1)

    digits.append(digit_1)
    print(digits)

    multipliers = [mult for mult in range(1, 12)]
    total_sum_2 = 0
    for digit, number in zip(digits[0:10], reversed(multipliers)):
        verification_2 = digit * number
        #print(f'{digit}x{number}={verification_2}')
        total_sum_2 += verification_2

    digit_2 = total_sum_2 % 11
    if digit_2 in [0, 1]:
        digit_2 = 0
    elif digit_2 in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
        digit_2 = 11 - digit_2
    digits.append(digit_2)
    print('#', digits)

elif len(cpf) == 11:
    full_cpf = ''.join(str(digit) for digit in digits)
    print(full_cpf)