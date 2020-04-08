import pandas as pd
import numpy as np 

def wrangle_historical_county_df():
    """ This function is only here just in case there needs to be 
    manual adjustment of historical data prior to April 07. 
    Returns df_confirmed_historical_T """

    data = {'Albany': [0],'Allegany':[0],'Bronx': [1],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [1],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [0],'New York': [1],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [1],'Rensselaer':[0],'Richmond':[1],'Rockland': [0],'Saratoga': [0],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [0],'Wyoming': [0],'Yates':[0]}
    df1 = pd.DataFrame.from_dict(data, orient='index')
    df1 = df1.rename(columns={0: "March 1"})
    df1["date"] = "March 1"
    df1["date_sort"] = 1
    df1 = df1.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [1],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [1],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [0],'New York': [1],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [1],'Rensselaer':[0],'Richmond':[1],'Rockland': [0],'Saratoga': [0],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [0],'Wyoming': [0],'Yates':[0]}
    df2 = pd.DataFrame.from_dict(data, orient='index')
    df2 = df2.rename(columns={0: "March 2"})
    df2["date"] = "March 2"
    df2["date_sort"] = 2
    df2 = df2.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [1],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [1],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [0],'New York': [1],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [1],'Rensselaer':[0],'Richmond':[1],'Rockland': [0],'Saratoga': [0],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [1],'Wyoming': [0],'Yates':[0]}
    df3 = pd.DataFrame.from_dict(data, orient='index')
    df3 = df3.rename(columns={0: "March 3"})
    df3["date"] = "March 3"
    df3["date_sort"] = 3
    df3 = df3.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [1],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [1],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [0],'New York': [1],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [1],'Rensselaer':[0],'Richmond':[1],'Rockland': [0],'Saratoga': [0],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [10],'Wyoming': [0],'Yates':[0]}
    df4 = pd.DataFrame.from_dict(data, orient='index')
    df4 = df4.rename(columns={0: "March 4"})
    df4["date"] = "March 4"
    df4["date_sort"] = 4
    df4 = df4.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [3],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [3],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [1],'New York': [3],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [3],'Rensselaer':[0],'Richmond':[3],'Rockland': [0],'Saratoga': [0],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [18],'Wyoming': [0],'Yates':[0]}
    df5 = pd.DataFrame.from_dict(data, orient='index')
    df5 = df5.rename(columns={0: "March 5"})
    df5["date"] = "March 5"
    df5["date_sort"] = 5
    df5 = df5.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [4],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [4],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [4],'New York': [4],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [4],'Rensselaer':[0],'Richmond':[4],'Rockland': [2],'Saratoga': [0],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [34],'Wyoming': [0],'Yates':[0]}
    df6 = pd.DataFrame.from_dict(data, orient='index')
    df6 = df6.rename(columns={0: "March 6"})
    df6["date"] = "March 6"
    df6["date_sort"] = 6
    df6 = df6.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [11],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [11],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [4],'New York': [11],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [11],'Rensselaer':[0],'Richmond':[11],'Rockland': [2],'Saratoga': [2],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [0],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [0],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [70],'Wyoming': [0],'Yates':[0]}
    df7 = pd.DataFrame.from_dict(data, orient='index')
    df7 = df7.rename(columns={0: "March 7"})
    df7["date"] = "March 7"
    df7["date_sort"] = 7
    df7 = df7.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [12],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [12],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [5],'New York': [12],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [12],'Rensselaer':[0],'Richmond':[12],'Rockland': [2],'Saratoga': [2],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [1],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [1],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [82],'Wyoming': [0],'Yates':[0]}
    df8 = pd.DataFrame.from_dict(data, orient='index')
    df8 = df8.rename(columns={0: "March 8"})
    df8["date"] = "March 8"
    df8["date_sort"] = 8
    df8 = df8.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [19],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [19],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [17],'New York': [19],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [19],'Rensselaer':[0],'Richmond':[19],'Rockland': [4],'Saratoga': [2],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [1],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [1],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [98],'Wyoming': [0],'Yates':[0]}
    df9 = pd.DataFrame.from_dict(data, orient='index')
    df9 = df9.rename(columns={0: "March 9"})
    df9["date"] = "March 9"
    df9["date_sort"] = 9
    df9 = df9.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [36],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [36],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [19],'New York': [36],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [36],'Rensselaer':[0],'Richmond':[36],'Rockland': [6],'Saratoga': [2],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [1],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [1],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [108],'Wyoming': [0],'Yates':[0]}
    df10 = pd.DataFrame.from_dict(data, orient='index')
    df10 = df10.rename(columns={0: "March 10"})
    df10["date"] = "March 10"
    df10["date_sort"] = 10
    df10 = df10.reset_index()

    data = {'Albany': [0],'Allegany':[0],'Bronx': [52],'Broome': [0],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [0],'Dutchess': [0],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [0],'Jefferson':[0],'Kings': [52],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [0],'Montgomery': [0],'Nassau': [28],'New York': [52],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [0],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [52],'Rensselaer':[0],'Richmond':[52],'Rockland': [6],'Saratoga': [2],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [6],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [1],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [121],'Wyoming': [0],'Yates':[0]}
    df11 = pd.DataFrame.from_dict(data, orient='index')
    df11 = df11.rename(columns={0: "March 11"})
    df11["date"] = "March 11"
    df11["date_sort"] = 11
    df11 = df11.reset_index()

    data = {'Albany': [0],'Albany': [1],'Allegany':[0],'Bronx': [95],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [1],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [1],'Jefferson':[0],'Kings': [95],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [1],'Montgomery': [0],'Nassau': [41],'New York': [95],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [1],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [95],'Rensselaer':[0],'Richmond':[95],'Rockland': [7],'Saratoga': [3],'Schenectady': [0],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [20],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [4],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [148],'Wyoming': [0],'Yates':[0]}
    df12 = pd.DataFrame.from_dict(data, orient='index')
    df12 = df12.rename(columns={0: "March 12"})
    df12["date"] = "March 12"
    df12["date_sort"] = 12
    df12 = df12.reset_index()

    data = {'Albany': [0],'Albany': [2],'Allegany':[0],'Bronx': [154],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [1],'Erie': [0],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [1],'Jefferson':[0],'Kings': [154],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [1],'Montgomery': [0],'Nassau': [51],'New York': [154],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [3],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [154],'Rensselaer':[0],'Richmond':[154],'Rockland': [9],'Saratoga': [3],'Schenectady': [1],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [28],'Sullivan': [0],'Tioga': [0],'Tompkins': [0],'Ulster': [5],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [158],'Wyoming': [0],'Yates':[0]}
    df13 = pd.DataFrame.from_dict(data, orient='index')
    df13 = df13.rename(columns={0: "March 13"})
    df13["date"] = "March 13"
    df13["date_sort"] = 13
    df13 = df13.reset_index()

    data = {'Albany': [5],'Allegany':[0],'Bronx': [269],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [4],'Erie': [3],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [0],'Hamilton': [0],'Herkimer': [1],'Jefferson':[0],'Kings': [269],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [2],'Montgomery': [0],'Nassau': [79],'New York': [269],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [6],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [0],'Queens': [269],'Rensselaer':[0],'Richmond':[269],'Rockland': [12],'Saratoga': [3],'Schenectady': [0],'Schenectady': [1],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [41],'Sullivan': [0],'Tioga': [1],'Tompkins': [1],'Ulster': [5],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [178],'Wyoming': [0],'Yates':[0]}
    df14 = pd.DataFrame.from_dict(data, orient='index')
    df14 = df14.rename(columns={0: "March 14"})
    df14["date"] = "March 14"
    df14["date_sort"] = 14
    df14 = df14.reset_index()

    data = {'Albany': [8],'Allegany':[0],'Bronx':[329],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [7],'Erie': [3],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [2],'Hamilton': [0],'Herkimer': [1],'Jefferson':[0],'Kings':[329],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [2],'Montgomery': [1],'Nassau': [98],'New York': [329],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [6],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [2],'Queens':[329],'Rensselaer':[0],'Richmond':[329],'Rockland': [13],'Saratoga': [3],'Schenectady': [2],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [47],'Sullivan': [0],'Tioga': [1],'Tompkins': [1],'Ulster': [5],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [196],'Wyoming': [0],'Yates':[0]}
    df15 = pd.DataFrame.from_dict(data, orient='index')
    df15 = df15.rename(columns={0: "March 15"})
    df15["date"] = "March 15"
    df15["date_sort"] = 15
    df15 = df15.reset_index()

    data = {'Albany': [8],'Allegany':[0],'Bronx':[329],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [7],'Erie': [3],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [2],'Hamilton': [0],'Herkimer': [1],'Jefferson':[0],'Kings':[329],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [2],'Montgomery': [1],'Nassau': [98],'New York': [329],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [6],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [2],'Queens':[329],'Rensselaer':[0],'Richmond':[329],'Rockland': [13],'Saratoga': [3],'Schenectady': [2],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [74],'Sullivan': [0],'Tioga': [1],'Tompkins': [1],'Ulster': [5],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [196],'Wyoming': [0],'Yates':[0]}
    df16 = pd.DataFrame.from_dict(data, orient='index')
    df16 = df16.rename(columns={0: "March 16"})
    df16["date"] = "March 16"
    df16["date_sort"] = 16
    df16 = df16.reset_index()

    data = {'Albany': [23],'Allegany':[0],'Bronx': [644],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [0],'Clinton': [0],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [16],'Erie': [7],'Essex': [0],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [2],'Hamilton': [0],'Herkimer': [1],'Jefferson':[0],'Kings': [644],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [10],'Montgomery': [1],'Nassau': [131],'New York': [644],'Niagara': [0],'Oneida':[0],'Onondaga': [0],'Ontario':[0],'Orange': [15],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [2],'Queens': [644],'Rensselaer':[0],'Richmond':[644],'Rockland': [22],'Saratoga': [9],'Schenectady': [5],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [84],'Sullivan': [0],'Tioga': [1],'Tompkins': [2],'Ulster': [8],'Warren': [0],'Washington': [0],'Wayne':[0],'Westchester': [380],'Wyoming': [0],'Yates':[0]}
    df17 = pd.DataFrame.from_dict(data, orient='index')
    df17 = df17.rename(columns={0: "March 17"})
    df17["date"] = "March 17"
    df17["date_sort"] = 17
    df17 = df17.reset_index()

    data = {'Albany': [36],'Allegany':[2],'Bronx': [1339],'Broome': [1],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [1],'Clinton': [1],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [20],'Erie': [7],'Essex': [1],'Franklin':[0],'Fulton':[0],'Genesee':[0],'Greene': [2],'Hamilton': [1],'Herkimer': [1],'Jefferson':[0],'Kings': [1339],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [14],'Montgomery': [2],'Nassau': [183],'New York': [1339],'Niagara': [0],'Oneida':[0],'Onondaga': [2],'Ontario':[0],'Orange': [32],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [2],'Queens': [1339],'Rensselaer':[4],'Richmond':[1339],'Rockland': [30],'Saratoga': [14],'Schenectady': [14],'Schoharie':[0],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [116],'Sullivan': [0],'Sullivan': [1],'Tioga': [1],'Tompkins': [3],'Ulster': [9],'Warren': [1],'Washington': [0],'Washington': [1],'Wayne':[0],'Westchester': [538],'Wyoming': [1],'Yates':[0]}
    df18 = pd.DataFrame.from_dict(data, orient='index')
    df18 = df18.rename(columns={0: "March 18"})
    df18["date"] = "March 18"
    df18["date_sort"] = 18
    df18 = df18.reset_index()

    data = {'Albany': [43],'Allegany':[2],'Bronx': [2469],'Broome': [2],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [2],'Clinton': [2],'Columbia':[0],'Cortland':[0],'Delaware': [1],'Dutchess': [31],'Erie': [28],'Essex': [1],'Franklin':[0],'Fulton':[1],'Genesee':[1],'Greene': [2],'Hamilton': [2],'Herkimer': [1],'Jefferson':[0],'Kings': [2469],'Lewis':[0],'Livingston':[0],'Madison':[0],'Monroe': [27],'Montgomery': [2],'Nassau': [372],'New York': [2469],'Niagara': [1],'Oneida':[1],'Onondaga': [5],'Ontario':[1],'Orange': [51],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [5],'Queens': [2469],'Rensselaer':[6],'Richmond':[2469],'Rockland': [53],'Saratoga': [18],'Schenectady': [18],'Schoharie':[1],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [178],'Sullivan': [3],'Tioga': [1],'Tompkins': [6],'Ulster': [10],'Warren': [1],'Washington': [1],'Wayne':[1],'Westchester': [798],'Wyoming': [1],'Yates':[0]}
    df19 = pd.DataFrame.from_dict(data, orient='index')
    df19 = df19.rename(columns={0: "March 19"})
    df19["date"] = "March 19"
    df19["date_sort"] = 19
    df19 = df19.reset_index()

    data = {'Albany': [61],'Allegany':[2],'Bronx': [4408],'Broome': [2],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [2],'Clinton': [2],'Columbia':[1],'Cortland':[0],'Delaware': [1],'Dutchess': [36],'Erie': [31],'Essex': [1],'Franklin':[0],'Fulton':[0],'Fulton':[1],'Genesee':[1],'Greene': [2],'Hamilton': [2],'Herkimer': [2],'Jefferson':[1],'Kings': [4408],'Lewis':[0],'Livingston':[1],'Madison':[0],'Monroe': [32],'Montgomery': [2],'Nassau': [754],'New York': [4408],'Niagara': [3],'Oneida':[2],'Onondaga': [8],'Ontario':[3],'Orange': [84],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [7],'Queens': [4408],'Rensselaer':[20],'Richmond':[4408],'Rockland': [101],'Saratoga': [24],'Schenectady': [21],'Schoharie':[1],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[0],'Suffolk': [371],'Sullivan': [8],'Tioga': [1],'Tompkins': [7],'Ulster': [12],'Warren': [1],'Washington': [1],'Wayne':[1],'Westchester': [1091],'Wyoming': [2],'Yates':[0]}
    df20 = pd.DataFrame.from_dict(data, orient='index')
    df20 = df20.rename(columns={0: "March 20"})
    df20["date"] = "March 20"
    df20["date_sort"] = 20
    df20 = df20.reset_index()

    data = {'Albany': [88],'Allegany':[2],'Bronx': [6211],'Broome': [2],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [2],'Clinton': [4],'Columbia':[2],'Cortland':[0],'Delaware': [1],'Dutchess': [49],'Erie': [38],'Essex': [2],'Franklin':[0],'Fulton':[0],'Fulton':[1],'Genesee':[1],'Greene': [2],'Hamilton': [2],'Herkimer': [3],'Jefferson':[1],'Kings': [6211],'Lewis':[0],'Livingston':[2],'Madison':[0],'Monroe': [42],'Montgomery': [3],'Nassau': [1234],'New York': [6211],'Niagara': [4],'Oneida':[4],'Onondaga': [17],'Ontario':[4],'Orange': [163],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [22],'Queens': [6211],'Rensselaer':[20],'Richmond':[6211],'Rockland': [262],'Saratoga': [35],'Schenectady': [32],'Schoharie':[1],'Schuyler':[0],'Seneca':[0],'St Lawrence':[0],'Steuben':[2],'Suffolk': [662],'Sullivan': [12],'Tioga': [1],'Tompkins': [11],'Ulster': [18],'Warren': [1],'Washington': [1],'Wayne':[3],'Westchester': [1387],'Wyoming': [2],'Yates':[0]}
    df21 = pd.DataFrame.from_dict(data, orient='index')
    df21 = df21.rename(columns={0: "March 21"})
    df21["date"] = "March 21"
    df21["date_sort"] = 21
    df21 = df21.reset_index()

    data = {'Albany': [123],'Allegany':[2],'Bronx': [9045],'Broome': [3],'Cattaraugus':[0],'Cayuga':[0],'Chautauqua':[0],'Chemung':[0],'Chenango': [3],'Clinton': [4],'Columbia':[5],'Cortland':[1],'Delaware': [3],'Dutchess': [82],'Erie': [54],'Essex': [3],'Franklin':[0],'Fulton':[0],'Fulton':[1],'Genesee':[1],'Greene': [2],'Hamilton': [2],'Herkimer': [4],'Jefferson':[1],'Kings': [9045],'Lewis':[0],'Livingston':[2],'Madison':[0],'Monroe': [57],'Montgomery': [3],'Nassau': [1900],'New York': [9045],'Niagara': [6],'Oneida':[5],'Onondaga': [29],'Ontario':[6],'Orange': [247],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [37],'Queens': [9045],'Rensselaer':[26],'Richmond':[9045],'Rockland': [455],'Saratoga': [41],'Schenectady': [39],'Schoharie':[1],'Schuyler':[0],'Seneca':[0],'St Lawrence':[1],'Steuben':[3],'Suffolk': [1034],'Sullivan': [16],'Tioga': [1],'Tompkins': [13],'Ulster': [26],'Warren': [1],'Washington': [1],'Wayne':[3],'Westchester': [1873],'Wyoming': [2],'Yates':[0]}
    df22 = pd.DataFrame.from_dict(data, orient='index')
    df22 = df22.rename(columns={0: "March 22"})
    df22["date"] = "March 22"
    df22["date_sort"] = 22
    df22 = df22.reset_index()

    data = {'Albany': [127],'Allegany':[2],'Bronx': [12305],'Broome': [7],'Cattaraugus':[0],'Cayuga':[2],'Chautauqua':[0],'Chemung':[0],'Chenango': [3],'Clinton': [6],'Columbia':[10],'Cortland':[2],'Delaware': [3],'Dutchess': [100],'Erie': [87],'Essex': [3],'Franklin':[0],'Fulton':[1],'Genesee':[1],'Greene': [4],'Hamilton': [2],'Herkimer': [4],'Jefferson':[2],'Kings': [12305],'Lewis':[0],'Livingston':[3],'Madison':[4],'Monroe': [76],'Montgomery': [3],'Nassau': [2442],'New York': [12305],'Niagara': [10],'Oneida':[7],'Onondaga': [52],'Ontario':[6],'Orange': [389],'Orleans':[0],'Oswego':[0],'Otsego':[0],'Putnam': [45],'Queens': [12305],'Rensselaer':[29],'Richmond':[12305],'Rockland': [592],'Saratoga': [53],'Schenectady': [44],'Schoharie':[1],'Schuyler':[0],'Seneca':[0],'St Lawrence':[1],'Steuben':[4],'Suffolk': [1458],'Sullivan': [23],'Tioga': [1],'Tompkins': [15],'Ulster': [35],'Warren': [2],'Washington': [3],'Wayne':[6],'Westchester': [2894],'Wyoming': [4],'Yates':[0]}
    df23 = pd.DataFrame.from_dict(data, orient='index')
    df23 = df23.rename(columns={0: "March 23"})
    df23["date"] = "March 23"
    df23["date_sort"] = 23
    df23 = df23.reset_index()

    data = {'Albany': [146],'Allegany':[2],'Bronx': [14904],'Broome': [7],'Cattaraugus':[0],'Cayuga':[2],'Chautauqua':[0],'Chemung':[0],'Chenango': [3],'Clinton': [6],'Columbia':[10],'Cortland':[2],'Delaware': [3],'Dutchess': [124],'Erie': [107],'Essex': [3],'Franklin':[0],'Fulton':[1],'Genesee':[1],'Greene': [4],'Hamilton': [2],'Herkimer': [4],'Jefferson':[2],'Kings': [14904],'Lewis':[0],'Livingston':[3],'Madison':[4],'Monroe': [96],'Montgomery': [3],'Nassau': [2869],'New York': [14904],'Niagara': [10],'Oneida':[7],'Onondaga': [52],'Ontario':[6],'Orange': [489],'Orleans':[0],'Oswego':[1],'Otsego':[1],'Putnam': [45],'Queens': [14904],'Rensselaer':[29],'Richmond':[14904],'Rockland': [671],'Saratoga': [53],'Schenectady': [44],'Schoharie':[1],'Schuyler':[0],'Seneca':[0],'St Lawrence':[1],'Steuben':[4],'Suffolk': [1880],'Sullivan': [23],'Tioga': [1],'Tompkins': [15],'Ulster': [35],'Warren': [2],'Washington': [3],'Wayne':[6],'Westchester': [3891],'Wyoming': [4],'Yates':[0]}
    df24 = pd.DataFrame.from_dict(data, orient='index')
    df24 = df24.rename(columns={0: "March 24"})
    df24["date"] = "March 24"
    df24["date_sort"] = 24
    df24 = df24.reset_index()

    data = {'Albany': [152],'Allegany':[2],'Bronx': [20011],'Broome': [11],'Cattaraugus':[0],'Cayuga':[2],'Chautauqua':[1],'Chemung':[1],'Chenango': [3],'Clinton': [10],'Columbia':[12],'Cortland':[2],'Delaware': [5],'Dutchess': [153],'Erie': [122],'Essex': [4],'Franklin':[0],'Fulton':[1],'Genesee':[2],'Greene': [4],'Hamilton': [2],'Herkimer': [5],'Jefferson':[2],'Kings': [20011],'Lewis':[0],'Livingston':[3],'Madison':[7],'Monroe': [118],'Montgomery': [4],'Nassau': [3285],'New York': [20011],'Niagara': [12],'Oneida':[9],'Onondaga': [65],'Ontario':[9],'Orange': [638],'Orleans':[2],'Oswego':[2],'Otsego':[2],'Putnam': [84],'Queens': [20011],'Rensselaer':[31],'Richmond':[20011],'Rockland': [968],'Saratoga': [64],'Schenectady': [55],'Schoharie':[2],'Schuyler':[0],'Seneca':[0],'St Lawrence':[1],'Steuben':[8],'Suffolk': [2260],'Sullivan': [39],'Tioga': [1],'Tompkins': [16],'Ulster': [65],'Warren': [2],'Washington': [4],'Wayne':[7],'Westchester': [4691],'Wyoming': [4],'Yates':[0]}
    df25 = pd.DataFrame.from_dict(data, orient='index')
    df25 = df25.rename(columns={0: "March 25"})
    df25["date"] = "March 25"
    df25["date_sort"] = 25
    df25 = df25.reset_index()

    data = {'Albany': [171],'Allegany':[2],'Bronx': [21873],'Broome': [16],'Cattaraugus':[0],'Cayuga':[2],'Chautauqua':[1],'Chemung':[7],'Chenango': [3],'Clinton': [11],'Columbia':[13],'Cortland':[2],'Delaware': [7],'Dutchess': [190],'Erie': [134],'Essex': [4],'Franklin':[1],'Fulton':[1],'Genesee':[4],'Greene': [5],'Hamilton': [2],'Herkimer': [7],'Jefferson':[3],'Kings': [21873],'Lewis':[0],'Livingston':[3],'Madison':[9],'Monroe': [139],'Montgomery': [5],'Nassau': [3914],'New York': [21873],'Niagara': [14],'Oneida':[13],'Onondaga': [83],'Ontario':[11],'Orange': [751],'Orleans':[2],'Oswego':[4],'Otsego':[2],'Putnam': [94],'Queens': [21873],'Rensselaer':[32],'Richmond':[21873],'Rockland': [1197],'Saratoga': [73],'Schenectady': [62],'Schoharie':[2],'Schuyler':[0],'Seneca':[0],'St Lawrence':[2],'Steuben':[11],'Suffolk': [2735],'Sullivan': [53],'Tioga': [2],'Tompkins': [22],'Ulster': [78],'Warren': [2],'Washington': [4],'Wayne':[8],'Westchester': [5944],'Wyoming': [7],'Yates':[0]}
    df26 = pd.DataFrame.from_dict(data, orient='index')
    df26 = df26.rename(columns={0: "March 26"})
    df26["date"] = "March 26"
    df26["date_sort"] = 26
    df26 = df26.reset_index()

    data = {'Albany': [187],'Allegany':[2],'Bronx': [25573],'Broome': [18],'Cattaraugus':[0],'Cayuga':[2],'Chautauqua':[1],'Chemung':[11],'Chenango': [4],'Clinton': [11],'Columbia':[20],'Cortland':[4],'Delaware': [8],'Dutchess': [225],'Erie': [219],'Essex': [4],'Franklin':[2],'Fulton':[1],'Genesee':[6],'Greene': [6],'Hamilton': [2],'Herkimer': [9],'Jefferson':[3],'Kings': [25573],'Lewis':[0],'Livingston':[3],'Madison':[17],'Monroe': [160],'Montgomery': [5],'Nassau': [4657],'New York': [25573],'Niagara': [23],'Oneida':[13],'Onondaga': [115],'Ontario':[14],'Orange': [910],'Orleans':[3],'Oswego':[4],'Otsego':[5],'Putnam': [111],'Queens': [25573],'Rensselaer':[35],'Richmond':[25573],'Rockland': [1457],'Saratoga': [82],'Schenectady': [66],'Schoharie':[3],'Schuyler':[0],'Seneca':[0],'St Lawrence':[3],'Steuben':[12],'Suffolk': [3385],'Sullivan': [64],'Tioga': [2],'Tompkins': [26],'Ulster': [98],'Warren': [8],'Washington': [6],'Wayne':[11],'Westchester': [7187],'Wyoming': [7],'Yates':[0]}
    df27 = pd.DataFrame.from_dict(data, orient='index')
    df27 = df27.rename(columns={0: "March 27"})
    df27["date"] = "March 27"
    df27["date_sort"] = 27
    df27 = df27.reset_index()

    data = {'Albany': [195],'Allegany':[2],'Bronx': [29766],'Broome': [23],'Cattaraugus':[1],'Cayuga':[2],'Chautauqua':[5],'Chemung':[12],'Chenango': [8],'Clinton': [12],'Columbia':[22],'Cortland':[5],'Delaware': [8],'Dutchess': [262],'Erie': [318],'Essex': [4],'Franklin':[4],'Fulton':[1],'Genesee':[7],'Greene': [7],'Hamilton': [2],'Herkimer': [9],'Jefferson':[6],'Kings': [29766],'Lewis':[0],'Livingston':[5],'Madison':[19],'Monroe': [192],'Montgomery': [5],'Nassau': [5537],'New York': [29766],'Niagara': [33],'Oneida':[23],'Onondaga': [129],'Ontario':[16],'Orange': [1101],'Orleans':[3],'Oswego':[7],'Otsego':[7],'Putnam': [131],'Queens': [29766],'Rensselaer':[38],'Richmond':[29766],'Rockland': [1896],'Saratoga': [96],'Schenectady': [72],'Schoharie':[5],'Schuyler':[1],'Seneca':[0],'St Lawrence':[8],'Steuben':[13],'Suffolk': [4138],'Sullivan': [72],'Tioga': [4],'Tompkins': [45],'Ulster': [128],'Warren': [13],'Washington': [6],'Wayne':[12],'Westchester': [7875],'Wyoming': [7],'Yates':[0]}
    df28 = pd.DataFrame.from_dict(data, orient='index')
    df28 = df28.rename(columns={0: "March 28"})
    df28["date"] = "March 28"
    df28["date_sort"] = 28
    df28 = df28.reset_index()

    data = {'Albany': [205],'Allegany':[6],'Bronx': [33768],'Broome': [29],'Cattaraugus':[4],'Cayuga':[2],'Chautauqua':[5],'Chemung':[15],'Chenango': [15],'Clinton': [13],'Columbia':[23],'Cortland':[6],'Delaware': [8],'Dutchess': [320],'Erie': [358],'Essex': [4],'Franklin':[6],'Fulton':[1],'Genesee':[9],'Greene': [7],'Hamilton': [2],'Herkimer': [10],'Jefferson':[7],'Kings': [33768],'Lewis':[2],'Livingston':[10],'Madison':[24],'Monroe': [219],'Montgomery': [6],'Nassau': [6445],'New York': [33768],'Niagara': [38],'Oneida':[26],'Onondaga': [152],'Ontario':[18],'Orange': [1247],'Orleans':[3],'Oswego':[8],'Otsego':[10],'Putnam': [144],'Queens': [33768],'Rensselaer':[39],'Richmond':[33768],'Rockland': [2209],'Saratoga': [102],'Schenectady': [76],'Schoharie':[5],'Schuyler':[1],'Seneca':[0],'St Lawrence':[12],'Steuben':[17],'Suffolk': [5023],'Sullivan': [88],'Tioga': [4],'Tompkins': [52],'Ulster': [146],'Warren': [18],'Washington': [7],'Wayne':[12],'Westchester': [8519],'Wyoming': [8],'Yates':[0]}
    df29 = pd.DataFrame.from_dict(data, orient='index')
    df29 = df29.rename(columns={0: "March 29"})
    df29["date"] = "March 29"
    df29["date_sort"] = 29
    df29 = df29.reset_index()

    data = {'Albany': [217],'Allegany':[7],'Bronx': [37453],'Broome': [35],'Cattaraugus':[6],'Cayuga':[3],'Chautauqua':[5],'Chemung':[15],'Chenango': [17],'Clinton': [17],'Columbia':[26],'Cortland':[8],'Delaware': [11],'Dutchess': [392],'Erie': [376],'Essex': [4],'Franklin':[6],'Fulton':[1],'Genesee':[9],'Greene': [10],'Hamilton': [2],'Herkimer': [12],'Jefferson':[11],'Kings': [37453],'Lewis':[2],'Livingston':[12],'Madison':[34],'Monroe': [242],'Montgomery': [6],'Nassau': [7344],'New York': [37453],'Niagara': [41],'Oneida':[34],'Onondaga': [180],'Ontario':[20],'Orange': [1435],'Orleans':[4],'Oswego':[14],'Otsego':[17],'Putnam': [167],'Queens': [37453],'Rensselaer':[40],'Richmond':[37453],'Rockland': [2511],'Saratoga': [105],'Schenectady': [80],'Schoharie':[6],'Schuyler':[2],'Seneca':[0],'St Lawrence':[13],'Steuben':[19],'Suffolk': [5791],'Sullivan': [101],'Tioga': [4],'Tompkins': [66],'Ulster': [190],'Warren': [18],'Washington': [7],'Wayne':[15],'Westchester': [9326],'Wyoming': [8],'Yates':[0]}
    df30 = pd.DataFrame.from_dict(data, orient='index')
    df30 = df30.rename(columns={0: "March 30"})
    df30["date"] = "March 30"
    df30["date_sort"] = 30
    df30 = df30.reset_index()

    data = {'Albany': [226],'Allegany':[7],'Bronx': [43139],'Broome': [38],'Cattaraugus':[6],'Cayuga':[3],'Chautauqua':[6],'Chemung':[20],'Chenango': [19],'Clinton': [21],'Columbia':[30],'Cortland':[8],'Delaware': [16],'Dutchess': [484],'Erie': [438],'Essex': [4],'Franklin':[9],'Fulton':[1],'Genesee':[10],'Greene': [16],'Hamilton': [2],'Herkimer': [12],'Jefferson':[12],'Kings': [43139],'Lewis':[2],'Livingston':[13],'Madison':[41],'Monroe': [292],'Montgomery': [7],'Nassau': [8544],'New York': [43139],'Niagara': [42],'Oneida':[40],'Onondaga': [194],'Ontario':[22],'Orange': [1556],'Orleans':[6],'Oswego':[15],'Otsego':[18],'Putnam': [186],'Queens': [43139],'Rensselaer':[41],'Richmond':[43139],'Rockland': [2863],'Saratoga': [108],'Schenectady': [85],'Schoharie':[6],'Schuyler':[2],'Seneca':[0],'Seneca':[2],'St Lawrence':[30],'Steuben':[24],'Suffolk': [6713],'Sullivan': [109],'Tioga': [7],'Tompkins': [66],'Ulster': [211],'Warren': [18],'Washington': [10],'Wayne':[19],'Westchester': [9967],'Wyoming': [9],'Yates':[0]}
    df31 = pd.DataFrame.from_dict(data, orient='index')
    df31 = df31.rename(columns={0: "March 31"})
    df31["date"] = "March 31"
    df31["date_sort"] = 31
    df31 = df31.reset_index()

    data = {'Albany': [240],'Allegany':[9],'Bronx': [47439],'Broome': [42],'Cattaraugus':[7],'Cayuga':[3],'Chautauqua':[6],'Chemung':[22],'Chenango': [26],'Clinton': [25],'Columbia':[31],'Cortland':[8],'Delaware': [20],'Dutchess': [547],'Erie': [464],'Essex': [6],'Franklin':[9],'Fulton':[2],'Genesee':[13],'Greene': [18],'Hamilton': [2],'Herkimer': [12],'Jefferson':[12],'Kings': [47439],'Lewis':[2],'Livingston':[14],'Madison':[51],'Monroe': [349],'Montgomery': [7],'Nassau': [9554],'New York': [47439],'Niagara': [46],'Oneida':[50],'Onondaga': [217],'Ontario':[24],'Orange': [1756],'Orleans':[6],'Oswego':[17],'Otsego':[19],'Putnam': [207],'Queens': [47439],'Rensselaer':[43],'Richmond':[47439],'Rockland': [3321],'Saratoga': [122],'Schenectady': [93],'Schoharie':[8],'Schuyler':[2],'Seneca':[0],'Seneca':[2],'St Lawrence':[34],'Steuben':[38],'Suffolk': [7605],'Sullivan': [121],'Tioga': [7],'Tompkins': [68],'Ulster': [221],'Warren': [18],'Washington': [10],'Wayne':[24],'Westchester': [10683],'Wyoming': [10],'Yates':[0]}
    df32 = pd.DataFrame.from_dict(data, orient='index')
    df32 = df32.rename(columns={0: "April 01"})
    df32["date"] = "April 01"
    df32["date_sort"] = 32
    df32 = df32.reset_index()

    data = {'Albany': [253],'Allegany':[12],'Bronx': [51809],'Broome': [46],'Cattaraugus':[8],'Cayuga':[4],'Chautauqua':[8],'Chemung':[22],'Chenango': [28],'Clinton': [25],'Columbia':[36],'Cortland':[8],'Delaware': [22],'Dutchess': [667],'Erie': [617],'Essex': [6],'Franklin':[9],'Fulton':[6],'Genesee':[14],'Greene': [21],'Hamilton': [2],'Herkimer': [14],'Jefferson':[15],'Kings': [51809],'Lewis':[2],'Livingston':[14],'Madison':[60],'Monroe': [420],'Montgomery': [8],'Nassau': [10587],'New York': [51809],'Niagara': [76],'Oneida':[61],'Onondaga': [234],'Ontario':[26],'Orange': [1993],'Orleans':[6],'Oswego':[22],'Otsego':[21],'Putnam': [216],'Queens': [51809],'Rensselaer':[53],'Richmond':[51809],'Rockland': [3751],'Saratoga': [132],'Schenectady': [101],'Schoharie':[8],'Schuyler':[3],'Seneca':[4],'St Lawrence':[39],'Steuben':[43],'Suffolk': [8746],'Sullivan': [143],'Tioga': [7],'Tompkins': [74],'Ulster': [240],'Warren': [18],'Washington': [12],'Wayne':[27],'Westchester': [11567],'Wyoming': [14],'Yates':[1]}#48462 #51809
    df33 = pd.DataFrame.from_dict(data, orient='index')
    df33 = df33.rename(columns={0: "April 02"})
    df33["date"] = "April 02"
    df33["date_sort"] = 33
    df33 = df33.reset_index()

    data = {'Albany': [267],'Allegany':[14],'Bronx': [57159],'Broome': [56],'Cattaraugus':[9],'Cayuga':[6],'Chautauqua':[9],'Chemung':[35],'Chenango': [32],'Clinton': [30],'Columbia':[42],'Cortland':[10],'Delaware': [24],'Dutchess': [809],'Erie': [720],'Essex': [6],'Franklin':[10],'Fulton':[6],'Genesee':[16],'Greene': [23],'Hamilton': [2],'Herkimer': [14],'Jefferson':[18],'Kings': [57159],'Lewis':[2],'Livingston':[16],'Madison':[70],'Monroe': [464],'Montgomery': [10],'Nassau': [12024],'New York': [57159],'Niagara': [94],'Oneida':[71],'Onondaga': [252],'Ontario':[28],'Orange': [2397],'Orleans':[9],'Oswego':[26],'Otsego':[21],'Putnam': [252],'Queens': [57159],'Rensselaer':[56],'Richmond':[57159],'Rockland': [4289],'Saratoga': [141],'Schenectady': [110],'Schoharie':[9],'Schuyler':[3],'Seneca':[6],'St Lawrence':[43],'Steuben':[46],'Suffolk': [10154],'Sullivan': [168],'Tioga': [7],'Tompkins': [84],'Ulster': [263],'Warren': [19],'Washington': [15],'Wayne':[30],'Westchester': [12351],'Wyoming': [15],'Yates':[1]}
    df34 = pd.DataFrame.from_dict(data, orient='index')
    df34 = df34.rename(columns={0: "April 03"})
    df34["date"] = "April 03"
    df34["date_sort"] = 34
    df34 = df34.reset_index()

    data = {'Albany': [293],'Allegany':[16],'Bronx': [63306],'Broome': [65],'Cattaraugus':[9],'Cayuga':[7],'Chautauqua':[10],'Chemung':[36],'Chenango': [39],'Clinton': [31],'Columbia':[49],'Cortland':[10],'Delaware': [26],'Dutchess': [938],'Erie': [808],'Essex': [7],'Franklin':[10],'Fulton':[9],'Genesee':[20],'Greene': [24],'Hamilton': [2],'Herkimer': [18],'Jefferson':[20],'Kings': [63306],'Lewis':[2],'Livingston':[18],'Madison':[74],'Monroe': [512],'Montgomery': [13],'Nassau': [13346],'New York': [63306],'Niagara': [101],'Oneida':[80],'Onondaga': [262],'Ontario':[31],'Orange': [2741],'Orleans':[10],'Oswego':[26],'Otsego':[26],'Putnam': [283],'Queens': [63306],'Rensselaer':[58],'Richmond':[63306],'Rockland': [4872],'Saratoga': [141],'Schenectady': [117],'Schoharie':[10],'Schuyler':[4],'Seneca':[6],'St Lawrence':[52],'Steuben':[55],'Suffolk': [11370],'Sullivan': [193],'Tioga': [7],'Tompkins': [85],'Ulster': [290],'Warren': [20],'Washington': [16],'Wayne':[30],'Westchester': [13081],'Wyoming': [18],'Yates':[1]}
    df35 = pd.DataFrame.from_dict(data, orient='index')
    df35 = df35.rename(columns={0: "April 04"})
    df35["date"] = "April 04"
    df35["date_sort"] = 35
    df35 = df35.reset_index()

    data = {'Albany': [305],'Allegany':[16],'Bronx': [67551],'Broome': [71],'Cattaraugus':[10],'Cayuga':[8],'Chautauqua':[11],'Chemung':[38],'Chenango': [43],'Clinton': [33],'Columbia':[51],'Cortland':[10],'Delaware': [27],'Dutchess': [1077],'Erie': [918],'Essex': [7],'Franklin':[10],'Fulton':[9],'Genesee':[22],'Greene': [24],'Hamilton': [2],'Herkimer': [22],'Jefferson':[26],'Kings': [67551],'Lewis':[3],'Livingston':[19],'Madison':[74],'Monroe': [548],'Montgomery': [15],'Nassau': [14398],'New York': [67551],'Niagara': [116],'Oneida':[87],'Onondaga': [268],'Ontario':[32],'Orange': [3102],'Orleans':[11],'Oswego':[28],'Otsego':[29],'Putnam': [314],'Queens': [67551],'Rensselaer':[60],'Richmond':[67551],'Rockland': [5326],'Saratoga': [148],'Schenectady': [128],'Schoharie':[11],'Schuyler':[4],'Seneca':[9],'St Lawrence':[55],'Steuben':[63],'Suffolk': [12405],'Sullivan': [234],'Tioga': [7],'Tompkins': [88],'Ulster': [332],'Warren': [25],'Washington': [18],'Wayne':[32],'Westchester': [13723],'Wyoming': [22],'Yates':[1]}
    df36 = pd.DataFrame.from_dict(data, orient='index')
    df36 = df36.rename(columns={0: "April 05"})
    df36["date"] = "April 05"
    df36["date_sort"] = 36
    df36 = df36.reset_index()

    data = {'Albany': [319],'Allegany':[17],'Bronx': [72181],'Broome': [76],'Cattaraugus':[12],'Cayuga':[11],'Chautauqua':[15],'Chemung':[47],'Chenango': [46],'Clinton': [36],'Columbia':[59],'Cortland':[13],'Delaware': [29],'Dutchess': [1189],'Erie': [1023],'Essex': [7],'Franklin':[10],'Fulton':[11],'Genesee':[23],'Greene': [24],'Hamilton': [2],'Herkimer': [25],'Jefferson':[33],'Kings': [72181],'Lewis':[6],'Livingston':[22],'Madison':[82],'Monroe': [574],'Montgomery': [15],'Nassau': [15616],'New York': [72181],'Niagara': [120],'Oneida':[100],'Onondaga': [271],'Ontario':[32],'Orange': [3397],'Orleans':[13],'Oswego':[29],'Otsego':[34],'Putnam': [345],'Queens': [72181],'Rensselaer':[62],'Richmond':[72181],'Rockland': [5703],'Saratoga': [153],'Schenectady': [138],'Schoharie':[11],'Schuyler':[4],'Seneca':[9],'St Lawrence':[59],'Steuben':[75],'Suffolk': [13487],'Sullivan': [253],'Tioga': [8],'Tompkins': [94],'Ulster': [372],'Warren': [26],'Washington': [19],'Wayne':[34],'Westchester': [14294],'Wyoming': [23],'Yates':[1]}
    df37 = pd.DataFrame.from_dict(data, orient='index')
    df37 = df37.rename(columns={0: "April 06"})
    df37["date"] = "April 06"
    df37["date_sort"] = 37
    df37 = df37.reset_index()

    data = {'Albany': [333], 'Allegany':[17], 'Broome': [86],'Cattaraugus':[13],'Cayuga':[14],'Chautauqua':[16],'Chemung':[49], 'Chenango': [51], 'Clinton': [37], 'Columbia':[61],'Cortland':[16], 'Delaware': [36], 'Dutchess': [1249], 'Erie': [1135], 'Essex': [7],'Franklin':[10], 'Fulton':[13], 'Genesee':[33], 'Greene': [24], 'Hamilton': [2], 'Herkimer': [27],'Jefferson':[39],'Lewis':[6],'Livingston':[23],'Madison':[88], 'Monroe': [596], 'Montgomery': [18], 'Nassau': [16610], 'Niagara': [126], 'New York': [76876], 'Oneida':[118], 'Onondaga': [335], 'Ontario':[33], 'Orange': [3599],'Orleans':[15], 'Oswego':[31],'Otsego':[34], 'Putnam': [366], 'Rensselaer':[67], 'Rockland': [5990], 'Saratoga': [155], 'Schenectady': [145],'Schoharie':[12],'Schuyler':[4],'Seneca':[10],'St Lawrence':[60], 'Steuben':[75], 'Suffolk': [14517], 'Sullivan': [270],'Tioga': [8], 'Tompkins': [97], 'Ulster': [398], 'Warren': [31], 'Washington': [19], 'Wayne':[35], 'Westchester': [14804], 'Wyoming': [23],'Yates':[1], 'Kings': [76876], 'Queens': [76876], 'Bronx': [76876], 'Richmond':[76876]}
    df38 = pd.DataFrame.from_dict(data, orient='index')
    df38 = df38.rename(columns={0: "April 07"})
    df38["date"] = "April 07"
    df38["date_sort"] = 38
    df38 = df38.reset_index()

    df_confirmed_historical = pd.concat([df38, df37, df36, df35, df34, df33, df32, df31, df30, df29, df28, df27, df26, df25, df24, df23, df22, df21, df20, df19, df18, df17, df16, df15, df14, df13, df12, df11, df10, df9, df8, df7, df6, df5, df4, df3, df2, df1], axis=1)
    del [df38, df37, df36, df35, df34, df33, df32, df31, df30, df29, df28, df27, df26, df25, df24, df23, df22, df21, df20, df19, df18, df17, df16, df15, df14, df13, df12, df11, df10, df9, df8, df7, df6, df5, df4, df3, df2, df1]
    df_confirmed_historical_T = df_confirmed_historical.T
    del df_confirmed_historical
    df_confirmed_historical_T.columns = df_confirmed_historical_T.iloc[0]
    df_confirmed_historical_T = df_confirmed_historical_T.drop(df_confirmed_historical_T.index[0])
    df_confirmed_historical_T = df_confirmed_historical_T.drop(['date_sort','date'])
    df_confirmed_historical_T = df_confirmed_historical_T.reset_index()
    df_confirmed_historical_T = df_confirmed_historical_T.rename(columns={'index':'date'})

    return df_confirmed_historical_T
