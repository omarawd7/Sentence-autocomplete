This code is a Python script and a simple frontend page, the Python script collects text data from various URLs related to football and builds a language model based on trigrams. It also provides a Flask API endpoint for predicting the most likely next words given a user input.

Code Structure:
The code consists of the following main parts:

Importing necessary libraries: The code imports the required libraries, including requests, BeautifulSoup, os, nltk, and Flask.

Web scraping and text collection: The get_website_text function uses the requests library to retrieve the HTML content of a given URL and then uses BeautifulSoup to extract the text from the HTML. The collect_corpus function collects text data from a list of URLs by calling get_website_text for each URL and concatenating the results.

Corpus collection: The code defines a list of URLs related to football and uses the collect_corpus function to collect the text data from those URLs. The resulting corpus is then saved to a file named corpus.txt.

Trigram language model: The code tokenizes the corpus into lowercase words, removes punctuation and spaces, and creates a dictionary to store trigram frequencies. It then counts the frequencies of each trigram in the corpus.

Flask API endpoint: The code creates a Flask application and defines a /predict route that expects a POST request with a JSON payload containing a user_input field. The predict function retrieves the user input, tokenizes it, retrieves the last two words as the prefix for the trigram, and returns the top 5 predicted words based on the trigram model.

CORS configuration: The code enables Cross-Origin Resource Sharing (CORS) to allow requests from different origins. It allows requests from http://localhost:8000 for the /predict endpoint.

Running the application: Finally, the code runs the Flask application if the script is executed directly.

Usage
To use this code:

Install the required libraries by running pip install requests beautifulsoup4 nltk flask flask_cors.

Copy the code into a Python file (e.g., football_language_model.py).

Run the Python script. This will collect the text data from the provided URLs, build the trigram language model, and start the Flask application.

Send a POST request to http://localhost:5000/predict with a JSON payload containing the user_input field. The value of user_input should be a string representing the user's input text.

The API will return a JSON response containing the top_predicted_words, which are the most likely next words based on the trigram model.

Note: Make sure to update the CORS configuration in the code to match your desired origins.
