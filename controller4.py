from flask import Flask, render_template, request
from sklad import Sklad

HOST_PORT="5004"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_sklad"},
        {"name": "POST", "url": "post_sklad"},
        {"name": "DELETE", "url": "delete_sklad"},
        {"name": "PUT", "url": "put_sklad"}]

@app.route("/")
def index():
    result = Sklad.get_sklad()
    return render_template("Sklad/Sklad.html", title="Просмотр складов", menu=menu, sklads=result)

@app.route('/get_sklad', methods=['GET'])
def get():
    result = Sklad.get_sklad()
    return render_template('Sklad/Sklad.html', title="Просмотр складов", menu=menu, sklads=result)

@app.route('/post_sklad', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        sklads = Sklad.add_sklad(request.form["number"], request.form["ylica"], request.form["num_home"], request.form["ploshad"])
    return render_template('Sklad/post_sklad.html', title="Добавление складов", menu=menu)

@app.route('/delete_sklad', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        sklads = Sklad.delete_sklad(int(request.form["number"]))
    return render_template('Sklad/delete_sklad.html', title="Удаление складов", menu=menu)

@app.route('/put_sklad', methods=['POST', 'GET'])
def put():
    if request.method == 'POST':
        sklads = Sklad.update_sklad(request.form["number"], request.form["ylica"], request.form["num_home"], request.form["ploshad"])
    return render_template('Sklad/put_sklad.html', title="Обновление и информации о складах", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)