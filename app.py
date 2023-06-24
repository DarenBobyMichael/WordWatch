from flask import Flask, render_template, request, redirect, session
import filtering_GPT
from firebase_admin import auth

app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def login():
#     email = request.form['email']
#     password = request.form['password']

#     try:
#         user = auth.get_user_by_email(email)
#         auth.sign_in_with_email_and_password(email, password)
#         return redirect('/main_page')
#     except auth.AuthError:
#         return render_template('index.html', message='Invalid credentials.')


@app.route('/main_page', methods=['GET', 'POST'])
def main_page():
    if request.method == 'POST':
        text = request.form.get('text')
        filtered_text = filtering_GPT.filter_(text)
        return render_template('main_page.html', output=filtered_text)
    
    return render_template('main_page.html')




if __name__ == '__main__':
    app.run(debug=True)
