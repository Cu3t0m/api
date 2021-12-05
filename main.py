from flask import Flask, render_template, request, jsonify, abort
from random import randrange
from english_words import english_words_set
from flask.templating import render_template
import pyjokes
from memeGen import ScrapMemes
from prsaw import *



words = list(english_words_set)
links = ['/numbers', '/letters', '/words','/jokes', '/gimme/<amount>', '/gimme/<topic>', '/gimme/<topic>/<amount>', '/ai/response/<string:question>']

url = "http://api.cu3t0m.repl.co"
rs = RandomStuffV2()
for i in links:
    index = links.index(i)
    links[index] = url+i

    
app = Flask("app")
app.config['JSON_SORT_KEYS'] = False

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



@app.route('/ai/response/<string:question>/')
def ai_response(question):
    airesp = rs.get_ai_response(question)
    return airesp


@app.route('/gimme')
def meme_api():
    result = ScrapMemes()
    return jsonify(result)

# Numbered Meme Generator
@app.route('/gimme/<int:num>/')
def meme_api_no(num):
    result = ScrapMemes(num=num)
    return jsonify(result)

# Topic wise Meme Generator
@app.route('/gimme/<string:topic>/')
def meme_api_topic(topic):
    result = ScrapMemes(topic=topic)
    return jsonify(result)

# Topicwise and numbered meme generator
@app.route('/gimme/<string:topic>/<int:num>/')
def meme_api_topic_and_no(topic, num):
    result = ScrapMemes(topic=topic, num=num)
    return jsonify(result)

@app.route('/numbers')
def randomjson():
    no = {
    'number':randrange(0,100000000)
    }
    return no

# @app.route('/')
# def hello():
#     return 'Welcome to the randomness API! '
@app.route('/jokes')
def joke():
    jokes = {
    'joke':pyjokes.get_joke()
    }  
    return jokes
@app.route('/letters')
def letterjson():
    letter = {
        'letter':letters[randrange(0, len(letters))]
    }
    return letter

@app.route('/words')
def wordsjson():
    word = {
        'word':words[randrange(0, len(words))]
    }
    return word

@app.route("/")
def site_map():
    return render_template('index.html', links = links)


if __name__ == "__main__":
    # running the flask app in threaded mode 
    # to allow handling more requests at once
    app.run(host='0.0.0.0', port=8080, threaded=True)