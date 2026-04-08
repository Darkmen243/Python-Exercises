'''
Даны два строковых представления чисел A и B. Нужно максимизировать A, заменив в нём любую
цифру на цифру из B. Каждую цифру B можно использовать только один раз.
'''
def maximize_A(A:str,B:str) -> str:
    B = "".join(sorted(B,reverse=True))
    print(B)
    list_A = list(A)
    index_of_B = 0
    for i in range(0,len(list_A)):
       if index_of_B < len(B) and B[index_of_B]>list_A[i]:
           list_A[i] = B[index_of_B]
           index_of_B+=1
           print(list_A)
    return "".join(list_A)
A = '12345'
B = '96578'
C = maximize_A(A,B)
print(C)
