import pandas as pd
import json
import numpy as np
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


heros = ('Anti-Mage', 'Axe', 'Bane', 'Bloodseeker', 'Crystal Maiden', 'Drow Ranger', 'Earthshaker', 'Juggernaut', 'Mirana', 'Morphling', 'Shadow Fiend', 'Phantom Lancer', 'Puck', 'Pudge', 'Razor', 'Sand King', 'Storm Spirit', 'Sven', 'Tiny', 'Vengeful Spirit', 'Windranger', 'Zeus', 'Kunkka', 'Lina', 'Lion', 'Shadow Shaman', 'Slardar', 'Tidehunter', 'Witch Doctor', 'Lich', 'Riki', 'Enigma', 'Tinker', 'Sniper', 'Necrophos', 'Warlock', 'Beastmaster', 'Queen of Pain', 'Venomancer', 'Faceless Void', 'Wraith King', 'Death Prophet', 'Phantom Assassin', 'Pugna', 'Templar Assassin', 'Viper', 'Luna', 'Dragon Knight', 'Dazzle', 'Clockwerk', 'Leshrac', "Nature's Prophet", 'Lifestealer', 'Dark Seer', 'Clinkz', 'Omniknight', 'Enchantress', 'Huskar', 'Night Stalker', 'Broodmother', 'Bounty Hunter', 'Weaver', 'Jakiro', 'Batrider', 'Chen', 'Spectre', 'Ancient Apparition', 'Doom', 'Ursa', 'Spirit Breaker', 'Gyrocopter', 'Alchemist', 'Invoker', 'Silencer', 'Outworld Devourer', 'Lycan', 'Brewmaster', 'Shadow Demon', 'Lone Druid', 'Chaos Knight', 'Meepo', 'Treant Protector', 'Ogre Magi', 'Undying', 'Rubick', 'Disruptor', 'Nyx Assassin', 'Naga Siren', 'Keeper of the Light', 'Io', 'Visage', 'Slark', 'Medusa', 'Troll Warlord', 'Centaur Warrunner', 'Magnus', 'Timbersaw', 'Bristleback', 'Tusk', 'Skywrath Mage', 'Abaddon', 'Elder Titan', 'Legion Commander', 'Techies', 'Ember Spirit', 'Earth Spirit', 'Underlord', 'Terrorblade', 'Phoenix', 'Oracle', 'Winter Wyvern', 'Arc Warden', 'Monkey King', 'Dark Willow', 'Pangolier', 'Grimstroke', 'Void Spirit', 'Snapfire', 'Mars')

heronameswithside = ['RadWin']
for hero in heros:
    radiantname = 'radi_'+hero
    heronameswithside.append(radiantname)
for hero in heros:
    direname = 'dire_' + hero
    heronameswithside.append(direname)

df = pd.read_csv("ProDota2Matchs.csv")

