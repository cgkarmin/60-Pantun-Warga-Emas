import streamlit as st
import pandas as pd
import os

# ✅ Konfigurasi halaman tanpa sidebar
st.set_page_config(page_title="Pantun Warga Emas", layout="wide")

# ✅ CSS untuk sembunyikan sidebar sepenuhnya
st.markdown(
    """
    <style>
        /* Sembunyikan sidebar sepenuhnya */
        section[data-testid="stSidebar"] {
            display: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ✅ Path ke fail
csv_path = "data/60_Pantun_Warga_Emas.csv"
pdf_path = "data/60_Pantun_Warga_Emas_Final.pdf"
docx_path = "data/60_Pantun_Warga_Emas_Final.docx"

# ✅ Semak kewujudan fail secara automatik
pantun_available = os.path.exists(csv_path)
pdf_available = os.path.exists(pdf_path)
docx_available = os.path.exists(docx_path)

# ✅ Fungsi untuk memuatkan pantun hanya jika fail ada
@st.cache_data
def load_pantun():
    if pantun_available:
        return pd.read_csv(csv_path, encoding='utf-8')
    return None

df_pantun = load_pantun()

# ✅ Menu Navigasi
st.markdown("<h1 style='text-align: center;'>📖 Pantun Warga Emas</h1>", unsafe_allow_html=True)
menu = st.radio("📌 Pilih Menu:", ["App", "Carian Pantun", "Muat Turun Buku"], horizontal=True)

# ✅ Halaman APP
if menu == "App":
    st.write("Inisiatif untuk mendokumentasikan dan menyebarkan hikmah dalam bentuk pantun.")
    st.markdown("""
    **📌 Apa yang boleh anda lakukan?**
    - 🔍 **Cari pantun mengikut tema, jenis, atau situasi penggunaan**
    - 📖 **Baca pantun dengan format yang kemas**
    - 📥 **Muat turun koleksi pantun dalam format PDF & DOCX**
    """)

# ✅ Halaman Carian Pantun
elif menu == "Carian Pantun":
    st.markdown("<h2 style='text-align: center;'>🔍 Carian Pantun</h2>", unsafe_allow_html=True)

    if not pantun_available:
        st.error("❌ Fail pantun tidak ditemui. Admin sila muat naik fail CSV.")
        uploaded_file = st.file_uploader("📂 Muat Naik Fail CSV Pantun", type=["csv"])
        if uploaded_file is not None:
            with open(csv_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            st.success("✅ Fail CSV pantun berjaya dimuat naik! Sila refresh halaman.")
    else:
        pilihan_carian = st.radio("Bagaimana anda mahu cari pantun?", ["Tema", "Jenis", "Situasi Penggunaan", "Kata Kunci"], horizontal=True)

        if pilihan_carian == "Tema":
            pilihan = st.selectbox("📌 Pilih Tema:", ["Semua"] + sorted(df_pantun["Tema"].unique()))
            filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Tema"] == pilihan]
        elif pilihan_carian == "Jenis":
            pilihan = st.selectbox("🏷 Pilih Jenis Pantun:", ["Semua"] + sorted(df_pantun["Jenis"].unique()))
            filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Jenis"] == pilihan]
        elif pilihan_carian == "Situasi Penggunaan":
            pilihan = st.selectbox("🎯 Pilih Situasi Penggunaan:", ["Semua"] + sorted(df_pantun["Situasi Penggunaan"].unique()))
            filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Situasi Penggunaan"] == pilihan]
        else:
            search_query = st.text_input("🔎 Masukkan kata kunci pantun:")
            filtered_pantun = df_pantun[
                df_pantun.apply(lambda row: search_query.lower() in row.astype(str).str.lower().to_string(), axis=1)
            ] if search_query else df_pantun

        jumlah_pantun = len(filtered_pantun)
        if jumlah_pantun > 0:
            st.success(f"✅ {jumlah_pantun} pantun dijumpai:")
            for index, row in filtered_pantun.iterrows():
                st.markdown(f"""
                <div style="border: 2px solid #EAEAEA; padding: 15px; border-radius: 10px; background-color: #FAFAFA; margin-bottom: 20px;">
                    <h3 style="color: #2E86C1;">📖 {row['Tema']}</h3>
                    <p style="font-style: italic; font-size: 18px; color: #555;">{row['Pantun'].replace("\\n", "<br>")}</p>
                    <p>🔖 <b>Jenis:</b> {row['Jenis']}</p>
                    <p>🎯 <b>Situasi Penggunaan:</b> {row['Situasi Penggunaan']}</p>
                    <p>💡 <b>Cara Penggunaan:</b> {row['Cara Penggunaan']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("❌ Tiada pantun ditemui berdasarkan pilihan anda.")

# ✅ Halaman Muat Turun Buku
elif menu == "Muat Turun Buku":
    st.markdown("<h2 style='text-align: center;'>📥 Muat Turun Buku</h2>", unsafe_allow_html=True)
    st.write("Muat turun buku pantun dalam format PDF atau DOCX.")

    if not pdf_available:
        st.error("❌ Fail PDF tidak ditemui. Admin sila muat naik fail PDF.")
        uploaded_pdf = st.file_uploader("📂 Muat Naik Fail PDF", type=["pdf"])
        if uploaded_pdf is not None:
            with open(pdf_path, "wb") as f:
                f.write(uploaded_pdf.getbuffer())
            st.success("✅ Fail PDF berjaya dimuat naik! Sila refresh halaman.")

    if not docx_available:
        st.error("❌ Fail DOCX tidak ditemui. Admin sila muat naik fail DOCX.")
        uploaded_docx = st.file_uploader("📂 Muat Naik Fail DOCX", type=["docx"])
        if uploaded_docx is not None:
            with open(docx_path, "wb") as f:
                f.write(uploaded_docx.getbuffer())
            st.success("✅ Fail DOCX berjaya dimuat naik! Sila refresh halaman.")

# ✅ Footer
st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px;">
    © 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.
    </p>
    """, unsafe_allow_html=True)
