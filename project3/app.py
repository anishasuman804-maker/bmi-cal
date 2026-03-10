from flask import Flask, render_template, request
app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("index.html")
    height = request.form.get("height")
    weight = request.form.get("weight")
    height = float(height)
    weight = float(weight)
    bmi = weight / (height * height)
    return render_template("index.html", bmi=bmi)
if __name__ == "__main__":
    app.run(port=5000)