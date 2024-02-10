import random
import pandas as pd
import functions


artistData = r'/Users/sanjith/Personal/Development/VSCodeProjects/RandomSongIdeaGenerator/SongGenData.xlsx'
songGenres = ['Trap', 'Rock', 'Lofi', 'Orchestral', 'EDM', 'Cinematic Modern Music']
artists  = pd.read_excel(artistData)
artists.AnirudhMovies[1]



q1 = input('Do you need a song idea? y/n: ')

if q1 == 'n': 
    print('Ok have a good day.')
elif q1 == 'y':
    genre = random.choice(songGenres)
    q2 = input('Choose a reference artist: \nA:Anirudh \nB:A.R.Rahman \nC:Yuvan \nD:MetroBoomin \nE:Kendrick Lamar: \n')
else:
    print('Please enter either y/n')
    q1 = input('Do you need a song idea? y/n')

if q2 == 'A':
    AnirudhChoice = functions.Anirudh()
    print('Your Reference is the Anirudh Scored Movie:', AnirudhChoice)
elif q2 == 'B':
    ARRCHoice = functions.ARR()
    print('Your reference is the ARR Scored Movie:', ARRCHoice)
elif q2 == 'C':
    YuvanChoice = functions.Yuvan()
    print('Your reference is the Yuvan Scored Movie:', YuvanChoice)
elif q2 == 'D':
    MetroChoice = functions.Metro()
    print('Your reference is the Metro Boomin Album:', MetroChoice)
elif q2 == 'E':
    KendrickChoice = functions.Kendrick()
    print('Your reference is the Kendrick Lamar Album:', KendrickChoice)
else: 
    print('please enter a capial letter of either A,B,C or D')


print('Your genre is:', genre)
    










