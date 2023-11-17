from app.routes import db


def create_template(templates):
    db.truncate()
    for template in templates:
        db.insert(template)
    return {"message": "Templates created successfully"}


def main():
    templates = (
        {"name": "MyForm", "field_name_1": "email", "field_name_2": "phone"},
        {
            "name": "FoundationForm",
            "user_email": "email",
            "created_at": "date",
        },
    )
    print(create_template(templates))


if __name__ == "__main__":
    main()
