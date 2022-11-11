"""

    Pulizia dei dataset e creazione
    del dataset da lavorare

"""

# importazione librerie
import pandas as pd
import numpy as np

# Dichiarazione type per le colonne del dataset di CERVED

print('--- Carico il dataset Cerved ---')

dtype_Cerved = {
    'COD_CLIENTE' : 'str'
    , 'NATURA_GIURIDICA' : 'str'
    , 'PV' : 'str'
    , 'CODICE_ISTAT' : 'str'
    , 'DECISIONE' : 'str'
    , 'VALUTAZIONE_TEMPI_PAG' : 'str'
    , 'FATTURATO' : 'float'
    , 'FATTURATO_MESE' : 'float'
    , 'CLASSE_RISCHIO' : 'int'
    , 'CLASSE_RISCHIO_DESCR' : 'str'
}

# Importazione dataset CERVED
df_Cerved = pd.read_csv(
    filepath_or_buffer = 'Data/DatiCerved.csv'
    , sep = ','
    , decimal = ','
    , dtype = dtype_Cerved
    , index_col = 'COD_CLIENTE'
)

# Dichiarazione type per le colonne del dataset fornito dall'azienda

print('--- Carico il dataset Azienda ---')

dtype_Azienda = {
    'CodiceCliente' : 'str'
    , 'AnnoDocumento' : 'str'
    , 'NumeroDocumento' : 'str'
    , 'Servizio' : 'str'
    , 'ScadenzaFattura' : 'object'
    , 'ImportoFattura' : 'float'
    , 'ModPagamento' : 'str'
    , 'DescrizionePagamento' : 'str'
    , 'DataIncasso' : 'object'
    , 'ImportoIncasso' : 'float'
    , 'Saldo' : 'float'
}

# Importazione dataset Azienda
df_Azienda = pd.read_csv(
    filepath_or_buffer = 'Data/ElencoFatture.csv'
    , sep = ','
    , decimal = '.'
    , dtype = dtype_Azienda
    , index_col = 'CodiceCliente'
)

# Rimozione righe doppie

print('--- Rimuovo Duplicati ---')

df_Cerved.drop_duplicates(
    inplace=True
)

df_Azienda.drop_duplicates(
    inplace=True
)

# Gestione valori NaN

print('--- Gestione valori NaN ---')

df_Cerved['NATURA_GIURIDICA'].fillna(value='Sconosciuto', inplace=True)

df_Cerved['VALUTAZIONE_TEMPI_PAG'].fillna(value='Sconosciuto', inplace=True)

df_Cerved['PV'].fillna(value='Sconosciuto', inplace=True)

df_Cerved['CODICE_ISTAT'].fillna(value='Sconosciuto', inplace=True)

df_Cerved.dropna(subset=["DECISIONE", "GG_PATTUITI", "GG_RITARDO", "FATTURATO", "FATTURATO_MESE"], inplace=True)

df_Cerved['FIDO_PAYLINE'].fillna(value = 0.0, inplace=True)

df_Azienda['DataIncasso'].fillna(value=pd.to_datetime('today'), inplace=True)

df_Azienda['ImportoIncasso'].fillna(value=0.0, inplace=True)

# Creazione nuove colonne

print('--- Creazione nuove colonne ---')

df_Cerved['Regione'] = np.where(
    df_Cerved['PV'].isin(['AQ','TE','CH']), 'Abruzzo'
    , np.where(df_Cerved['PV'].isin(['PZ','MT']), 'Basilicata'
    , np.where(df_Cerved['PV'].isin(['KR','RC','CS']), 'Calabria'
    , np.where(df_Cerved['PV'].isin(['SA','BN','CE','AV']), 'Campania'
    , np.where(df_Cerved['PV'].isin(['PR','PC','RE','FC','BO','RN','RA','MO','FE']), 'EmiliaRomagna'
    , np.where(df_Cerved['PV'].isin(['UD','PN','GO','TS']), 'FriuliVeneziaGiulia'
    , np.where(df_Cerved['PV'].isin(['RM','FR','VT','LT']), 'Lazio'
    , np.where(df_Cerved['PV'].isin(['GE','SP','SV']), 'Liguria'
    , np.where(df_Cerved['PV'].isin(['CR','MI','LO','PV','MN','BS','NO','BI','BG','VA' 'LC' 'CO' 'MB']), 'Lombardia'
    , np.where(df_Cerved['PV'].isin(['AN','AP','MC','FM','PU']), 'Marche'
    , np.where(df_Cerved['PV'].isin(['AL','TO','AT','CN','VC']), 'Piemonte'
    , np.where(df_Cerved['PV'].isin(['FG','BA','TA']), 'Puglia'
    , np.where(df_Cerved['PV'].isin(['SS']), 'Sardegna'
    , np.where(df_Cerved['PV'].isin(['PA','ME','RG','MS','CT','AG','TP','CL']), 'Sicilia'
    , np.where(df_Cerved['PV'].isin(['FI','PI','AR','PT','LU','SI','PO']), 'Toscana'
    , np.where(df_Cerved['PV'].isin(['BZ','TN']), 'TrentinoAltoAdige'
    , np.where(df_Cerved['PV'].isin(['PG','TR']), 'Umbria'
    , np.where(df_Cerved['PV'].isin(['AO']), 'ValleDAosta'
    , np.where(df_Cerved['PV'].isin(['PD','VR','VI','TV','BL','RO','VE']), 'Veneto'
    , 'Sconosciuto'
)))))))))))))))))))

