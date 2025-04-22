from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form.get("name", "")
        if name.lower().startswith('a'):
            message = "Hello World!"
        else:
            message = f"Hello, {name}!"
        return render_template("home.html", message=message)
    return render_template("home.html", message=None)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
