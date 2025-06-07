from flask import Flask, request, render_template
from chat_engine import get_response_from_query

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def chat():
    response = ""
    query = ""
    if request.method == "POST":
        query = request.form["query"]
        response = get_response_from_query(query)
    return render_template("chat.html", response=response, query=query)

if __name__ == "__main__":
    app.run(debug=True)
