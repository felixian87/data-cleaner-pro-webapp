# Data Cleaner Pro – Web App

Web app Streamlit per pulire rapidamente file CSV ed Excel e scaricare i dati puliti in vari formati (JSON, CSV, XLSX).[file:2]

---

## 1. Cos'è e a cosa serve

Questo progetto è una **webapp interattiva** sviluppata in Python con Streamlit che ti permette di:
- caricare un file di dati “sporco” (CSV o Excel)
- visualizzare un’anteprima delle prime righe
- applicare una serie di pulizie di base
- scaricare il risultato pulito in JSON, CSV o XLSX.[file:2]

È pensata per chi lavora spesso con file esportati da gestionali, marketplace, CRM o altri sistemi che generano CSV/Excel pieni di righe vuote, duplicati o spazi indesiderati.

---

## 2. Cosa fa il codice

Nel file `appDC.py` l’app esegue questi passaggi principali:[file:2]

1. Imposta la pagina Streamlit con titolo “Data Cleaner Pro” e layout wide.
2. Mostra una sidebar con la scelta del **formato di esportazione**: `JSON`, `CSV`, `XLSX`.
3. Permette di caricare un file tramite `st.file_uploader`, accettando estensioni `csv`, `xlsx`, `xls`.
4. Se il file è CSV, lo legge con `pandas.read_csv` usando `;` come separatore; altrimenti usa `pandas.read_excel`.
5. Visualizza l’**anteprima** delle prime 10 righe del dataset originale (`st.dataframe(df.head(10))`).
6. Quando clicchi su “✨ Pulisci i Dati”:
   - copia il DataFrame originale
   - rimuove spazi iniziali/finali dai nomi colonna
   - elimina le righe completamente vuote (`dropna(how='all')`)
   - elimina i duplicati (`drop_duplicates()`)
   - toglie spazi iniziali/finali da tutte le celle di tipo stringa (`applymap(lambda x: x.strip() ...)`).
7. Mostra un messaggio di successo e l’anteprima dei **dati puliti** (`df_clean.head(10)`).
8. In base al formato scelto:
   - **JSON**: `df_clean.to_json(orient='records', indent=4, force_ascii=False)` e pulsante `Scarica JSON`
   - **CSV**: `df_clean.to_csv(index=False, sep=';').encode('utf-8-sig')` e pulsante `Scarica CSV`
   - **XLSX**: usa `io.BytesIO()` e `pandas.ExcelWriter(engine='openpyxl')` per creare `data_clean.xlsx` scaricabile.[file:2]

---

## 3. Tipi di file supportati

**Input:**
- CSV (`.csv`) con separatore `;`
- Excel (`.xlsx`, `.xls`).[file:2]

**Output:**
- JSON (`data_clean.json`) – record orientato
- CSV (`data_clean.csv`) – separatore `;`
- XLSX (`data_clean.xlsx`) – foglio “Dati Puliti”.[file:2]

---

## 4. Linguaggi e librerie

- **Linguaggio:** Python
- **Librerie principali:**[file:2]
  - `streamlit` – interfaccia web, layout, caricamento file
  - `pandas` – lettura, manipolazione e pulizia dei dati
  - `openpyxl` – scrittura file Excel tramite `pandas.ExcelWriter`
  - `io` – buffer in memoria per la creazione del file XLSX

---

## 5. A chi è utile

Questa web app può servire a:
- analisti dati che ricevono spesso CSV/Excel sporchi
- freelance che gestiscono esportazioni da marketplace, CRM, ERP, ecc.
- studenti o data enthusiast che vogliono un tool veloce per ripulire dati tabellari
- chiunque non voglia scrivere codice ma abbia bisogno di una pulizia base ripetibile.

---

## 6. Installazione (completa, passo per passo)

### 6.1. Prerequisiti

- Python 3.9+ installato
- `pip` disponibile nel PATH
- Git installato (se vuoi clonare/gestire la repo da terminale).[web:3]

---

### 6.2. Clonare o scaricare il progetto

Se la repository è su GitHub:

```bash
git clone https://github.com/<TUO_USERNAME>/data-cleaner-pro-webapp.git
cd data-cleaner-pro-webapp
