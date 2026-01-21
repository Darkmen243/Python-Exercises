'''
Given a file:

INFO User logged in
ERROR Invalid password
INFO Page loaded
ERROR Timeout
ERROR Invalid password

Tasks:
Count error lines
Return list of unique error messages
'''
errors = set()
counter = 0
try:
     with open("Decent Tasks/3.txt") as file:
        for line in file:
            if "ERROR" in line:
                    counter+=1
                    errors.add(line.strip())
        print(f"This file has {counter} errors inside and following unique errors\n {errors}")
except Exception as ex:
    print(ex)

