from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

X = [[100], [200], [300], [0], [1000]]
model = KMeans(n_clusters=2, n_init=10) # n_init=10 suppresses a future warning
model.fit(X)

print(model.labels_)