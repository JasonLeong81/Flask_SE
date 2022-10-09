from flask import Flask, render_template

app = Flask(__name__, template_folder='template',static_folder='template/static')


# @app.route('/')
# @app.route('/index')
@app.route('/testing')
def index():
	return render_template('index.html')

# this is so the app won't run if the file is imported somewhere, run using a different methed, etc.
if __name__ == '__main__':
	app.run('127.0.0.1', port=8080, debug=True)  #