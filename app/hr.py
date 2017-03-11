from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    current_app,
    session,
)
import os

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("construction.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8400, debug=True)
