"""
Description:
 Prints the name and age of all people in the Social Network database
 who are age 50 or older, and saves the information to a CSV file.

Usage:
 python old_people.py
"""
import os
from create_db import db_path, script_dir
import pandas as pd
import sqlite3


def main():
    old_people_list = get_old_people()
    print_name_and_age(old_people_list)

    old_people_csv = os.path.join(script_dir, 'old_people.csv')
    save_name_and_age_to_csv(old_people_list, old_people_csv)

def get_old_people():
    """Queries the Social Network database for all people who are at least 50 years old.

    Returns:
        list: (name, age) of old people 
    """
    # TODO: Create function body
    # Hint: See example code in lab instructions entitled "Getting People Data from the Database"
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()

    cur.execute('SELECT name,age FROM people WHERE age >= 50')

    data = cur.fetchall()
    

    con.commit()
    con.close()

    return data


def print_name_and_age(name_and_age_list):
    """Prints name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
    """
    # TODO: Create function body
    # Hint: Use a for loop to iterate the list of tuples to print a sentence for each old person
    
    for person in name_and_age_list:
        nam = person[0]
        ag = person[1]

        print(f'{nam} is {ag} years old.')
    
    return

def save_name_and_age_to_csv(name_and_age_list, csv_path):
    """Saves name and age of all people in provided list

    Args:
        name_and_age_list (list): (name, age) of people
        csv_path (str): Path of CSV file
    """
    # TODO: Create function body
    # Hint: In Lab 3, we converted a list of tuples into a pandas DataFrame and saved it to a CSV file
    df = pd.DataFrame(name_and_age_list)
    df.to_csv(csv_path, header=['Name', 'Age'], index=False)

    return

if __name__ == '__main__':
   main()