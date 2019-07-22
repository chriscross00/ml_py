#!/usr/bin/env python

from sklearn.datasets import load_wine
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import train_test_split
from sklearn import metrics

import numpy as np
import pandas as pd


def load_data():
	wine = load_wine()

	features, target = wine.data, wine.target
	X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.25, random_state=0)

	return X_train, X_test, y_train, y_test


def a_boost():
	clf = AdaBoostClassifier(random_state=0)

	param_grid = {'n_estimators': np.linspace(0, 100, 5),
				  'learning_rate': np.linspace(0.01, 0.1, 11)}
	
	trained_model = GridSearchCV(clf, param_grid=param_grid, scoring='f1_micro', cv=5)
	
	print('hopefully the model finished...')
	return trained_model


def scoring(model, X_tr, X_te, y_tr, y_te):

	model.fit(X_tr, y_tr)
	pred = model.predict(X_te)
	score = metrics.accuracy_score(y_te, pred)
	f1 = metrics.f1_score(y_te, pred, average='micro')

	print(f'Standard score: {score}')
	print(f'f1 score: {f1}')
	print(pd.crosstab(pred, y_te, rownames=['Predicted'], colnames=['True']))


def main():

	print('Running model')
	
	X_train, X_test, y_train, y_test = load_data()
	cv_model = a_boost()
	scoring(cv_model, X_train, X_test, y_train, y_test)
	
	print('Done!!')


if __name__ == '__main__':
	main()

# To do:
# Find out the return parameters of GridSearchCV
# Implement appropriate return parameters of GridSearchCV
# Fix scoring
