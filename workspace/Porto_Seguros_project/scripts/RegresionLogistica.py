# =============================================================================
# =============================================================================
# =============================================================================
# ---------------   LOGISTIC REGRESSION   ----------------------------------
# =============================================================================
# =============================================================================

def RegresionLogistica(X_train, y_train, X_test, y_test):
    clf = LogisticRegression(random_state=0, solver='lbfgs',n_jobs=-1, max_iter=200)
    clf.get_params()
    clf=clf.fit(X_train,y_train)
    print("----- Training Done -----")
    betas=clf.coef_
    alfa=clf.intercept_
    variables=X_train.columns.values
    coeficientes= list(zip(variables, betas[0]))
    print("Alfa=",alfa,"\n","Betas=",coeficientes)
    
    y_pred=clf.predict(X_test)
    y_probs=clf.predict_proba(X_test)
    y_probs=y_probs[:,1]

    #METRICS
    roc_auc=roc_auc_score(y_test, y_probs) 
    GINI = (2 * roc_auc) - 1 
    print ("\nLogistic Regresion --------->")
    print("roc_auc=%.5f\nGini=%.5f"
          % (roc_auc, GINI))
    
    y_train_probs=clf.predict_proba(X_train)
    y_train_probs=y_train_probs[:,1]
    
    return y_train_probs, y_probs
    

    
def RegresionLogisticaEnsemble(X_train, y_train, X_test, y_test):
    clf = LogisticRegression(random_state=0, solver='lbfgs',n_jobs=-1, max_iter=200)
    clf.get_params()
    clf=clf.fit(X_train,y_train)
    print("----- Training Done -----")
    betas=clf.coef_
    alfa=clf.intercept_
    variables=X_train.columns.values
    coeficientes= list(zip(variables, betas[0]))
    print("Alfa=",alfa,"\n", "Betas=",coeficientes)
    
    y_probs=clf.predict_proba(X_test)
    y_probs=y_probs[:,1]
    
    #METRICS
    roc_auc=roc_auc_score(y_test, y_probs) 
    GINI = (2 * roc_auc) - 1 
    print("Ensemble Logistic Regression ------->")
    print("\nroc_auc=%.5f\nGini=%.5f" % (roc_auc, GINI))
