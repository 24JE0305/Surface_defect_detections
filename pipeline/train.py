from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('yolov8s.pt')
    model.train(
        data = 'data.yaml',
        epochs = 150,
        imgsz = 416,
        device = 0,
        project = 'models',
        name = 'defect_detector',
        
        augment=True,         # Turns the master augmentation switch ON
        degrees=10.0,         # Slightly rotates images by up to 10 degrees
        fliplr=0.5,           # 50% chance to flip images left-to-right
        flipud=0.5,           # 50% chance to flip images up-and-down
        hsv_s=0.5,            # Adjusts color saturation (simulates lighting changes)
        hsv_v=0.4,            # Adjusts brightness (simulates shadow/glare)
        mosaic=1.0            # Combines 4 images into 1 (great for small defects)
    )