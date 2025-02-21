import streamlit as st
import pandas as pd
import os

# ✅ Matikan sidebar
st.set_page_config(page_title="Pantun Warga Emas", layout="wide", initial_sidebar_state="collapsed")

# ✅ Pastikan fail CSV & Muat Turun tersedia
csv_path = "data/60_Pantun_Warga_Emas.csv"
pdf_path = "data/60_Pantun_Warga_Emas_Final.pdf"
docx_path = "data/60_Pantun_Warga_Emas_Final.docx"

# ✅ Pastikan fail ada
if not os.path.exists(csv_path):
    st.error("❌ Fail pantun tidak ditemui. Sila pastikan fail telah dimuat naik dengan betul.")
    st.stop()

# ✅ Muat Data Pantun
df_pantun = pd.read_csv(csv_path)

# ✅ Pilihan Menu
menu = st.radio("📌 Pilih Menu:", ["App", "Carian Pantun", "Muat Turun Buku"])

# ✅ Halaman: APP (Informasi)
if menu == "App":
    st.markdown("<h1>📖 Pantun Warga Emas</h1>", unsafe_allow_html=True)
    st.markdown("""
    🏠 **Selamat Datang ke Aplikasi Pantun Warga Emas!**  
    Gunakan aplikasi ini untuk mencari dan memahami 60 pantun penuh hikmah, nasihat, dan warisan budaya.
    """, unsafe_allow_html=True)

# ✅ Halaman: CARIAN PANTUN
elif menu == "Carian Pantun":
    st.markdown("<h2>🔍 Carian Pantun</h2>", unsafe_allow_html=True)

    pilihan_carian = st.selectbox("🔹 Cari Berdasarkan:", ["Tema", "Jenis", "Situasi Penggunaan", "Kata Kunci"])

    # Carian berdasarkan dropdown
    if pilihan_carian in ["Tema", "Jenis", "Situasi Penggunaan"]:
        pilihan = st.selectbox(f"📌 Pilih {pilihan_carian}:", ["Semua"] + sorted(df_pantun[pilihan_carian].dropna().unique().tolist()))
        if pilihan != "Semua":
            df_pantun = df_pantun[df_pantun[pilihan_carian] == pilihan]

    # Carian Kata Kunci
    elif pilihan_carian == "Kata Kunci":
        kata_kunci = st.text_input("🔎 Masukkan Kata Kunci:")
        if kata_kunci:
            df_pantun = df_pantun[df_pantun["Pantun"].str.contains(kata_kunci, case=False, na=False)]

    # ✅ Paparkan Pantun yang Dijumpai
    if not df_pantun.empty:
        st.success(f"✅ {len(df_pantun)} pantun dijumpai:")
        for index, row in df_pantun.iterrows():
            st.markdown(f"""
            ### 📖 {row['Tajuk Pantun']}
            _{row['Pantun'].replace('. ', '.<br>')}_  
            📌 **Makna:** {row['Makna']}
            """, unsafe_allow_html=True)
    else:
        st.error("❌ Tiada pantun yang sepadan.")

# ✅ Halaman: MUAT TURUN BUKU
elif menu == "Muat Turun Buku":
    st.markdown("<h2>📥 Muat Turun Buku</h2>", unsafe_allow_html=True)

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as file_pdf:
            st.download_button("📄 Muat Turun PDF", file_pdf, file_name="Pantun_Warga_Emas.pdf")

    if os.path.exists(docx_path):
        with open(docx_path, "rb") as file_docx:
            st.download_button("📄 Muat Turun DOCX", file_docx, file_name="Pantun_Warga_Emas.docx")

    if not os.path.exists(pdf_path) or not os.path.exists(docx_path):
        st.error("❌ Fail PDF/DOCX tidak ditemui. Sila semak semula.")

# ✅ Footer
st.markdown("""
---
© 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.
""", unsafe_allow_html=True)
