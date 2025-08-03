from flask import Flask, request, jsonify
import kociemba

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve_cube():
    data = request.get_json()
    facelets = data.get('facelets', '')
    try:
        solution = kociemba.solve(facelets)
        return jsonify({'solution': solution})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run()