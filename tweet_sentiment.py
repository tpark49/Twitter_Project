import sys
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_sentiment(sent_file, tweet_file):

    #open up raw csv_file and construct DF
    df = pd.read_csv(tweet_file)

    #initiate score to 0 for each tweet
    df["score"] = 0

    #clean up data
    df = df.drop("Unnamed: 0",1)

    #iterate through each tweet text and assign a value based on scores dictionary
    for tweet_number in range(df.shape[0]):
        for each_word in df.at[tweet_number, "Message"].split(" "):
            if each_word in sent_file:
                df.at[tweet_number, "score"] += sent_file[each_word]
            else:
                continue

    return df


def score_to_dictionary(f):
    scores = {}

    #convert setiment words to dictionary
    for line in f:
        term, score = line.split("\t")
        scores[term] = int(score)

    return scores



#def new_terms(sent_file, tweet_file):





def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    #create dictionary of scores
    score_dict = score_to_dictionary(sent_file)

    #gives each tweet a score based on sentiment analysis
    analyze_sentiment(score_dict, tweet_file)

    #generates terms outside of sent_file from tweet_file based on analyzed sentiment
    #new_terms(sent_file, tweet_file)




if __name__ == '__main__':
    main()
