# Sviluppo di un Modello di Regressione e Web App per la Predizione dei Prezzi Immobiliari
Progetto Esame Sistemi Informativi a.a. 2024-2025, D'Angelo Mattia William.

## 📊 Descrizione dataset
Il dataset contiene dati relativi a degli immobili. In particolare, le covariate (features) presenti sono:
- **Latitudine**;
- **Longitudine**;
- **Età dell'immobile**;
- **Vicinanza alla stazione MRT (Singapore)**;
- **Numero di minimarket vicini**;
- **Prezzo per ogni unità di area** (variabile target).

L'obiettivo è creare un modello per prevedere il prezzo sulla base delle altre covariate.

## 📈 Descrizione modello
Ho deciso di utilizzare un modello Random Forest Regressor perché risulta essere, solitamente, molto accurato nelle previsioni e non ha bisogno di particolari strategie di preprocessing.
Ho deciso di creare 3 modelli diversi:
- il primo, in cui l'utente ha la possibilità di inserire solamente Latitudine e Longitudine;
- il secondo, nel quale l'utente ha la possibilità di inserire età della casa, vicinanza alla stazione MRT e numero di minimarket vicini;
- il terzo, in cui l'utente ha la possibilità di inserire informazioni su tutte le variabili.

I modelli sono stati allenati tutti con Random Forest Regressor (opzione di default è il tuning predefinito dei parametri) e sono stati allenati sulle relative covariate, che deve inserire l'utente (il primo modello è stato allenato solo su Latitudine e Longitudine, il secondo solo su Età della casa, Vicinanza alla stazione, Numero di market vicini...).

## 📝 Istruzioni per eseguire l'applicazione
Una volta scaricata ed estratta la cartella del progetto, aprire un IDE come VsCode. Per generare i modelli sarà sufficiente eseguire il file python run_pipeline.py (comando --> python run_pipeline.py) dopo aver impostato come cartella di lavoro "/scripts".

Una volta generati i modelli, per avviare l'applicazione sarà sufficiente eseguire il file python UI.py (comando --> streamlit run ui.py) sempre dopo aver impostato come cartella di lavoro "/scripts".

Qui, bisognerà decidere quali variabili inserire (e quindi, indirettamente, quale modello utilizzare), immetere i dati e premere "Prevedi costo casa" per avere la previsione.

Per qualunque cosa, segnalare, grazie!