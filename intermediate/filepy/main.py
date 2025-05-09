# with open("/Users/anirudhmulky/Desktop/python/filepy/weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv

# with open("/Users/anirudhmulky/Desktop/python/filepy/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))

#     print(temp)

# import pandas
# data = pandas.read_csv("/Users/anirudhmulky/Desktop/python/filepy/weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()


# print(data["temp"].mean())
# print(data["temp"].max())

# #get data in columns
# print(data["condition"])
# #one more way
# print(data.condition)

# #Get data in rows
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])#gets the max value

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]

# #create a data frame from scractch
# anydata = pandas.DataFrame(data_dict)

import pandas

data = pandas.read_csv("/Users/anirudhmulky/Desktop/python/filepy/nyc.csv")
grey_sq = len(data[data["Primary Fur Color"] == "Gray"])
cina_sq = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_sq = len(data[data["Primary Fur Color"] == "Black"])
print(grey_sq)
print(black_sq)
print(cina_sq)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [grey_sq,cina_sq,black_sq]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squ_count.csv")