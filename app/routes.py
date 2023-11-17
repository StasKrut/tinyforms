import re

from flask import jsonify, request
from tinydb import TinyDB

from app import app
from app.utils import DATE, EMAIL, PHONE

db = TinyDB("./forms.json")


@app.route("/get_form", methods=["POST"])
def get_form():
    pattern_types = {DATE: "date", PHONE: "phone", EMAIL: "email"}
    data = request.args
    if not data:
        return jsonify({"message": "Form is empty"})
    # Валидация типов значений формы
    form_types = {}
    for field, val in data.items():
        field_types = [
            field_type
            for pattern, field_type in pattern_types.items()
            if re.match(pattern, val)
        ]
        if len(field_types) == 1:
            form_types[field] = field_types[0]
        else:
            form_types[field] = "text"
    # Поиск подходящего шаблона формы
    for template in db:
        template_name = template.pop("name")
        if set(template.items()).issubset(set(form_types.items())):
            return jsonify({"template_name": template_name})
    return jsonify(form_types)
