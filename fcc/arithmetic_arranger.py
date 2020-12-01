# def arithmetic_arranger(problems):
#     mathArr = []
#     line1 = ''
#     line2 = ''
#     line3 = ''
#     line4 = ''

#     for i in problems:
#         x = i.split(' ')
#         mathArr.append(x)
#     # print(mathArr)
#     for prob in mathArr:
#         line1 += prob[0] + " "
#         line2 += prob[1] + " " + prob[2] + " "
#         line3 += '-' * len(prob[1] + " " + prob[2] + " ") + " "
#         if prob[1] == '+':
#             line4 += str(int(prob[0]) + int(prob[2])) + ' '
#         elif prob[1] == '-':
#             line4 += str(int(prob[0]) - int(prob[2])) + ' '

#     print(line1)
#     print(line2)
#     print(line3)
#     print(line4)

#     # return arranged_problems

# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

def arithmetic_arranger(problems):
    mathArr = []
    line1 = ''
    line2 = ''
    line3 = ''
    line4 = ''

    for i in problems:
        x = i.split(' ')
        mathArr.append(x)
    # print(mathArr)
    for j in mathArr:
        for k in mathArr[j]:
            print(mathArr[j][k])
    # print(line1)
    # print(line2)
    # print(line3)
    # print(line4)

    # return arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])