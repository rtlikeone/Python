import pandas

data = pandas.read_csv("squirrel-data.csv")
# print(data.__dict__)

# Get "Primary Fur Color" column
fur_color = data["Primary Fur Color"]
# Get individual color count
gray = len(data[fur_color == "Gray"])
cinnamon = len(data[fur_color == "Cinnamon"])
black = len(data[fur_color == "Black"])

print(type(data[fur_color == "Gray"]))

# print(gray)
# print(cinnamon)
# print(black)

# Add data to dict to then convert to .csv file
data_fur_color = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray, cinnamon, black]
}
# First convert our dict to a DataFrame with .DataFrame()
dict_to_dataFrame = pandas.DataFrame(data_fur_color)
# Then convert it into a .csv file with .to_csv("file_name.csv")
dict_to_dataFrame.to_csv("squirrel_fur_color_data.csv")
