# =============================================================================
# =============================================================================
# =============================================================================
# ---------------   PLOTS   ----------------------------------
# =============================================================================
# =============================================================================

def histograma_bin(variable):
    plot=sns.countplot(variable,palette="ch:2.5,-.2,dark=.3")
    plt.show()
    
def histograma_cat(variable):  
    if "miss" in variable.unique():
        clases=list(variable.value_counts().index)
        clases.remove("miss")
        clases=sorted(clases,key=lambda x: int(x))
        clases.append("miss")     
    else:
        clases=sorted(variable.unique(),key=lambda x: int(x))  
    plot=sns.countplot(variable,order=clases)
    plt.show()

def histograma(variable):
    plot=sns.distplot(variable,kde=False)
    plt.show()

def Histogramas(X,y):
    variables=X.columns
    cat_variables=[obj for obj in variables if "cat" in obj]
    bin_variables=[obj for obj in variables if "bin" in obj]
    cont_variables=[obj for obj in variables if "bin" not in obj and "cat" not in obj]

    #target
    histograma_bin(y)
    #binarias
    for element in bin_variables:
        histograma_bin(X[element])
    #categoricas
    for element in cat_variables:
        histograma_cat(X[element])
    #numericas
    for element in cont_variables:
        histograma(X[element])
    
    
def target_bin(variable,dt): 
    plot=sns.catplot(x=variable,y="target",kind="bar",data=dt,capsize=.1)
    plt.gca().set_yticklabels(['{:.1f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.show() 
    
def target_cat(variable,dt): 
    if "miss" in dt[variable].unique():
        clases=list(dt[variable].value_counts().index)
        clases.remove("miss")
        clases=sorted(clases,key=lambda x: int(x))
        clases.append("miss")     
    else:
        clases=sorted(dt[variable].unique(),key=lambda x: int(x))  
    plot=sns.catplot(x=variable,y="target",kind="bar",data=dt,capsize=.1,order=clases)
    plt.gca().set_yticklabels(['{:.1f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.show() 

def target_disc(variable,dt): 
    plot=sns.catplot(x=variable,y="target",kind="point",data=dt,capsize=.1,join=False,aspect=1.5)
    plt.gca().set_yticklabels(['{:.1f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.show()
          
def target_cont(variable,dt): 
    clases=list(dt[variable].value_counts().index)
    clases=sorted(clases)
    plot=sns.catplot(x=variable,y="target",kind="bar",data=dt,capsize=.1,aspect=1.5,order=clases)
    plt.gca().set_yticklabels(['{:.1f}%'.format(x*100) for x in plt.gca().get_yticks()])
    plt.show() 

def Bivariantes(X,dt):
    variables=X.columns
    cat_variables=[obj for obj in variables if "cat" in obj]
    bin_variables=[obj for obj in variables if "bin" in obj]
    cont_variables=[obj for obj in variables if "bin" not in obj and "cat" not in obj]
    variables_cont=["ps_reg_01","ps_reg_02","ps_reg_03","ps_car_12","ps_car_13","ps_car_14","ps_car_15","ps_calc_10", "ps_calc_11","ps_calc_14"]
    discretas=["ps_reg_01","ps_reg_02","ps_car_15","ps_calc_10","ps_calc_11","ps_calc_14"]
    continuas=["ps_reg_03","ps_car_12","ps_car_13","ps_car_14",]
    variables_disc=[label for label in cont_variables if label not in variables_cont]
    #binarias
    for element in bin_variables:
        target_bin(element,dt)
    #categoricas
    for element in cat_variables:
        target_cat(element,dt)
    #numericas,separadas en continuas y discretas
    for element in continuas:   
        rango=dt[element].max()-dt[element].min()
        intervalo=rango/20
        bins=[intervalo*i +dt[element].min() for i in range(1,21)]
        binis=[round(item,2) for item in bins]
        dt[element]=pd.cut(dt[element], 20,labels=binis)
        
    for element in variables_disc:
        target_disc(element,dt)   
    for element in discretas:
        target_disc(element,dt)   
    for element in continuas:
        target_cont(element,dt)    


def Correlation (X):
    corr = X.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(30, 30))
        ax = sns.heatmap(corr, annot = True,mask=mask, vmax=.3,fmt='.2f', square=True) 
        
        


def Roc_Auc(y_test, y_probs, model): 
    fpr, tpr, threshold = metrics.roc_curve(y_test, y_probs) 
    roc_auc = metrics.auc(fpr, tpr) 
    plt.title(model+' Receiver Operating Characteristic')
    plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
    plt.legend(loc = 'lower right')
    plt.plot([0, 1], [0, 1],'r--')
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    plt.ylabel('True Positive Rate')
    plt.xlabel('False Positive Rate')
    plt.show()

def Precission_Recall(y_test, y_probs, model):
    precision, recall, thresholds = precision_recall_curve(y_test, y_probs)
    no_skill = len(y_test[y_test==1]) / len(y_test) 
    plt.plot([0,1], [no_skill,no_skill], linestyle='--', label='No Skill')
    plt.plot(recall, precision, marker='.', label=model,linewidth=0.1,markersize=0.1)
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.legend()
    plt.show()

def mostrar_resultados(y_test, y_pred, model):
    conf_matrix = confusion_matrix(y_test, y_pred)   
    plt.figure(figsize=(5, 5))
    sns.heatmap(conf_matrix, xticklabels=["0","1"], yticklabels=["0","1"], annot=True, fmt="d",cmap="BuPu");
    plt.title(model+" Confusion matrix")
    plt.ylabel('True class')
    plt.xlabel('Predicted class')
    plt.show()
    print ("\n******************"+model+"**********************")
    print (classification_report(y_test, y_pred))  
 


