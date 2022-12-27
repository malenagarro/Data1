#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PRIMER PASO: IMPORTAR LIBERIAS

import pandas as pd


# In[2]:


#SEGUNDO PASO: IMPORTAR BASE DE DATOS DE ARCHIVO EXCEL
#donde debemos crear una variable en el que se almacenara ducho archivo

basedatos=pd.read_excel(r'C:\Users\garro\OneDrive\Escritorio\DATA SCIENCE\TRABAJO PRACTICO\ViolenciaGenero.xlsx', sheet_name='casos')


# In[4]:


#TERCER CASO: VERFICAMOS SI SE REALIZÓ LA CARGA A PARTIR DE M0STRAR LOS PRIMEROS CINCO DATOS
#(donde la primer fila son los nombres de las columnas, por lo que se mstraran cuatro filas con datos)

basedatos.head()


# Este dataset contiene los datos de llamadas que se reciben en la línea 104 informando un caso de violencia de genero. Presenta los siguientes datos: 
#                      - la fecha del llamado
#                      - provincia de residencia de la persona
#                      - género 
#                      - edad
#                      - de la columna 5 a 16 se describen el tipo de violencia que tuvo
#                      - vinculo de la persona que generó la violencia
#                      - genero de la persona que ejerció violencia
# Al momento de realizar un análisis los datos más importantes que se pueden tener en cuenta son: la provincia, edad, tipo de agresión y vinculo de la persona que se generó la violencia. Esto permitirá definir cuales son las provincias en que se genera una mayor violencia de género, cuales son las edades más afectadas y cual es el vinculo con el agresor para poder generar mayores medidas o leyes en contra de la violencia de género. 
