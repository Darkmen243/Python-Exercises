import csv
tasks = {}
inp = 0
print(r"1. Add new task to a todo list \n" 
"       2. Remove existing task from a todo list \n" 
"       3. Edit existing task from a todo list \n" 
"       4. Save your todo list to a csv file \n" 
"       5. Exit the program")
while inp !=5:
    try:
        inp = int(input())
    except ValueError:
        print("Please enter a valid number.")
        continue
    match inp:
        case 1:
            print(r"Input a name and status for your task separated by a comma")
            name,status = input().split(',')
            pos = len(tasks)
            tasks[pos] = {'name': name,
                           'status':status
                        }         
            print(tasks)
        case 2:
            length=len(tasks)
            if length>0:
                print('Select which task number you want to delete.')
                print(tasks)
                number = int(input())
                if number in tasks:
                    tasks.pop(number)
                    print('Sucessfully deleted a task')
                else:
                    print('Entered task number is invalid.')
            else: 
                print("The list is empty.")
            
        case 3:
            length=len(tasks)
            if length>0:
                print('Select which task number you want to edit.')
                print(tasks)
                number = int(input())
                if number in tasks:
                    print('Enter new name and status separated by a comma')
                    name, status = input().split(',')
                    tasks[number] = { 'name': name,
                                      'status':status
                                     }
                    print('Sucessfully edited a task')
                else:
                    print('Entered task number is invalid.')
            else:
                print("The list is empty.")
        case 4:
            if len(tasks)!=0:
                fields = ['number', 'name', 'status']
                with open('todolist.csv', mode='w') as todolist:
                    writer = csv.DictWriter(todolist, fieldnames=fields)
                    writer.writeheader()
                    for number, task in tasks.items():
                        writer.writerow({
                            'number': number,
                            'name': task['name'],
                            'status': task['status']
                        })    
                print('Todo list saved to a file.')  
        case 5:
            print('Exiting the program...')
            break