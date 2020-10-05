import streamlit as st# streamlit library
import pandas as pd#for manipualting data
import numpy as np#for numerical calculations
import matplotlib.pyplot as plt # for plotting graphs and histogram
import seaborn as sns # uses matplotlib to visualise distribution


#Data cleaing
def clean(data,d):
    df = data.drop(columns = {'parent_zcta'})
    df = df[df[d]!=0]
    return df

#Function to plot bar chart
def barplot(df,d):
    data = df[d]
    plt.bar(list(df.index), data)
    plt.xticks(fontsize=13)
    st.pyplot()

#Function to perform basic statistics
def stats(data):
    df = clean(data,'population')
    st.write("Least populated zip code :",df[df['population'] == min(df.population)])#Display details of least populated zip code
    st.write("Most populated zip code :",df[df['population'] == max(df.population)])#Display details of most populated zip code
    
    
    df = clean(data,'density')
    st.write("Least dense zip code :",df[df['density'] == min(df.density)])#Display details of least dense zip code
    st.write("Most dense zip code :",df[df['density'] == max(df.density)])#Display details of most dense zip code
    
    st.markdown('### Box plot and histogram for population and density')
    
    #Box plot and histogram to check the whole distribution
    for var in ['population','density']:
        plt.figure(figsize = (15,6))
        plt.subplot(1, 2, 1)
        fig = sns.boxplot(y = data[var])
        fig.set_title('Box plot')
        fig.set_ylabel(var)
    
        plt.subplot(1, 2, 2)
        fig = sns.distplot(data[var].dropna())
        fig.set_title('Histogram plot')
        fig.set_ylabel('')
        fig.set_xlabel(var)
        
        st.pyplot()
 

    #State details
    st.markdown('### Some details of the corresponding states of zip codes from the data')
    #Population details
    st.markdown('#### Population details')
    df = clean(data,'population')
    df = pd.pivot_table(df, index=['state_name'],values=['population'],aggfunc=np.sum)
    st.write(df)
    st.write("Least populated State :",df.index[df['population'] == min(df['population'])])#Display details of least populated zip code
    st.write("Most populated State :",df.index[df['population'] == max(df['population'])])#Display details of most populated zip code
    barplot(df,'population')


   #Density details
    st.markdown('#### Density details')
    df = clean(data,'density')
    df = pd.pivot_table(df, index=['state_name'],values=['density'],aggfunc=np.mean)
    st.write(df)
    st.write("Least dense State :",df.index[df['density'] == min(df['density'])])#Display details of least populated zip code
    st.write("Most dense State :",df.index[df['density'] == max(df['density'])])#Display details of most populated zip code
    barplot(df,'density')
   
    
     
    
    
