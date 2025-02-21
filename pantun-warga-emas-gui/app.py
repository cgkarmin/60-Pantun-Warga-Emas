import streamlit as st
import pandas as pd
import os

# Tetapan halaman utama
st.set_page_config(page_title="Pantun Warga Emas", layout="wide", initial_sidebar_state="collapsed")

# 📌 Pastikan fail berada dalam folder yang betul
data_folder = "data"
csv_filename = os.path.join(data_folder, "60_Pantun_Warga_Emas.csv")
pdf_filename = os.path.join(data_folder, "60_Pantun_Warga_Emas_Final.pdf")
docx_filename = os.path.join(data_folder, "60_Pantun_Warga_Emas_Final.docx")

# Periksa kewujudan fail
pantun_loaded = os.path.exists(csv_filename)
pdf_available = os.path.exists(pdf_filename)
docx_available = os.path.exists(docx_filename)

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
        try:
            df_pantun = pd.read_csv(csv_filename)

            # Pastikan kolum "Tema" wujud dalam CSV
            required_columns = ["Tema", "Pantun", "Makna", "Situasi Penggunaan"]
            if not all(col in df_pantun.columns for col in required_columns):
                st.error("🚨 Ralat: Fail CSV tidak mempunyai kolum yang lengkap! Sila semak format fail.")
            else:
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

        except Exception as e:
            st.error(f"🚨 Ralat membaca fail CSV: {str(e)}")

    else:
        st.error("❌ Fail pantun tidak ditemui. Pastikan ia telah dimuat naik ke folder `data/`.")

# 📌 3. Bahagian Muat Turun Buku
elif menu == "Muat Turun Buku":
    st.subheader("📥 Muat Turun Buku")
    st.write("Muat turun buku pantun dalam format PDF atau DOCX.")

    if pdf_available:
        with open(pdf_filename, "rb") as file_pdf:
            st.download_button(label="📄 Muat Turun PDF", data=file_pdf, file_name="Pantun_Warga_Emas.pdf", mime="application/pdf")
    else:
        st.error("❌ Fail PDF tidak ditemui. Pastikan fail berada dalam folder `data/`.")

    if docx_available:
        with open(docx_filename, "rb") as file_docx:
            st.download_button(label="📝 Muat Turun DOCX", data=file_docx, file_name="Pantun_Warga_Emas.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    else:
        st.error("❌ Fail DOCX tidak ditemui. Pastikan fail berada dalam folder `data/`.")

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; font-size: 14px;'>© 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.</p>", unsafe_allow_html=True)
