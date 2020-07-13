import pandas as pd
import requests
import json

with open('apikey.txt') as f:
    apikey = f.read().strip()

heros = pd.read_json('heroes.json')
heros = pd.Series(heros.localized_name.values,index=heros.id).to_dict()

radhero1 = []
radhero2 = []
radhero3 = []
radhero4 = []
radhero5 = []
direhero1 = []
direhero2 = []
direhero3 = []
direhero4 = []
direhero5 = []
radiantwin = []

match_ids = []

failedmatches = []
i= 0
minmatch_id = 0

promatchids = requests.get('https://api.opendota.com/api/proMatches/')
promatchjson = json.loads(promatchids.text)
for match in promatchjson:
    i = i+1
    match_idz = match['match_id']
    match_ids.append(match_idz)
    if i == 100:
        minmatch_id = match['match_id']


for y in range(65):
    print('Pulling Match ids for Number:' + str(y))
    promatchidsmin = requests.get('https://api.opendota.com/api/proMatches?less_than_match_id=' + str(minmatch_id))
    promatchjson2 = json.loads(promatchidsmin.text)
    x = 0
    for matchz in promatchjson2:
        x = x+1
        try:
            match_idz = matchz['match_id']
            match_ids.append(match_idz)
            if x == 100:
                minmatch_id = match['match_id']
        except:
            print('Failed to pull match numbers for ' + str(y))

print(len(match_ids))

matchnum = 0
for match in match_ids:
    matchnum = matchnum + 1
    try:
        r = requests.get("https://api.opendota.com/api/matches/"+ str(match))
        minf = json.loads(r.text)
        minfplayers = minf['players']
        for player in minfplayers:
            slot = player['player_slot']
            hero_id = player['hero_id']
            if slot == 0:
                radhero1.append(hero_id)
            if slot == 1:
                radhero2.append(hero_id)
            if slot == 2:
                radhero3.append(hero_id)
            if slot == 3:
                radhero4.append(hero_id)
            if slot == 4:
                radhero5.append(hero_id)
            if slot == 128:
                direhero1.append(hero_id)
            if slot == 129:
                direhero2.append(hero_id)
            if slot == 130:
                direhero3.append(hero_id)
            if slot == 131:
                direhero4.append(hero_id)
            if slot == 132:
                direhero5.append(hero_id)

        radwin = minf['radiant_win']
        if radwin == True:
            radiantwin.append(1)
        if radwin == False:
            radiantwin.append(0)
    except:
        print('Failed to find match id')
        failedmatches.append(match)
        continue
    print('Finished on Pulling data for ' + str(matchnum) + '!')

df = pd.DataFrame()
df['Radiant1'] = radhero1
df['Radiant2'] = radhero2
df['Radiant3'] = radhero3
df['Radiant4'] = radhero4
df['Radiant5'] = radhero5
df['Dire1'] = direhero1
df['Dire2'] = direhero2
df['Dire3'] = direhero3
df['Dire4'] = direhero4
df['Dire5'] = direhero5

df = df.replace(heros)

df['RadWin'] = radiantwin

df2 = pd.DataFrame
df2['FailedMatches'] = failedmatches

df.to_csv('ProDota2Matchs.csv', index=False)
df2.to_csv('FailedMatches.csv', index=False)
df.to_excel('ProDota2Matchs.xlsx', index=False)