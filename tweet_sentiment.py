import sys
import csv
import json
import pandas as pd
import matplotlib.pyplot as plt

def analyze_sentiment(sent_file, tweet_file):
    #convert setiment words to dictionary
    sent_file.seek(0)
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    #open up raw csv_file and construct DF
    df = pd.read_csv(tweet_file)

    #initiate score to 0 for each tweet
    df["score"] = 0

    #clean up data
    df = df.drop("Unnamed: 0",1)

    #iterate through each tweet text and assign a value based on scores dictionary
    for tweet_number in range(df.shape[0]):
        for each_word in df.at[tweet_number, "Message"].split(" "):
            if each_word in scores:
                df.at[tweet_number, "score"] += scores[each_word]
            else:
                continue

    return df


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    analyze_sentiment(sent_file, tweet_file)


if __name__ == '__main__':
    main()
