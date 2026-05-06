import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


#------------------------/=======/-------------------------------

from ultralytics import YOLO
from database.db import save_detection,clear_detections
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def detect_and_save(model,image_path):

    results = model.predict(
        source=image_path,
        save=True,
        conf=0.25,
        project='tries',
        name='hope'
    )
    for r in results:
        for box in r.boxes:
            class_id = int(box.cls)
            defect_class = model.names[class_id] 

            confidence = float(box.conf)

            coords = box.xywhn[0]
            x = float(coords[0])
            y = float(coords[1])
            w = float(coords[2])
            h = float(coords[3])
            
            save_detection(defect_class, confidence, image_path, x, y, w, h)


## for testing
if __name__ == '__main__':

    model_path = os.path.join(BASE_DIR,'models','defect_detector6','weights','best.pt')
    model = YOLO(model_path)

    ## clear the table first:
    clear_detections()

    for image in os.listdir(os.path.join(BASE_DIR,'data','validation','images')):
        if image.lower().endswith('.jpg'):
            print(f"Starting detection and database logging for: {image}")
            test_image = os.path.join(BASE_DIR,'data','validation','images',image)
            detect_and_save(model,test_image)