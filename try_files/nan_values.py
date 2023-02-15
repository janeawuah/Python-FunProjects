import random
import pandas as pd
from typing import List

def clean_list(item_list) -> List:
    return [x for x in item_list if str(x) != ""]

def main():
    names = pd.read_csv("try_files/names.csv")
    names.fillna("", inplace=True)


    female_names = clean_list(names['female'])
    male_names = clean_list(names['male'])
    last_names = clean_list(names['lastname'])
    first_names = male_names +female_names

    print("Length of female name is: ", len(female_names))
    print("Length of male name is: ", len(male_names))
    print("Length of last name is: ", len(last_names))
    print("Length of first name is: ", len(first_names))


main()