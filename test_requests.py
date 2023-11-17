import requests


# Запрос на определение шаблона формы для переданных данных
def test_request(forms):
    for data in forms:
        response = requests.post("http://localhost:5000/get_form", params=data)
        print(response.json())


def main():
    forms = (
        {
            "field_name1": "email@example.com",
            "field_name2": "+7 123 456 78 90",
            "created_at": "2023-11-15",
        },
        {
            "field_name_1": "email@example.com",
            "field_name_2": "+7 123 456 78 90",
            "created_at": "2023-11-15",
        },
        {"field_name_1": "+7 123 456 78 90", "field_name_2": "15.11.2023"},
        {"created_at": "2023-11-15", "user_email": "email@example.com"},
        {"field_name_1": "+7 123 456 78 90"},
    )
    test_request(forms)


if __name__ == "__main__":
    main()
