import csv
import numpy as np
from sklearn.cluster import KMeans

with open('example_data.csv', 'rb') as csvFile:
    A = []
    csvReader = csv.reader(csvFile, delimiter=',', quotechar='"')
    for row in csvReader:
        #print(' - '.join(row))
        A.append(row)
    print(A)
kmeans = KMeans(n_clusters=3, random_state=1).fit(A)
print('labels '+str( kmeans.labels_))
print('centers' + str(kmeans.cluster_centers_))