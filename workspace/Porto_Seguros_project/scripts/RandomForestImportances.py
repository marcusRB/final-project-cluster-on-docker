# =============================================================================
# =============================================================================
# =============================================================================
# ---------------   RANDOM FOREST IMPORTANCES   ----------------------------------
# =============================================================================
# =============================================================================

def RandomForestImportances(X, y, n, maxdepth=8, minsamplesleaf=4, maxfeatures=0.2):                      
    RF = RandomForestClassifier(criterion="gini", max_depth=maxdepth, 
                                min_samples_leaf=minsamplesleaf,max_features=maxfeatures,
                                n_jobs=-1,random_state=0)
    RF.fit(X, y)
    print("----- Training Done -----")
    variables=X.columns.values
    print ("Variables ordenadas por importancia:\n **************************************************")    
    print (sorted(zip(map(lambda x: round(x, 4), RF.feature_importances_), variables), reverse=True))
    
    #seleccionamos las primeras 30
    importances=sorted(zip(map(lambda x: round(x, 4), RF.feature_importances_), variables), reverse=True)
    features=importances[:n]
    fi=pd.DataFrame(features,columns=["Importance","Feature"])
    
    #horizontal bar plot
    plot = sns.catplot(x="Importance", y="Feature", kind="bar", data=fi ,capsize=.1,orient="h", height=10, palette= "Blues_d")
    plt.show()
    
    return fi["Feature"]
    
    
    
    
