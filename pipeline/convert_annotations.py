import xml.etree.ElementTree as ET
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ---------/class name declaration/-------------------

defects = ['crazing', 'inclusion', 'patches', 
               'pitted_surface', 'rolled-in_scale', 'scratches']

def convert_folder(annotation_path,label_path):
    
    os.makedirs(label_path,exist_ok=True)

    for filename in os.listdir(annotation_path):
        
        if filename.endswith('.xml'):

            full_path = os.path.join(annotation_path,filename)
            tree = ET.parse(full_path)
            root =  tree.getroot()

            Width = int(root.find('size').find('width').text)
            Height = int(root.find('size').find('height').text)

            lines = []

            for obj in root.findall('object'):
                class_name = obj.find('name').text
                class_id = defects.index(class_name)

                bndbox = obj.find('bndbox')
                xmin = int(bndbox.find('xmin').text)
                ymin = int(bndbox.find('ymin').text)
                xmax = int(bndbox.find('xmax').text)
                ymax = int(bndbox.find('ymax').text)


                ## conversion in yolo format

                center_x = ((xmin+xmax)/2)/Width
                center_y = ((ymin+ymax)/2)/Height
                w = (xmax-xmin)/Width
                h = (ymax-ymin)/Height

                lines.append(f"{class_id} {center_x} {center_y} {w} {h}")

            txt_filename = filename.replace('.xml','.txt')

            with open (os.path.join(label_path,txt_filename),'w') as f:
                f.write("\n".join(lines))

convert_folder(os.path.join(BASE_DIR, 'data', 'train', 'annotations'),
               os.path.join(BASE_DIR, 'data', 'train', 'labels'))

convert_folder(os.path.join(BASE_DIR, 'data', 'validation', 'annotations'),
               os.path.join(BASE_DIR, 'data', 'validation', 'labels'))