df_Azienda[['ScadenzaFattura','DataIncasso']] = df_Azienda[['ScadenzaFattura','DataIncasso']].apply(pd.to_datetime)

df_Azienda['GiorniRitardoIncasso'] = (df_Azienda['DataIncasso'] - df_Azienda['ScadenzaFattura']).dt.days

df_Azienda['ScadenzaFatturaMese'] = pd.DatetimeIndex(df_Azienda['ScadenzaFattura']).month

df_Azienda['DataIncassoMese'] = pd.DatetimeIndex(df_Azienda['DataIncasso']).month

df_Azienda['ScadenzaFatturaWeek'] = df_Azienda['ScadenzaFattura'].dt.isocalendar().week

df_Azienda['DataIncassoWeek'] = df_Azienda['DataIncasso'].dt.isocalendar().week

df_Azienda['ChiaveFattura'] = df_Azienda['AnnoDocumento'].astype('str') + '-' + df_Azienda['NumeroDocumento'].astype('str')

def CMOR(Saldo):
    if Saldo < 0:
        return 1
    else:
        return 0

df_Azienda['CMOR'] = df_Azienda['Saldo'].apply(lambda x: CMOR(x))

df_Azienda['CMORStorico'] = np.where(df_Azienda['GiorniRitardoIncasso'] > 0,1,0)

# Colonna Rolling

print(' --- Inizio colonna Rolling ---')

df_Azienda_Rolling = pd.DataFrame()

for cliente in df_Azienda.index.unique():
    df_cliente = df_Azienda[df_Azienda.index == cliente][['ScadenzaFattura','CMORStorico']].reset_index()
    
    df_cliente = df_cliente.groupby(by=['CodiceCliente','ScadenzaFattura']).sum().reset_index()
  
    df_cliente_rolling = df_cliente[['ScadenzaFattura','CMORStorico']]
    
    df_cliente_rolling = df_cliente_rolling.rolling('120D',on='ScadenzaFattura').sum()
    
    df_totale = pd.merge(df_cliente, df_cliente_rolling, how = 'left', left_on = 'ScadenzaFattura', right_on='ScadenzaFattura')
    
    df_totale = df_totale.drop(columns = ['CMORStorico_x'])
    
    df_Azienda_Rolling = pd.concat([df_Azienda_Rolling, df_totale],ignore_index=True)

df_Azienda = pd.merge(
    left = df_Azienda
    , right = df_Azienda_Rolling
    , how = 'left'
    , left_on = ['CodiceCliente', 'ScadenzaFattura']
    , right_on = ['CodiceCliente', 'ScadenzaFattura']
)

df_Azienda.rename(columns = {'CMORStorico_y':'CMORRolling'}, inplace=True)

# Unione dei dataframe

print('--- Marge Dataframe ---')

df = pd.merge(
    left = df_Azienda
    , right = df_Cerved
    , how = 'inner'
    , left_on = 'CodiceCliente'
    , right_index = True
)

# Rinomino le colonne

print('--- Rinomino le colonne ---')

NuovoNomeColonne = {
    'NATURA_GIURIDICA' : 'NaturaGiuridica'
    , 'PV' : 'Pv'
    , 'CODICE_ISTAT' : 'CodiceIstat'
    , 'FIDO_PAYLINE' : 'FidoPayline'
    , 'DECISIONE' : 'Decisione'
    , 'VALUTAZIONE_TEMPI_PAG' : 'ValutazioneTempiPagamento'
    , 'GG_PATTUITI' : 'GiorniPattuiti'
    , 'GG_RITARDO' : 'GiorniRitardo'
    , 'FATTURATO' : 'Fatturato'
    , 'FATTURATO_MESE' : 'FatturatoMese'
    , 'CLASSE_RISCHIO' : 'ClasseRischio'
    , 'CLASSE_RISCHIO_DESCR' : 'ClasseRischioDescrizione'
}

df.rename(
    columns = NuovoNomeColonne
    , inplace=True
)

# Esporto il csv definitivo

print('--- Esporto CSV ---')

df.to_csv(
    path_or_buf = 'Data/DatiDefinitivi.csv'
    , index= False
)