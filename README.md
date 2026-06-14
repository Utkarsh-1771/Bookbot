# Project Overview
I made this project as I was learning python, during my learning period I thought what would be a better way to test the things that I have learned so I built this simple bookbot.
You give the path of the .txt file(preferably the content of a book) and it fetches the text inside it and it will give you a simple menu with 3 options,
- Give the count of each character present in the text
- Summarize the text
- Exit the program

**The file structure is**

```
Bookbot/
├── books/
│   └── yourbook.txt
├── main.py
├── stats.py
├── .env
└── .gitignore
```

## Character count
For this I just used a normal [dictionary](https://docs.python.org/3/tutorial/datastructures.html#dictionaries) and stored the count for each word in the from of key value pair. It returns the count of each character in descending order.

The syntax for that part is
```
words=words.lower()
    words_count={}
    for ch in words:
        if ch in words_count:
            words_count[ch]+=1;
        else:
            words_count[ch]=1;
```
## Summarize the text
I have used Gemini API to summarize the text

I will suggest to create a virtual environment(venv) first and install the dependencies there

`python3 -m venv venv`

**Also add the venv/ along with .env to your .gitignore file**

you will first have to install dotenv to load environment variables from the .env file

`pip install python-dotenv`

Then genai package from google

`pip install google-genai`

### For the api key
- Go to https://aistudio.google.com and get their own Gemini API key
- Create a .env file in the project folder
- Add this line to it
- `GEMINI_API_KEY=their-key-here`
  
## To run the program
**Make sure you have python installed in your system.**

commands to run the program 
- If you have created a virtual environment(venv) then

`source venv/bin/activate`
- to run the program

`python3 main.py books/yourbook.txt`

instead of `books/yourbook.txt` give the path where the .txt file that you want to used is stored

## Where do I get the books in .txt?
You can get free books in .txt format from [Project Gutenberg](https://www.gutenberg.org)