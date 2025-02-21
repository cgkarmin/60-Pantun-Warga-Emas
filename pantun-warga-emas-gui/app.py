import os
import streamlit as st
import pandas as pd

# ✅ Konfigurasi halaman Streamlit
st.set_page_config(
    page_title="Pantun Warga Emas",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ✅ Pastikan fail CSV boleh dibaca di laptop & Streamlit Cloud
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_filename = os.path.join(BASE_DIR, "data", "60_Pantun_Warga_Emas.csv")

if not os.path.exists(csv_filename):
    st.error(f"❌ Fail CSV tidak ditemui! Pastikan ia berada dalam folder `data/`. Path: {csv_filename}")
    st.stop()

# ✅ Baca fail CSV
df_pantun = pd.read_csv(csv_filename)

# ✅ Header utama aplikasi
st.markdown("<h1 style='text-align: center;'>📜 Pantun Warga Emas</h1>", unsafe_allow_html=True)

# ✅ Menu navigasi utama
menu = st.radio(
    "Pilih menu:",
    ["App", "Carian Pantun", "Paparan Pantun", "Muat Turun Buku"],
    horizontal=True
)

st.markdown("---")

# ✅ HALAMAN UTAMA (APP)
if menu == "App":
    st.subheader("✨ Selamat Datang ke Carian Pantun Warga Emas")
    st.write("Aplikasi ini membolehkan anda mencari dan membaca pantun bernilai emas yang penuh nasihat dan hikmah.")

    st.markdown("""
    **🎯 Apa yang boleh anda lakukan di sini?**
    - 🔍 **Cari pantun** mengikut **tema, jenis, atau situasi penggunaan**
    - 📖 **Baca pantun dengan format yang kemas**
    - 📥 **Muat turun koleksi pantun dalam format PDF & DOCX**
    """)

# ✅ CARIAN PANTUN
elif menu == "Carian Pantun":
    st.subheader("🔍 Cari Pantun Warga Emas")

    # 🔹 Pilihan profil pengguna
    profil_pengguna = st.selectbox(
        "👤 Pilih Profil Pengguna:",
        ["Umum", "Guru", "Ibu Bapa", "Pakar Motivasi", "Hos Majlis"]
    )

    # 🔹 Pilihan kaedah carian
    pilihan_carian = st.radio(
        "Bagaimana anda mahu cari pantun?",
        ["Tema", "Jenis", "Situasi Penggunaan", "Kata Kunci"],
        horizontal=True
    )

    # 🔹 Dropdown berdasarkan kaedah carian
    if pilihan_carian == "Tema":
        pilihan = st.selectbox("📌 Pilih Tema:", ["Semua"] + sorted(df_pantun["Tema"].unique()))
        filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Tema"] == pilihan]
    elif pilihan_carian == "Jenis":
        pilihan = st.selectbox("🏷 Pilih Jenis Pantun:", ["Semua"] + sorted(df_pantun["Jenis"].unique()))
        filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Jenis"] == pilihan]
    elif pilihan_carian == "Situasi Penggunaan":
        pilihan = st.selectbox("🎯 Pilih Situasi Penggunaan:", ["Semua"] + sorted(df_pantun["Situasi Penggunaan"].unique()))
        filtered_pantun = df_pantun if pilihan == "Semua" else df_pantun[df_pantun["Situasi Penggunaan"] == pilihan]
    else:  # Kata kunci
        search_query = st.text_input("🔎 Masukkan kata kunci pantun:")
        filtered_pantun = df_pantun[
            df_pantun.apply(lambda row: search_query.lower() in row.astype(str).str.lower().to_string(), axis=1)
        ] if search_query else df_pantun

    # 🔹 Paparkan hasil carian
    jumlah_pantun = len(filtered_pantun)
    if jumlah_pantun > 0:
        st.success(f"✅ {jumlah_pantun} pantun dijumpai:")
        for index, row in filtered_pantun.iterrows():
            with st.container():
                pantun_rangkap = "<br>".join(row["Pantun"].split("\n"))  # Format rangkap pantun
                
                st.markdown(
                    f"""
                    <div style="background-color: #f9f9f9; padding: 15px; border-radius: 10px;">
                    <h3>📖 {row['Tema']}</h3>
                    <p style='font-size: 18px; font-style: italic;'>
                    {pantun_rangkap}
                    </p>
                    <p><b>📌 Makna:</b> {row['Makna']}</p>
                    <p><b>🏷 Jenis:</b> {row['Jenis']} | <b>🎯 Situasi Penggunaan:</b> {row['Situasi Penggunaan']}</p>
                    <p><b>💡 Cara Penggunaan:</b> {row['Cara Penggunaan']}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                st.markdown("---")
    else:
        st.warning("❌ Tiada pantun ditemui berdasarkan pilihan anda.")

# ✅ MUAT TURUN BUKU
elif menu == "Muat Turun Buku":
    st.subheader("📥 Muat Turun Buku Pantun Warga Emas")
    st.write("Klik butang di bawah untuk memuat turun buku penuh dalam format PDF atau DOCX.")

    pdf_path = os.path.join(BASE_DIR, "data", "60_Pantun_Warga_Emas_Final.pdf")
    docx_path = os.path.join(BASE_DIR, "data", "60_Pantun_Warga_Emas_Final.docx")

    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as file_pdf:
            st.download_button("📄 Muat Turun PDF", file_pdf, file_name="60_Pantun_Warga_Emas.pdf", mime="application/pdf")

    if os.path.exists(docx_path):
        with open(docx_path, "rb") as file_docx:
            st.download_button("📜 Muat Turun DOCX", file_docx, file_name="60_Pantun_Warga_Emas.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")

# ✅ FOOTER
st.markdown("---")
st.markdown(
    """<p style='text-align: center; font-size: 14px;'>
    © 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025.  
    Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.
    </p>""",
    unsafe_allow_html=True
)
