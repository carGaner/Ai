import wikipedia
from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re

def ask_question_and_get_answer(self,question, max_sentences=5):
    try:
        search_results = search(question, num=1, stop=1, pause=2)  # Perform a Google search
        first_result = next(search_results)  # Get the first search result
        response = requests.get(first_result)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')  # Extract all <p> elements
        sentences = []
        for p in paragraphs:
            text = p.get_text()
            # Split text into sentences using regex
            sentences.extend(re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text))
            if len(sentences) >= max_sentences:
                break
        return ' '.join(sentences[:max_sentences])
    except StopIteration:
        return "No relevant answer found."


def get_wikipedia_summary(self, topic, sentences=2):
    try:
        # Get the summary for the given topic
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple options for the topic, you can handle it here
        options = e.options
        print(f"There are multiple options for '{topic}': {options}")
        return None
    except wikipedia.exceptions.PageError:
        # If the topic doesn't exist, handle the error here
        print(f"'{topic}' does not exist on Wikipedia.")
        return None


def get_wikipedia_summary(self, topic, sentences=2):
    try:
        # Get the summary for the given topic
        summary = wikipedia.summary(topic, sentences=sentences)
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple options for the topic, you can handle it here
        options = e.options
        print(f"There are multiple options for '{topic}': {options}")
        return None
    except wikipedia.exceptions.PageError:
        # If the topic doesn't exist, handle the error here
        print(f"'{topic}' does not exist on Wikipedia.")
        return None
