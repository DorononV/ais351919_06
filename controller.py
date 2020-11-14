from flask import Flask, render_template, request
from user import Users

HOST_PORT="5001"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_users"},
        {"name": "POST", "url": "post_user"},
        {"name": "DELETE", "url": "delete_user"},
        {"name": "PUT", "url": "put_user"}]

@app.route("/")
def index():
    result = Users.get_users()
    return render_template("Users.html", title="Просмотр пользоватей", menu=menu, users=result)

@app.route('/get_users', methods=['GET'])
def get():
    result = Users.get_users()
    return render_template('Users.html', title="Просмотр пользоватей", menu=menu, users=result)

@app.route('/post_user', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        print(request.form)
        clients = Users.add_user(request.form["number"], request.form["firstname"], request.form["lastname"], request.form["midname"], request.form["birthday"])
    return render_template('post_user.html', title="Добавление пользователя", menu=menu)

@app.route('/delete_user', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        print(request.form)
        clients = Users.delete_user(int(request.form["number"]))
    return render_template('delete_user.html', title="Удаление пользователя", menu=menu)

@app.route('/put_user', methods=['POST', 'GET'])
def put():
    if request.method == 'POST':
        #print(request.form)
        clients = Users.update_user(request.form["number"], request.form["firstname"], request.form["lastname"], request.form["midname"], request.form["birthday"])
    return render_template('put_user.html', title="Обновление и информации о пользователе", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)