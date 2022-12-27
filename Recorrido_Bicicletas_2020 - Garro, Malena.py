#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PRIMER PASO: IMPORTAR LIBERIAS

import pandas as pd


# In[2]:


#SEGUNDO PASO: IMPORTAR BASE DE DATOS DE ARCHIVO EXCEL
#donde debemos crear una variable en el que se almacenara ducho archivo

basedatos=pd.read_excel(r'C:\Users\garro\OneDrive\Escritorio\DATA SCIENCE\TRABAJO PRACTICO\ViajesBicicleta2020.xlsx', sheet_name= 'viajes')


# In[4]:


#TERCER CASO: VERFICAMOS SI SE REALIZÓ LA CARGA A PARTIR DE M0STRAR LOS PRIMEROS CINCO DATOS
#(donde la primer fila son los nombres de las columnas, por lo que se mstraran cuatro filas con datos)

basedatos.head()

Este dataset contiene los datos de los recorridos que se hicieron con las bicicletas públicas de la Ciudad de Buenos Aires en el año 2020. Presenta los siguientes datos: 
                        - ID_recorrido
                        - duración de recorrido 
                        - fecha de inicio de recorrido
                        - ID_estación_origen
                        - nombre de estación de origen
                        - dirección de estación origen (y sus coordenadas de longitud y latitud)
                        - fecha de final de recorrido
                        - ID_estación_final
                        - dirección de estación final (y sus coordenadas de longitud y latitud)
                        - ID_usuario
                        - modelo_bicicleta

Al momento de realizar un análisis se podría hacer una limpieza de datos y poder hacer diferentes tablas relacionando algunos datos para evitar las repeticiones. Por ejemplo: se puede eliminar los datos los nombre de estaciones, su dirección y coordenadas (de estaciones origen y final) y en una tabla aparte relacionarlas con su respectivo ID. Esto permite reducir que se repitan los datos, y por lo tanto, reducir la memoria. Por lo tanto, los datos más importantes son ID_recorrido, ID_estación y ID_usuario. Con estos datos se pueden realizar varios analisis, desde cuantos viajes, cuales son los recorridos más usuales y que día los usa cada usucario, hasta cuales son las estaciones más usadas. 