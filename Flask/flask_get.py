# pip install Flask-WTF
# pip install email_validator

from typing import Optional
from flask import Flask, request, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange # https://wtforms.readthedocs.io/en/2.3.x/validators/
from urllib.parse import unquote_plus
import json


app = Flask(__name__)

@app.route("/search/", methods=["GET"])
def search():
    cell_tower_ids: list[int] = request.args.getlist("cell_tower_id", type=int)
    if not cell_tower_ids:
        return "You mast specify at least one cell_tower_id", 400
    phone_prefixes: list[str] = request.args.getlist("phone_prefix")
    protocol: list[str] = request.args.getlist("protocol")
    signal_level: Optional[float] = request.args.get("signal_level", type=float, default=None)

    return (
        f"Search for {cell_tower_ids} cell towers. Criteria: "
        f"{phone_prefixes=} "
        f"{protocol=} "
        f"{signal_level=} "
            )

@app.route("/sum/", methods=["POST"])
def _sum():
    arr_1 = request.form.getlist("arr1", type=int)
    arr_2 = request.form.getlist("arr2", type=int)

    result = ",".join(str(a1+a2) for (a1, a2) in zip(arr_1, arr_2))

    return f"arr_sum: {result}"


@app.route("/sumx/", methods=["POST"])
def sumx():
    x = request.get_data(as_text=True)
    print(f'--> {x}\n{unquote_plus(x)}')
    arrays = {}
    for encoded_chunk in unquote_plus(x).split("&"):
        k, v = encoded_chunk.split("=")
        arrays[k] = [int(it) for it in v.split(",")]

    result = ",".join(str(a1+a2) for (a1, a2) in zip(arrays['arr1'], arrays['arr2']))

    return f"--> {result}"


@app.route("/sum_json/", methods=["POST"])
def sum_json():
    x = request.get_data(as_text=True)
    data = json.loads(x)

    result = ",".join(str(a1+a2) for (a1, a2) in zip(data['arr1'], data['arr2']))

    return f"--> {result}"

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberRange(min=100_00_00_000, max=999_99_99_999)])
    name = StringField(validators=[InputRequired()])

    def validate_email(self, email: Optional[str]) -> None:
        if email is None:
            raise ValueError("email is None")

    def validate_phone(self, phone: Optional[int]) -> None:
        if phone is None:
            raise ValueError("phone is None")


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()
    if not form.is_submitted():
        return "form is not submitted", 400
    if not form.validate():
        return "form is not valid", 400
    email = form.email.data
    phone = form.phone.data
    name = form.name.data
    if email is None or phone is None or name is None:
        return "null pointer references", 500
    return f"--> {email}, {phone}, {name}"







def run_flask_app(debug: bool = True, **kwargs: Any) -> Flask:
    """
    Run the flask app.

    Args:
        debug: If True, flask will run in debug mode.
        kwargs: Keyword arguments to pass to Flask.run

    Returns:
        The app that was run
    """
    app.config["WTF_CSRF_ENABLED"] = False
    return app.run(debug=debug, **kwargs)


if __name__ == "__main__":
    run_flask_app(debug=True)
