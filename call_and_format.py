#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:46:56 2024

@author: emilypayne
"""

import pandas as pd
import numpy as np

def call_excel(excel_name, sheetname1, sheetname2):
    #excel_name = "200_tripartite_matrixes.xlsx"
    
    # read in the specific sheet
    df = pd.read_excel(excel_name, sheet_name=sheetname1)
    # change the df to be ready for 
    names_h_phy_cps = df.columns.tolist()
    df_without_header = df.copy()  # Create a copy of the original DataFrame
    # this resets column names to integers
    #df_without_header.columns = range(len(df_without_header.columns))
    # Extracting the first column
    first_column = df.iloc[:, 0]
    df_ready = df.drop(df.columns[0], axis=1)
    names_relays_cps = pd.DataFrame(first_column)
    # lastly change it to a numpy array to be processed
    herbivore_plant_matrix = df_ready.to_numpy()
    
    # read in the specific sheet
    df = pd.read_excel(excel_name, sheet_name=sheetname2)
    # change the df to be ready for 
    names_c_cyb_cps = df.columns.tolist()
    df_without_header = df.copy()  # Create a copy of the original DataFrame
    # this resets column names to integers
    #df_without_header.columns = range(len(df_without_header.columns))
    # Extracting the first column
    first_column = df.iloc[:, 0]
    df_ready = df.drop(df.columns[0], axis=1)
    names_relays_cps = pd.DataFrame(first_column)
    # lastly change it to a numpy array to be processed
    carnivore_herbivore_matrix = df_ready.to_numpy()
    
    # make sure the names of relays are in a list
    names_relays_cps = df[df.columns[0]].values.tolist()
    
    # make physical and cyber drop name 0 bc it is not actually a name
    names_c_cyb_cps = np.delete(names_c_cyb_cps, 0)
    names_h_phy_cps = np.delete(names_h_phy_cps, 0)
    
    print("these are the results for normal")
    num_relays = len(herbivore_plant_matrix)
    num_physical = len(herbivore_plant_matrix[0])
    num_cyber = len(carnivore_herbivore_matrix[0])
    
    return num_relays, num_physical, num_cyber,herbivore_plant_matrix, carnivore_herbivore_matrix, names_h_phy_cps, names_c_cyb_cps, names_relays_cps


#excel_name = "200_tripartite_matrixes.xlsx"
#sheetname1 = "DS1_CPS_phys"
#sheetname2 = "DS1_CPS_cyber"

#num_relays, num_physical, num_cyber,herbivore_plant_matrix, carnivore_herbivore_matrix, names_h_phy_cps, names_c_cyb_cps, names_relays_cps = call_excel(excel_name, sheetname1, sheetname2)


'''
x1,y1,removed_nodes_1 = trpartite(num_relays, num_physical, num_cyber, 
          herbivore_plant_matrix, carnivore_herbivore_matrix, "DS1",
          names_h_phy_cps, names_c_cyb_cps, names_relays_cps)
'''