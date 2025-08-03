from flask import Flask, request, jsonify
from kociemba import solve

app = Flask(__name__)

# ✅ Health check route (homepage)
@app.route("/")
def home():
    return "✅ Kociemba Solver API is running."

# ✅ API endpoint to solve cube
@app.route("/solve", methods=["POST"])
def solve_cube():
    data = request.get_json()
    if not data or "input" not in data:
        return jsonify({"error": "Missing 'input' in request body"}), 400
    try:
        solution = solve(data["input"])
        return jsonify({"solution": solution})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ✅ Local development
if __name__ == "__main__":
    app.run(debug=True)
