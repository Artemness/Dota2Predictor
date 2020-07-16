import pandas as pd
import json
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.metrics import balanced_accuracy_score, accuracy_score, confusion_matrix, f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import lightgbm as lgb
from sklearn.externals import joblib
import pickle

heros = ('Anti Mage', 'Axe', 'Bane', 'Bloodseeker', 'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Morphling', 'Shadow Fiend', 'Phantom Lancer', 'Puck', 'Pudge', 'Razor', 'Sand King', 'Storm Spirit', 'Sven', 'Tiny', 'Vengeful Spirit', 'Windranger', 'Zeus', 'Kunkka', 'Lina', 'Lion', 'Shadow Shaman', 'Slardar', 'Tidehunter', 'Witch Doctor', 'Lich', 'Riki', 'Enigma', 'Tinker', 'Sniper', 'Necrophos', 'Warlock', 'Beastmaster', 'Queen of Pain', 'Venomancer', 'Faceless Void', 'Wraith King', 'Death Prophet', 'Phantom Assassin', 'Pugna', 'Templar Assassin', 'Viper', 'Luna', 'Dragon Knight', 'Dazzle', 'Clockwerk', 'Leshrac', "Natures Prophet", 'Lifestealer', 'Dark Seer', 'Clinkz', 'Omniknight', 'Enchantress', 'Huskar', 'Night Stalker', 'Broodmother', 'Bounty Hunter', 'Weaver', 'Jakiro', 'Batrider', 'Chen', 'Spectre', 'Ancient Apparition', 'Doom', 'Ursa', 'Spirit Breaker', 'Gyrocopter', 'Alchemist', 'Invoker', 'Silencer', 'Outworld Devourer', 'Lycan', 'Brewmaster', 'Shadow Demon', 'Lone Druid', 'Chaos Knight', 'Meepo', 'Treant Protector', 'Ogre Magi', 'Undying', 'Rubick', 'Disruptor', 'Nyx Assassin', 'Naga Siren', 'Keeper of the Light', 'Io', 'Visage', 'Slark', 'Medusa', 'Troll Warlord', 'Centaur Warrunner', 'Magnus', 'Timbersaw', 'Bristleback', 'Tusk', 'Skywrath Mage', 'Abaddon', 'Elder Titan', 'Legion Commander', 'Techies', 'Ember Spirit', 'Earth Spirit', 'Underlord', 'Terrorblade', 'Phoenix', 'Oracle', 'Winter Wyvern', 'Arc Warden', 'Monkey King', 'Dark Willow', 'Pangolier', 'Grimstroke', 'Void Spirit', 'Snapfire', 'Mars')

heronameswithside = ['RadWin']
for hero in heros:
    radiantname = 'radi_'+hero
    heronameswithside.append(radiantname)
for hero in heros:
    direname = 'dire_' + hero
    heronameswithside.append(direname)

df = pd.read_csv("ProDota2Matchs.csv")

df.replace("Nature's", "Natures")
df.replace("Anti-Mage", "Anti Mage")

RadWin = []

row = 0
radi = {}
dire = {}
for x in range(len(heros)):
    heroname = heros[x]
    heronamenospace = heroname.replace(' ', '_')
    radiantheroname = 'radi_' + heronamenospace
    direheroname = 'dire_' + heronamenospace
    radi[radiantheroname] = []
    dire[direheroname] = []

for i in range(len(df)):
    radwin = df['RadWin'].iloc[i]
    RadWin.append(radwin)
    for x in range(len(heros)):
        heroname = heros[x]
        heronamenospace = heroname.replace(' ', '_')
        radiantheroname = 'radi_' +heronamenospace
        direheroname = 'dire_' +heronamenospace
        if df['Radiant1'].loc[i] == heroname or df['Radiant2'].iloc[i] == heroname or df['Radiant3'].iloc[i] \
                == heroname or df['Radiant4'].iloc[i] == heroname or df['Radiant5'].iloc[i] == heroname:
            radi[radiantheroname].append(1)
        else:
            radi[radiantheroname].append(0)
        if df['Dire1'].loc[i] == heroname or df['Dire2'].iloc[i] == heroname or df['Dire3'].iloc[i] \
                == heroname or df['Dire4'].iloc[i] == heroname or df['Dire5'].iloc[i] == heroname:
            dire[direheroname].append(1)
        else:
            dire[direheroname].append(0)
    print('Working on row number ' + str(i))

