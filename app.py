from flask import Flask
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def form_pki():
    return render_template('index.html')

@app.route('/SSL_form')
def form_ssl():
    return render_template('SSL_form.html')

@app.route('/standard_form')
def standard_ssl():
    return render_template('standard_certificate_form.html')




if __name__ == '__main__':
    app.run()
