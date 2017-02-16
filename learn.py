from sklearn import datasets
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import scipy as sp
import os, signals
from sklearn.externals import joblib
from sklearn.model_selection import GridSearchCV

'''
Author: Federico Terzi
This is a work in progress, don't judge please :)
'''

if __name__ == '__main__':
	x_data = []
	y_data = []

	root="D:\Dropbox\Progetti\Tesi\ML\Signals\data"

	for path, subdirs, files in os.walk(root):
		for name in files:
			filename = os.path.join(path, name)
			#print filename
			sample = signals.Sample.load_from_file(filename)
			x_data.append(sample.get_linearized())
			category = name.split("_")[0]
			number = ord(category) - ord("a")
			y_data.append(number)

	#print x_data[0]

	params = {'C':[0.001,0.01,0.1], 'kernel':['linear']}

	svc = svm.SVC()
	clf = GridSearchCV(svc, params,verbose =10, n_jobs=8)

	X_train, X_test, Y_train, Y_test = train_test_split(x_data, 
				y_data, test_size=0.35, random_state=0)

	clf.fit(X_train, Y_train)
	Y_predicted = clf.predict(X_test)

	print clf.score(X_test, Y_test)
	print clf.best_estimator_
	print confusion_matrix(Y_test, Y_predicted)

	sample_test = signals.Sample.load_from_file("c_sample_24.txt")
	lin = sp.reshape(sample_test.get_linearized(), (1,-1))
	print clf.predict(lin)

	joblib.dump(clf, 'model.pkl') 

	# n_img = im.NormalizedImage.load_from_file("f_0.png", 10)
	# #n_img.show_image()
	# img = skimage.img_as_uint(n_img.image)
	# lin = sp.reshape(img, (1,-1))
	# print lin
	# print clf.predict(lin)

	#sio.imshow(sp.reshape(digits.data[-1:], (8,8)),cmap='gray')
	#sio.show()

	# img = im.NormalizedImage.load_from_file('0.png', 8)
	# linearized = sp.reshape(img.image,(1,-1))
	# print linearized
	# print clf.predict(linearized)
	# img.show_image()