radiant = pd.DataFrame.from_dict(radi, orient='index')
radiant = radiant.transpose()
dire = pd.DataFrame.from_dict(dire, orient='index')
dire = dire.transpose()

df_dummies = pd.concat([radiant, dire], axis=1, sort=False)
df_dummies['RadWin'] = RadWin
df_dummies.to_csv('dotadummies.csv', index=False)

df_dummies = pd.read_csv('dotadummies.csv')
X = df_dummies.iloc[:,0:238]
Y = df_dummies['RadWin']

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.4, random_state=42)

d_train = lgb.Dataset(X_train, label=y_train)
lgb_eval = lgb.Dataset(X_test, y_test)

lgbparams = {}
lgbparams['learning_rate'] = 0.003
lgbparams['boosting_type'] = 'gbdt'
lgbparams['objective'] = 'binary'
lgbparams['metric'] = 'binary_error'
lgbparams['sub_feature'] = 0.5
lgbparams['num_leaves'] = 5
lgbparams['min_data'] = 100
lgbparams['max_bin']= 3
lgbparams['max_depth'] = 10
clf = lgb.train(lgbparams, d_train, valid_sets=lgb_eval, early_stopping_rounds=5)

cv_results = lgb.cv(lgbparams,
        d_train,
        num_boost_round=100,
        nfold=3,
        metrics='mae',
        early_stopping_rounds=3,
        # This is what I added
        stratified=False
        )

lgby_pred = clf.predict(X_test)
for i in range(0,len(lgby_pred)):
    if lgby_pred[i]>=.5:
       lgby_pred[i]=1
    else:
       lgby_pred[i]=0

lgb_matrix = confusion_matrix(y_test, lgby_pred)
lgb_acc = f1_score(y_test, lgby_pred, average='binary')
print('Light GBM Accuracy')
print(lgb_acc*100)

ax= plt.subplot()
ax1 = sns.heatmap(lgb_matrix, annot=True, fmt='g', ax = ax);
ax1.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
ax1.set_title('Confusion Matrix for LightGBM Classifier');
ax1.xaxis.set_ticklabels(['RadWin', 'RadLoss']); ax.yaxis.set_ticklabels(['RadWin', 'RadLoss']);
fig1 = ax1.get_figure()
fig1.savefig('LightGBM.png')


rf_model = RandomForestClassifier(n_estimators=10000, max_features=130, max_depth=2, min_samples_leaf=5)
rf_model.fit(X_train, y_train)
random_forest_pred = rf_model.predict(X_test)
print(random_forest_pred)

rf_matrix = confusion_matrix(y_test, random_forest_pred)
rf_acc = balanced_accuracy_score(y_test, random_forest_pred)
print('Random Forest Accuracy')
print(rf_acc*100)

ax.remove()
ax= plt.subplot()
ax2 = sns.heatmap(rf_matrix, annot=True, fmt='g', ax = ax);
ax2.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
ax2.set_title('Confusion Matrix for Random Forest Classifier');
ax2.xaxis.set_ticklabels(['RadWin', 'RadLoss']); ax.yaxis.set_ticklabels(['RadWin', 'RadLoss']);
fig2 = ax2.get_figure()
fig2.savefig('RandomForest.png')

knn_model = KNeighborsClassifier()
knn_model.fit(X_train, y_train)
knn_pred = knn_model.predict(X_test)
print(knn_pred)

knn_matrix = confusion_matrix(y_test, knn_pred)
knn_acc = balanced_accuracy_score(y_test, knn_pred)
print('kNN accuracy:')
print(rf_acc*100)

ax.remove()
ax= plt.subplot()
ax2 = sns.heatmap(rf_matrix, annot=True, fmt='g', ax = ax);
ax2.set_xlabel('Predicted labels');ax.set_ylabel('True labels');
ax2.set_title('Confusion Matrix for Random Forest Classifier');
ax2.xaxis.set_ticklabels(['RadWin', 'RadLoss']); ax.yaxis.set_ticklabels(['RadWin', 'RadLoss']);
fig2 = ax2.get_figure()
fig2.savefig('RandomForest.png')


joblib.dump(rf_model, 'RandomForestDota.pkl')