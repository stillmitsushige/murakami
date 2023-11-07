from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    checked_know = ''
    checked_not_know = ''
    if request.method == 'POST':
        if 'choice' in request.form:
            if request.form['choice'] == 'know':
                result = 'お笑いについてカルチャーを理解している可能性があります'
                checked_know = 'checked'
            else:
                result = 'ノーカルチャーです。指導を受けてください'
                checked_not_know = 'checked'
        else:
            result = '選択肢を選んでください'
    return render_template('index.html', result=result, checked_know=checked_know, checked_not_know=checked_not_know)

if __name__ == '__main__':
    app.run(debug=True)