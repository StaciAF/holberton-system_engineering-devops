#!/usr/bin/python3
"""
this script returns information about a given employees TODO list
"""


if __name__ == '__main__':
    import csv
    import requests
    from sys import argv
    url = "https://jsonplaceholder.typicode.com/"
    emp_id = int(argv[1])
    user = requests.get(url + "users/{}".format(emp_id)).json()
    get_todo = requests.get(url + "users/{}/todos".format(emp_id)).json()
    USERNAME = user.get('username')
    with open('{}.csv'.format(emp_id), 'w', newline='') as csv_version:
        write_csv = csv.writer(csv_version, quoting=csv.QUOTE_ALL)
        for each in get_todo:
            write_csv.writerow([emp_id, USERNAME,
                                each.get('completed'), each.get('title')])
