from sklearn.datasets import load_wine

data = load_wine()
x = data.data
y = data.target

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest = train_test_split(x,y,stratify=y,random_state=1,test_size=0.3)

from sklearn.preprocessing import StandardScaler

std = StandardScaler()
xtrain_std = std.fit_transform(xtrain)
xtest_std = std.fit_transform(xtest)

from sklearn.decomposition import PCA

lpca = PCA(n_components=4) # how many main lines
xtrain_pca = lpca.fit_transform(xtrain_std)
xtest_pca = lpca.transform(xtest_std)
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression()
lr.fit(xtrain_pca,ytrain)
ytrain_pred = lr.predict(xtrain_pca)
ytest_pred = lr.predict(xtest_pca)

from sklearn import metrics
print(metrics.accuracy_score(ytest,ytest_pred))