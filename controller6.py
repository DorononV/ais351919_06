from flask import Flask, render_template, request
from Stanok import Stanok

HOST_PORT="5006"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_stanok"},
        {"name": "POST", "url": "post_stanok"},
        {"name": "DELETE", "url": "delete_stanok"},
        {"name": "PUT", "url": "put_stanok"}]

@app.route("/")
def index():
    result = Stanok.get_stanok()
    return render_template("Stanok/Stanok.html", title="Просмотр станков", menu=menu, stanoks=result)

@app.route('/get_stanok', methods=['GET'])
def get():
    result = Stanok.get_stanok()
    return render_template('Stanok/Stanok.html', title="Просмотр станков", menu=menu, stanoks=result)

@app.route('/post_stanok', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        stanoks = Stanok.add_stanok(request.form["number"], request.form["model_st"], request.form["type_st"], request.form["user"], request.form["expl"])
    return render_template('Stanok/post_stanok.html', title="Добавление станков", menu=menu)

@app.route('/delete_stanok', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        stanoks = Stanok.delete_stanok(int(request.form["number"]))
    return render_template('Stanok/delete_stanok.html', title="Удаление станков", menu=menu)

@app.route('/put_stanok', methods=['POST', 'GET'])
def put():
    if request.method == 'POST':
        stanoks = Stanok.update_stanok(request.form["number"], request.form["model_st"], request.form["type_st"], request.form["user"], request.form["expl"])
    return render_template('Stanok/put_stanok.html', title="Обновление и информации о станках", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)