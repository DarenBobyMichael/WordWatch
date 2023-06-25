from flask import Flask, render_template, request, redirect, session,url_for
import filtering_GPT
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'


conn = sqlite3.connect('users.db', check_same_thread=False)
c = conn.cursor()
conn.commit()


@app.route('/')
def home():
    return redirect('/login')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        print(email)
        print(password)
        # Check if the username and password match the database
        c.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = c.fetchone()
        
        if user is not None:
            session['email'] = email
            return redirect('/main_page')
        else:
            error = 'Invalid email or password. Please try again.'
            return render_template('login.html', error=error)
    
    return render_template('login.html')

@app.route('/main_page', methods=['GET', 'POST'])
def main_page():

    if 'email' in session:
        text = request.form.get('text')
        if text == None:
            text=' '
        filtered_text = filtering_GPT.filter_(text)
        return render_template('main_page.html', output=filtered_text)
    
    else:
        return redirect('/login')
        # else:
        #     return redirect('/')
    # return redirect('/')
    # if request.method == 'POST':
    #     text = request.form.get('text')
    #     filtered_text = filtering_GPT.filter_(text)
    #     return render_template('main_page.html', output=filtered_text)
    
    # return render_template('main_page.html')




if __name__ == '__main__':
    app.run(debug=True,port=2000)
