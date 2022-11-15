from flask import Flask, render_template, request
import requests
app = Flask(__name__)
url = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "<f50dae66d6msh719422f3b99f765p1c60d7j>",
  }
random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"
@app.route('/')
def search_page():
  joke_response = str(requests.request("GET", url + random_joke, headers=headers).json()['text'])
  return render_template('search.html', joke=joke_response)
if __name__ == '__main__':
  app.run()