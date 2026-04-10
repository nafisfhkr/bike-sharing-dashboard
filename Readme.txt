# Bike Sharing Data Analysis Dashboard 🚲✨

## Deskripsi
Proyek ini merupakan tugas akhir dari kelas "Belajar Analisis Data dengan Python" di Dicoding. Fokus utama proyek ini adalah melakukan siklus analisis data lengkap pada **Bike Sharing Dataset**, mulai dari pembersihan data hingga pembuatan dashboard interaktif.

Analisis mencakup:
1.  **Analisis Pengaruh Cuaca & Musim:** Bagaimana faktor eksternal memengaruhi minat masyarakat dalam menyewa sepeda.
2.  **Analisis Pola Waktu (Clustering):** Mengelompokkan waktu penyewaan menjadi *Morning Rush Hour*, *Evening Rush Hour*, dan *Non-Rush Hour* untuk melihat perbedaan perilaku pengguna di hari kerja vs hari libur.

## Struktur Folder
- `dashboard/`: Berisi file dashboard utama (`dashboard.py`) dan dataset yang sudah dibersihkan (`day_clean.csv`, `hour_clean.csv`).
- `data/`: Berisi dataset mentah (`day.csv`, `hour.csv`).
- `notebook.ipynb`: Dokumentasi teknis analisis data (Wrangling, EDA, Visualisasi, Clustering).
- `requirements.txt`: Daftar library Python yang digunakan.
- `url.txt`: Tautan dashboard yang sudah di-deploy ke Streamlit Cloud.

## Cara Menjalankan Secara Lokal
Ikuti langkah-langkah berikut untuk menjalankan dashboard di komputer Anda:

1. **Clone atau Download Repositori**
2. **Instal Library yang Dibutuhkan**
   Buka terminal/command prompt dan jalankan perintah:
   ```bash
   pip install -r requirements.txt
3. Jalankan Dashboard dengan Streamlit
  Bash
  streamlit run dashboard/dashboard.py
  Buka di Browser
  Kunjungi tautan yang muncul di terminal (biasanya http://localhost:8501).

Tautan Dashboard (Streamlit Cloud)
Anda dapat mengakses dashboard versi online melalui tautan berikut:
https://bike-sharing-dashboard-pi8hz62zfpka37pxdvbf9m.streamlit.app/

Disusun oleh: M Nafis Fakhrudin - Politeknik Negeri Banyuwangi
