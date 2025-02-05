from flask import Flask, jsonify, request
import requests
from flask_cors import CORS


def is_perfect(number):
    """
    Check if a number is a perfect number.

    Args:
        number (int): The number to check.

    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    if number < 0:
        return False  # Negative numbers cannot be perfect numbers
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
        return False  # Negative numbers and numbers less than 2 cannot be prime
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
    if n < 0:
        return False  # Armstrong numbers are typically positive, so reject negative numbers
    
    power = len(str(abs(n)))  # Consider absolute value for calculating power
    digits = [int(d) ** power for d in str(abs(n))]  # Use absolute value for digits
    return sum(digits) == abs(n)  # Compare the sum with the absolute value of n

app = Flask(__name__)
CORS(app)

@app.route("/api/classify-number", methods=["GET"])
def classy_numb():
    try:
        num = request.args.get("number")  # 'num' should be a string
        if not num or not num.isdigit() and not (num[0] == '-' and num[1:].isdigit()):
            response = {
                "error": True,
                "num": "num"
            }
            return jsonify(response), 400

        num = int(num)

        # Properties
        parity = "even" if num % 2 == 0 else "odd"
        sum_digit = sum(int(d) for d in str(abs(num)))  # Consider absolute value of number
        armstrong = is_armstrong(num)
        properties = ["armstrong", parity] if armstrong else [parity]

        # Fun fact (external API)
        base_url = "http://numbersapi.com/"
        fact_response = requests.get(f"{base_url}/{num}/math")
        fun_fact = fact_response.text if fact_response.status_code == 200 else f"No fact available for {num}"

        json_response = {
            "number": num,
            "is_prime": is_prime(num),
            "is_perfect": is_perfect(num),
            "properties": properties,
            "digit_sum": sum_digit,  # Sum of digits (positive sum)
            "fun_fact": fun_fact
        }

        return jsonify(json_response), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
