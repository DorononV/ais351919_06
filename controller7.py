from flask import Flask, render_template, request
from sklad_and_kompl import Sklad_and_kompl

HOST_PORT="5007"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_sknkumpl"},
        {"name": "POST", "url": "post_sknkumpl"},
        {"name": "DELETE", "url": "delete_sknkumpl"}]

@app.route("/")
def index():
    result = Sklad_and_kompl.get_sklad_and_kompl()
    return render_template("Sk_n_kumpl/Sk_n_kumpl.html", title="Просмотр комплектующих на складах", menu=menu, sklad_and_kompls=result)

@app.route('/get_sknkumpl', methods=['GET'])
def get():
    result = Sklad_and_kompl.get_sklad_and_kompl()
    return render_template('Sk_n_kumpl/Sk_n_kumpl.html', title="Просмотр комплектующих на складах", menu=menu, sklad_and_kompls=result)

@app.route('/post_sknkumpl', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        sklad_and_kompl = Sklad_and_kompl.add_sklad_and_kompl(request.form["number"], request.form["kompl"])
    return render_template('Sk_n_kumpl/post_Sk_n_kumpl.html', title="Добавление комплектующих на склад", menu=menu)

@app.route('/delete_sknkumpl', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        sklad_and_kompl = Sklad_and_kompl.delete_sklad_and_kompl(int(request.form["number"]), int(request.form["kompl"]))
    return render_template('Sk_n_kumpl/delete_Sk_n_kumpl.html', title="Удаление комплектующих со склада", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)