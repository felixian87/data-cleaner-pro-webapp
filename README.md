# data-cleaner-pro-webapp
# Data Cleaner Pro – Web App

Web app Streamlit per pulire rapidamente file CSV ed Excel e scaricare i dati puliti in vari formati (JSON, CSV, XLSX).

## Cos'è e a cosa serve

Questo progetto è una **web app interattiva** sviluppata in Python con Streamlit che permette di:

- caricare un file di dati “sporco” (CSV o Excel)  
- visualizzare un’anteprima delle prime righe  
- applicare una serie di pulizie di base  
- scaricare il risultato pulito in più formati.

È pensata per chi lavora spesso con file esportati da gestionali, e-commerce, CRM o altri sistemi che generano CSV/Excel pieni di righe vuote, duplicati o spazi indesiderati.

## Cosa fa il codice

A partire dal file `appDC.py` l’app:

1. Imposta la pagina Streamlit con titolo **“Data Cleaner Pro”** e layout *wide*. [file:2]  
2. Mostra una sidebar dove puoi scegliere il **formato di esportazione**: `JSON`, `CSV` o `XLSX`. [file:2]  
3. Permette di **caricare un file** tramite `st.file_uploader`, accettando estensioni `csv`, `xlsx`, `xls`. [file:2]  
4. Se il file è CSV, lo legge con `pandas.read_csv` usando `;` come separatore; altrimenti usa `pandas.read_excel`. [file:2]  
5. Visualizza un’**anteprima** delle prime 10 righe del dataset originale. [file:2]  
6. Quando clicchi su “✨ Pulisci i Dati”, esegue queste pulizie sul DataFrame: [file:2]  
   - copia i dati originali  
   - rimuove spazi iniziali/finali dai nomi colonna  
   - elimina le righe completamente vuote (`dropna(how='all')`)  
   - elimina i duplicati (`drop_duplicates()`)  
   - rimuove spazi iniziali/finali da tutte le celle di tipo stringa (`applymap` con `strip`)  
7. Mostra un messaggio di successo e un’anteprima delle prime 10 righe dei **dati puliti**. [file:2]  
8. In base al formato scelto nella sidebar, prepara il download: [file:2]  
   - **JSON**: esporta con `df_clean.to_json(orient='records', indent=4, force_ascii=False)` e fornisce un pulsante “Scarica JSON”.  
   - **CSV**: esporta con `df_clean.to_csv(index=False, sep=';')` codificato in `utf-8-sig` e fornisce “Scarica CSV”.  
   - **XLSX**: usa un buffer `io.BytesIO()` e `pandas.ExcelWriter` con engine `openpyxl` per salvare il foglio *Dati Puliti*, poi fornisce “Scarica XLSX”.  

## Tipi di file che può manipolare

In input:

- File **CSV** (`.csv`) con separatore `;`  
- File **Excel** (`.xlsx`, `.xls`)

In output:

- **JSON** (`data_clean.json`), record-orientato  
- **CSV** (`data_clean.csv`) con separatore `;`  
- **XLSX** (`data_clean.xlsx`) con un foglio chiamato “Dati Puliti”  

Tutti i formati di output sono generati a partire dal DataFrame pulito creato in memoria. [file:2]

## Linguaggi e librerie usati

- **Linguaggio**: Python  
- **Librerie principali**: [file:2]  
  - `streamlit` – interfaccia web e caricamento file  
  - `pandas` – lettura, manipolazione e pulizia dei dati  
  - `openpyxl` – salvataggio dei dati puliti in formato Excel (tramite `pandas.ExcelWriter`)  
  - `io` – gestione buffer in memoria per la creazione del file XLSX

## A chi può essere utile

Questa web app può essere utile a:

- analisti dati che ricevono spesso CSV/Excel sporchi  
- freelance che gestiscono esportazioni da marketplace, CRM, ERP, ecc.  
- studenti o data enthusiast che vogliono un tool veloce per pulire dati prima di analizzarli  
- chiunque non voglia scrivere codice ma abbia bisogno di una pulizia base ripetibile su file tabellari.

## Installazione

Prerequisiti:

- Python 3.9+ installato nel sistema  
- `pip` disponibile nel PATH

1. Clona o scarica questa repository:

```bash
git clone https://github.com/<TUO_USERNAME>/data-cleaner-pro-webapp.git
cd data-cleaner-pro-webapp
