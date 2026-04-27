# Bike Sharing Analytics Dashboard
-  Oleh: Fadhilah Aulia Zulfa
-  ID Dicoding: CDCC229D6X2021

# Deskripsi Proyek
Proyek ini merupakan dashboard analitik interaktif yang dibangun menggunakan Python dan Streamlit. Dashboard ini bertujuan untuk menganalisis dan memvisualisasikan data penyewaan sepeda (Bike Sharing Dataset) guna menggali insight terkait pola perilaku pengguna (terdaftar vs kasual), tren musiman, serta dampak kondisi cuaca terhadap operasional penyewaan sepeda.
Proyek ini adalah tugas akhir / submission untuk kelas Analisis Data dari Dicoding.

# Fitur Utama 
-  Filter Interaktif: Pengguna dapat menyaring data berdasarkan rentang tanggal (Waktu) tertentu melalui sidebar
-  Metrik Utama (Key Metrics): Menampilkan total penyewaan secara langsung yang terbagi atas pengguna member (registered) dan pengguna kasual (Casual)
-  Analisis Jam Operasional: Visualisasi tren penyewaan per jam yang membandingkan perilaku pengguna pada hari kerja (Workingday) dan hari libur
-  Analisis Faktor Cuaca: Grafik batang yang menunjukkan korelasi antara kondisi cuaca (Cerah, Mendung, Hujan Ringan) dengan volume penyewaan
-  Tren Musiman: Visualisasi garis waktu (Timeline) yang menyoroti pergerakan jumlah pengguna kasual dari bulan ke bulan

# Teknologi yang Digunakan
-  Bahasa Pemrograman: Python
-  Manipulasi Data: Pandas
-  Visualisasi Data: Matplotlib dan Seaborn
-  Dashboard: Streamlit

# Cara Menjalankan Dashboard Secara Lokal
Ikuti langkah-langkah berikut untuk menjalankan dashboard ini di komputer Anda:

# 1. Persiapkan Folder Proyek
Pastikan semua file berikut berada dalam satu folder yang sama:
- `dashboard.py`
- `hari_all_data.csv`
- `jam_all_data.csv`
- `requirements.txt`
- 
# 2. Membuat Virtual Environment
Sangat disarankan untuk menggunakan Virtual Environment agar tidak terjadi konflik versi library. Buka terminal/command prompt di folder proyek anda, lalu jalankan
*Windows*
python -m venv venv
venv\Scripts\activate

# 3. Instalasi Library yang Dibutuhkan
Setelah environment aktif, instal semua library yang tertera di requirements.txt dengan menjalankan perintah:
pip install -r requirements.txt

# 4. Menjalankan Aplikasi Streamlit
Terakhir, jalankan perintah berikut untuk membuka dashboard di browser Anda:
(https://bikesharingdashboard-gmnac2w7lps4jdrtjazgxu.streamlit.app/)
