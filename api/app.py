from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

@app.route("/health")
def health():
	return  {"status": "ok"}

def get_conn():
	return pymysql.connect(
		host=os.getenv("DB_HOST"),
		user=os.getenv("DB_USER"),
		password=os.getenv("DB_PASSWORD"),
		database=os.getenv("DB_NAME"),
		port=int(os.getenv("DB_PORT")),
		cursorclass=pymysql.cursors.DictCursor
	)

@app.route("/clients")
def clients():
    try:
        conn = get_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients")
        result = cur.fetchall()
        conn.close()
        return jsonify(result)
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
