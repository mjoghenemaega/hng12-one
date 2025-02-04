 💻# Number Classification API

## Overview
The **Number Classification API** is a Django-based API that classifies numbers based on their properties. It determines whether a given number is prime, perfect, odd/even, Armstrong, and provides a fun fact about the number.

## Features
- Checks if a number is **prime**.
- Checks if a number is **perfect**.
- Determines whether a number is **odd** or **even**.
- Identifies if a number is an **Armstrong number**.
- Calculates the **sum of the digits**.
- Fetches a **fun fact** about the number from [NumbersAPI](http://numbersapi.com/).

## API Endpoint
### GET `/api/classify-number`

#### Request Parameters
| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| number    | int    | Yes      | The number to be classified. |

#### Example Request
```sh
GET http://127.0.0.1:8000/api/classify-number?number=28
```

#### Response Format
```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even"],
  "digit_sum": 10,
  "fun_fact": "28 is a perfect number, as it is the sum of its proper divisors."
}
```

#### Error Responses
| Scenario | Response |
|----------|----------|
| No number provided | `{ "number": "Number is required!", "error": true }` |
| Invalid input | `{ "number": "abc", "error": true }` |

## Installation & Setup
### Prerequisites
- Python 3.x
- Django

### Steps to Install
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/number-classification-api.git
   cd number-classification-api
   ```
2. Create a virtual environment:
   ```sh
   virtualenv env
   env/scripts/activate  # On mac , use 'source env/bin/activate '
   ```
3. Install dependencies:
   ```sh
   pip install django requests django-cors-headers
   ```
4. Run migrations:
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Start the server:
   ```sh
   python manage.py runserver
   ```
6. Access the API at `http://127.0.0.1:8000/api/classify-number`.


