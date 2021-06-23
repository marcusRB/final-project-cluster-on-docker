# =============================================================================
# =============================================================================
# =============================================================================
# ---------------   MISSINGS      ----------------------------------
# =============================================================================
# =============================================================================

def Missings(dataframe):
    #los missings vienen con valor = -1
    dataframe[dataframe["ps_car_12"]==-1]
    dataframe[dataframe["ps_car_11"]==-1]
    missing_car_12=dataframe[dataframe["ps_car_12"]==-1].index
    missing_car_11=dataframe[dataframe["ps_car_11"]==-1].index
    dataframe.iloc[missing_car_12]  
    dataframe.iloc[missing_car_11]
    #todos esos registros no contienen un target positivo, al ser una cantidad muy pequeña de ellos, se pueden eliminar
    dataframe=dataframe.drop(missing_car_12,axis=0)
    dataframe=dataframe.drop(missing_car_11,axis=0)
    
    #remplazamiento de  missings (-1) por string miss y conversion a tipo string las variables categoricas
    variables=dataframe.columns
    cat_variables=[obj for obj in variables if "cat" in obj]
    bin_variables=[obj for obj in variables if "bin" in obj]
    dataframe[cat_variables]=dataframe[cat_variables].replace({-1:"miss"})
    
    dataframe[cat_variables]=dataframe[cat_variables].astype(str)

    
    #missings continuas
    cont_variables=[obj for obj in variables if ("cat" not in obj) and ("bin" not in obj) and ("targ" not in obj)and ("id" not in obj)] 
    #sustitucion de los -1 por nans para que no afecten al calculo de la mediana
    dataframe[cont_variables]=dataframe[cont_variables].replace({-1:np.nan})
    #calculo de las medianas
    median_ps_reg_03=dataframe["ps_reg_03"].median()
    median_ps_car_14=dataframe["ps_car_14"].median()
    # remplazamiento de nans por la mediana
    dataframe["ps_reg_03"]=dataframe["ps_reg_03"].fillna(median_ps_reg_03)
    dataframe["ps_car_14"]=dataframe["ps_car_14"].fillna(median_ps_car_14)
    
    return dataframe
    