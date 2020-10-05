import numpy as np#for numerical calculations
import pandas as pd#for manipualting data
import folium#For plotting maps
from streamlit_folium import folium_static# to display folium map
import streamlit as st # streamlit library

#Function to find route between 2 points
def navigate(df):
    centroid_lat = (df.iloc[0]['lat']+df.iloc[1]['lat'])/2
    centroid_lon = (df.iloc[0]['lng']+df.iloc[1]['lng'])/2
    
    #Map initialised
    m = folium.Map(location=[centroid_lat, centroid_lon], zoom_start=10)
    
    #Adding locations to the map
    tooltip = 'Zip: '+str(df.iloc[0]['zip'])+' City: '+df.iloc[0]['city']+'  State: '+df.iloc[0]['state_name']
    folium.Marker(
        [df.iloc[0]['lat'], df.iloc[0]['lng']], popup='Zip: '+str(df.iloc[0]['zip'])+' City: '+df.iloc[0]['city']+'  State: '+df.iloc[0]['state_name'], tooltip=tooltip
    ).add_to(m)
    
    tooltip = 'Zip: '+str(df.iloc[1]['zip'])+' City: '+df.iloc[1]['city']+'  State: '+df.iloc[0]['state_name']
    folium.Marker(
        [df.iloc[1]['lat'], df.iloc[1]['lng']], popup='Zip: '+str(df.iloc[1]['zip'])+'City: '+df.iloc[1]['city']+'  State: '+df.iloc[0]['state_name'], tooltip=tooltip
    ).add_to(m)
    
    #Adding a line between the plotted locations
    folium.PolyLine([[df.iloc[0]['lat'], df.iloc[0]['lng']], 
                     [df.iloc[1]['lat'],df.iloc[1]['lng']]]).add_to(m)
    
    folium_static(m)

