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
        if not number.isdigit():
            return JsonResponse({"number": number, "error": True}, status=400)

        number = int(number)
        is_prime = self.is_prime(number)
        is_perfect = self.is_perfect(number)
        properties = self.get_properties(number)
        digit_sum = sum(int(digit) for digit in str(number))
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
        return sum(i for i in range(1, n) if n % i == 0) == n

    def get_properties(self, n):
        is_armstrong = n == sum(pow(int(digit), len(str(n))) for digit in str(n))
        is_odd = n % 2 != 0
        if is_armstrong and is_odd:
            return ["armstrong", "odd"]
        elif is_armstrong:
            return ["armstrong", "even"]
        elif is_odd:
            return ["odd"]
        else:
            return ["even"]

    def get_fun_fact(self, n):
        url = f"http://numbersapi.com/{n}/math"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
        except requests.RequestException:
            pass
        return "Fun fact not available."
