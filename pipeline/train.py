from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8s.pt')
    model.train(
        data = 'data.yaml',
        epochs = 50,
        imgsz = 200,
        device = 0,
        project = 'models',
        name = 'defect_detector'
    )