import pandas
from sklearn.model_selection import train_test_split
import numpy as np
import time
from sklearn.externals import joblib
import Recommenders as Recommenders
import tkinter as tk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.title("Music Recommendation System")
window.geometry("1250x555")
title1 = tk.Label(text = "Enter User ID(0-364): ")
title1.grid(column = 0,row = 0)
entry1 = tk.Entry()
entry1.grid(column = 1,row = 0)
title2 = tk.Label(text = "Get Predictions using:")
title2.grid(column = 0,row = 1)
#Read userid-songid-listen_count triplets
#This step might take time to download data from external sources
triplets_file = '10000.txt'
songs_metadata_file = 'song_data.csv'

song_df_1 = pandas.read_table(triplets_file,header=None)
song_df_1.columns = ['user_id', 'song_id', 'listen_count']

#Read song  metadata
song_df_2 =  pandas.read_csv(songs_metadata_file)

#Merge the two dataframes above to create input dataframe for recommender systems
song_df = pandas.merge(song_df_1, song_df_2.drop_duplicates(['song_id']), on="song_id", how="left")

song_df = song_df.head(10000)


#Merge song title and artist_name columns to make a merged column
song_df['song'] = song_df['title'].map(str) + " - " + song_df['artist_name']
song_grouped = song_df.groupby(['song']).agg({'listen_count': 'count'}).reset_index()
grouped_sum = song_grouped['listen_count'].sum()
song_grouped['percentage']  = song_grouped['listen_count'].div(grouped_sum)*100
song_grouped.sort_values(['listen_count', 'song'], ascending = [0,1])
users = song_df['user_id'].unique()
songs = song_df['song'].unique()
train_data, test_data = train_test_split(song_df, test_size = 0.20, random_state=0)
pm = Recommenders.popularity_recommender_py()
pm.create(train_data, 'user_id', 'song')
is_model = Recommenders.item_similarity_recommender_py()
is_model.create(train_data, 'user_id', 'song')

def pop_display():
	temp = entry1.get()
	if (temp.isnumeric() == False):
		showinfo("Input Error", "Please enter a numeric value!")
	elif (int(temp) < 0 or int(temp) > 364):
		showinfo("Input Error", "Used ID Invalid! Please enter a User ID between 0 and 364")
	else:
		user_id = users[int(temp)]
		result = pm.recommend(user_id)
		result_display = tk.Text(master = window, height = 12, width = 75)
		result_display.grid(column = 1, row = 2)
		result_display.insert(tk.END, result)


def cf_display():
	temp = entry1.get()
	if (temp.isnumeric() == False):
		showinfo("Input Error", "Please enter a numeric value!")
	elif (int(temp) < 0 or int(temp) > 364):
		showinfo("Input Error", "Used ID Invalid! Please enter a User ID between 0 and 364")
	else:
		user_id = users[int(temp)]
		user_items = is_model.get_user_items(user_id)
		result = is_model.recommend(user_id)
		result_display = tk.Text(master = window, height = 12, width = 75)
		result_display.grid(column = 1, row = 3)
		result_display.insert(tk.END, result)


button1 = tk.Button(text = "Popularity Model", command = pop_display)
button1.grid(column = 1, row = 1)

button2 = tk.Button(text = "Collaborative Filtering Model", command = cf_display)
button2.grid(column = 2, row = 1)


window.mainloop()
