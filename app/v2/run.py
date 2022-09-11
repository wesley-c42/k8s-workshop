from flask import Flask, request, abort

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def index():
    return "Ciao, mondo!", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)