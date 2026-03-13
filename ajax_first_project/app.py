from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/get-message')
def get_message():
    data = {
        "message": "Hello User, What about your day! 😊 Good"
    }
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)