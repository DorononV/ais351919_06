from flask import Flask, render_template, request
from kompl_and_st import Kompl_n_st

HOST_PORT="5008"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dvw4wg4dv4ytd4vwr3dwy'

menu = [{"name": "GET", "url": "get_komplnst"},
        {"name": "POST", "url": "post_komplnst"},
        {"name": "DELETE", "url": "delete_komplnst"}]

@app.route("/")
def index():
    result = Kompl_n_st.get_kompl_n_st()
    return render_template("Kompl_n_stan/k_n_st.html", title="Комплектующие к станкам", menu=menu, kompl_n_sts=result)

@app.route('/get_komplnst', methods=['GET'])
def get():
    result = Kompl_n_st.get_kompl_n_st()
    return render_template('Kompl_n_stan/k_n_st.html', title="Просмотр комплектующих к станкам", menu=menu, kompl_n_sts=result)

@app.route('/post_komplnst', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        kompl_n_st = Kompl_n_st.add_kompl_n_st(request.form["number"], request.form["kompl"])
    return render_template('Kompl_n_stan/post_k_n_st.html', title="Добавление комплектующих к станкам", menu=menu)

@app.route('/delete_komplnst', methods=['POST', 'GET'])
def delete():
    if request.method == 'POST':
        kompl_n_st = Kompl_n_st.delete_kompl_n_st(int(request.form["number"]), int(request.form["kompl"]))
    return render_template('Kompl_n_stan/delete_k_n_st.html', title="Удаление комплектующих к станкам", menu=menu)

if __name__ == '__main__':
    app.run(port=HOST_PORT)