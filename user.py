import csv
from PyInquirer import prompt
user_questions = [
{
        "type":"input",
        "name":"label",
        "message":"New User - Name: ",
    }
]

def add_user():
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    with open('users.csv', 'a') as f:
    # create the csv writer
        writer = csv.writer(f)
    # write a row to the csv file
        writer.writerow(infos.values())
    print("Expense Added !")
    return True


def get_user(answers):
    user = []
    with open('users.csv') as f:
        reader = csv.reader(f)
        for row in reader:
            user.append(row[0])
    return user
    

def get_user_option(answers):
    tmp = get_user(answers)
    options = []
    for res in tmp:
        if (res == answers['user']):
            options += [{'name' : res, 'checked': True }]
        else:
            options += [{'name' : res}]
    return options