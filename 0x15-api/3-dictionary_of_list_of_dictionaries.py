#!/usr/bin/python3
"""
this script returns information about a given employees TODO list
"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/").json()
    get_todo = requests.get(url + "todos").json()
    usr_dict = {}
    name_dict = {}
    for every in user:
        emp_id = every.get("id")
        usr_dict[emp_id] = []
        name_dict[emp_id] = every.get('username')
    for each in get_todo:
        u_tsk_dict = {}
        emp_id = each.get("userId")
        u_tsk_dict["task"] = each.get('title')
        u_tsk_dict["completed"] = each.get('completed')
        u_tsk_dict["username"] = name_dict.get(emp_id)
        usr_dict.get(emp_id).append(u_tsk_dict)
    with open("todo_all_employees.json", 'w') as json_f:
        json.dump(usr_dict, json_f)
