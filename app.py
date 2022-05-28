import streamlit as st
import pandas as pd
st.title("miPrimeraAplicacion")
st.sidebar.title("Parametros")
num1=st.slider("Seleccione un valor 1",min_value=0,max_value=10,value=3)
num2=st.slider("Seleccione un valor 2",min_value=0,max_value=10,value=3)
st.write("La suma es ",num1+num2)

archivo_cargado=st.sidebar.file_uploader("carge su base de datos",type=[".xlsx",".xls"])
if archivo_cargado is not None :
    df=pd.read_excel(archivo_cargado)
    st.write(df)

csv=df.to_csv()
st.download_button(label="descargar archivo csv",data=csv)