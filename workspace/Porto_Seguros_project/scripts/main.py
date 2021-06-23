import os
os.chdir("scripts/")
# =============================================================================
# =============================================================================

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt 
import statsmodels.api as sm
from sklearn.metrics import precision_recall_curve
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import lightgbm as lgb
import scipy
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import roc_auc_score
from keras.wrappers.scikit_learn import KerasClassifier
from keras import models
from keras import layers
from keras import regularizers
from keras import losses
from keras import metrics as mtrc
from keras import optimizers



exec(open("Data.py").read())
exec(open("Missings.py").read())
exec(open("Plots.py").read())
exec(open("Split.py").read())
exec(open("RandomForestImportances.py").read())
exec(open("RegresionLogistica.py").read())
exec(open("LightGBM.py").read())
exec(open("NN.py").read())
exec(open("RandomForest.py").read())
exec(open("Threshold.py").read())


# =============================================================================
# =======================INSPECTION=========================================

data=Data(path+"/Data/")
dt=Missings(data)
y=dt["target"]
X=dt.drop(['id', 'target'],axis=1)

Histogramas(X,y)
Bivariantes(X,dt)
Correlation(X)

X=pd.get_dummies(X)  
variables=RandomForestImportances(X, y, 35)

# =============================================================================
# =======================MODELS=========================================

X_train, X_test, y_train, y_test = Split(X,y)  

RL_train_probs,RL_test_probs = RegresionLogistica(X_train, y_train, X_test, y_test)
LGBM_train_probs, LGBM_test_probs = LightGBM(X_train, X_test, y_train, y_test)
NN_train_probs, NN_test_probs = NN(X_train, X_test, y_train, y_test)
RF_train_probs, RF_test_probs = RandomForest(X_train, X_test, y_train, y_test)

# logistic regression ensemble of previous models
X_train = pd.DataFrame({"RF":RF_train_probs, "NN":NN_train_probs,"LGBM":LGBM_train_probs})
X_test = pd.DataFrame({"RF":RF_test_probs, "NN":NN_test_probs,"LGBM":LGBM_test_probs})
RegresionLogisticaEnsemble(X_train, y_train, X_test, y_test)


# =============================================================================
# ==================== PREDICTION ANALYSIS ===============================

Roc_Auc(y_test,RL_test_probs, "Logistic Regression")
Precission_Recall(y_test,RL_test_probs, "Logistic Regression")
RL_test_pred = Threshold(RL_test_probs, 0.5)
mostrar_resultados(y_test, RL_test_pred, "Logistic Regression")

Roc_Auc(y_test,LGBM_test_probs, "LightGBM")
Precission_Recall(y_test,LGBM_test_probs, "LightGBM")
LGBM_test_pred = Threshold(LGBM_test_probs, 0.5)
mostrar_resultados(y_test, LGBM_test_pred, "LightGBM")

Roc_Auc(y_test,NN_test_probs, "Neural Network")
Precission_Recall(y_test,NN_test_probs, "Neural Network")
NN_test_pred = Threshold(NN_test_probs, 0.5)
mostrar_resultados(y_test, NN_test_pred, "Neural Network")

Roc_Auc(y_test,RF_test_probs, "Random Forest")
Precission_Recall(y_test,RF_test_probs, "Random Forest")
RF_test_pred = Threshold(RF_test_probs, 0.5)
mostrar_resultados(y_test, RF_test_pred, "Random Forest")

