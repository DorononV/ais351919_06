from flask import Flask, render_template, request
from kompl import Kompl

HOST_PORT="5005"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_kompl"},
        {"name": "POST", "url": "post_kompl"},
        {"name": "DELETE", "url": "delete_kompl"},
        {"name": "PUT", "url": "put_kompl"}]

@app.route("/")
def index():
    result = Kompl.get_kompl()
    return render_template("Kompl/Kompl.html", title="Просмотр комплектующих", menu=menu, kompls=result)

@app.route('/get_kompl', methods=['GET'])
def get():
    result = Kompl.get_kompl()
    return render_template('Kompl/Kompl.html', title="Просмотр комплектующих", menu=menu, kompls=result)

@app.route('/post_kompl', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        kompls = Kompl.add_kompl(request.form["number"], request.form["detalname"])
    return render_template('Kompl/post_kompl.html', title="Добавление комплектующих", menu=menu)

@app.route('/delete_kompl', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        clients = Kompl.delete_kompl(int(request.form["number"]))
    return render_template('Kompl/delete_kompl.html', title="Удаление комплектующих", menu=menu)

@app.route('/put_kompl', methods=['POST', 'GET'])
def put():
    if request.method == 'POST':
        clients = Kompl.update_kompl(request.form["number"], request.form["detalname"])
    return render_template('Kompl/put_kompl.html', title="Обновление и информации о комплектующих", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)