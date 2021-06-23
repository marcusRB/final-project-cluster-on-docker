# =============================================================================
# =============================================================================
# =============================================================================
# --------------------   RANDOM FOREST  -------------------------------------------
# =============================================================================
# =============================================================================

def RandomForest(X_train, X_test, y_train, y_test): 
                     
    RF = RandomForestClassifier(random_state=0)
    RF.get_params()
    
    params={'ccp_alpha': [0.0],
             'class_weight': ["balanced"],
             'criterion': ['gini'],
             'max_depth': [8],
             'max_features': [0.2],
             'n_jobs': [-1],
             'max_leaf_nodes': [None],
             'max_samples': [None],
              'min_impurity_decrease': [0.0],
              'min_impurity_split': [None],
              'min_samples_leaf': [1],
              'min_samples_split': [2],
              'min_weight_fraction_leaf': [0.0],
              'n_estimators': [150],
              'oob_score': [False],
              'random_state': [0],
              'verbose': [0],
              'warm_start': [False]}
    
    scoring = 'roc_auc'
    grid_solver = GridSearchCV(estimator = RF, 
                        param_grid = params, 
                        scoring = scoring,
                        cv = 5,
                        n_jobs=-1)
    
    model_result = grid_solver.fit(X_train,y_train)
    print("----- Training Done -----")
    print("best parametres:\n",model_result.best_params_) 
    y_probs=model_result.predict_proba(X_test)
    y_probs=y_probs[:,1]
    
    #METRICS
    roc_auc=roc_auc_score(y_test, y_probs) 
    GINI = (2 * roc_auc) - 1 
    print("\nRandom Forest ------------>")
    print("roc_auc=%.5f\nGini=%.5f" % (roc_auc, GINI))
    
    y_train_probs=model_result.predict_proba(X_train)
    y_train_probs=y_train_probs[:,1]
    return y_train_probs, y_probs
    