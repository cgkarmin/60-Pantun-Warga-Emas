import streamlit as st
import pandas as pd
import os

# 🎯 Tetapan Direktori Data
DATA_FOLDER = "data"
CSV_FILE = os.path.join(DATA_FOLDER, "60_Pantun_Warga_Emas.csv")
PDF_FILE = os.path.join(DATA_FOLDER, "60_Pantun_Warga_Emas_Final.pdf")
DOCX_FILE = os.path.join(DATA_FOLDER, "60_Pantun_Warga_Emas_Final.docx")

# 🎯 Semak Fail CSV Wujud atau Tidak
if os.path.exists(CSV_FILE):
    df_pantun = pd.read_csv(CSV_FILE)
else:
    df_pantun = None

# 🎯 Tajuk Utama Aplikasi
st.title("📜 Pantun Warga Emas")

# 🎯 Menu Navigasi
menu = st.radio("📌 Pilih menu:", ["App", "Carian Pantun", "Muat Turun Buku"])

# ✅ **Halaman Utama**
if menu == "App":
    st.subheader("🏠 Selamat Datang ke Aplikasi Pantun Warga Emas!")
    st.write("""
    Aplikasi ini direka khas untuk mencari, membaca, dan memahami 60 pantun penuh hikmah. 
    Sesuai digunakan oleh **guru, ibu bapa, pakar motivasi, hos majlis**, dan sesiapa sahaja yang berminat dengan pantun.
    """)

# ✅ **Halaman Carian Pantun**
elif menu == "Carian Pantun":
    st.subheader("🔍 Cari Pantun Warga Emas")
    
    if df_pantun is not None:
        search_query = st.text_input("Masukkan kata kunci pantun:")
        if search_query:
            results = df_pantun[df_pantun.apply(lambda row: search_query.lower() in str(row).lower(), axis=1)]
            if not results.empty:
                st.success(f"✅ {len(results)} pantun dijumpai:")
                for _, row in results.iterrows():
                    st.write(f"📖 **{row['Tajuk']}**")
                    st.write(f"*{row['Pantun']}*")
            else:
                st.warning("⚠️ Tiada pantun yang sepadan dengan carian anda.")
    else:
        st.error("❌ Fail pantun tidak ditemui. Sila pastikan fail telah dimuat naik dengan betul.")

# ✅ **Halaman Muat Turun Buku**
elif menu == "Muat Turun Buku":
    st.subheader("📥 Muat Turun Buku")
    
    # Butang muat turun PDF
    if os.path.exists(PDF_FILE):
        with open(PDF_FILE, "rb") as file_pdf:
            st.download_button("📄 Muat Turun PDF", file_pdf, file_name="60_Pantun_Warga_Emas_Final.pdf")
    else:
        st.error("❌ Fail PDF tidak ditemui. Sila semak semula.")

    # Butang muat turun DOCX
    if os.path.exists(DOCX_FILE):
        with open(DOCX_FILE, "rb") as file_docx:
            st.download_button("📄 Muat Turun DOCX", file_docx, file_name="60_Pantun_Warga_Emas_Final.docx")
    else:
        st.error("❌ Fail DOCX tidak ditemui. Sila semak semula.")
