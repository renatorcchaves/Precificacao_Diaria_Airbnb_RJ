#!/usr/bin/env python
# coding: utf-8

# In[2]:

import pandas as pd
import streamlit as st
import joblib

# In[5]:

dados = pd.read_csv('../dados/dados_finais.csv')

# In[6]:

ordem_colunas_modelo = list(dados.columns)[1:-1]


x_numericos = {'latitude': 0, 'longitude': 0, 'accommodates': 0, 'bathrooms': 0, 'bedrooms': 0, 'beds': 0, 'extra_people': 0, 'host_listings_count': 0, 
               'minimum_nights': 0, 'ano': 0, 'mes': 0, 'n_amenities': 0}

x_tf = {'host_is_superhost': 0, 'instant_bookable': 0, 'is_business_travel_ready': 0 }

x_listas = {'property_type': ['Apartment', 'House', 'Outros'], 
            'room_type': ['Entire home/apt', 'Outros'], 
            'cancellation_policy': ['flexible', 'moderate', 'Strict**']
           }

dicionario = {}
for item in x_listas:
    for valor in x_listas[item]:
        dicionario[f'{item}_{valor}'] = 0        

print(dicionario)

# In[7]:


for item in x_numericos:
    if item in ('latitude', 'longitude'):
        valor = st.number_input(f'{item}', step=0.00001, value=float(0), format="%.5f")                  
    elif item == 'extra_people':
        valor = st.number_input(f'{item}', step=0.01, value=0.0)
    else: 
        valor = st.number_input(f'{item}', step=1, value=0) 
    
    x_numericos[item] = valor

for item in x_tf:
    valor = st.selectbox(f'{item}', ('Sim', 'Não'))
    if valor == "Sim":
        x_tf[item] = 1
    else:
        x_tf[item] = 0

for item in x_listas: 
    valor = st.selectbox(f'{item}', x_listas[item])
    dicionario[f"{item}_{valor}"] = 1


# In[8]:

botao = st.button('Prever valor do imóvel')

if botao:
    
    dicionario.update(x_numericos)                     
    dicionario.update(x_tf)                            
    
    valores_x = pd.DataFrame(dicionario, index=[0])
    valores_x = valores_x[ordem_colunas_modelo]        
    
    modelo = joblib.load('../modelos/modelo_extratrees.joblib')
    preco = modelo.predict(valores_x)

    st.write("O valor da diária imóvel será de preco: R$ {:.2f}".format(preco[0]))
