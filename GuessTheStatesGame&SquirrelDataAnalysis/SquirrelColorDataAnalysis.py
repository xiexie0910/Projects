import pandas as pd 
# reading csv file 
data = pd.read_csv('squirrel_data.csv')
# this is going to access all the column informations if the row value of the Primary Fur color == 'Gray
print(data[data['Primary Fur Color'] == 'Gray'])

# repeat 3 times for all the different colors
gray = len(data[data['Primary Fur Color'] == 'Gray'])
black = len(data[data['Primary Fur Color'] == 'Black'])
cinnamon = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# put into pandas dataframe
df = pd.DataFrame({'Fur Color': ['Gray',"Black","Cinnamon"],
                   'Count': [gray, black,cinnamon]})
# convert to csv
df.to_csv('primaryfurcolor.csv')