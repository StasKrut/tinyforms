import requests


# Запрос на определение шаблона формы для переданных данных
def test_request(forms):
    for data in forms:
        response = requests.post("http://localhost:5000/get_form", data=data)
        print(response.json())


def main():
    forms = (
        {"f_name1": "email@example.com", "f_name2": "+7 123 456 78 90"},
        {"f_name1": "+7 123 456 78 90", "f_name2": "email@example.com"},
        {"f_name1": "+7 123 456 78 90", "f_name2": "15.11.2023"},
        {"f_name1": "15.11.2023", "f_name2": "email@example.com"},
    )
    test_request(forms)


if __name__ == "__main__":
    main()
