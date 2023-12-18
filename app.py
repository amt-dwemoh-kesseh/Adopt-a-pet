from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return """<h1>Adopt a Pet!</h1>
  <p>Browse through the links below to find your new furry frined:</p>
  <ul><li><a href="/animals/dogs">Dogs</a></li>
  <li><a href="/animals/cats">Cats</a></li>
  <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  """

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = f'<h1>List of {pet_type}</h1>'
  for pet in pets[pet_type]:
    html += '<li><a href = "/animals/{pet_type}/{index}">'.format(pet_type = pet_type, index = index) + pet['name'] + '</a></li>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type,pet_id):
  pet = pets[pet_type][pet_id]
  pets_name = pet["name"]
  return f'<h1>{pet_name}</h1>'.format(pets_name=pets_name)