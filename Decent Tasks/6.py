def process (input_string:str) ->str:
    a=0
    b=0
    c=0
    numbers = input_string.split()
    for number in numbers:
        if int(number)>0:
            a+=1
        elif int(number)<0:
            b+=1
        elif int(number)==0:
            c+=1
    return_string = f"выше нуля: {a}, ниже нуля: {b}, равня нулю: {c}"
    return return_string
input_string = input()
output_string = process(input_string)
print(output_string)