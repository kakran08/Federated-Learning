from server import Server
from flask import Flask, request

app = Flask(__name__)
server_kali = Server("Federated Server", "model", app.logger)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Home Page
    """
    if request.method == "POST":
        # Try to get JSON data; if not present, fall back to form data.
        data = request.get_json(silent=True) or request.form
        if data.get("send") == "True":
            server_kali.validate_update_data(data)
            return "Success"
        else:
            return server_kali.read_weights()
    else:  # GET request
        if request.args.get("send") == "True":
            server_kali.validate_update_data(request.args)
            return "Success"
        else:
            return server_kali.read_weights()

def main():
    app.run(debug=True, threaded=True)

if __name__ == "__main__":
    main()