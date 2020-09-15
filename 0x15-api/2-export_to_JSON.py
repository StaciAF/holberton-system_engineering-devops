#!/usr/bin/python3
"""
this script returns information about a given employees TODO list
"""


if __name__ == '__main__':
    import json
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(argv[1])
    user = requests.get(url + "users/{}".format(emp_id)).json()
    get_todo = requests.get(url + "users/{}/todos".format(emp_id)).json()
    USERNAME = user.get('username')
    all_tasks = []
    for each in get_todo:
        u_tsk_dict = {}
        u_tsk_dict["task"] = each.get('title')
        u_tsk_dict["completed"] = each.get('completed')
        u_tsk_dict["username"] = USERNAME
        all_tasks.append(u_tsk_dict)
    json_exp = {}
    json_exp[emp_id] = all_tasks
    with open("{}.json".format(emp_id), 'w') as json_f:
        json.dump(json_exp, json_f)
