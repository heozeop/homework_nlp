import numpy as np
import json

from script_extract_part.preprocessor import processor
from script_extract_part.vs_model import VSModel


def convert_emotion_to_genre(emotion):
    '''
    array(['anger', 'boredom', 'enthusiam', 'fun', 'happiness', 'hate',
       'love', 'relief', 'sadness', 'surprise', 'worry'], dtype=object)
       분노 => 분노 => 공포 => Horror
    '''
    if emotion == 'love':
        return 'Romance'
    elif emotion == 'anger' or emotion == 'hate':
        return 'Crime'
    elif emotion == 'boredom':
        return 'Adventure'
    elif emotion == 'enthusiam':
        return 'Action'
    elif emotion == 'fun':
        return 'Comedy'
    elif emotion == 'happiness':
        return 'Family'
    elif emotion == 'sadness':
        return 'Drama'
    elif emotion == 'relief':
        return 'Musical'
    elif emotion == 'surprise':
        return 'Thriller'
    elif emotion == 'worry':
        return 'Mystery'
    else:
        return 'Family'

def movie_sort_with_genre(genre):
    f = open(f'./data/grouped_by_genre/raw/{genre}.json', 'r')
    movie_scripts = json.loads(f.read())
    return movie_scripts


def recommende(emotion, text, count=10):
    query = text
    genre = convert_emotion_to_genre(emotion)

    movie_scripts_ = movie_sort_with_genre(genre)
    movie_scripts = [movie[1] for movie in movie_scripts_]

    vsmodel = VSModel(movie_scripts, processor)

    out = vsmodel.query(query, count)

    out = np.array(out)[:, 0]
    movie_scripts = np.array(movie_scripts_)[:, 0]
    recommedation = [movie_scripts[int(o)] for o in out]
    return recommedation, genre

