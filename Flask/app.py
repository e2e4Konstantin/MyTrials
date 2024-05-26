import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return ("Hello main")

@app.route("/hello/<user>")
def hello(user: str):
    return (f"Hello {user}")

# if __name__ == '__main__':
#     app.run(debug=True)


@app.route("/get_flask_version")
def get_flask_version():
    return {"version":Flask.__version__}
