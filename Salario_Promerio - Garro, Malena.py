#!/usr/bin/env python
# coding: utf-8

# In[1]:


#PRIMER PASO: IMPORTAR LIBERIAS

import pandas as pd


# In[2]:


#SEGUNDO PASO: IMPORTAR BASE DE DATOS DE ARCHIVO EXCEL
#donde debemos crear una variable en el que se almacenara ducho archivo

basedatos=pd.read_excel(r'C:\Users\garro\OneDrive\Escritorio\DATA SCIENCE\TRABAJO PRACTICO\SalarioPromedio.xlsx', sheet_name='empresas')


# In[3]:


#TERCER CASO: VERFICAMOS SI SE REALIZÓ LA CARGA A PARTIR DE M0STRAR LOS PRIMEROS CINCO DATOS
#(donde la primer fila son los nombres de las columnas, por lo que se mstraran cuatro filas con datos)

basedatos.head()


# Este dataset contiene los datos de los salarios en la Argentina desde el 2014 hasta 2022, mes a mes. Presenta los siguientes datos: 
#        - nombre de provincia 
#        - ID_provincia (valor único que se le otorga a cada provincia/CABA) 
#        - nombre de departamento 
#        - ID_departamente (valor único que se le entrega a cada departamento)
#        - de la columna 5 a última se encuentran los salarios desde el 2014 hasta 2022 
#       
#   Al momento de realizar un análisis se podría hacer una limpieza de datos y poder hacer diferentes tablas relacionando algunos datos para evitar las repeticiones. Por ejemplo: se puede eliminar los datos de los nombres de provincia y generar una segunda tabla que relacione el ID_provincia con su respectivo nombre, como tambien eliminar el nombre del departamento y crear una tercera tabla para relacionar los nombres de departamentos con su respectiva ID. Esto permite reducir que se repitan los datos, y por lo tanto, reducir la memoria. Por lo tanto, los datos más importantes son ID_provincia, ID_departamento y los salarios.
