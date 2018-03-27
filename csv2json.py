import json

import pandas as pd

df = pd.read_excel('input.xls')
df.fillna(value="", inplace=True)
flavor = {"Ingredient name", "Type", "Milliliters", "Grams", "Drops*", "% of total"}

juice = {}
params = {}
juice_list = []

result = []

for index, row in df.iterrows():
    for i in range(len(df.columns)):
        if df.columns[i] in flavor:
            juice[df.columns[i]] = row[df.columns[i]]
        else:
            if "empty" == params.get(df.columns[i], "empty"):
                params[df.columns[i]] = row[df.columns[i]]
            elif params.get(df.columns[0]) != row[df.columns[0]]:
                juice_list = []
                result.append(params)
                params = {}
                params[df.columns[i]] = row[df.columns[i]]

    juice_list.append(juice)
    juice = {}
    params["flavor"] = juice_list
result.append(params)
print json.dumps(result)

with open('data.json', 'w') as outfile:
    json.dump(result, outfile)
