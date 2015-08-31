from flask import (Flask,
                   redirect,
                   render_template,
                   request,
                   url_for)

from image_maker import ImageMaker
from name_meaning import NameMeaning

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        return render_template('welcome.html')


@app.route('/post', methods=['POST'])
def post():
    name = request.form.get('firstname', None)
    meaning = NameMeaning.get_meaning(name) if name else None
    image_path, hashed = ImageMaker.get_image(name, meaning)
    return redirect(url_for('name_meaning', url_path=hashed))


@app.route('/meaning/<url_path>')
def name_meaning(url_path):
    image_path = '/static/images/cached/{}.png'.format(url_path)
    return render_template('name_meaning.html',
                           image_path=image_path)

if __name__ == '__main__':
    app.debug = True
    app.run()