RadWin = []
radi_Anti_Mage = []
radi_Axe = []
radi_Bane = []
radi_Bloodseeker = []
radi_Crystal_Maiden = []
radi_Drow_Ranger = []
radi_Earthshaker = []
radi_Juggernaut = []
radi_Mirana = []
radi_Morphling = []
radi_Shadow_Fiend = []
radi_Phantom_Lancer = []
radi_Puck = []
radi_Pudge = []
radi_Razor = []
radi_Sand_King = []
radi_Storm_Spirit = []
radi_Sven = []
radi_Tiny = []
radi_Vengeful_Spirit = []
radi_Windranger = []
radi_Zeus = []
radi_Kunkka = []
radi_Lina = []
radi_Lion = []
radi_Shadow_Shaman = []
radi_Slardar = []
radi_Tidehunter = []
radi_Witch_Doctor = []
radi_Lich = []
radi_Riki = []
radi_Enigma = []
radi_Tinker = []
radi_Sniper = []
radi_Necrophos = []
radi_Warlock = []
radi_Beastmaster = []
radi_Queen_of_Pain = []
radi_Venomancer = []
radi_Faceless_Void = []
radi_Wraith_King = []
radi_Death_Prophet = []
radi_Phantom_Assassin = []
radi_Pugna = []
radi_Templar_Assassin = []
radi_Viper = []
radi_Luna = []
radi_Dragon_Knight = []
radi_Dazzle = []
radi_Clockwerk = []
radi_Leshrac = []
radi_Natures_Prophet = []
radi_Lifestealer = []
radi_Dark_Seer = []
radi_Clinkz = []
radi_Omniknight = []
radi_Enchantress = []
radi_Huskar = []
radi_Night_Stalker = []
radi_Broodmother = []
radi_Bounty_Hunter = []
radi_Weaver = []
radi_Jakiro = []
radi_Batrider = []
radi_Chen = []
radi_Spectre = []
radi_Ancient_Apparition = []
radi_Doom = []
radi_Ursa = []
radi_Spirit_Breaker = []
radi_Gyrocopter = []
radi_Alchemist = []
radi_Invoker = []
radi_Silencer = []
radi_Outworld_Devourer = []
radi_Lycan = []
radi_Brewmaster = []
radi_Shadow_Demon = []
radi_Lone_Druid = []
radi_Chaos_Knight = []
radi_Meepo = []
radi_Treant_Protector = []
radi_Ogre_Magi = []
radi_Undying = []
radi_Rubick = []
radi_Disruptor = []
radi_Nyx_Assassin = []
radi_Naga_Siren = []
radi_Keeper_of_the_Light = []
radi_Io = []
radi_Visage = []
radi_Slark = []
radi_Medusa = []
radi_Troll_Warlord = []
radi_Centaur_Warrunner = []
radi_Magnus = []
radi_Timbersaw = []
radi_Bristleback = []
radi_Tusk = []
radi_Skywrath_Mage = []
radi_Abaddon = []
radi_Elder_Titan = []
radi_Legion_Commander = []
radi_Techies = []
radi_Ember_Spirit = []
radi_Earth_Spirit = []
radi_Underlord = []
radi_Terrorblade = []
radi_Phoenix = []
radi_Oracle = []
radi_Winter_Wyvern = []
radi_Arc_Warden = []
radi_Monkey_King = []
radi_Dark_Willow = []
radi_Pangolier = []
radi_Grimstroke = []
radi_Void_Spirit = []
radi_Snapfire = []
radi_Mars = []
dire_Anti_Mage = []
dire_Axe = []
dire_Bane = []
dire_Bloodseeker = []
dire_Crystal_Maiden = []
dire_Drow_Ranger = []
dire_Earthshaker = []
dire_Juggernaut = []
dire_Mirana = []
dire_Morphling = []
dire_Shadow_Fiend = []
dire_Phantom_Lancer = []
dire_Puck = []
dire_Pudge = []
dire_Razor = []
dire_Sand_King = []
dire_Storm_Spirit = []
dire_Sven = []
dire_Tiny = []
dire_Vengeful_Spirit = []
dire_Windranger = []
dire_Zeus = []
dire_Kunkka = []
dire_Lina = []
dire_Lion = []
dire_Shadow_Shaman = []
dire_Slardar = []
dire_Tidehunter = []
dire_Witch_Doctor = []
dire_Lich = []
dire_Riki = []
dire_Enigma = []
dire_Tinker = []
dire_Sniper = []
dire_Necrophos = []
dire_Warlock = []
dire_Beastmaster = []
dire_Queen_of_Pain = []
dire_Venomancer = []
dire_Faceless_Void = []
dire_Wraith_King = []
dire_Death_Prophet = []
dire_Phantom_Assassin = []
dire_Pugna = []
dire_Templar_Assassin = []
dire_Viper = []
dire_Luna = []
dire_Dragon_Knight = []
dire_Dazzle = []
dire_Clockwerk = []
dire_Leshrac = []
dire_Natures_Prophet = []
dire_Lifestealer = []
dire_Dark_Seer = []
dire_Clinkz = []
dire_Omniknight = []
dire_Enchantress = []
dire_Huskar = []
dire_Night_Stalker = []
dire_Broodmother = []
dire_Bounty_Hunter = []
dire_Weaver = []
dire_Jakiro = []
dire_Batrider = []
dire_Chen = []
dire_Spectre = []
dire_Ancient_Apparition = []
dire_Doom = []
dire_Ursa = []
dire_Spirit_Breaker = []
dire_Gyrocopter = []
dire_Alchemist = []
dire_Invoker = []
dire_Silencer = []
dire_Outworld_Devourer = []
dire_Lycan = []
dire_Brewmaster = []
dire_Shadow_Demon = []
dire_Lone_Druid = []
dire_Chaos_Knight = []
dire_Meepo = []
dire_Treant_Protector = []
dire_Ogre_Magi = []
dire_Undying = []
dire_Rubick = []
dire_Disruptor = []
dire_Nyx_Assassin = []
dire_Naga_Siren = []
dire_Keeper_of_the_Light = []
dire_Io = []
dire_Visage = []
dire_Slark = []
dire_Medusa = []
dire_Troll_Warlord = []
dire_Centaur_Warrunner = []
dire_Magnus = []
dire_Timbersaw = []
dire_Bristleback = []
dire_Tusk = []
dire_Skywrath_Mage = []
dire_Abaddon = []
dire_Elder_Titan = []
dire_Legion_Commander = []
dire_Techies = []
dire_Ember_Spirit = []
dire_Earth_Spirit = []
dire_Underlord = []
dire_Terrorblade = []
dire_Phoenix = []
dire_Oracle = []
dire_Winter_Wyvern = []
dire_Arc_Warden = []
dire_Monkey_King = []
dire_Dark_Willow = []
dire_Pangolier = []
dire_Grimstroke = []
dire_Void_Spirit = []
dire_Snapfire = []
dire_Mars = []

