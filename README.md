# Kociemba Solver API (Self-Hosted)

This is a lightweight Flask-based API for solving a Rubik's Cube using the Kociemba algorithm.

## 🔧 Requirements
- Python 3.x
- pip

## 📦 Setup Instructions

1. Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python app.py
```

The server will start at `http://127.0.0.1:5000/`

---

## ✅ How to Use

### POST `/solve`

- **URL:** `http://127.0.0.1:5000/solve`
- **Method:** `POST`
- **Body (JSON):**

```json
{
  "facelets": "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
}
```

- **Response:**

```json
{
  "solution": "R U R' U R U2 R'"
}
```

### Root `/`

- `GET http://127.0.0.1:5000/` — returns status message.

---

## 🧠 Notes

- Make sure the facelet string is exactly 54 characters.
- Each letter typically stands for a face color:
  - U = Up (White)
  - R = Right (Red)
  - F = Front (Green)
  - D = Down (Yellow)
  - L = Left (Orange)
  - B = Back (Blue)

---

## 🧪 Test using curl

```bash
curl -X POST http://127.0.0.1:5000/solve \
     -H "Content-Type: application/json" \
     -d '{"facelets":"UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"}'
```

