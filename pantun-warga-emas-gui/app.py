import streamlit as st
import pandas as pd
import os

# ✅ Konfigurasi halaman utama
st.set_page_config(page_title="Pantun Warga Emas", layout="wide")

# ✅ Path ke fail CSV dalam Streamlit Cloud
csv_path = "data/60_Pantun_Warga_Emas.csv"
pdf_path = "data/60_Pantun_Warga_Emas_Final.pdf"
docx_path = "data/60_Pantun_Warga_Emas_Final.docx"

# ✅ Fungsi untuk memuatkan data pantun
@st.cache_data
def load_pantun():
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path, encoding='utf-8')
        return df
    else:
        return None  # Kembalikan None jika fail tidak wujud

# ✅ Muatkan DataFrame pantun
df_pantun = load_pantun()

# ✅ Menu navigasi utama (Paparan Pantun dibuang)
menu = st.radio("Pilih menu:", ["App", "Carian Pantun", "Muat Turun Buku"], horizontal=True)

# ✅ Halaman APP (Halaman utama)
if menu == "App":
    st.markdown("<h1 style='text-align: center;'>📖 Pantun Warga Emas</h1>", unsafe_allow_html=True)
    st.write("Inisiatif untuk mendokumentasikan dan menyebarkan hikmah dalam bentuk pantun.")

    st.markdown("""
    **📌 Apa yang boleh anda lakukan?**
    - 🔍 **Cari pantun mengikut tema, jenis, atau situasi penggunaan**
    - 📖 **Baca pantun dengan format yang kemas**
    - 📥 **Muat turun koleksi pantun dalam format PDF & DOCX**
    """)

# ✅ Halaman Carian Pantun (Pantun hanya dipaparkan di sini)
elif menu == "Carian Pantun":
    st.markdown("<h1 style='text-align: center;'>🔍 Carian Pantun</h1>", unsafe_allow_html=True)

    if df_pantun is None:
        st.error("❌ Fail pantun tidak ditemui. Sila pastikan fail telah dimuat naik dengan betul.")
    else:
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
    st.markdown("<h1 style='text-align: center;'>📥 Muat Turun Buku</h1>", unsafe_allow_html=True)
    st.write("Muat turun buku pantun dalam format PDF atau DOCX.")

    # 🔹 Semak kewujudan fail sebelum membenarkan muat turun
    if os.path.exists(pdf_path):
        with open(pdf_path, "rb") as file_pdf:
            st.download_button("📄 Muat Turun PDF", file_pdf, file_name="60_Pantun_Warga_Emas.pdf", mime="application/pdf")
    else:
        st.error("❌ Fail PDF tidak ditemui. Sila semak semula.")

    if os.path.exists(docx_path):
        with open(docx_path, "rb") as file_docx:
            st.download_button("📜 Muat Turun DOCX", file_docx, file_name="60_Pantun_Warga_Emas.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    else:
        st.error("❌ Fail DOCX tidak ditemui. Sila semak semula.")

# ✅ Footer
st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px;">
    © 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.
    </p>
    """, unsafe_allow_html=True)
