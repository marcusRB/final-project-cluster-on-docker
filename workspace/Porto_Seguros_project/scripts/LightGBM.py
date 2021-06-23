# =============================================================================
# =============================================================================
# =============================================================================
# --------------------   LIGHTGBM  -------------------------------------------
# =============================================================================
# =============================================================================

def LightGBM(X_train, X_test, y_train, y_test):
    
    LGBM = lgb.LGBMClassifier()
    LGBM.get_params()
    min_child_samples=[10,20]
    min_child_weight=[1,100]
    num_leaves=[30]
    params={'boosting_type': ['gbdt'],
             'class_weight': [None],
             'colsample_bytree': [1.0],
             'importance_type': ['split'],
             'learning_rate': [0.1],
             'max_depth': [-1],
             'min_child_samples': [20],
             'min_child_weight': [0.001],
             'min_split_gain': [0.0],
             'n_estimators': [100],
             'n_jobs': [-1],
             'num_leaves': [31],
             'objective': [None],
             'random_state': [None],
             'reg_alpha': [0.0],
             'reg_lambda': [0.0],
             'silent': [True],
             'subsample': [1.0],
             'subsample_for_bin': [200000],
             'subsample_freq': [0]}

    gsearch = GridSearchCV(estimator = LGBM, 
                           param_grid=params, 
                           scoring="roc_auc",
                           n_jobs=4,
                           cv=5)
    
    lgb_model = gsearch.fit(X_train,y_train)
    print("----- Training Done -----")
    print("best parametres:\n",lgb_model.best_params_)
    y_probs=lgb_model.predict_proba(X_test)
    y_probs=y_probs[:,1]
    
    #METRICS
    roc_auc=roc_auc_score(y_test, y_probs) 
    GINI = (2 * roc_auc) - 1
    print("\nLightGBM ------------>")
    print("roc_auc=%.5f\nGini=%.5f"
          % (roc_auc, GINI))
    
    y_train_probs=lgb_model.predict_proba(X_train)
    y_train_probs=y_train_probs[:,1]
    return y_train_probs, y_probs