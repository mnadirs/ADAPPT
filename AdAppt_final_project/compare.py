import pandas as pd
from tqdm import tqdm
import os
#/Users/mesutnadirseyfelioglu/School/Bitirme/bert_output_word.csv

def category_name():
    filenames = []
    directory = r'/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/cat_csv'
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filenames.append(filename)
        else:
            continue

    headers = []
    for i in range(len(filenames)):
        headers.append(filenames[i].split("_")[0])
    #filenames
    #headers

    bert_df = pd.read_csv("/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/bert_output_word.csv")
    #bert_df

    maxCount = 0
    cat_csv_df = pd.DataFrame()

    for j in range(len(filenames)):
        cat_csv_df = cat_csv_df.fillna(0)
        full_path = os.path.join("/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/cat_csv/", filenames[j])
        cat_csv_df = pd.read_csv(full_path)

        cat_csv_df[headers[j]] = cat_csv_df[headers[j]].str.split().str[0]
        count = 0

        for i in tqdm(range(len(cat_csv_df))):
            for k in tqdm(range(len(bert_df))):
                if (cat_csv_df[headers[j]][i] == bert_df["Words"][k]):
                    print("from cat_csv_df = ", cat_csv_df[headers[j]][i], "from bert = ", bert_df["Words"][k])
                    count = count + 1
            k = 0
        i = 0

        if (count > maxCount):
            maxCount = count
            fileName = headers[j]


    print("Category: ", fileName)


