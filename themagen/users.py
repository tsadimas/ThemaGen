"""
helper module, reads CSV file with users

CSV file has the format:

Name1 Surname1, email1@host
Name2 Surname2, email2@host
Name3 Surname3, email3@host
...

"""
from dataclasses import dataclass
import csv


@dataclass
class User:
    full_name: str
    email: str
    full_name_sanitized: str


def read_csv(users_file = 'users.csv'):
    users = []
    with open(users_file, 'r') as f:
        csvreader = csv.reader(f, delimiter=',')
        for line in csvreader:
            user = User(
                full_name = line[0],
                email = line[1],
                full_name_sanitized = line[0].strip().replace(' ',''),
            )
            users.append(user)
    return users
       
