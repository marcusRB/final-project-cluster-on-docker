# =============================================================================
# =============================================================================
# =============================================================================
# --------------------   NEURAL NETWORK   ----------------------------------------
# =============================================================================
# =============================================================================

def NN(X_train, X_test, y_train, y_test):
    def create_model(l2=0.001):
        model = models.Sequential()
        model.add(layers.Dense(100, kernel_regularizer=regularizers.l2(l2), activation='relu', input_shape=(227,)))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(50, kernel_regularizer=regularizers.l2(l2), activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(10, kernel_regularizer=regularizers.l2(l2), activation='relu'))
        model.add(layers.Dropout(0.5))
        model.add(layers.Dense(1, activation='sigmoid'))
        model.compile(optimizer='rmsprop',
                  loss='binary_crossentropy',
                  metrics=['accuracy'])
                  
        return model
    
    model = KerasClassifier(build_fn=create_model, epochs=15, batch_size=1000, verbose=2)
    l2 = [0.0001]
    param_grid = dict(l2=l2)
    
    grid = GridSearchCV(estimator=model,
                        param_grid=param_grid,
                        n_jobs=-1,
                        scoring="roc_auc",
                        cv=2)
    
    grid_results=grid.fit(X_train,y_train)
    print("----- Training Done -----")
    print("best parametres:\n",grid_results.best_params_)
    y_probs = grid_results.predict_proba(X_test)
    y_probs=y_probs[:,1]
    
    #METRICS
    roc_auc=roc_auc_score(y_test, y_probs) 
    GINI = (2 * roc_auc) - 1 
    print("\nNeural Network ------------>")
    print("roc_auc=%.5f\nGini=%.5f"
          % (roc_auc, GINI))
    
    y_train_probs=grid_results.predict_proba(X_train)
    y_train_probs=y_train_probs[:,1]
    
    return y_train_probs, y_probs