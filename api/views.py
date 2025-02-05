import requests
from math import pow, isqrt
from django.http import JsonResponse
from django.views import View

class NumberClassificationAPI(View):
    def get(self, request):
        number = request.GET.get("number")

        # Validate input
        if not number:
            return JsonResponse({"number": "Number is required!", "error": True}, status=400)

        try:
            number = int(number)
        except ValueError:
            return JsonResponse({"number": number, "error": True, "message": "Invalid number format!"}, status=400)

        is_prime = self.is_prime(number)
        is_perfect = self.is_perfect(number)
        properties = self.get_properties(number)
        digit_sum = sum(abs(int(digit)) for digit in str(number) if digit.isdigit())  # Ensure digits are positive
        fun_fact = self.get_fun_fact(number)

        return JsonResponse({
            "number": number,
            "is_prime": is_prime,
            "is_perfect": is_perfect,
            "properties": properties,
            "digit_sum": digit_sum,
            "fun_fact": fun_fact
        })

    def is_prime(self, n):
        if n < 2:
            return False
        for i in range(2, isqrt(n) + 1):
            if n % i == 0:
                return False
        return True

    def is_perfect(self, n):
        return n > 0 and sum(i for i in range(1, n) if n % i == 0) == n

    def get_properties(self, n):
        abs_n = abs(n)  # Work with absolute value
        is_armstrong = abs_n == sum(pow(int(digit), len(str(abs_n))) for digit in str(abs_n))
        is_odd = n % 2 != 0
        properties = []

        if is_armstrong:
            properties.append("armstrong")
        properties.append("odd" if is_odd else "even")

        return properties

    def get_fun_fact(self, n):
        url = f"http://numbersapi.com/{abs(n)}/math"  # Use absolute value for facts
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            pass
        return "Fun fact not available."
