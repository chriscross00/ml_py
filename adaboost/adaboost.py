#!/usr/bin/env python

from sklearn.datasets import load_wine
from sklearn.ensemble import AdaBoostClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

def load_data():
	wine = load_wine()

	features, target = wine.data, wine.target
	X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=0)

	return X_train, X_test, y_train, y_test


def a_boost(X_tr, X_te, y_tr, y_te):
	clf = AdaBoostClassifier(n_estimators=50,
							learning_rate=0.01,
							random_state=0)

	clf.fit(X_tr, y_tr)
	pred = clf.predict(X_te)
	score = metrics.accuracy_score(y_te, pred)
	f1 = metrics.f1_score(y_te, pred, average='micro')
	
	print(f'Standard score: {score}')
	print(f'f1 score: {f1}')
	

def main():

	print('Running model')
	
	X_train, X_test, y_train, y_test = load_data()
	a_boost(X_train, X_test, y_train, y_test)
	
	print('Done!')


if __name__ == '__main__':
	main()
