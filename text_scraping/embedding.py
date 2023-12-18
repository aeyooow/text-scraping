import pandas as pd 
import re

import nltk
from nltk.probability import FreqDist
from matplotlib import pyplot as plt 
import seaborn as sns

word_count = 50
dataset = pd.read_csv('data.csv')
print(dataset)

stop_words = ['ako', 'sya', 'will', 'in', 'this', 'my', 'but', 'a', 'hindi', 'ang', 'ko', 'and', 'sa', 'na', 'ng', 'yung', 'naman', 
              'the', 'for', 'is', 'at', 'to', 'it', 'so', 'i', 'you', 'po', 'of', "it's", 'pa', 'its', 'din', 'lang', 'are', 'really', 
              'was', 'very', 'seller', 'pero', 'with', 'on', 'not', 'all', 'siya', 'again', 'buy', 'that']


all_words = list()
# Loop through the CSV file
for index, data in dataset.iterrows():
    words = str(data.comment).split()
    for w in words:
        temp_word = w.lower()
        temp_word = temp_word.encode('ascii', 'ignore').decode('ascii')
        temp_word = temp_word.strip()
        # Remove non alpha-enumeric characters
        temp_word = re.sub(r'W\+', '', temp_word)
        if temp_word != '' and temp_word not in stop_words:
            all_words.append(temp_word)
    
new_dataframe = pd.DataFrame(all_words)
new_dataframe = new_dataframe[0].value_counts()

freq_doctor = FreqDist()
for word in new_dataframe:
    freq_doctor[word] += 1

# Plot in histogram

new_dataframe = new_dataframe[:word_count]

#some styles
sns.set_style("whitegrid")
sns.set(font_scale=1, rc={'font.family': 'cursive'})

#pastel colors because the theme is makeup (eyeshadows)
sns.barplot(x=new_dataframe.values, y=new_dataframe.index, palette='pastel')

plt.title('Most Frequent Word\nShopee Comments\nCategory: Makeup (Eyeshadows)')

#red and orange for shopee themed
plt.xticks(color='orange')
plt.yticks(color='red')
plt.xlabel('Word')
plt.ylabel('Frequency')

plt.show()
