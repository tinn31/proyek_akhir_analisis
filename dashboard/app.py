import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Kualitas Udara")

@st.cache_data
def load_data():
    return pd.read_csv('combined_df.csv')

combined_df = load_data()


st.sidebar.header("Pengaturan Analisis")

if st.sidebar.button('Tampilkan Data Kualitas Udara'):
    st.write("Data Kualitas Udara:")
    st.dataframe(combined_df)


num_vars = st.sidebar.selectbox('Pilih Jumlah Variabel untuk Analisis Korelasi:', [2, 3, 4, 5])
all_vars = ['PM2.5', 'PM10', 'TEMP', 'SO2', 'NO2', 'CO', 'O3'] 


selected_vars = st.sidebar.multiselect('Pilih Variabel untuk Korelasi:', options=all_vars, default=all_vars[:num_vars])


if len(selected_vars) != num_vars:
    st.warning(f"Silakan pilih tepat {num_vars} variabel untuk analisis korelasi.")
else:
    st.subheader("Matriks Korelasi antara Variabel yang Dipilih")
    corr_matrix = combined_df[selected_vars].corr()
    st.write(corr_matrix)

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    st.pyplot(plt.gcf())

st.sidebar.header("Pengaturan Analisis Tren")
trend_vars = st.sidebar.multiselect('Pilih Variabel untuk Analisis Tren (PM2.5, PM10):', options=['PM2.5', 'PM10'], default=['PM2.5', 'PM10'])


if trend_vars:
    annual_trend = combined_df.groupby('year')[trend_vars].mean().reset_index()

    plt.figure(figsize=(12, 6))
    for var in trend_vars:
        sns.lineplot(x='year', y=var, data=annual_trend, label=var, marker='o')
    plt.title('Tren Konsentrasi per Tahun')
    plt.xlabel('Tahun')
    plt.ylabel('Rata-rata Konsentrasi')
    plt.legend()
    st.pyplot(plt.gcf())

