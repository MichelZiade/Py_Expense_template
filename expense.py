from PyInquirer import prompt
import csv

from user import get_user, get_user_option



expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"user",
        "message":"New Expense - Spender: ",
        "choices": get_user
    },
    {
        'type': 'checkbox',
        'qmark': '➡',
        'message': 'Select all the spenders',
        'name': 'allspenders',
        "choices": get_user_option,
    },
]

def new_expense(*args):
    infos = prompt(expense_questions)
    try:
        int(infos['amount']) 
    except ValueError:
        raise("This is not a number!")
    with open('expense_report.csv', 'a') as f:
    # create the csv writer
        writer = csv.writer(f)
    # write a row to the csv file
        writer.writerow(infos.values())
    print("Expense Added !")
    return True