from flask import Flask, render_template
from datos import select_persona, select_estudiante
from werkzeug.utils import redirect
from flask.helpers import url_for

app = Flask(__name__)


@app.route('/persona')
def persona():
    datos1 = select_persona()
    return render_template('mostrar.html', datos1=datos1)


@app.route('/estudiante')
def estudiante():
    datos2 = select_estudiante()
    return render_template('mostrar2.html', datos2=datos2)


@app.route('/estudiante')
def redireccionar():
    return redirect(url_for('estudiante'))


@app.route('/persona')
def redireccionar2():
    return redirect(url_for('persona'))


if __name__ == '__main__':
    app.run(debug=True)
