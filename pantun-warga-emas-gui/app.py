import streamlit as st
import pandas as pd

# Tetapan halaman utama
st.set_page_config(page_title="Pantun Warga Emas", layout="wide", initial_sidebar_state="collapsed")

# Muatkan data pantun
csv_filename = "data/60_Pantun_Warga_Emas.csv"

try:
    df_pantun = pd.read_csv(csv_filename)
    pantun_loaded = True
except FileNotFoundError:
    df_pantun = None
    pantun_loaded = False

# Header utama
st.markdown("<h1 style='text-align: center;'>📖 Pantun Warga Emas</h1>", unsafe_allow_html=True)

# Menu utama
menu = st.radio("📌 Pilih menu:", ["App", "Carian Pantun", "Muat Turun Buku"], horizontal=True)

# 📌 1. Bahagian App (Maklumat Aplikasi)
if menu == "App":
    st.subheader("🏠 Selamat Datang ke Aplikasi Pantun Warga Emas!")
    st.write("""
    Aplikasi ini direka khas untuk membantu **guru, ibu bapa, pakar motivasi, dan hos majlis** 
    mendapatkan pantun yang sesuai untuk pelbagai situasi.  
      
    🔍 **Fungsi utama aplikasi ini:**  
    ✅ **Carian pantun berdasarkan kata kunci, tema, atau situasi penggunaan.**  
    ✅ **Setiap pantun disertakan dengan makna dan cadangan cara penggunaan.**  
    ✅ **Muat turun buku penuh dalam format PDF dan DOCX.**  

    🎯 **Gunakan aplikasi ini untuk menghidupkan budaya pantun dalam kehidupan seharian!**  
    """)

# 📌 2. Bahagian Carian Pantun
elif menu == "Carian Pantun":
    st.subheader("🔍 Carian Pantun Warga Emas")

    if pantun_loaded:
        search_keyword = st.text_input("Masukkan kata kunci untuk mencari pantun:")
        if search_keyword:
            filtered_pantun = df_pantun[df_pantun.apply(lambda row: search_keyword.lower() in row.to_string().lower(), axis=1)]
            if not filtered_pantun.empty:
                for index, row in filtered_pantun.iterrows():
                    st.markdown(f"""
                    **📖 {row['Tema']}**
                    *{row['Pantun']}*
                    
                    📌 **Makna:** {row['Makna']}
                    🎯 **Situasi Penggunaan:** {row['Situasi Penggunaan']}
                    """)
            else:
                st.warning("⚠️ Tiada pantun yang sepadan.")
        else:
            st.info("💡 Masukkan kata kunci untuk mula mencari pantun.")

    else:
        st.error("❌ Fail pantun tidak ditemui. Sila pastikan fail telah dimuat naik dengan betul.")

# 📌 3. Bahagian Muat Turun Buku
elif menu == "Muat Turun Buku":
    st.subheader("📥 Muat Turun Buku")
    st.write("Muat turun buku pantun dalam format PDF atau DOCX.")

    pdf_path = "data/60_Pantun_Warga_Emas_Final.pdf"
    docx_path = "data/60_Pantun_Warga_Emas_Final.docx"

    pdf_found = False
    docx_found = False

    try:
        with open(pdf_path, "rb") as file_pdf:
            pdf_found = True
            st.download_button(label="📄 Muat Turun PDF", data=file_pdf, file_name="Pantun_Warga_Emas.pdf", mime="application/pdf")
    except FileNotFoundError:
        st.error("❌ Fail PDF tidak ditemui. Sila semak semula.")

    try:
        with open(docx_path, "rb") as file_docx:
            docx_found = True
            st.download_button(label="📝 Muat Turun DOCX", data=file_docx, file_name="Pantun_Warga_Emas.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    except FileNotFoundError:
        st.error("❌ Fail DOCX tidak ditemui. Sila semak semula.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.</p>", unsafe_allow_html=True)
