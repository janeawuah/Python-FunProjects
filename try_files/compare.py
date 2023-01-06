# This is to figure out how to compare variablesnames to datatypes in python

import random
from faker import Faker
import json



faker = Faker()

def get_name(*gndr):
    random_name = faker.name()
    print("In the function name is : ", random_name)
    return random_name

def get_dob():
    random_dob = faker.date()


def get_gender():
    return random.choice(['f','m'])

def main():
    piis = ["name","dob","gender"]
    piis_value = []
    num = len(piis)



    for n in piis:
        if(n == "name"):
            piis_value.append(get_name())
        elif(n =="dob"):
            piis_value.append(get_dob())
        elif(n =="gender"):
            piis_value.append(get_gender())



    data = []
    for i in range(num):
        data.append([piis[i]," : ",piis_value[i]])
        # print(piis[i]," : ",piis_value[i])
    
    jsonString = json.dumps(data)

    print(jsonString)


main()



