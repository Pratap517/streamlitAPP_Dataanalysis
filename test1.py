import streamlit as st
import pandas as pd

st.title("  This is Dataset Explorer  ")

file=st.file_uploader(" Please upload ur file",type=['csv','xlsx'])

if file:
    
    try:
        df=pd.read_csv(file)
        if st.button("Click Here to View Ur Dataset"):
            st.dataframe(df)
    
    except Exception as e:
            df=pd.read_excel(file)
            if st.button("Click Here to View Ur Dataset"):
                  st.dataframe(df)
    if st.button("Click Here to Explore More About the data"):
        
        
        if st.checkbox(" Check Shape of Data "):
            
            shape = df.shape
            st.write(shape)
        
        
        

    
        if st.checkbox(" Check total columns "):
            
            cols = df.columns
            st.write(cols)
            
            
            
        if st.checkbox(" Check Missing Values "):
            
            null = df.isnull().sum()
            st.write(null)
            
            
        if st.checkbox(" Check Datatypes "):
            
            datatype = df.dtypes
            st.write(datatype)
        
        if st.checkbox(" Check the Summary "):
            
            desc = df.describe().T
            st.write(desc)