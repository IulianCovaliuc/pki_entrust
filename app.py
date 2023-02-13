from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def form_pki():
    return render_template('form.html')



if __name__ == '__main__':
    app.run()
