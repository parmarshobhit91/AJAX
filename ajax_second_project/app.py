from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

items = [
    "C",
    "C++",
    "Java",
    "Json",
    "Python",
    "Pytorch",
    "Shobhit",
    "Shrasti",
    "Shriyash",
    "Shivam",
    "Dewas"
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/search')
def search_items():
    query = request.args.get('q', '').lower()

    results = []

    for item in items:
        if query in item.lower():
            results.append(item)
    
    return jsonify(results)


if __name__ == '__main__':
    app.run(debug=True)