from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    input_shape = request.form.get("shape")
    selected_option = request.form.get("can_you_drive")
    return render_template(
        "hello.html",
        name=input_name,
        age=input_age,
        shape=input_shape,
        option=selected_option,
    )
