import streamlit as st

st.title("🔍 Carian Pantun Warga Emas")
st.write("Gunakan carian ini untuk mencari pantun berdasarkan tema, jenis, atau situasi penggunaan.")

# Tambah carian pantun (akan dipautkan dengan database pantun)
search_query = st.text_input("Masukkan kata kunci pantun:", "")

if search_query:
    st.success(f"Menunjukkan hasil carian untuk: **{search_query}**")
    # Nanti kita sambungkan ini dengan database pantun
else:
    st.warning("Sila masukkan kata kunci untuk mencari pantun.")
