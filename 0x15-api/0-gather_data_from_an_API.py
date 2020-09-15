#!/usr/bin/python3
"""
this script returns information about a given employees TODO list
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    count = 0
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(argv[1])
    user = requests.get(url + "users/{}".format(emp_id)).json()
    get_todo = requests.get(url + "users/{}/todos".format(emp_id)).json()
    complete_tasks = []
    for task in get_todo:
        if task.get('completed') is True:
            complete_tasks.append(task.get('title'))
    EMPLOYEE_NAME = user.get('name')
    NUM_OF_DONE_TASKS = len(complete_tasks)
    TOTAL_NUM_OF_TASKS = len(get_todo)
    print("Employee {} is done with tasks({}/{}):".format(EMPLOYEE_NAME,
                                                          NUM_OF_DONE_TASKS,
                                                          TOTAL_NUM_OF_TASKS))
    for each in complete_tasks:
        print("\t {}".format(each))
