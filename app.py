from flask import Flask, render_template, request
import filtering_GPT


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form.get('text')
        capitalized_text = filtering_GPT.filter_(text)
        return render_template('main_page.html', output=capitalized_text)
    
    return render_template('main_page.html')

if __name__ == '__main__':
    app.run(debug=True)
