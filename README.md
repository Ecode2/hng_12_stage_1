# Stage 1 Backend - Number Classification API

This project is a Django-based API that accepts a number via a GET request and returns a JSON response containing mathematical properties and a fun fact about the number.

---

## Project Description

The API takes a query parameter `number` and returns the following information:

- **number**: The provided integer.
- **is_prime**: A boolean indicating if the number is prime.
- **is_perfect**: A boolean indicating if the number is a perfect number (for this task, simply determined by evenness).
- **properties**: A list indicating whether the number is "armstrong" and whether it is "even" or "odd".  
  - Examples:
    - `["armstrong", "odd"]`
    - `["armstrong", "even"]`
    - `["odd"]`
    - `["even"]`
- **digit_sum**: The sum of the digits of the number.
- **fun_fact**: A fun fact about the number retrieved from the [Numbers API](http://numbersapi.com/#42).

Invalid inputs result in a 400 Bad Request response with an appropriate error message.

---

## API Specification

### Endpoint

```
GET /api/classify-number?number=<number>
```

### Successful Response (200/201 OK)

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

### Error Response (400 Bad Request)

```json
{
    "number": "alphabet",
    "error": true,
    "message": "query parameter must be number"
}
```

---

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Ecode2/hng_12_stage_1.git
cd hng_12_stage_1
```

### 2. Create and Activate a Virtual Environment

For Linux/macOS:

```bash
python -m venv venv
source venv/bin/activate
```

For Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

Create a **.env** file in the project root with settings similar to:

```
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost,hng-stage1-96c03cc41e90.herokuapp.com
```

---

## Running the Project

### 1. Apply Migrations

```bash
python manage.py migrate
```

### 2. Start the Development Server

```bash
python manage.py runserver
```

The API will be accessible at: [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Testing the API

You can test the API using cURL or Python’s requests module.

### Using cURL

```bash
curl -X GET "http://127.0.0.1:8000/api/classify-number?number=371"
```

### Using Python

```python
import requests

response = requests.get("http://127.0.0.1:8000/api/classify-number", params={"number": 371})
print(response.json())
```
