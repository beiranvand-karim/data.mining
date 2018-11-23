from pandas import read_csv, DataFrame

words = read_csv("constants/stopwords.csv")

stopwords = []

for row in words.values:
    wordlist = row[0].split()

    for word in wordlist:
        stopwords.append('\"' + word + '\",')


df = DataFrame(stopwords)

df.to_csv('constants/myqlstopwords.csv', index=False, header=False)

