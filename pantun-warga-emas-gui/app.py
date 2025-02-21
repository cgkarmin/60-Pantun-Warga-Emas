import streamlit as st
import pandas as pd
import os

# **🔹 Konfigurasi halaman Streamlit**
st.set_page_config(
    page_title="Pantun Warga Emas",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={"Get Help": None, "Report a bug": None, "About": None}
)

# **🔹 Sembunyikan sidebar sepenuhnya dan tukar warna latar belakang**
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            display: none !important;
        }
        /* Pastikan teks sentiasa hitam untuk mod gelap & terang */
        body, .stApp {
            color: black !important;
            background: linear-gradient(to right, #d9f99d, #fef9c3) !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# **🔹 Cari fail CSV dalam direktori yang betul**
csv_filename = "pantun-warga-emas-gui/data/60_Pantun_Warga_Emas.csv"
if not os.path.exists(csv_filename):
    st.error("❌ Fail pantun tidak ditemui! Pastikan ia berada dalam folder 'pantun-warga-emas-gui/data/'.")
    st.stop()

# **🔹 Muatkan data CSV**
df_pantun = pd.read_csv(csv_filename)

# **🔹 MENU UTAMA**
st.markdown("<h1 style='text-align: center; color: black;'>📜 Pantun Warga Emas</h1>", unsafe_allow_html=True)

menu = st.radio(
    "Pilih Menu:",
    ["App", "Carian Pantun", "Muat Turun Buku"],
    horizontal=True
)

st.markdown("---")

# **🔹 HALAMAN UTAMA (APP)**
if menu == "App":
    st.markdown("<h2 style='color: black;'>📖 Pantun Warga Emas</h2>", unsafe_allow_html=True)
    st.markdown("""
    🏠 **Selamat Datang ke Aplikasi Pantun Warga Emas!**  
    Gunakan aplikasi ini untuk mencari dan memahami 60 pantun penuh hikmah, nasihat, dan warisan budaya.
    """, unsafe_allow_html=True)

# **🔎 CARIAN PANTUN**
elif menu == "Carian Pantun":
    st.markdown("<h2 style='color: black;'>🔍 Cari Pantun Warga Emas</h2>", unsafe_allow_html=True)
    pilihan_carian = st.radio(
        "Bagaimana anda mahu cari pantun?",
        ["Tema", "Jenis", "Situasi Penggunaan"],
        horizontal=True
    )

    if pilihan_carian == "Tema":
        pilihan = st.selectbox("📌 Pilih Tema:", ["Semua"] + sorted(df_pantun["Tema"].dropna().unique()))
        filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Tema"] == pilihan]
    elif pilihan_carian == "Jenis":
        pilihan = st.selectbox("🏷 Pilih Jenis Pantun:", ["Semua"] + sorted(df_pantun["Jenis"].dropna().unique()))
        filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Jenis"] == pilihan]
    elif pilihan_carian == "Situasi Penggunaan":
        pilihan = st.selectbox("🎯 Pilih Situasi Penggunaan:", ["Semua"] + sorted(df_pantun["Situasi Penggunaan"].dropna().unique()))
        filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Situasi Penggunaan"] == pilihan]

    # **Paparkan Hasil Carian**
    for index, row in filtered_pantun.iterrows():
        pantun_rangkap = row['Pantun'].replace("\n", "<br>")
        st.markdown(
            f"""
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px; color: black;">
            <h3 style='color: black;'>📖 {row['Tema']}</h3>
            <p style='font-size: 18px; font-style: italic; color: black;'>{pantun_rangkap}</p>
            <p><b>📌 Makna:</b> {row['Makna']}</p>
            <p><b>🏷 Jenis:</b> {row['Jenis']} | <b>🎯 Situasi Penggunaan:</b> {row['Situasi Penggunaan']}</p>
            <p><b>🌿 Konteks Alam:</b> {row['Konteks Alam']}</p>
            <p><b>💡 Makna Sosial & Etika:</b> {row['Makna Sosial & Etika']}</p>
            <p><b>📚 Pengajaran & Nilai:</b> {row['Pengajaran']}</p>
            <p><b>🔖 Cara Penggunaan:</b> {row['Cara Penggunaan']}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown("---")

# **🔹 Footer**
st.markdown(
    """
    <hr>
    <p style='text-align: center; font-size: 14px; color: black;'>
    © 2023-2025 Carian Pantun Warga Emas. v1. 2008-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara, tempat dan majlis.
    </p>
    """,
    unsafe_allow_html=True
)
