# -*- coding: utf-8 -*-
"""
Created on Thu Apr 21 22:03:58 2022

@author: Notis
"""

import pandas as pd
import streamlit as st
import plotly.express as px


avgerr = pd.read_csv('SSavg.csv', index_col=0)
avgerr = avgerr.iloc[1:]
avgerr = avgerr.dropna(how='all', axis=1)
avgerr = avgerr.stack()
avgerr = avgerr.to_frame()
avgerr = avgerr.reset_index()
avgerr.columns = ['Year','Postcode','HPI']

ops = avgerr['Postcode'].unique()
labels = [{'label':i, 'value':i} for i in ops]
####################################################################################
avgpr = pd.read_csv('SSer.csv', index_col=0)
avgpr = avgpr.iloc[1:]
avgpr = avgpr.dropna(how='all', axis=1)
avgpr = avgpr.stack()
avgpr = avgpr.to_frame()
avgpr = avgpr.reset_index()
avgpr.columns = ['Year','Postcode','AVG']

opsavg = avgpr['Postcode'].unique()
labelsavg = [{'label':i, 'value':i} for i in ops]
###############################################################

st.set_page_config(layout="wide")
st.title('House Price Index for UK properties.')

pstcd = st.multiselect(label='Select a Postcode or more', options= ops)



if len(pstcd)==0:
    fig = px.line(avgerr.loc[avgerr['Postcode'] == ops[0]], x="Year", y="HPI", color='Postcode', title='House Price Index from 1995 to 2022')
    st.plotly_chart(fig)
elif len(pstcd)>0:    
    fig = px.line(avgerr.loc[avgerr['Postcode'].isin(pstcd)], x="Year", y="HPI", color='Postcode', title='House Price Index from 1995 to 2022')
    st.plotly_chart(fig)
if len(pstcd)==0:
    fig2 = px.line(avgpr.loc[avgpr['Postcode'] == ops[0]], x="Year", y="AVG", color='Postcode', title='Average Property Price from 1995 to 2022')
elif len(pstcd)>0:   
    fig2 = px.line(avgpr.loc[avgpr['Postcode'].isin(pstcd)], x="Year", y="AVG", color='Postcode', title='Average Property Price from 1995 to 2022')

st.plotly_chart(fig2)

