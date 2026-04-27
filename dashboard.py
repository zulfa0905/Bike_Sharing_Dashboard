import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# ==============================
# 1. KONFIGURASI HALAMAN
# ==============================
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# ==============================
# 2. LOAD DATASET 
# ==============================
@st.cache_data
def load_data():
    # Membaca data yang sudah bersih
    day_df = pd.read_csv("hari_all_data.csv")
    hour_df = pd.read_csv("jam_all_data.csv")
    
    # Mengubah kolom dteday menjadi tipe tanggal
    day_df['dteday'] = pd.to_datetime(day_df['dteday'])
    hour_df['dteday'] = pd.to_datetime(hour_df['dteday'])
    
    return day_df, hour_df

day_df, hour_df = load_data()

# ==============================
# 3. SIDEBAR (Bagian Kiri)
# ==============================
st.sidebar.title("🚲 Bike Sharing")
st.sidebar.markdown("**Oleh: Fadhilah Aulia Zulfa**")

min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

with st.sidebar:
    st.header("Filter Data")
    date_range = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
    if len(date_range) == 2:
        start_date, end_date = date_range
    else:
        start_date = end_date = date_range[0]

main_day_df = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                     (day_df["dteday"] <= pd.to_datetime(end_date))].copy()

main_hour_df = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & 
                       (hour_df["dteday"] <= pd.to_datetime(end_date))].copy()

# ==============================
# 4. MAIN DASHBOARD (Isi Utama)
# ==============================
st.title("🚲 Bike Sharing Analytics Dashboard")
st.markdown("Dashboard interaktif untuk menganalisis penyewaan sepeda berdasarkan cuaca, tren, dan pola jam operasional.")

# --- METRIK UTAMA ---
col1, col2, col3 = st.columns(3)
with col1:
    total_rentals = main_day_df['cnt'].sum()
    st.metric("Total Penyewaan (Semua)", value=f"{total_rentals:,}")
with col2:
    total_registered = main_day_df['registered'].sum()
    st.metric("Pengguna Member", value=f"{total_registered:,}")
with col3:
    total_casual = main_day_df['casual'].sum()
    st.metric("Pengguna Kasual", value=f"{total_casual:,}")

st.markdown("---")

# --- GRAFIK BARIS 1 ---
col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.subheader("Pola Sewa per Jam (Pengguna Terdaftar)") 
    fig_hour, ax_hour = plt.subplots(figsize=(10, 6))
    
    main_hour_df['kategori_hari'] = main_hour_df['workingday'].map({0: 'Hari Libur', 1: 'Hari Kerja'})
    
    sns.lineplot(
        data=main_hour_df, x='hr', y='registered', hue='kategori_hari', 
        palette=['#ff7f0e', '#1f77b4'], marker='o', ax=ax_hour
    )
    ax_hour.set_xlabel("Jam Operasional")
    ax_hour.set_ylabel("Rata-rata Penyewaan (Member)")
    st.pyplot(fig_hour)

with col_chart2:
    st.subheader("Dampak Cuaca terhadap Penyewaan")
    fig_weather, ax_weather = plt.subplots(figsize=(10, 6))
    
    sns.barplot(
        data=main_day_df, x='weather_label', y='cnt', 
        hue='weather_label', palette='viridis', ax=ax_weather, legend=False, errorbar=None
    )
    ax_weather.set_xlabel("Kondisi Cuaca")
    ax_weather.set_ylabel("Rata-rata Penyewaan")
    st.pyplot(fig_weather)

st.markdown("---")

# --- GRAFIK BARIS 2 ---
st.subheader("Tren Penyewaan Pengguna Kasual")
fig_trend, ax_trend = plt.subplots(figsize=(16, 6))

if 'year_month' not in main_day_df.columns:
    main_day_df['year_month'] = main_day_df['dteday'].dt.strftime('%Y-%m')
    
casual_trend = main_day_df.groupby('year_month')['casual'].sum().reset_index()

sns.lineplot(
    data=casual_trend, x='year_month', y='casual', 
    marker='o', color='#d62728', linewidth=3, ax=ax_trend
)
ax_trend.set_xlabel("Tahun & Bulan")
ax_trend.set_ylabel("Total Penyewaan Kasual")
ax_trend.tick_params(axis='x', rotation=45) 
st.pyplot(fig_trend)

st.caption("Copyright (c) Fadhilah Aulia Zulfa 2026")