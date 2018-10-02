from sklearn.neighbors import KNeighborsClassifier
features =[[1,0],[5,1],[10,2],[20,0],[50,3],[30,0],[55,4],[25,2],[60,5],[54,3]] # 0 = lottery, 1 = gift , 2 = price money, 3 = twitter, 4 = facebook, 5 = paytm
labels = [['spam'],['spam'],['spam'],['spam'],['not spam'],['spam'],['not spam'],['spam'],['not spam'],['not spam']]
clf = KNeighborsClassifier()
clf = clf.fit(features,labels)
prediction = c.predict([[46,3]])
print(prediction)
