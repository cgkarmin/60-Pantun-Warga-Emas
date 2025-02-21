import streamlit as st
import pandas as pd
import random

# ✅ Konfigurasi halaman
st.set_page_config(page_title="Paparan Pantun", layout="wide")

# ✅ Path ke fail CSV dalam Streamlit Cloud
csv_path = "data/60_Pantun_Warga_Emas.csv"

# ✅ Fungsi untuk memuatkan data pantun
@st.cache_data
def load_pantun():
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
        st.success(f"✅ Data pantun dimuat dari: `{csv_path}`")
        return df
    except FileNotFoundError:
        st.error("❌ Fail pantun tidak ditemui. Sila pastikan fail telah dimuat naik dengan betul.")
        return pd.DataFrame()

# ✅ Muatkan DataFrame pantun
df_pantun = load_pantun()

# ✅ Debug: Paparkan data CSV dalam bentuk tabel jika wujud
if not df_pantun.empty:
    st.write("📋 **Data Pantun (Debug Mode):**")
    st.dataframe(df_pantun.head(5))  # Hanya paparkan 5 baris pertama untuk semakan
else:
    st.warning("⚠ Data pantun tidak berjaya dimuat. Sila semak semula fail CSV.")

# ✅ Tajuk halaman
st.markdown("<h1 style='text-align: center;'>📖 Paparan Pantun</h1>", unsafe_allow_html=True)

# ✅ Jika CSV berjaya dimuatkan, papar pantun
if not df_pantun.empty:
    # 🟢 Ambil 1-3 pantun secara rawak jika tiada carian
    random_pantun = df_pantun.sample(n=min(3, len(df_pantun)))

    # ✅ Paparkan pantun dalam format yang tersusun
    for index, row in random_pantun.iterrows():
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
    # Jika CSV kosong atau gagal dimuatkan
    st.warning("⚠ Tiada pantun tersedia untuk dipaparkan.")

# ✅ Footer
st.markdown("""
    <hr>
    <p style="text-align: center; font-size: 14px;">
    © 2008-2025 Carian Pantun Warga Emas. v1. 2023-2025. Sebuah carian pantun berguna yang boleh digunakan dalam acara dan majlis.
    </p>
    """, unsafe_allow_html=True)
