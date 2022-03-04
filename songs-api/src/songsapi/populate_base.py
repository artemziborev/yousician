from pymongo import MongoClient
import json
from pathlib import Path
import os


BASE_DIR = Path(__file__).parent.parent.parent.parent
client = MongoClient("mongodb://localhost:27017/")
SONGS_DATA_FILE_PATH = os.path.join(BASE_DIR, 'data', 'songs.json')
db = client.yousician
songs = db.songs


def populate_db():
    with open(SONGS_DATA_FILE_PATH) as file:
        lines = file.readlines()
        for line in lines:
            data = json.loads(line.strip())
            songs.insert_one(data)


def create_indexes():
    songs.drop_indexes()
    songs.create_index([('artist', 'text'), ('title', 'text')],
                       name='song_search')



if __name__ == '__main__':
    populate_db()
    create_indexes()
