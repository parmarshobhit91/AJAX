from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/send', methods=['POST'])
def send():

    sender = request.form.get("sender")
    receiver = request.form.get("receiver")
    message = request.form.get("message")

    messages.append({
        "sender": sender,
        "receiver": receiver,
        "message": message
    })

    return jsonify({"status": "ok"})


@app.route('/messages')
def get_messages():

    user1 = request.args.get("user1")
    user2 = request.args.get("user2")

    chat = []

    for msg in messages:

        if (msg["sender"] == user1 and msg["receiver"] == user2) or \
           (msg["sender"] == user2 and msg["receiver"] == user1):

            chat.append(msg)

    return jsonify(chat)


if __name__ == "__main__":
    app.run(debug=True)