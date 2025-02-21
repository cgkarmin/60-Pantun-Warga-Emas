import streamlit as st

st.title("📥 Muat Turun Buku Pantun Warga Emas")
st.write("Klik butang di bawah untuk memuat turun buku penuh dalam format PDF atau DOCX.")

# Butang muat turun PDF
with open("data/60_Pantun_Warga_Emas_Final.pdf", "rb") as file_pdf:
    st.download_button("📄 Muat Turun PDF", file_pdf, file_name="60_Pantun_Warga_Emas.pdf", mime="application/pdf")

# Butang muat turun DOCX
with open("data/60_Pantun_Warga_Emas_Final.docx", "rb") as file_docx:
    st.download_button("📜 Muat Turun DOCX", file_docx, file_name="60_Pantun_Warga_Emas.docx", mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
