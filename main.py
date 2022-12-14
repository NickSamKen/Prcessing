# This is a sample Python script.
import collections
import json
import string
from collections import Counter
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

def plot_graph(list):
    y = []
    x = []
    rank = 1
    for entry in list:
        freq = int(entry[1])
        y.append(freq)
        x.append(rank)
        rank += 1
    plt.plot(x, y)
    plt.xlabel('x - axis: word ranking')
    plt.ylabel('y - axis: word frequency')
    plt.title('frequency word graph')
    plt.show()
    log_graph(x, y)

def log_graph(x, y):
    plt.loglog(x, y)
    plt.xlabel('x - axis: word ranking log')
    plt.ylabel('y - axis: word frequency log')
    plt.title('frequency word graph log')
    plt.show()


def print_fancy(list, total_words):
    rank = 1
    print("Rank : Words\t : Frequency\tWord Percentage")
    for line in list:
        print(rank," : ", line[0], "\t\t : ", line[1], "\t\t", round(int(line[1])/total_words, 3))
        rank+=1

def freq_list(list, top):
    counterPlus = collections.Counter(list)
    most_freq = counterPlus.most_common(top)
    if top > 10:
        return most_freq
    else:
        plot_graph(counterPlus.most_common(500))
        return most_freq

#use ranking as x axis and frequence as Y
#plt.loglog(x,y)
def remove_stop(word_list):
    #nltk.download("all")
    filtered_word_list = word_list[:]  # make a copy of the word_list
    for word in word_list:  # iterate over word_list
        if word in stopwords.words('english') or word in string.punctuation:
            filtered_word_list.remove(word)
    return filtered_word_list


if __name__ == '__main__':
    with open('C:/Users/User/PycharmProjects/scrapyProject/tutorial/tutorial/entry.json') as f:
        data = json.load(f)
    words = 0
    total = 0
    count = 0
    counter = []
    word_list = []
    num_email = 0
    for i in data:
        if i['emails']:
            num_email += 1
            email = i['emails']
            counter.extend(email)
        word_list.extend(i['body'])
        words = len(i['body'])
        total = total + words
        count += 1
    average_words = round(total / count)
    #creates a list without the stop words
    better_list = remove_stop(word_list)
    print('average words per doc', average_words)
    print('email frequency: ')
    email_freq= freq_list(counter, 10)
    print(email_freq)
    print('percentage of websites with a email', round(num_email / count, 3))
    print('word frequency: ')
    # uses count to find the frequency of words
    st_freq_list = freq_list(word_list, 30)
    print_fancy(st_freq_list, total)
    print('word frequency without stop words: ')
    #uses count to find the frequency of words without stopwords
    nst_freq_list = freq_list(better_list, 30)
    print_fancy(st_freq_list, total)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
