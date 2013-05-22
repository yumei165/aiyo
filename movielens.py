#data source: http://www.grouplens.org/node/73

import pandas as pd

#read data into dataframe
unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', header = None, names=unames )

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::', header=None, names=mnames)

#extract data for mean rating of movie by user gender
data = pd.merge(pd.merge(users,ratings),movies)
mean_ratings = data.pivot_table('rating', rows='title', cols='gender', aggfunc='mean')

#subset with titles with >250 ratings
ratings_by_title = data.groupby('title').size()
active_titles = rating_by_title.index[rating_by_title >= 250]
mean_ratings = mean_ratings.ix[active_titles]

#sort by F column to get top female rating titles
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)

#find titles with biggest diff rating between M/F
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by='diff')
sorted_by_diff[::-1][:15]  #reverse order and return 15 records

#find titles with most disagreement(standard deviation)
rating_std_by_title = data.groupby('title')['rating'].std()
rating_std_by_title = rating_std_by_title.ix[active_titles]
rating_std_by_title.order(ascending=False)[:10]
