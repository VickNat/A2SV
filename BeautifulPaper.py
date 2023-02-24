testCase = int(input())
 
for idx in range(testCase):
    matrix1 = list(map(int, input().split()))
    matrix2 = list(map(int, input().split()))
    answer = ""
    
    if matrix1[0]+matrix2[0] == matrix1[1] and matrix1[1] == matrix2[1]:
        answer = "Yes"
        print(answer)
    elif matrix1[0]+matrix2[1] == matrix1[1] and matrix1[1] == matrix2[0]:
        answer = "Yes"
        print(answer)
    elif matrix1[1]+matrix2[0] == matrix1[0] and matrix1[0] == matrix2[1]:
        answer = "Yes"
        print(answer)
    elif matrix1[1]+matrix2[1] == matrix1[0] and matrix1[0] == matrix2[0]:
        answer = "Yes"
        print(answer)
    else:
        answer = "No"
        print(answer)
