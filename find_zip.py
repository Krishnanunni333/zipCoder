import streamlit as st# streamlit library
import ast#ast module helps Python applications to process trees of the Python abstract syntax
import pandas as pd#for manipualting data
import numpy as np#for numerical calculations
import folium#For plotting maps

from streamlit_folium import folium_static# to display folium map




#Function to search and show details of a zip code
def search(df):

        
    #Basic details of the zip code
    st.markdown('# Zip Code:  {}  '.format(df.iloc[0]['zip']))
    st.markdown('## State:  {}  '.format(df.iloc[0]['state_name']))
    st.markdown('## County (major):  {}  '.format(df.iloc[0]['county_name']))
    st.markdown('## City:  {}  '.format(df.iloc[0]['city']))
    st.markdown('## Population:  {}  '.format(df.iloc[0]['population']))
    st.markdown('## Density:  {}  '.format(df.iloc[0]['density']))
        
    #County details
    comb=[]
    for i,j in df.iterrows():
        l=j[13].split('|')
        d = ast.literal_eval(j[12])
        for a,b in zip(l,list(d.values())):
            comb.append(str(a)+":  "+str(b)+"  ")
    st.write("% of area of each county in this zip code -- ",*comb )
    



    #code to locate a zip code on map
    m = folium.Map(location=[df.iloc[0]['lat'], df.iloc[0]['lng']], zoom_start=16)
    tooltip = 'City: '+df.iloc[0]['city']+'  State: '+df.iloc[0]['state_name']
    folium.Marker(
        [df.iloc[0]['lat'], df.iloc[0]['lng']], popup='City: '+df.iloc[0]['city']+'  State: '+df.iloc[0]['state_name'], tooltip=tooltip
    ).add_to(m)

    # call to render Folium map in Streamlit
    folium_static(m)



  
    
