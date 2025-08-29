from flask import Flask, request, jsonify

app = Flask(__name__)

FULL_NAME = "john_doe"
DOB = "17091999"   # ddmmyyyy
EMAIL = "john@xyz.com"
ROLL = "ABCD123"


@app.route("/bfhl", methods=["POST"])
def bfhl():
    try:
        data = request.get_json().get("data", [])

        if not isinstance(data, list):
            return jsonify({"is_success": False, "message": "Invalid input"}), 400

        odd_numbers = []
        even_numbers = []
        alphabets = []
        special_characters = []
        total_sum = 0
        concat_str = ""

        for item in data:
            if str(item).lstrip("-").isdigit():  # number check
                num = int(item)
                total_sum += num
                if num % 2 == 0:
                    even_numbers.append(str(item))
                else:
                    odd_numbers.append(str(item))
            elif str(item).isalpha():  # alphabets only
                alphabets.append(str(item).upper())
                concat_str += str(item)
            else:
                special_characters.append(str(item))

        # Reverse + alternating caps
        rev = list(concat_str[::-1])
        alt_caps = "".join(
            ch.upper() if i % 2 == 0 else ch.lower()
            for i, ch in enumerate(rev)
        )

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": alt_caps,
        }

        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "message": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to Flask API. Use POST /bfhl"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
