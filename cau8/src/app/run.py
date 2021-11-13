from flask import Flask
import sys


app = Flask(__name__)


@app.route("/", methods=['GET'])
def wellcome():
    return "Helluuuu !!!"


if __name__ == "__main__":
    try:
        port = int(sys.argv[1])
    except (TypeError, IndexError):
        port = 8080
    print(port)
    app.run(debug=True, port=port)
