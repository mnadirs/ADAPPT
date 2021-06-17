from transformers import BertTokenizer, BertForMaskedLM
from torch.nn import functional as F
import torch
import csv
import pandas as pd



def bert(keyword):
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    model = BertForMaskedLM.from_pretrained('bert-base-uncased',    return_dict = True)
    text = keyword +" is a keyword about the " + tokenizer.mask_token + " field."
    #text = "DNA test is in the, " + tokenizer.mask_token + " field." very important text example sileni sikerim
    #text = "CoinGecko is a keyword about the " + tokenizer.mask_token + " field." very important text example sileni sikerim v1
    input = tokenizer.encode_plus(text, return_tensors = "pt")
    mask_index = torch.where(input["input_ids"][0] == tokenizer.mask_token_id)
    output = model(**input)
    logits = output.logits
    softmax = F.softmax(logits, dim = -1)
    mask_word = softmax[0, mask_index, :]
    top_100 = torch.topk(mask_word, 10, dim = 1)[1][0]
    new_sentence = []
    new_word = []
    for token in top_100:
        word = tokenizer.decode([token])
        new_sentence.append(text.replace(tokenizer.mask_token, word))
        new_word.append(word)

    #save words to csv
    df = pd.DataFrame(new_word, columns=['Words'])
    df.to_csv("/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/bert_output_word.csv")

    #save sentences to csv
    df = pd.DataFrame(new_sentence, columns=['Sentences'])
    df.to_csv("/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/bert_output_sentences.csv")

    #compare.category_name()
    print("Generated words",new_word)
    return new_word


bert("Keyword")




'''
def save_word_to_csv():

    new_word = bert()
    df = pd.DataFrame(new_word, columns=['Words'])

    df.to_csv("/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/bert_output_word.csv")

def save_sentence_to_csv():

    new_sentence =
    df = pd.DataFrame(new_sentence, columns=['Sentences'])
    df.to_csv("/Users/mesutnadirseyfelioglu/PycharmProjects/final_project/bert_output_sentences.csv")

'''