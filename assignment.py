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

months = ["2010-01", "2010-02", "2010-03", "2010-04", "2010-05", "2010-06", "2010-07", "2010-08", "2010-09", "2010-10", "2010-11", "2010-12"]
with open('result.json','w') as file_result:
    result = []
    for month in months:
        prec_monthly = 0
        for i in prec_seattle:
            if month in i['date']:
                prec_monthly += i['value']
        result.append({month: prec_monthly})
    json.dump(result,file_result,indent=1)

# --- part 2 ---
#for month in result:
#    print(result[month])