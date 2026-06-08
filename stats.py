import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
load_dotenv()

def count_words(words):
    words_list=words.split()
    count=len(words_list)
    return count

def count_characters(words):
    words=words.lower()
    words_count={}
    for ch in words:
        if ch in words_count:
            words_count[ch]+=1;
        else:
            words_count[ch]=1;
    return words_count

def sort_on(store):
    return store["num"]

def summarize_text(text):
    API_KEY = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=API_KEY)
    prompt=f"Please provide a concise summary of the following text:\n\n{text}"
    response = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=prompt,
    config=types.GenerateContentConfig(
        temperature=0,
        top_p=0.95,
        top_k=20,
        ),
    )
    return response.text

def sort_dictionary(store):
    sorted_list=[]
    for ch in store:
        sorted_list.append({"char": ch, "num": store[ch]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list
