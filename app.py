from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV file once
df = pd.read_csv("2027 Btech cse sem-2 cgpa list LF SBB.csv")

@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if request.method == "POST":
        search_key = request.form["search_key"]  # e.g. Name, Regd No., etc.
        search_value = request.form["search_value"].strip()

        if search_key in df.columns:
            if search_key == "Name":  # multiple results for Name
                results = df[df[search_key].str.contains(search_value, case=False, na=False)].to_dict(orient="records")
            else:  # exact match for others
                results = df[df[search_key].astype(str).str.strip().str.lower() == search_value.lower()].to_dict(orient="records")

    return render_template("index.html", results=results, columns=df.columns)

if __name__ == "__main__":
    app.run(debug=True)