from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def welcome():
    if request.method == 'GET':
        return render_template('welcome.html')

    elif request.method == 'POST':
        name = get(request.form, 'name', None)
        meaning = NameMeaning.get_meaning(name) if name else None
        return render_template('name_meaning.html', meaning)

if __name__ == '__main__':
    app.debug = True
    app.run()
