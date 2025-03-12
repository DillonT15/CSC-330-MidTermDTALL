from flask import Flask, render_template

app = Flask(__name__)

animal_templates = {
    'dog': 'dog.html',
    'cat': 'cat.html',
    'elephant': 'elephant.html'
}

@app.route('/fact/<animal>')
def fact(animal):
    template = animal_templates.get(animal.lower())
    return render_template(template)
if __name__ == '__main__':
    app.run(debug=True)