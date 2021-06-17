AddAPT Project Installations & Specifications

AddAPT project has been created in Python 3.8. To get best performance it is very important to run project in Python 3.8.

1- Needed Libraries
    In order to run project in your local device, first of all it is very important to install used libraries and
    their correct versions. Needed libraries are specified as;
    - flask 1.1.2
    - transformers 4.5.1
    - pytorch 1.8.1
    - pandas 1.2.4
    - tqdm 4.60.0

2- File Locations
    The important thing about to project is that used files and file locations. Since we are working with different files
    we decided to collect our users data also the reason is that we need to increase our datasets.
    For that purpose before running the project you have to change some of the locations in the code with your local locations.
    These locations are;
    - In BERT_implementation class in line 31 you have to give the local location of the bert_output_word.csv
    - In BERT_implementation class in line 35 you have to give the local location of the bert_output_sentences.csv
    - In compare class in line 21 you have to give the local location of the bert_output_word.csv
    - In compare class in line 29 you have to give the local location of the cat_csv files
    - In find_chaneles class in line 21 you have to give the local location of the GBvideos.csv files


