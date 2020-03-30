# -*- coding: utf-8 -*-
import pandas as pd

HV_loss = 0.005     #HV Transformer Loss
TX_loss = 0.003     #Transmission Line Loss

ExportLim = 25000000    #Plant Export Limit

#Read CSV file into dataframe
data = pd.read_csv("data.CSV",delimiter=';')    #read CSV file into dataframe
               

#replace all negative numbers with 0
num = data._get_numeric_data()   
num[num < 0] = 0

#Apply Export Limit and convert to MV
def expLim(x):
    if x > ExportLim:
        return ExportLim/1000000
    else:
        return x/1000000

#Apply external losses
data['KWH'] = data.apply(lambda row: row.KWH - (row.KWH * TX_loss), axis = 1) #TX Lline Loss
data['KWH'] = data.apply(lambda row: row.KWH - (row.KWH * HV_loss), axis = 1) #HV Trafo Loss

#apply export limit
data['KWH'] = data['KWH'].apply(expLim)

KWH_tot = data['KWH'].sum()
print(KWH_tot)



