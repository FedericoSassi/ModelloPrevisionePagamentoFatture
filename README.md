Il progetto è stato sviluppato durante il Master in Data Science ( [Attestato](https://www.linkedin.com/in/federico-sassi/overlay/1635492119523/single-media-viewer/) ) erogato da [Neural Academy](https://www.linkedin.com/school/neuralacademy/)

# Il problema e il quadro generale

L'azienda ha la necessità di prevedere la solvibilità delle fatture emesse per i clienti industriali a cui fornisce la corrente Elettrica e il GAS.
Una fattura scaduta con un saldo negativo indica la morosità del cliente.
Questa previsione si rende necessaria per organizzare le attività future del reparto crediti.

## Obiettivo: costruire un modello preddittivo che sia di supporto al cliente

Considerare un cliente moroso (CMOR) se l’ultima bolletta scaduta non è stata ancora saldata.

Alcune possibilità di modalità di lavoro:

* costruire un modello che classifichi il singolo cliente.
* costruire un modello che classifichi le singole fatture

## Descrizioni dei dataset

Le fonti di dati che verranno usate sono due, la prima proviene da CERVED e descrive lo stato dell'azienda cliente con le relative informazioni sulla sua solvibilità; il secondo set di dati proviene dall'azienda e rappresenta l'elenco delle fatture emesse nell'anno 2021 e 2022 per ogni cliente in oggetto.

### Descrizione Dati Cerved

I dati provenienti da Cerved si trovano nel file denominato DatiCerved.csv, di seguito una descrizione delle Feature in esso.

- <b>Codice Cliente</b> *[Stringa]*: codice univoco che identifica il cliente
- <b>Natura Giuridica</b> *[Stringa]*: sigla della natura giuridica del cliente
- <b>Provincia</b> *[Stringa]*: provincia in cui il cliente ha sede
- <b>Codice Istat</b> *[Stringa]*: codice istat del cliente
- <b>Fido payline</b> *[int]*: fido bancario massimo associato al cliente
- <b>Decisione</b> *[Stringa]*: decisione sul fido payline
- <b>Valutazione Tempi Pagamento</b> *[Stringa]*: situazione descrittiva sulla situazione dei pagamenti
- <b>Giorni Pattuiti</b> *[Int]*: Giorni medi pattuiti per i pagamenti da parte del cliente
- <b>Giorni Ritardo</b> *[Int]*: Giorni medi di ritardo sui pagamenti da parte del cliente
- <b>Fatturato</b> *[Float]*: Fatturato annuo del cliente
- <b>Fatturato Mese</b> *[Float]*: fatturato mensile del cliente
- <b>Classe rischio</b> *[Int]*: identificativo della classe di rischio
- <b>Classe rischio descrizione</b> *[Stringa]*: descrizione identificativo della classe di rischio

### Descrizione Dati Azienda
I dati propri dell'azienda cliente si trovano nel file denominato DatiAzienda.csv, di seguito una descrizione delle Feature in esso.

- <b>Codice Cliente</b> *[Stringa]*: codice univoco che identifica il cliente
- <b>Anno Documento</b> *[Stringa]*: anno di emissione della fattura
- <b>Numero Documento</b> *[Stringa]*: numero progressivo della fattura
- <b>Servizio</b> *[Stringa]*: servizio associato alla fattura (GA = Gas; EE = Energia Elettrica)
- <b>Scadenza Fattura</b> *[TimeStamp]*: data scadenza fattura / pagamento
- <b>Importo Fattura</b> *[Float]*: Importo della fattura
- <b>Modalità Pagamento</b> *[Stringa]*: Tipologia di pagamento associato al cliente
- <b>Descrizione Pagamento</b> *[Stringa]*: descrizione tipologia di pagamento associato al cliente
- <b>Importo incasso</b> *[TimeStamp]*: importo incassato sulla fattura
- <b>Saldo</b> *[Float]*: Saldo totale della fattura (Importo - Incasso)