row = 0
for i in range(len(df)):
    radwin = df['RadWin'].iloc[i]
    RadWin.append(radwin)
    if df['Radiant1'].loc[i] == 'Anti-Mage' or df['Radiant2'].iloc[i] == 'Anti-Mage' or df['Radiant3'].iloc[i] == 'Anti-Mage' or df['Radiant4'].iloc[i]=='Anti-Mage' or df['Radiant5'].iloc[i] =='Anti-Mage':
        radi_Anti_Mage.append(1)
    else:
        radi_Anti_Mage.append(0)
    if df['Dire1'].loc[i] == 'Anti-Mage' or df['Dire2'].iloc[i] == 'Anti-Mage' or df['Dire3'].iloc[i] == 'Anti-Mage' or df['Dire4'].iloc[i]=='Anti-Mage' or df['Dire5'].iloc[i] =='Anti-Mage':
        dire_Anti_Mage.append(1)
    else:
        dire_Anti_Mage.append(0)

    if df['Radiant1'].loc[i] == 'Axe' or df['Radiant2'].iloc[i] == 'Axe' or df['Radiant3'].iloc[i] == 'Axe' or \
            df['Radiant4'].iloc[i] == 'Axe' or df['Radiant5'].iloc[i] == 'Axe':
        radi_Axe.append(1)
    else:
        radi_Axe.append(0)
    if df['Dire1'].loc[i] == 'Axe' or df['Dire2'].iloc[i] == 'Axe' or df['Dire3'].iloc[i] == 'Axe' or df['Dire4'].iloc[
        i] == 'Axe' or df['Dire5'].iloc[i] == 'Axe':
        dire_Axe.append(1)
    else:
        dire_Axe.append(0)

    if df['Radiant1'].loc[i] == 'Bane' or df['Radiant2'].iloc[i] == 'Bane' or df['Radiant3'].iloc[i] == 'Bane' or \
            df['Radiant4'].iloc[i] == 'Bane' or df['Radiant5'].iloc[i] == 'Bane':
        radi_Bane.append(1)
    else:
        radi_Bane.append(0)
    if df['Dire1'].loc[i] == 'Bane' or df['Dire2'].iloc[i] == 'Bane' or df['Dire3'].iloc[i] == 'Bane' or \
            df['Dire4'].iloc[i] == 'Bane' or df['Dire5'].iloc[i] == 'Bane':
        dire_Bane.append(1)
    else:
        dire_Bane.append(0)

    if df['Radiant1'].loc[i] == 'Bloodseeker' or df['Radiant2'].iloc[i] == 'Bloodseeker' or df['Radiant3'].iloc[
        i] == 'Bloodseeker' or df['Radiant4'].iloc[i] == 'Bloodseeker' or df['Radiant5'].iloc[i] == 'Bloodseeker':
        radi_Bloodseeker.append(1)
    else:
        radi_Bloodseeker.append(0)
    if df['Dire1'].loc[i] == 'Bloodseeker' or df['Dire2'].iloc[i] == 'Bloodseeker' or df['Dire3'].iloc[
        i] == 'Bloodseeker' or df['Dire4'].iloc[i] == 'Bloodseeker' or df['Dire5'].iloc[i] == 'Bloodseeker':
        dire_Bloodseeker.append(1)
    else:
        dire_Bloodseeker.append(0)

    if df['Radiant1'].loc[i] == 'Crystal Maiden' or df['Radiant2'].iloc[i] == 'Crystal Maiden' or df['Radiant3'].iloc[
        i] == 'Crystal Maiden' or df['Radiant4'].iloc[i] == 'Crystal Maiden' or df['Radiant5'].iloc[
        i] == 'Crystal Maiden':
        radi_Crystal_Maiden.append(1)
    else:
        radi_Crystal_Maiden.append(0)
    if df['Dire1'].loc[i] == 'Crystal Maiden' or df['Dire2'].iloc[i] == 'Crystal Maiden' or df['Dire3'].iloc[
        i] == 'Crystal Maiden' or df['Dire4'].iloc[i] == 'Crystal Maiden' or df['Dire5'].iloc[i] == 'Crystal Maiden':
        dire_Crystal_Maiden.append(1)
    else:
        dire_Crystal_Maiden.append(0)

    if df['Radiant1'].loc[i] == 'Drow Ranger' or df['Radiant2'].iloc[i] == 'Drow Ranger' or df['Radiant3'].iloc[
        i] == 'Drow Ranger' or df['Radiant4'].iloc[i] == 'Drow Ranger' or df['Radiant5'].iloc[i] == 'Drow Ranger':
        radi_Drow_Ranger.append(1)
    else:
        radi_Drow_Ranger.append(0)
    if df['Dire1'].loc[i] == 'Drow Ranger' or df['Dire2'].iloc[i] == 'Drow Ranger' or df['Dire3'].iloc[
        i] == 'Drow Ranger' or df['Dire4'].iloc[i] == 'Drow Ranger' or df['Dire5'].iloc[i] == 'Drow Ranger':
        dire_Drow_Ranger.append(1)
    else:
        dire_Drow_Ranger.append(0)

    if df['Radiant1'].loc[i] == 'Earthshaker' or df['Radiant2'].iloc[i] == 'Earthshaker' or df['Radiant3'].iloc[
        i] == 'Earthshaker' or df['Radiant4'].iloc[i] == 'Earthshaker' or df['Radiant5'].iloc[i] == 'Earthshaker':
        radi_Earthshaker.append(1)
    else:
        radi_Earthshaker.append(0)
    if df['Dire1'].loc[i] == 'Earthshaker' or df['Dire2'].iloc[i] == 'Earthshaker' or df['Dire3'].iloc[
        i] == 'Earthshaker' or df['Dire4'].iloc[i] == 'Earthshaker' or df['Dire5'].iloc[i] == 'Earthshaker':
        dire_Earthshaker.append(1)
    else:
        dire_Earthshaker.append(0)

    if df['Radiant1'].loc[i] == 'Juggernaut' or df['Radiant2'].iloc[i] == 'Juggernaut' or df['Radiant3'].iloc[
        i] == 'Juggernaut' or df['Radiant4'].iloc[i] == 'Juggernaut' or df['Radiant5'].iloc[i] == 'Juggernaut':
        radi_Juggernaut.append(1)
    else:
        radi_Juggernaut.append(0)
    if df['Dire1'].loc[i] == 'Juggernaut' or df['Dire2'].iloc[i] == 'Juggernaut' or df['Dire3'].iloc[
        i] == 'Juggernaut' or df['Dire4'].iloc[i] == 'Juggernaut' or df['Dire5'].iloc[i] == 'Juggernaut':
        dire_Juggernaut.append(1)
    else:
        dire_Juggernaut.append(0)

    if df['Radiant1'].loc[i] == 'Mirana' or df['Radiant2'].iloc[i] == 'Mirana' or df['Radiant3'].iloc[i] == 'Mirana' or \
            df['Radiant4'].iloc[i] == 'Mirana' or df['Radiant5'].iloc[i] == 'Mirana':
        radi_Mirana.append(1)
    else:
        radi_Mirana.append(0)
    if df['Dire1'].loc[i] == 'Mirana' or df['Dire2'].iloc[i] == 'Mirana' or df['Dire3'].iloc[i] == 'Mirana' or \
            df['Dire4'].iloc[i] == 'Mirana' or df['Dire5'].iloc[i] == 'Mirana':
        dire_Mirana.append(1)
    else:
        dire_Mirana.append(0)

    if df['Radiant1'].loc[i] == 'Morphling' or df['Radiant2'].iloc[i] == 'Morphling' or df['Radiant3'].iloc[
        i] == 'Morphling' or df['Radiant4'].iloc[i] == 'Morphling' or df['Radiant5'].iloc[i] == 'Morphling':
        radi_Morphling.append(1)
    else:
        radi_Morphling.append(0)
    if df['Dire1'].loc[i] == 'Morphling' or df['Dire2'].iloc[i] == 'Morphling' or df['Dire3'].iloc[i] == 'Morphling' or \
            df['Dire4'].iloc[i] == 'Morphling' or df['Dire5'].iloc[i] == 'Morphling':
        dire_Morphling.append(1)
    else:
        dire_Morphling.append(0)

    if df['Radiant1'].loc[i] == 'Shadow Fiend' or df['Radiant2'].iloc[i] == 'Shadow Fiend' or df['Radiant3'].iloc[
        i] == 'Shadow Fiend' or df['Radiant4'].iloc[i] == 'Shadow Fiend' or df['Radiant5'].iloc[i] == 'Shadow Fiend':
        radi_Shadow_Fiend.append(1)
    else:
        radi_Shadow_Fiend.append(0)
    if df['Dire1'].loc[i] == 'Shadow Fiend' or df['Dire2'].iloc[i] == 'Shadow Fiend' or df['Dire3'].iloc[
        i] == 'Shadow Fiend' or df['Dire4'].iloc[i] == 'Shadow Fiend' or df['Dire5'].iloc[i] == 'Shadow Fiend':
        dire_Shadow_Fiend.append(1)
    else:
        dire_Shadow_Fiend.append(0)

    if df['Radiant1'].loc[i] == 'Phantom Lancer' or df['Radiant2'].iloc[i] == 'Phantom Lancer' or df['Radiant3'].iloc[
        i] == 'Phantom Lancer' or df['Radiant4'].iloc[i] == 'Phantom Lancer' or df['Radiant5'].iloc[
        i] == 'Phantom Lancer':
        radi_Phantom_Lancer.append(1)
    else:
        radi_Phantom_Lancer.append(0)
    if df['Dire1'].loc[i] == 'Phantom Lancer' or df['Dire2'].iloc[i] == 'Phantom Lancer' or df['Dire3'].iloc[
        i] == 'Phantom Lancer' or df['Dire4'].iloc[i] == 'Phantom Lancer' or df['Dire5'].iloc[i] == 'Phantom Lancer':
        dire_Phantom_Lancer.append(1)
    else:
        dire_Phantom_Lancer.append(0)

    if df['Radiant1'].loc[i] == 'Puck' or df['Radiant2'].iloc[i] == 'Puck' or df['Radiant3'].iloc[i] == 'Puck' or \
            df['Radiant4'].iloc[i] == 'Puck' or df['Radiant5'].iloc[i] == 'Puck':
        radi_Puck.append(1)
    else:
        radi_Puck.append(0)
    if df['Dire1'].loc[i] == 'Puck' or df['Dire2'].iloc[i] == 'Puck' or df['Dire3'].iloc[i] == 'Puck' or \
            df['Dire4'].iloc[i] == 'Puck' or df['Dire5'].iloc[i] == 'Puck':
        dire_Puck.append(1)
    else:
        dire_Puck.append(0)

    if df['Radiant1'].loc[i] == 'Razor' or df['Radiant2'].iloc[i] == 'Razor' or df['Radiant3'].iloc[i] == 'Razor' or \
            df['Radiant4'].iloc[i] == 'Razor' or df['Radiant5'].iloc[i] == 'Razor':
        radi_Razor.append(1)
    else:
        radi_Razor.append(0)
    if df['Dire1'].loc[i] == 'Razor' or df['Dire2'].iloc[i] == 'Razor' or df['Dire3'].iloc[i] == 'Razor' or \
            df['Dire4'].iloc[i] == 'Razor' or df['Dire5'].iloc[i] == 'Razor':
        dire_Razor.append(1)
    else:
        dire_Razor.append(0)

    if df['Radiant1'].loc[i] == 'Pudge' or df['Radiant2'].iloc[i] == 'Pudge' or df['Radiant3'].iloc[i] == 'Pudge' or \
            df['Radiant4'].iloc[i] == 'Pudge' or df['Radiant5'].iloc[i] == 'Pudge':
        radi_Pudge.append(1)
    else:
        radi_Pudge.append(0)
    if df['Dire1'].loc[i] == 'Pudge' or df['Dire2'].iloc[i] == 'Pudge' or df['Dire3'].iloc[i] == 'Pudge' or \
            df['Dire4'].iloc[i] == 'Pudge' or df['Dire5'].iloc[i] == 'Pudge':
        dire_Pudge.append(1)
    else:
        dire_Pudge.append(0)

    if df['Radiant1'].loc[i] == 'Sand King' or df['Radiant2'].iloc[i] == 'Sand King' or df['Radiant3'].iloc[
        i] == 'Sand King' or df['Radiant4'].iloc[i] == 'Sand King' or df['Radiant5'].iloc[i] == 'Sand King':
        radi_Sand_King.append(1)
    else:
        radi_Sand_King.append(0)
    if df['Dire1'].loc[i] == 'Sand King' or df['Dire2'].iloc[i] == 'Sand King' or df['Dire3'].iloc[i] == 'Sand King' or \
            df['Dire4'].iloc[i] == 'Sand King' or df['Dire5'].iloc[i] == 'Sand King':
        dire_Sand_King.append(1)
    else:
        dire_Sand_King.append(0)

    if df['Radiant1'].loc[i] == 'Storm Spirit' or df['Radiant2'].iloc[i] == 'Storm Spirit' or df['Radiant3'].iloc[
        i] == 'Storm Spirit' or df['Radiant4'].iloc[i] == 'Storm Spirit' or df['Radiant5'].iloc[i] == 'Storm Spirit':
        radi_Storm_Spirit.append(1)
    else:
        radi_Storm_Spirit.append(0)
    if df['Dire1'].loc[i] == 'Storm Spirit' or df['Dire2'].iloc[i] == 'Storm Spirit' or df['Dire3'].iloc[
        i] == 'Storm Spirit' or df['Dire4'].iloc[i] == 'Storm Spirit' or df['Dire5'].iloc[i] == 'Storm Spirit':
        dire_Storm_Spirit.append(1)
    else:
        dire_Storm_Spirit.append(0)

    if df['Radiant1'].loc[i] == 'Sven' or df['Radiant2'].iloc[i] == 'Sven' or df['Radiant3'].iloc[i] == 'Sven' or \
            df['Radiant4'].iloc[i] == 'Sven' or df['Radiant5'].iloc[i] == 'Sven':
        radi_Sven.append(1)
    else:
        radi_Sven.append(0)
    if df['Dire1'].loc[i] == 'Sven' or df['Dire2'].iloc[i] == 'Sven' or df['Dire3'].iloc[i] == 'Sven' or \
            df['Dire4'].iloc[i] == 'Sven' or df['Dire5'].iloc[i] == 'Sven':
        dire_Sven.append(1)
    else:
        dire_Sven.append(0)