import streamlit as st

st.set_page_config(page_title="Paparan Penuh Pantun", layout="wide")

st.title("📖 Paparan Penuh Pantun")
st.write("Lihat pantun yang telah dipilih dengan lebih jelas di halaman ini.")

# Placeholder contoh paparan pantun - nanti disambungkan dengan database
selected_pantun = {
    "tajuk": "Pantun Kejujuran",
    "isi": """Siakap senohong gelama ikan duri,  
Bercakap bohong lama-lama mencuri.  
Kejujuran amalan sejati,  
Hidup berkat bahagia di hati.""",
    "makna": "Pantun ini mengingatkan kita bahawa kejujuran adalah asas kehidupan yang baik. Jika seseorang terbiasa berbohong, lama-kelamaan ia akan membawa kepada perkara yang lebih buruk.",
    "situasi": "Sesuai digunakan dalam ceramah motivasi tentang nilai kejujuran dan amanah.",
}

# Paparan pantun
st.header(f"🌿 {selected_pantun['tajuk']}")
st.markdown(f"**{selected_pantun['isi']}**")

# Makna pantun
st.info(f"**Makna Pantun:** {selected_pantun['makna']}")

# Situasi penggunaan
st.success(f"**Situasi Penggunaan:** {selected_pantun['situasi']}")

# Butang untuk
