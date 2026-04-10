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
    return day_df, hour_df

day_df, hour_df = load_data()


with st.sidebar:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png")
    st.title("Bike Sharing Dashboard")
    
    season_filter = st.selectbox(
        "Pilih Musim:",
        options=["Semua Musim", "Spring", "Summer", "Fall", "Winter"]
    )

# Filter data berdasarkan pilihan di sidebar
if season_filter != "Semua Musim":
    day_df_filtered = day_df[day_df['season'] == season_filter]
else:
    day_df_filtered = day_df


st.header("🚲 Bike Sharing Analytics Dashboard")

# Row 1: Menampilkan metrik utama
col1, col2 = st.columns(2)
with col1:
    total_rentals = day_df_filtered['cnt'].sum()
    st.metric("Total Penyewaan Sepeda", value=f"{total_rentals:,}")

with col2:
    avg_rentals = round(day_df_filtered['cnt'].mean())
    st.metric("Rata-rata Penyewaan Harian", value=f"{avg_rentals:,}")

st.markdown("---")

# Row 2: Visualisasi Pertanyaan 1 (Pengaruh Cuaca)
st.subheader("Pengaruh Kondisi Cuaca terhadap Penyewaan")
fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x="weathersit", y="cnt", data=day_df_filtered, ax=ax1, palette="magma", errorbar=None)
ax1.set_ylabel("Rata-rata Penyewaan")
ax1.set_xlabel("Kondisi Cuaca")
st.pyplot(fig1)

st.markdown("---")

# Row 3: Visualisasi Pertanyaan 2 (Clustering/Binning Waktu)
st.subheader("Tren Penyewaan: Jam Sibuk vs Jam Santai (Hasil Clustering)")
st.write("Visualisasi ini membandingkan pola penyewaan sepeda berdasarkan kategori waktu antara hari kerja dan hari libur.")

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x="time_category", y="cnt", hue="workingday", data=hour_df, ax=ax2, palette="Set2", errorbar=None)
ax2.set_ylabel("Rata-rata Penyewaan")
ax2.set_xlabel("Kategori Waktu")
ax2.legend(title="Hari Kerja", labels=["Libur", "Kerja"])
st.pyplot(fig2)

st.caption("Dashboard dibuat oleh: M Nafis Fakhrudin untuk Proyek Akhir Belajar Fundamental Analisis Data Dicoding")