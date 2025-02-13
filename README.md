# Number Classification API
This project provides an API that takes a number and returns interesting mathematical properties about it, including:
- Whether the number is prime
- Whether the number is perfect
- Whether the number is an Armstrong number
- The sum of its digits
- A fun fact about the number

The API responds with the information in JSON format and also offers an endpoint for getting a fun fact using the Numbers API.
## Technologies Used:
- Python
- Flask
- Requests (for calling Numbers API)
- JSON
- Flask-CORS (for CORS handling)
## API Specification:

### Endpoint:
- `GET /api/classify-number?number={number}`

### Parameters:
- `number`: A positive integer (query parameter)

### Response Format (200 OK):
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```
# Error Response (400 Bad Request):
```
{
    "number": "alphabet",
    "error": true
}
```


---

### 5. **Setup and Installation**:
- Provide clear steps on how to set up and run the project locally. This can include installing dependencies, setting up the environment, and running the server.

**Example**:
```markdown
## Setup and Installation:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/number-classification-api.git
   cd number-classification-api
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Flask app:
   ```bash
   python app.py
   ```

5. Access the API locally at:
   ```
   http://127.0.0.1:5000
   ```

**Note**: Replace `app.py` with your main application file name if different.
## Usage:

To classify a number, make a GET request to the endpoint:

GET http://127.0.0.1:5000/?number=371

Example response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}
```

If the number is invalid, you'll receive an error response:

```

{
    "number": "hello",
    "error": true
}
```


---

### 7. **Contributing**:
- Mention how others can contribute to the project (if open-source).

**Example**:
```markdown
## Contributing:

1. Fork the repository.
2. Create a new branch for your feature or fix.
3. Commit your changes.
4. Push your branch to your fork.
5. Open a Pull Request to the main repository.

 
