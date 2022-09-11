from flask import Flask, request, abort
import os

app = Flask(__name__)
app.url_map.strict_slashes = False

page_reply = os.environ.get("PAGE_REPLY", "missing")

if page_reply == "missing":
    print(f'Environment variable PAGE_REPLY is missing!')
    exit()

@app.route('/', methods=['GET'])
def index():
    return f"Hello, world! Master has given Dobby an environment variable: {page_reply}", 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8080", debug=True)