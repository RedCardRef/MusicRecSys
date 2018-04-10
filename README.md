# MusicRecSys

The goal is to build a recommender system, to display similar songs based on the user listening history. Million Song Dataset has been used to build the system. The Training Data consists of the triplets file (user_id, song_id, play_count) since there is no explicit rating system, we consider the implicit play_count for understanding if the user likes a particular song. The entire dataset consists of 48 million triplets of size 2.8 GB which can be found [here](http://labrosa.ee.columbia.edu/millionsong/sites/default/files/challenge/train_triplets.txt.zip) . But for convenience we use a smaller subset of about 10,000 triples which has the listening history of 365 users and contains 5151 songs. The associated song information is present in the song metadata file.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes

### Prerequisites

You need to have python 3 installed with pip, then 

```
python -m pip install --upgrade pip
pip install -r requirements.txt
```

or you can directly run 'Install Dependencies.bat' if you are on Windows.

This will install/upgrade all the python packages necessary for running the recommender.(Pandas, Numpy, SciPy and sklearn)

## Running the Recommender

Once you have all the dependencies installed you can run the recommender

NOTE: Starting up for the first time will take a while to run, because it needs to download files of about 200MB. This can be skipped if the files are downloaded locally.

To run the recommender

```
python script.py
```

or you can directly execute 'Run Recommender.bat' if you are on Windows.

This module contains both the Popularity Method and Collaborative Filtering Method. This module is used when the user listening history is already present in the dataset.

## Song Finder

This module is used if the listening history of a new user is not present in the dataset. So if the song name present in the dataset is entered, we can generate recommendations of similar songs.

To run the song finder 

```
python findSong.py
```

or you can directly execute 'Run Song Finder.bat' if you are on Windows.

### Usage

Try entering song names like 'U Smile - Justin Bieber' or 'Yellow - Coldplay'

## Misc

The Popularity Method does not consider the previous listening history of the user, it recommends the most popular songs to the user. If a popula song has already been listened by the user, then the songs is not shown in the recommendations.

The Collaborative Filtering Method uses User-User similarity for generating the recommendations. The Song Finder also uses the Collaborative Filtering Method to generate similar songs.

Tkinter has been used as the GUI, because if it is implemented as a Web Application then a lot of configuration changes are required when they are run on different operating systems.
