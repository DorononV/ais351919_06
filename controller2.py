from flask import Flask, render_template, request
from Nakladnaya import Bill

HOST_PORT="5002"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_bill"},
        {"name": "POST", "url": "post_bill"},
        {"name": "DELETE", "url": "delete_bill"},
        {"name": "PUT", "url": "put_bill"}]

@app.route("/")
def index():
    result = Bill.get_bill()
    return render_template("Bill/Bill.html", title="Просмотр накладных", menu=menu, bills=result)

@app.route('/get_bill', methods=['GET'])
def get():
    result = Bill.get_bill()
    return render_template('Bill/Bill.html', title="Просмотр накладных", menu=menu, bills=result)

@app.route('/post_bill', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        bills = Bill.add_bill(request.form["number"], request.form["sklad"], request.form["detail"], request.form["date_poluch"], request.form["price"], request.form["remontnik"])
    return render_template('Bill/post_bill.html', title="Добавление накладных", menu=menu)

@app.route('/delete_bill', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        bills = Bill.delete_bill(int(request.form["number"]))
    return render_template('Bill/delete_bill.html', title="Удаление накладных", menu=menu)

@app.route('/put_bill', methods=['POST', 'GET'])
def put():
    if request.method == 'POST':
        bills = Bill.update_bill(request.form["number"], request.form["sklad"], request.form["detail"], request.form["date_poluch"], request.form["price"], request.form["remontnik"])
    return render_template('Bill/put_bill.html', title="Обновление и информации о накладных", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)