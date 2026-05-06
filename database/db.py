import psycopg2
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def get_connection():
    return psycopg2.connect(
        host     = os.getenv('DB_HOST'),
        port     = os.getenv('DB_PORT'),
        database = os.getenv('DB_NAME'),
        user     = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD')
    )

def save_detection(defect_class,conf,img_path,x,y,w,h):
    
    conn= get_connection()

    cursor = conn.cursor()

    query = """
        INSERT INTO detections 
        (defect_class, confidence, image_path, x_center, y_center, width, height)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (defect_class,conf,img_path,x,y,w,h)

    cursor.execute(query,values)
    conn.commit()

    cursor.close()
    conn.close()
    print(f"Saved: {defect_class} | confidence: {conf:.2f}")

def clear_detections():

    conn = get_connection()
    cursor = conn.cursor()

    # TRUNCATE empties the table instantly
    cursor.execute("TRUNCATE TABLE detections RESTART IDENTITY;")
    
    conn.commit()
    cursor.close()
    conn.close()
    print("Table 'detections' cleared and ID counter reset.")


# for testing
if __name__ == '__main__':
    save_detection(
        defect_class = 'crazing',
        conf   = 0.90,
        img_path   = 'data/validation/images/crazing_1.jpg',
        x = 0.5,
        y = 0.4,
        w = 0.3,
        h = 0.2
    )