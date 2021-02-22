import pandas
import datetime as dt
import random


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthday.csv")

data_dict = {row.month: row.day for (index, row) in data.iterrows()}

print(data_dict)
