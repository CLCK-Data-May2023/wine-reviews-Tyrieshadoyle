# add your code here
import pandas as pd
reviews = pd.read_csv("data\\winemag-data-130k-v2.csv.zip")
reviews_per_country = reviews.country.value_counts()
avg_points = reviews.groupby('country')['points'].mean().round(1)
reviews_merge = pd.DataFrame.merge(reviews_per_country, avg_points, on='country', how='inner')
print(reviews_merge) 
with open('data\\reviews-per-country.csv', 'w') as csv_file:
    reviews_merge.to_csv(path_or_buf=csv_file)