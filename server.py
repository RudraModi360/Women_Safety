from flask import Flask, request, jsonify, render_template
import util

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        Area_name = request.form.get("dropdownButton", "Waghodiya Road")
        Safe_unsafe = util.predict_safety(Area_name)

        return render_template('base.html', Safe_unsafe=Safe_unsafe)
    else:
        Area_name = util.get_Area_names()
        return render_template("base.html", Area_name=Area_name)

@app.route("/get_Area_names", methods=["GET"])
def get_location_names():
    Area_name = util.get_Area_names()
    return render_template("base.html", Area_name=Area_name)

if __name__ == "__main__":
    print("Starting the python flask server for home prediction model...")
    util.load_data()
    app.run(debug=True)
