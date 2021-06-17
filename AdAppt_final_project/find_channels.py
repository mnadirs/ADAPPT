import pandas as pd
from tqdm import tqdm
import json
import compare

dict = {'cat_names': ["Film", "Animation", "Autos", "Vehicles", "Music", "Pets", "Animals", "Sports", "Short Movies",
                      "Travel", "Events", "Gaming", "Vlogging", "People", "Blogs",
                      "Comedy", "Entertainment", "News", "Politics", "Howto", "Style", "Education", "Science",
                      "Technology", "Movies", "Anime", "Animation",
                      "Action", "Adventure", "Classics", "Documentary", "Drama", "Family", "Foreign", "Horror",
                      "Sci-Fi", "Fantasy", "Thriller", "Shorts", "Shows", "Trailers"],
        'cat_id': [1, 1, 2, 2, 10, 15, 15, 17, 18, 19, 19, 20, 21, 22, 22,
                   23, 24, 25, 25, 26, 26, 27, 28, 28, 30, 31, 31,
                   32, 32, 33, 35, 36, 37, 38, 39, 40, 40, 41, 42, 43, 44]}

df = pd.DataFrame(dict)

#print(df)

data_videos = pd.read_csv(
    "/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/Youtube Datasets/Dataset2/GBvideos.csv",
    error_bad_lines=False)

#print(data_videos)

#category = compare.category_name()
def find_title(category):
    for i in range(len(df)):
        if (category == df['cat_names'][i]):
            name = df['cat_names'][i]
            id = df['cat_id'][i]
            for k in range(len(data_videos)):
                if (id == data_videos['category_id'][k]):
                    return(data_videos['channel_title'][k])

    #return data_videos['channel_title']



find_title("Sports")

