import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Set style seaborn
sns.set_theme(style="darkgrid")

# Menyiapkan data
@st.cache_data
def load_data():
    day_df = pd.read_csv("dashboard/day_clean.csv")
    hour_df = pd.read_csv("dashboard/hour_clean.csv")
    
    # Memastikan kolom dteday bertipe datetime
    day_df["dteday"] = pd.to_datetime(day_df["dteday"])
    hour_df["dteday"] = pd.to_datetime(hour_df["dteday"])
    return day_df, hour_df

day_df, hour_df = load_data()

# Mendapatkan rentang tanggal minimum dan maksimum
min_date = day_df["dteday"].min()
max_date = day_df["dteday"].max()

# ==============================
# SIDEBAR
# ==============================
with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Bike Sharing Dashboard")
    
    # 1. Filter Rentang Waktu (Memenuhi Syarat Reviewer)
    st.subheader("Filter Waktu")
    start_date, end_date = st.date_input(
        label='Pilih Rentang Waktu',
        min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )
    
    # 2. Filter Musim
    st.subheader("Filter Musim")
    season_filter = st.selectbox(
        "Pilih Musim:",
        options=["Semua Musim", "Spring", "Summer", "Fall", "Winter"]
    )

# Filter data berdasarkan input waktu
day_df_filtered = day_df[(day_df["dteday"] >= pd.to_datetime(start_date)) & 
                         (day_df["dteday"] <= pd.to_datetime(end_date))]

hour_df_filtered = hour_df[(hour_df["dteday"] >= pd.to_datetime(start_date)) & 
                           (hour_df["dteday"] <= pd.to_datetime(end_date))]

# Filter data berdasarkan pilihan musim
if season_filter != "Semua Musim":
    day_df_filtered = day_df_filtered[day_df_filtered['season'] == season_filter]

# ==============================
# MAIN DASHBOARD
# ==============================
st.header("🚲 Bike Sharing Analytics Dashboard")

# Row 1: Menampilkan metrik utama
col1, col2 = st.columns(2)
with col1:
    total_rentals = day_df_filtered['cnt'].sum()
    st.metric("Total Penyewaan Sepeda", value=f"{total_rentals:,}")

with col2:
    if not day_df_filtered.empty:
        avg_rentals = round(day_df_filtered['cnt'].mean())
    else:
        avg_rentals = 0
    st.metric("Rata-rata Penyewaan Harian", value=f"{avg_rentals:,}")

st.markdown("---")

# Row 2: Visualisasi Pertanyaan 1 (Pengaruh Cuaca)
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan")
fig1, ax1 = plt.subplots(figsize=(10, 5))
if not day_df_filtered.empty:
    sns.barplot(x="weathersit", y="cnt", data=day_df_filtered, ax=ax1, palette="magma", errorbar=None)
    ax1.set_ylabel("Rata-rata Penyewaan")
    ax1.set_xlabel("Kondisi Cuaca")
    st.pyplot(fig1)
else:
    st.warning("Data tidak tersedia untuk rentang waktu dan musim ini.")

st.markdown("---")

# Row 3: Visualisasi Pertanyaan 2 (Clustering/Binning Waktu)
st.subheader("Tren Penyewaan: Jam Sibuk vs Jam Santai")
st.write("Visualisasi ini membandingkan pola penyewaan sepeda berdasarkan kategori waktu (hasil clustering).")

fig2, ax2 = plt.subplots(figsize=(10, 5))
if not hour_df_filtered.empty:
    sns.barplot(x="time_category", y="cnt", hue="workingday", data=hour_df_filtered, ax=ax2, palette="Set2", errorbar=None)
    ax2.set_ylabel("Rata-rata Penyewaan")
    ax2.set_xlabel("Kategori Waktu")
    ax2.legend(title="Hari Kerja", labels=["Libur", "Kerja"])
    st.pyplot(fig2)
else:
    st.warning("Data tidak tersedia untuk rentang waktu ini.")

st.caption("Dashboard diperbarui untuk memenuhi kriteria interaktif.")