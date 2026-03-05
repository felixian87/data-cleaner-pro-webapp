import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Data Cleaner Pro", layout="wide")

st.title("🧹 Data Cleaner Pro")
st.write("Carica il tuo file sporco (CSV o Excel) e scaricalo pulito in JSON o CSV.")

# --- SIDEBAR PER LE OPZIONI ---
st.sidebar.header("Impostazioni Output")
output_format = st.sidebar.selectbox("Formato di esportazione", ["JSON", "CSV", "XLSX"])

# --- CARICAMENTO FILE ---
uploaded_file = st.file_uploader("Scegli un file", type=["csv", "xlsx", "xls"])

if uploaded_file is not None:
    st.subheader("👀 Anteprima Dati Originali")

    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file, sep=';', engine='python')
    else:
        df = pd.read_excel(uploaded_file)

    st.dataframe(df.head(10))

    if st.button("✨ Pulisci i Dati"):
        with st.spinner('Pulizia in corso...'):
            df_clean = df.copy()
            df_clean.columns = df_clean.columns.str.strip()
            df_clean.dropna(how='all', inplace=True)
            df_clean.drop_duplicates(inplace=True)
            df_clean = df_clean.applymap(lambda x: x.strip() if isinstance(x, str) else x)

            st.success("✅ Pulizia completata!")
            st.subheader("📊 Dati Puliti")
            st.dataframe(df_clean.head(10))

            # --- LOGICA DI DOWNLOAD ---
            if output_format == "JSON":
                result = df_clean.to_json(orient='records', indent=4, force_ascii=False)
                st.download_button("⬇️ Scarica JSON", result, "data_clean.json", "application/json")

            elif output_format == "CSV":
                result = df_clean.to_csv(index=False, sep=';').encode('utf-8-sig')
                st.download_button("⬇️ Scarica CSV", result, "data_clean.csv", "text/csv")

            elif output_format == "XLSX":
                buffer = io.BytesIO()
                with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                    df_clean.to_excel(writer, index=False, sheet_name='Dati Puliti')
                result = buffer.getvalue()
                st.download_button("⬇️ Scarica XLSX", result, "data_clean.xlsx",
                                   "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")