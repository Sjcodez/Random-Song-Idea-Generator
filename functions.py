import pandas as pd
import random

artistData = r"/Users/sanjith/Personal/Development/VSCodeProjects/RandomSongIdeaGenerator/SongGenData.xlsx"
artists  = pd.read_excel(artistData)

def Anirudh():
    x = random.randint(0, 26)
    artistChoice = artists.AnirudhMovies[x]
    return artistChoice    

def ARR():
    x = random.randint(0,28)
    artistChoice = artists.ARRMovies[x]
    return artistChoice

def Yuvan():
    x = random.randint(0,28)
    artistChoice = artists.YuvanMovies[x]
    return artistChoice

def Metro():
    x = random.randint(0,9)
    artistChoice = artists.MetroAlbums[x]
    return artistChoice

def Kendrick():
    x = random.randint(0,9)
    artistChoice = artists.KendrickAlbums[x]
    return artistChoice
                                       
