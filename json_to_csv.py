import json
import csv

with open('scraped_twitter/scraped_data.json',"r") as json_f:
    tweets_data = json.load(json_f)

    data_file = open('scraped_twitter/scraped_data.csv','w',encoding='utf-8')
    csv_writer = csv.writer(data_file)

    count = 0

    for tweet in tweets_data:
        if count == 0:
            header = tweet.keys()
            csv_writer.writerow(header)
            count += 1

        csv_writer.writerow(tweet.values())
    data_file.close()

