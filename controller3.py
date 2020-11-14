from flask import Flask, render_template, request
from expl import Expl

HOST_PORT="5003"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_expl"},
        {"name": "POST", "url": "post_expl"},
        {"name": "DELETE", "url": "delete_expl"},
        {"name": "PUT", "url": "put_expl"}]

@app.route("/")
def index():
    result = Expl.get_users()
    return render_template("Expl/Expl.html", title="Просмотр эксплуатации станков", menu=menu, expls=result)

@app.route('/get_expl', methods=['GET'])
def get():
    result = Expl.get_users()
    return render_template('Expl/Expl.html', title="Просмотр эксплуатации станков", menu=menu, expls=result)

@app.route('/post_expl', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        expls = Expl.add_user(request.form["number"], request.form["date_start"], request.form["expl_srok"], request.form["date_spis"])
    return render_template('Expl/post_expl.html', title="Добавление эксплуатации станков", menu=menu)

@app.route('/delete_expl', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        expls = Expl.delete_user(int(request.form["number"]))
    return render_template('Expl/delete_expl.html', title="Удаление эксплуатации станков", menu=menu)

@app.route('/put_expl', methods=['POST', 'GET'])
def put():
    if request.method == 'POST':
        expls = Expl.update_user(request.form["number"], request.form["date_start"], request.form["expl_srok"], request.form["date_spis"])
    return render_template('Expl/put_expl.html', title="Обновление и информации о эксплуатации станков", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)