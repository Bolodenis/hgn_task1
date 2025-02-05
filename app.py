import requests
import json
from flask import Flask, jsonify, request
from flask_cors  import CORS


def is_perfect(number):
    """
    Check if a number is a perfect number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    num = [i for i in range(1, number) if number % i == 0]
    return sum(num) == number

def is_prime(n):
    """
    A function that checks for prime numbers.

    Args:
        n (int): A positive number to check.

    Returns:
        bool: True if the number is prime, otherwise False.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_armstrong(n):
    """
    Check if a number is an Armstrong number.
    An Armstrong number is a number that is equal to the sum of its digits each raised to the power of the number of digits in the number.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    power = len(str(n))
    digits = [int(d) ** power for d in str(n)]
    return sum(digits) == n

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def classy_numb():
    try:
        num = request.args.get("num")  # 'num' should be a string
        if not num or not num.isdigit():
            response = {
                "error": True,
                "num": "num"
            }
            return jsonify(response), 400

        num = int(num)

        # Properties
        parity = "even" if num % 2 == 0 else "odd"
        sum_digit = sum(int(d) for d in str(num))
        armstrong = is_armstrong(num)
        properties = ["armstrong", parity] if armstrong else [parity]

        # Fun fact (external API)
        base_url = "http://numbersapi.com/"
        fact_response = requests.get(f"{base_url}/{num}/math")
        fun_fact = fact_response.text if fact_response.status_code == 200 else "No fact available"

        json_response = {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": sum_digit,
            "fun_fact": fun_fact
        }

        return jsonify(json_response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
