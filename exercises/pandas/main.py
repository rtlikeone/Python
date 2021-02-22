import pandas

# converts our csv data into a table
data = pandas.read_csv("weather_data.csv")
# Get the amount of times "Sunny" occurs with .count()
amount_sunny = data[data["condition"] == "Sunny"].count()
print(amount_sunny.condition)

# Get data in column:
# print(data.temp.to_list())
# or with brackets
# print(data["temp"].to_list())

# get data in row
# monday = data[data.day == "Monday"]
# print(monday)
# Get column data from row
# print((monday.temp * 9/5) + 32)
# print(monday.condition)

# create dataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "score": [76, 56, 65]
# }
#
# dict_to_dataFrame = pandas.DataFrame(data_dict)
# print(dict_to_dataFrame)
# # Convert our dict to csv file
# dict_to_dataFrame.to_csv("dict_to_csv")




# Get data from row on hottest day
# hottest_day_row = data[data.temp == data.temp.max()]
# print(hottest_day_row)

# get average of temp_list
# temp_list = data["temp"].to_list()
# sum_temp = sum(temp_list)
# avg = sum_temp / len(temp_list)
# print(f"Temp list average: {round(avg, 2)}")

# shorthand for getting the average is by using the .mean() in pandas
# print(data["temp"].mean())

# Get max num in temp list
# print(data["temp"].max())

# converts our data table into a dictionary
# data_dict = data.to_json()
# print(data_dict)
