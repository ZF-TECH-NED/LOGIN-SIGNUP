from flask import Flask, request, render_template ,jsonify

app = Flask(__name__)

@app.route("/formlogin", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        uname = request.form['login_username']
        password = request.form['login_password']
        if uname == "admin" and password == "123":
            return "Welcome " + uname
        else:
            return "Try again"
    else:
        return render_template('form.html')
    


#add signup functionality


users = []
print(users)

@app.route('/signup', methods=['POST','GET'])
#@app.post('/signup')
def create_user():
    if request.method == "POST":
        
        name = request.form['name']
        email = request.form['email']
        password=request.form['password']
        new_user = {'name': name, 'email': email, 'password':password}
        users.append(new_user)
       
        return jsonify(new_user), 202
    else:
        return render_template('form.html')
print(users)



if __name__ == '__main__':
    app.run(debug=True)