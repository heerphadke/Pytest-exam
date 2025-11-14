from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/status")
def status():
    return jsonify({"status": "ok"})

@app.route("/sum")
def sum_numbers():
    a = request.args.get("a")
    b = request.args.get("b")
    if a is None or b is None:
        return jsonify({"error": "missing params"}), 400
    try:
        a, b = float(a), float(b)
    except:
        return jsonify({"error": "invalid numbers"}), 400
    return jsonify({"result": a + b})

if __name__ == "__main__":
    app.run()
