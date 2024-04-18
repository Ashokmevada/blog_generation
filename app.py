from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

GEN_API_KEY = os.environ.get('GEN_API_KEY')


@app.route('/',methods=['GET'])  # route to display the home page
def homePage():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate_blog():
    genai.configure(api_key=GEN_API_KEY)
    model = genai.GenerativeModel('models/gemini-1.0-pro')
    print(f"key is {GEN_API_KEY}")
    data = request.get_json()
    title = data['title']
    response = model.generate_content(f"Write a blog on {title} 800 words")
    content = remove_chars(response.text)
  
    # Process the title, generate content based on it
    return jsonify({'title': title, 'content': content})

def remove_chars(string):
    chars_to_remove = ['*', '#']
    for char in chars_to_remove:
        string = string.replace(char, '')
    return string

if __name__ == '__main__':

    app.run(host= '0.0.0.0')