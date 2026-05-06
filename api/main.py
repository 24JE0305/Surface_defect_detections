from fastapi import FastAPI
import psycopg2

app = FastAPI()

@app.get('/detections')
def get_detections():

    conn = psycopg2.connect(
        host='localhost',
        port=5432,
        database='testdb',
        user='postgres',
        password='@tendtoS8'
    )
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM detections")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return [
    {
        "id": row[0],
        "timestamp": str(row[1]),
        "defect_class": row[2],
        "confidence": row[3],
        "image_path": row[4]
    }
    for row in rows
]