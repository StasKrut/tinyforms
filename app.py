import re

from flask import Flask, jsonify, request
from tinydb import TinyDB

from utils import DATE, EMAIL, PHONE

app = Flask(__name__)
db = TinyDB("./forms.json")


# Создание шаблона формы
@app.route("/create_template", methods=["POST"])
def create_template():
    template = request.json
    db.truncate()
    db.insert(template)
    return jsonify({"message": "Template created successfully"})


@app.route("/get_form", methods=["POST"])
def get_form():
    patterns = {EMAIL: "email", PHONE: "phone", DATE: "date"}
    data = request.form
    field_values = list(data.values())
    # Определение типов полей заполненной формы
    template_fields = [
        patterns[pattern]
        for pattern in patterns
        for val in field_values
        if re.match(pattern, val)
    ]
    # Поиск подходящего шаблона формы
    for template in db:
        if set(template_fields).issubset(set(template.values())):
            return jsonify({"template_name": template["name"]})
    return jsonify(dict(zip(["f_name1", "f_name2"], template_fields)))


if __name__ == "__main__":
    app.run(debug=True)
