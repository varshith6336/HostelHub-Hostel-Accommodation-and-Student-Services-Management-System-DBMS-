import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)
CORS(app)  # Restrict allowed origins before public production deployment.

def get_connection():
    return mysql.connector.connect(host=os.getenv("DB_HOST", "127.0.0.1"), port=int(os.getenv("DB_PORT", "3306")), database=os.getenv("DB_NAME", "hostelhub"), user=os.getenv("DB_USER", "root"), password=os.getenv("DB_PASSWORD", ""))

@app.get("/api/health")
def health():
    try:
        conn=get_connection(); conn.close()
        return jsonify({"ok": True, "message": "Flask API connected to MySQL."})
    except Error:
        app.logger.exception("Database connection failed")
        return jsonify({"ok": False, "message": "Database connection failed. Check backend environment settings."}), 503

@app.get("/api/students")
def list_students():
    try:
        conn=get_connection(); cursor=conn.cursor(dictionary=True)
        cursor.execute("SELECT student_id, student_code, full_name, course, academic_year, phone, email, status FROM students ORDER BY student_id DESC")
        rows=cursor.fetchall(); cursor.close(); conn.close()
        return jsonify(rows)
    except Error:
        app.logger.exception("Could not read students")
        return jsonify({"error": "Could not read student records."}), 500

@app.post("/api/students")
def create_student():
    data=request.get_json(silent=True) or {}
    required=("student_code", "full_name", "course", "academic_year")
    missing=[key for key in required if not str(data.get(key, "")).strip()]
    if missing: return jsonify({"error":"Missing required fields", "fields":missing}), 400
    try:
        conn=get_connection(); cursor=conn.cursor()
        cursor.execute("INSERT INTO students (student_code, full_name, course, academic_year, phone, email, status) VALUES (%s,%s,%s,%s,%s,%s,%s)", (data["student_code"].strip(),data["full_name"].strip(),data["course"].strip(),data["academic_year"].strip(),data.get("phone"),data.get("email"),data.get("status","Pending")))
        conn.commit(); new_id=cursor.lastrowid; cursor.close(); conn.close()
        return jsonify({"message":"Student created", "student_id":new_id}), 201
    except mysql.connector.IntegrityError:
        return jsonify({"error":"Student code already exists."}), 409
    except Error:
        app.logger.exception("Could not create student")
        return jsonify({"error":"Could not save student record."}), 500

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=int(os.getenv("PORT", "5000")), debug=False)
