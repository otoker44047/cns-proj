from flask import Flask, request, redirect, Response, jsonify, send_file

HOSTNAME = "mylocal"
PORT = 8081
BASE_URL = f"https://{HOSTNAME}:{PORT}"

app = Flask(__name__)

@app.route("/loopA", methods=["POST"])
def loop_a():
    return redirect(f"{BASE_URL}/loopB", code=307)

@app.route("/loopB", methods=["POST"])
def loop_b():
    return redirect(f"{BASE_URL}/loopA", code=307)

@app.route("/self", methods=["POST"])
def self_redirect():
    return redirect(f"{BASE_URL}/self", code=307)

@app.route("/echo", methods=["POST"])
def echo():
    return jsonify(headers=dict(request.headers),
                   body=request.get_data(as_text=True))
@app.route("/file", methods=["POST"])
def get_file():
    file_path = 'random.bin'
    return send_file(
        file_path,
        mimetype='application/octet-stream',
        as_attachment=True,
        download_name='random.bin'
    )

if __name__ == "__main__":
    context = ("mylocal.pem", "mylocal-key.pem")
    app.run(host="0.0.0.0", port=PORT, ssl_context=context, debug=True)

