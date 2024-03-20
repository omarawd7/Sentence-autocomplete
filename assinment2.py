import requests
from bs4 import BeautifulSoup
import os
import nltk
from nltk import trigrams
import string  # Import string module for punctuation removal

def get_website_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()
    return text.strip()

def collect_corpus(urls):
    corpus = ""
    for url in urls:
        text = get_website_text(url)
        corpus += text + "\n"  # Add a new line between each website's text

    return corpus

# Example usage:
urls = [
    'https://www.bbc.com/sport/football/68619899',
    'https://www.bbc.com/sport/football/68561544',
    'https://www.bbc.com/sport/football/68596737',
    'https://www.bbc.com/sport/68609126',
    'https://www.bbc.com/sport/football/68180753',
    'https://www.bbc.com/sport/football/68602074',
    'https://www.bbc.com/sport/football/68418314',
    'https://www.theguardian.com/football/2024/mar/20/wales-euro-2024-playoff-rob-page-aaron-ramsey-ethan-ampadu',
    'https://www.theguardian.com/football/2024/mar/20/brazil-coach-dorival-junior-england',
    'https://www.theguardian.com/football/who-scored-blog/2024/mar/20/england-team-picked-on-form-players',
    'https://www.britannica.com/sports/football-soccer/South-America',
    'https://www.fourfourtwo.com/news/arsenal-transfer-news-have-begun-talks-over-sensational-euro100m-striker-move-at-a-cut-price-deal-with-offer-made-report-viktor-gyokeres-sporting-cp-lisbon-signings-rumours-gossip-paper-talk-afc',
    'https://www.dailymail.co.uk/sport/football/article-13219099/Joey-Barton-England-stars-diamond-earrings-leggings-Drake-Bobby-Moore.html',
    'https://theconversation.com/premier-leagues-record-spending-could-help-make-english-football-fairer-and-more-competitive-but-it-depends-on-liz-truss-190271',
    'https://theconversation.com/englands-premier-league-homegrown-talent-problem-why-its-time-to-introduce-equivalent-of-barcelona-b-114645',
    'https://thesefootballtimes.co/2023/04/06/remembering-the-disaster-of-1991-92-bayern-munichs-worst-season-in-modern-history/',
    'https://thesefootballtimes.co/2023/01/02/pele-at-the-1970-world-cup-the-memories-beyond-the-goals/',
    'https://thesefootballtimes.co/2021/08/09/james-milner-is-not-a-robot-but-make-no-mistake-he-is-a-machine/',
    'https://thesefootballtimes.co/2016/09/13/why-adam-lallana-deserves-your-attention/',
    'https://thesefootballtimes.co/2016/08/24/james-milner-the-underappreciated-enigma-of-english-football/',
    'https://thesefootballtimes.co/2020/02/19/the-battle-of-barcelonas-trinities-stoichkov-laudrup-romario-or-messi-neymar-suarez/',
    'https://thesefootballtimes.co/2020/04/20/the-season-that-saw-ronald-koeman-top-the-champions-league-goalscoring-charts-from-defence/',
    'https://www.goal.com/story/salah-egypt/index.html',
    'https://www.independent.co.uk/sport/football/liverpool-mohamed-salah-klopp-manchester-united-b2513338.html',
    'https://en.wikipedia.org/wiki/Mohamed_Salah',
    'https://en.wikipedia.org/wiki/Lionel_Messi',
    'https://en.wikipedia.org/wiki/Lionel_Messi',
    'https://en.wikipedia.org/wiki/Cristiano_Ronaldo',
    'https://en.wikipedia.org/wiki/Kylian_Mbapp%C3%A9',
    'https://en.wikipedia.org/wiki/Karim_Benzema',
    'https://en.wikipedia.org/wiki/Sergio_Ramos'
    'https://en.wikipedia.org/wiki/Neymar',
    'https://en.wikipedia.org/wiki/Luis_Su%C3%A1rez',
    'https://en.wikipedia.org/wiki/Andr%C3%A9s_Iniesta',
    'https://en.wikipedia.org/wiki/Gerard_Pique',
    'https://en.wikipedia.org/wiki/David_Silva',
    'https://en.wikipedia.org/wiki/Carles_Puyol',
    'https://en.wikipedia.org/wiki/Xavi_Hern%C3%A1ndez',
    'https://en.wikipedia.org/wiki/J%C3%BCrgen_Klopp'
    'https://en.wikipedia.org/wiki/Jos%C3%A9_Mourinho',
    'https://en.wikipedia.org/wiki/Pep_Guardiola',
    'https://en.wikipedia.org/wiki/Carlo_Ancelotti',
    ]

full_corpus = collect_corpus(urls)
# Get the directory of the current script (where your code file is located)
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "corpus.txt")

with open(file_path, "w", encoding='utf-8') as f:
    f.write("corpus data:\n")
    f.write(full_corpus)

# Count the number of words in the corpus
word_count = len(full_corpus.split())

# Print the number of words
print("Number of words in the corpus:", word_count)

def get_top_predicted_words(trigram_freq, prefix, n=5):
    if prefix in trigram_freq:
        top_words = sorted(trigram_freq[prefix], key=trigram_freq[prefix].get, reverse=True)[:n]
    else:
        top_words = []
    return top_words

# Tokenize the corpus into lowercase words (without punctuation and spaces)
corpus_tokens = [
    word.translate(str.maketrans('', '', string.punctuation + ' '))
    .lower()  # Convert to lowercase during tokenization
    for word in nltk.word_tokenize(full_corpus)
    if word.isalnum() and len(word) > 1  # Keep only multi-character alphanumeric words
]
# Create a dictionary to store trigram frequencies
trigram_freq = {}
# Count the frequencies of each trigram
for word1, word2, word3 in trigrams(corpus_tokens):
    prefix = (word1, word2)
    if prefix in trigram_freq:
        trigram_freq[prefix][word3] = trigram_freq[prefix].get(word3, 0) + 1
    else:
        trigram_freq[prefix] = {word3: 1}

# Prompt the user to enter a sentence
user_input = "mo salah mo"
user_input=user_input.lower()
# Split the user's input into words
input_words = nltk.word_tokenize(user_input)
# Retrieve the last two words of the input as the prefix for the trigram
prefix = tuple(input_words[-2:])

# Get the top 5 predicted words
top_predicted_words = get_top_predicted_words(trigram_freq, prefix, n=5)

# Print the top 5 predicted words
print("Top 5 predicted words:")
for word in top_predicted_words:
    print(word)