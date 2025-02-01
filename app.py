# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# import json

# app = FastAPI()

# # Enable CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Load data from JSON file
# with open("q-vercel-python.json", "r") as f:
#     students_data = json.load(f)

# students_dict = {student["name"]: student["marks"] for student in students_data}

# @app.get("/api")
# def get_marks(name: list[str]):
#     marks = [students_dict.get(n, "Not Found") for n in name]
#     return {"marks": marks}



from flask import Flask, request, jsonify
from fastapi.middleware.cors import CORSMiddleware, CORS
import json

# Initialize Flask app
app = Flask(__name__)

# # Enable CORS
# CORS(app)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("q-vercel-python.json", "r") as f:
    students_data = json.load(f)

students_marks = {student["name"]: student["marks"] for student in students_data}


@app.route("/api", methods=["GET"])
def get_marks():
    # Extract the names from query parameters
    names = request.args.getlist('name')

    if not names:
        return jsonify({"error": "No student names provided."}), 400

    marks = []
    for name in names:
        mark = students_marks.get(name)
        if mark is None:
            marks.append({"name": name, "error": "Not Found"})
        else:
            marks.append({"name": name, "marks": mark})

    return jsonify({"marks": marks})

if __name__ == "__main__":
    app.run(debug=True)
