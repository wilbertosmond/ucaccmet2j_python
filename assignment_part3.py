import json

# --- part 3 ---
with open('stations.csv') as file_csv:
    headers = file_csv.readline()
    locations = []
    stations = []
    states = []
    for line in file_csv:
        Location, State, Station = line.strip().split(',')
        locations.append(Location)
        stations.append(Station)
        states.append(State)

# --- 3.1.1 ---
with open('precipitation.json') as file_json:
    prec = json.load(file_json)
    prec_stations = []
    for station in stations:
        prec_station = []
        for line in prec:
            if line['station'] == station:
                prec_station.append({'date': line['date'],
                                     'station': line['station'],
                                     'value': line['value']})
        prec_stations.append(prec_station)

months = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
totalMonthPrecs = []
for station in range(len(stations)):
    totalMonthPrec = []
    for month in months:
        MonthPrec = 0
        for i in prec_stations[station]:
            if f'2010-{month}' in i['date']:
                MonthPrec += i['value']
        totalMonthPrec.append(MonthPrec)
    totalMonthPrecs.append(totalMonthPrec)

# --- 3.1.2 ---
totalYearPrecs = []
for station in range(len(stations)):
    totalYearPrecs.append(sum(totalMonthPrecs[station]))
print(totalYearPrecs)

relativeMonthPrecs = []
for station in range(len(stations)):
    relativeMonthPrec = []
    for month in totalMonthPrecs[station]:
        relativeMonthPrec.append(month/totalYearPrecs[station])
    relativeMonthPrecs.append(relativeMonthPrec)

relativeYearPrecs = []
for station in range(len(stations)):
    relativeYearPrecs.append(totalYearPrecs[station]/sum(totalYearPrecs))

# --- 3.2 ---
with open('results_part3.json','w') as file:
    results = []
    for station in range(len(stations)):
        results.append({locations[station]: {'station': stations[station],
                                            'state': states[station],
                                           'totalMonthlyPrecipitation': totalMonthPrecs[station],
                                           'relativeMonthlyPrecipitation': relativeMonthPrecs[station],
                                           'totalYearlyPrecipitation': totalYearPrecs[station],
                                           'relativeYearlyPrecipitation': relativeYearPrecs[station]}})
    json.dump(results, file, indent=1)
