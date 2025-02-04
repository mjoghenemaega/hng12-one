Number Classification API

Overview

This API classifies numbers based on various mathematical properties, such as:

Checking if a number is prime.

Determining if a number is a perfect number.

Identifying if it is an Armstrong number.

Computing the sum of its digits.

Fetching a fun fact about the number using the Numbers API.

Installation

To run this project, you need to have Python and Django installed.

Clone the repository:

git clone https://github.com/your-repo/number-classification-api.git
cd number-classification-api

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Run the Django development server:

python manage.py runserver

Usage

API Endpoint

GET /api/classify-number?number={integer}

Example Request:

GET http://127.0.0.1:8000/api/classify-number?number=28

Example Response:

{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["even"],
    "digit_sum": 10,
    "fun_fact": "28 is the second perfect number."
}

Optimization Tips

Prime number checking: Implement more efficient algorithms like Miller-Rabin for larger numbers.

Caching: Store previous API responses to reduce external API calls.

Asynchronous requests: Use background tasks for slow operations.







Number Classification API

Overview

This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact fetched from the Numbers API.

Features

Determines if a number is prime.

Checks if a number is a perfect number.

Identifies if a number is an Armstrong number.

Classifies the number as odd or even.

Computes the sum of digits.

Fetches a fun fact from the Numbers API.

Technologies Used

Python

Django

Requests (for external API calls)

JSON Response Handling

Installation & Setup

Prerequisites

Ensure you have Python and pip installed. Then install the required packages:

pip install django requests

Running the Server

python manage.py runserver

API Endpoints

Number Classification

Request

GET /api/classify-number?number=<integer>

Successful Response (200 OK)

{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Response (400 Bad Request)

{
    "number": "alphabet",
    "error": true
}

Missing Number Parameter Response

{
    "error": "Number parameter is required"
}

Performance Optimization

Factors Affecting Response Time:

Network Latency – Minimized by caching API responses where possible.

External API Call (Numbers API) – Optimized by handling request failures gracefully.

Mathematical Computation Complexity – Optimized by using efficient algorithms for prime, perfect, and Armstrong number checks.

Ways to Improve Performance:

Implement request caching for repeated API calls.

Use asynchronous requests to fetch fun facts without blocking the main response.

Optimize database queries (if using one) and reduce redundant computations.

Deployment

To deploy this API, you can use:

Heroku

AWS Elastic Beanstalk

DigitalOcean App Platform

Vercel (For Django REST with Serverless setup)

Ensure CORS is handled properly to allow cross-origin requests.

License

MIT License.

Author

Moses Johnson Oghenemaega

