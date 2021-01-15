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
    result = []
    for month in months:
        prec_monthly = 0
        for i in prec_seattle:
            if f'2010-{month}' in i['date']:
                prec_monthly += i['value']
        result.append(prec_monthly)
    json.dump(result,file_result,indent=1)
#print(result)

# --- part 2 ---
annual_sum = sum(result)

with open('result.json','w') as file_result:
    prec_relative = []
    for month in result:
        prec_relative.append([month, month/annual_sum])
    json.dump(prec_relative, file_result, indent=1)

# --- part 3 ---
