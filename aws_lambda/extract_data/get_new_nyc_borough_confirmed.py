from datetime import datetime, date, time, timedelta
import pandas as pd
import pytz
import re

def get_borough_confirmed():
    today = datetime.now(tz=pytz.timezone('EST'))
    today = today.strftime('%m_%d' )

    data = {'Manhattan': [1863], 'Brooklyn': [2484], 'Queens': [2254], 'Bronx': [1071], 'Staten Island':[437]}
    df3_22 = pd.DataFrame.from_dict(data, orient='index')
    df3_22["date"] = "March 22"
    df3_22["date_sort"] = 22
    df3_22.reset_index(inplace=True)
    df3_22 = df3_22.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [2572], 'Brooklyn': [3494], 'Queens': [3621], 'Bronx': [1829], 'Staten Island':[817]}
    df3_23 = pd.DataFrame.from_dict(data, orient='index')
    df3_23["date"] = "March 23"
    df3_23["date_sort"] = 23
    df3_23.reset_index(inplace=True)
    df3_23 = df3_23.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [2887], 'Brooklyn': [4237], 'Queens': [4364], 'Bronx': [2328], 'Staten Island':[953]}
    df3_24 = pd.DataFrame.from_dict(data, orient='index')
    df3_24["date"] = "March 24"
    df3_24["date_sort"] = 24
    df3_24.reset_index(inplace=True)
    df3_24 = df3_24.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [3187], 'Brooklyn': [4656], 'Queens': [5066], 'Bronx': [2789], 'Staten Island':[1084]}
    df3_25 = pd.DataFrame.from_dict(data, orient='index')
    df3_25["date"] = "March 25"
    df3_25["date_sort"] = 25
    df3_25.reset_index(inplace=True)
    df3_25 = df3_25.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [3907], 'Brooklyn': [5705], 'Queens': [7026], 'Bronx': [3924], 'Staten Island':[1276]}
    df3_26 = pd.DataFrame.from_dict(data, orient='index')
    df3_26["date"] = "March 26"
    df3_26["date_sort"] = 26
    df3_26.reset_index(inplace=True)
    df3_26 = df3_26.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [4478], 'Brooklyn': [6750], 'Queens': [8214], 'Bronx': [4655], 'Staten Island':[1440]}
    df3_27 = pd.DataFrame.from_dict(data, orient='index')
    df3_27["date"] = "March 27"
    df3_27["date_sort"] = 27
    df3_27.reset_index(inplace=True)
    df3_27 = df3_27.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [5036], 'Brooklyn': [7789], 'Queens': [9928], 'Bronx': [5352], 'Staten Island':[1718]}
    df3_28 = pd.DataFrame.from_dict(data, orient='index')
    df3_28.reset_index(inplace=True)
    df3_28["date"] = "March 28"
    df3_28["date_sort"] = 28
    df3_28 = df3_28.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [5438], 'Brooklyn': [8451], 'Queens': [10373], 'Bronx': [6145], 'Staten Island':[1866]}
    df3_29 = pd.DataFrame.from_dict(data, orient='index')
    df3_29.reset_index(inplace=True)
    df3_29["date"] = "March 29"
    df3_29["date_sort"] = 29
    df3_29 = df3_29.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [5877], 'Brooklyn': [9521], 'Queens': [11868], 'Bronx': [6830], 'Staten Island':[2091]}
    df3_30 = pd.DataFrame.from_dict(data, orient='index')
    df3_30.reset_index(inplace=True)
    df3_30["date"] = "March 30"
    df3_30["date_sort"] = 30
    df3_30 = df3_30.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [6446], 'Brooklyn': [10904], 'Queens': [13576], 'Bronx': [7625], 'Staten Island':[2314]}
    df3_31 = pd.DataFrame.from_dict(data, orient='index')
    df3_31.reset_index(inplace=True)
    df3_31["date"] = "March 31"
    df3_31["date_sort"] = 31
    df3_31 = df3_31.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [6960], 'Brooklyn': [12076], 'Queens': [14966], 'Bronx': [8398], 'Staten Island':[2480]}
    df4_01 = pd.DataFrame.from_dict(data, orient='index')
    df4_01.reset_index(inplace=True)
    df4_01["date"] = "April 01"
    df4_01["date_sort"] = 32
    df4_01 = df4_01.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [7022], 'Brooklyn': [12274], 'Queens': [15217], 'Bronx': [8607], 'Staten Island':[2552]}
    df4_02 = pd.DataFrame.from_dict(data, orient='index')
    df4_02.reset_index(inplace=True)
    df4_02["date"] = "April 02"
    df4_02["date_sort"] = 32
    df4_02 = df4_02.rename(columns={'index': "boro_name",0:'Confirmed'})

    #data = {'Manhattan': [7713], 'Brooklyn': [14420], 'Queens': [17832], 'Bronx': [9936], 'Staten Island':[3012]}
    data = {'Manhattan': [7398], 'Brooklyn': [13290], 'Queens': [16819], 'Bronx': [9343], 'Staten Island':[2822]}
    df4_03 = pd.DataFrame.from_dict(data, orient='index')
    df4_03.reset_index(inplace=True)
    df4_03["date"] = "April 03"
    df4_03["date_sort"] = 33
    df4_03 = df4_03.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [8222], 'Brooklyn': [15327], 'Queens': [18823], 'Bronx': [10765], 'Staten Island':[3117]}
    df4_04 = pd.DataFrame.from_dict(data, orient='index')
    df4_04.reset_index(inplace=True)
    df4_04["date"] = "April 04"
    df4_04["date_sort"] = 34
    df4_04 = df4_04.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [8781], 'Brooklyn': [16488], 'Queens': [20371], 'Bronx': [11820], 'Staten Island':[3355]}
    df4_05 = pd.DataFrame.from_dict(data, orient='index')
    df4_05.reset_index(inplace=True)
    df4_05["date"] = "April 05"
    df4_05["date_sort"] = 35
    df4_05 = df4_05.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [9251], 'Brooklyn': [17520], 'Queens': [21781], 'Bronx': [12738], 'Staten Island':[3628]}
    df4_06 = pd.DataFrame.from_dict(data, orient='index')
    df4_06.reset_index(inplace=True)
    df4_06["date"] = "April 06"
    df4_06["date_sort"] = 36
    df4_06 = df4_06.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [9691], 'Brooklyn': [18434], 'Queens': [23083], 'Bronx': [13680], 'Staten Island':[3851]}
    df4_07 = pd.DataFrame.from_dict(data, orient='index')
    df4_07.reset_index(inplace=True)
    df4_07["date"] = "April 07"
    df4_07["date_sort"] = 37
    df4_07 = df4_07.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [10254], 'Brooklyn': [20235], 'Queens': [24840], 'Bronx': [14941], 'Staten Island':[4325]}
    df4_08 = pd.DataFrame.from_dict(data, orient='index')
    df4_08.reset_index(inplace=True)
    df4_08["date"] = "April 08"
    df4_08["date_sort"] = 38
    df4_08 = df4_08.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [10862], 'Brooklyn': [21580], 'Queens': [26204], 'Bronx': [16419], 'Staten Island':[5102]}
    df4_09 = pd.DataFrame.from_dict(data, orient='index')
    df4_09.reset_index(inplace=True)
    df4_09["date"] = "April 09"
    df4_09["date_sort"] = 39
    df4_09 = df4_09.rename(columns={'index': "boro_name",0:'Confirmed'})

    data = {'Manhattan': [11486], 'Brooklyn': [23408], 'Queens': [27759], 'Bronx': [18736], 'Staten Island':[6298]}
    df4_10 = pd.DataFrame.from_dict(data, orient='index')
    df4_10.reset_index(inplace=True)
    df4_10["date"] = "April 10"
    df4_10["date_sort"] = 40
    df4_10 = df4_10.rename(columns={'index': "boro_name",0:'Confirmed'})

    dt = pd.concat([df3_22, df3_23, df3_24, df3_25, df3_26, df3_27, df3_28, df3_29, df3_30, df3_31, df4_01, df4_02, df4_03, df4_04, df4_05, df4_06, df4_07, df4_08, df4_09, df4_10], sort=False)
    dt = dt.reset_index()
    dt = dt.rename(columns={"index": "borough"})

    dt = pd.pivot_table(dt, values='Confirmed',index=['date'], columns='boro_name')
    dt = dt.reset_index()
    dt['total']  = dt['Bronx'] + dt['Brooklyn'] + dt['Manhattan'] + dt['Queens'] + dt['Staten Island']
    dt = dt.sort_values(by='Manhattan', ascending= True)
    dt = dt.rename(columns={"Bronx": "The Bronx"})

    df = dt.T
    df = df.reset_index()
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.rename(columns={'date': 'BOROUGH_GROUP'})

    df4_11 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/3fdd59a195bff5c4473a2086093ed656702d6569/boro.csv')
    df4_11 = df4_11[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_11.rename(columns={'COVID_CASE_COUNT':'April 11'}, inplace=True)

    df4_12 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/8542fbf18049d804eb8de7594123c13e533d1a42/boro.csv')
    df4_12 = df4_12[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_12.rename(columns={'COVID_CASE_COUNT':'April 12'}, inplace=True)

    df4_13 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/d34e6aab1e0dd0e0125e74519489e7893d33c9dd/boro.csv')
    df4_13 = df4_13[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_13.rename(columns={'COVID_CASE_COUNT':'April 13'}, inplace=True)

    df4_14 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/8e4627dd2f00d1de53355b01c8a9476d1c381b70/boro.csv')
    df4_14 = df4_14[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_14.rename(columns={'COVID_CASE_COUNT':'April 14'}, inplace=True)

    df4_15 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/165e694647d8319d7dc5cec6abc7d70cfc03c1ec/boro.csv')
    df4_15 = df4_15[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_15.rename(columns={'COVID_CASE_COUNT':'April 15'}, inplace=True)

    df4_16 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/86e9f032ba7fe1a6c61591cfc2413f23b7aa387b/boro.csv')
    df4_16 = df4_16[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_16.rename(columns={'COVID_CASE_COUNT':'April 16'}, inplace=True)

    df4_17 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/21916256325a11aae77bbe69029085f43592f2d1/boro.csv')
    df4_17 = df4_17[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_17.rename(columns={'COVID_CASE_COUNT':'April 17'}, inplace=True)

    df4_18 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/d3a8994716870cfdbd6cc2fb356c31588446fc25/boro.csv')
    df4_18 = df4_18[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_18.rename(columns={'COVID_CASE_COUNT':'April 18'}, inplace=True)

    df4_19 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/498c34f8534bc865b15dd09e9b560bd457ef5b9b/boro.csv')
    df4_19 = df4_19[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_19.rename(columns={'COVID_CASE_COUNT':'April 19'}, inplace=True)

    df4_20 = pd.read_csv('https://raw.githubusercontent.com/nychealth/coronavirus-data/0a74f0850087758da3579886ae8b7365e182ed9e/boro.csv')
    df4_20 = df4_20[['BOROUGH_GROUP', 'COVID_CASE_COUNT']]
    df4_20.rename(columns={'COVID_CASE_COUNT':'April 20'}, inplace=True)


    da = df.merge(df4_11, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_12, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_13, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_14, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_15, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_16, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_17, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_18, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_19, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    da = da.merge(df4_20, right_on='BOROUGH_GROUP', left_on='BOROUGH_GROUP')
    return da
