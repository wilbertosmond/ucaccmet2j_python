import json

# --- part 1 ---
with open('precipitation.json') as file_json:
    prec = json.load(file_json)
    prec_seattle = []
    for line in prec:
        if line['station'] == 'GHCND:US1WAKG0038':
            prec_seattle.append({'date': line['date'],
                                'value': line['value']})
#print(prec_seattle)

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
with open('result.json','w') as file_result:
    totalMonthPrec = []
    for month in months:
        MonthPrec = 0
        for i in prec_seattle:
            if f'2010-{month}' in i['date']:
                MonthPrec += i['value']
        totalMonthPrec.append(MonthPrec)
    json.dump(totalMonthPrec,file_result,indent=1)
#print(totalMonthPrec)

# --- part 2 ---
totalYearPrec = sum(totalMonthPrec)

with open('result.json','w') as file_result:
    relativeMonthPrec = []
    for month in totalMonthPrec:
        relativeMonthPrec.append([month, month/totalYearPrec])
    json.dump(relativeMonthPrec, file_result, indent=1)
