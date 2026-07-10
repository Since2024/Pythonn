from sklearn.linear_model import LinearRegression
X=[[1],[3],[4]]
y=[2,6,8]
model=LinearRegression()
model.fit(X,y)
print(model.predict([[2.5]]))