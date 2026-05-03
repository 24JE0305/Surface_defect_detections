from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO('C:\\Users\\papat\\OneDrive\\Desktop\\Project\\models\\defect_detector5\\weights\\best.pt')

    model.predict(
        source = 'C:\\Users\\papat\\OneDrive\\Desktop\\Project\\data\\validation\\images\\patches_289.jpg',
        save=True,
        conf=0.25,
        project='tries',
        name='hope'
    )