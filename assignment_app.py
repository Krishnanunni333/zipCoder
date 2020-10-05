#import all the required modules, packages and libraries

import streamlit as st# streamlit library
import pandas as pd#for manipualting data
import numpy as np#for numerical calculations
from basic_statistics import stats#basic_statistics module
from find_zip import search#find_zip module
from route import navigate#route module
from io import BytesIO#Input output module
from PIL import Image#Python image processing library



img = Image.open('../images/icon.jpg')
#Name and icon of webapp
st.beta_set_page_config(page_title='zipCoder',page_icon=img)
#US flag
img = Image.open('../images/flag.jpg')
img = img.convert('RGB')
newsize = (100, 100) 
img = img.resize(newsize)
st.image(img)

#Title of the app
st.title(" **ZIP-CODE DETAILS (US) WEB APP** ")

st.header("This application is a Streamlit dashboard that can be used to analyze  properties of some zip codes in US")




#To read the csv file and caching it to increase perfomance
@st.cache(persist=True)
def load_data():
    data = pd.read_csv("../assignment/uszips.csv")
    return data,True


#Main function to call each function.
def main():
    data,v = load_data()
    st.sidebar.markdown("### Zip code finder")
    if(v):
        st.write("Data loaded...!!!")
    

    #selectboxes on sidebar to find zip code.
    

    #Top down approach
    if(st.sidebar.checkbox("Find zip code by filtering")):
        states = list(data.state_name.unique())
        state = st.sidebar.selectbox('Select state',states)
        df = data[data['state_name']==state]
        cities = list(df.city.unique())
        city = st.sidebar.selectbox('Select city',cities)
        df = df[df['city']==city]
        zips = list(df.zip.unique())
        zip = st.sidebar.selectbox('Select zip code',zips)
        df = df[df['zip']==zip]
        if(st.sidebar.button('Search')):
            search(df)
   
    
    #Search approach
    elif(st.sidebar.checkbox("Randomly find a zip code")):
        codes = list(data.zip)
        code = st.sidebar.selectbox('Type or select zip code',codes)

        if(st.sidebar.button('Search')):
             df = data[data['zip'] == code]
             search(df)



    #main window
    else:
        selection = st.radio("What to do?", ['Basic overall statistics','Find route between 2 zip codes'])
        #Basic statistics on main window.(default)
        if(selection == 'Basic overall statistics'):
            stats(data)
        #For finding the route between 2 zip codes
        elif(selection == 'Find route between 2 zip codes'):
            codes = list(data.zip)
            code_1 = st.selectbox('Type or select first zip code',codes)
            codes.remove(code_1)
            code_2 = st.selectbox('Type or select second zip code',codes)
            df = data[(data['zip'] == code_1) | (data['zip'] == code_2)]
            if(st.button('Find route')):
                navigate(df)
        
    #Sample video tutorial
    if(st.checkbox("Watch tutorial")):
        st.markdown("### Assignment Video")
        st.video('https://youtu.be/jWWAk53-6gU')

#Calling main function...
if __name__=="__main__":
    main()
