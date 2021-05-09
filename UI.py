import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import time

class YOLO:

    def __init__(self, config, model, labels, size=416, confidence=0.5, threshold=0.3):
        self.confidence = confidence
        self.threshold = threshold
        self.size = size
        self.labels = labels
        self.net = cv2.dnn.readNetFromDarknet(config, model)

    def inference(self, image):
        ih, iw = image.shape[:2]

        ln = self.net.getLayerNames()
        ln = [ln[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]

        blob = cv2.dnn.blobFromImage(image, 1 / 255.0, (self.size, self.size), swapRB=True, crop=False)
        self.net.setInput(blob)
        start = time.time()
        layerOutputs = self.net.forward(ln)
        end = time.time()
        inference_time = end - start

        boxes = []
        confidences = []
        classIDs = []

        for output in layerOutputs:
            for detection in output:
                scores = detection[5:]
                classID = np.argmax(scores)
                confidence = scores[classID]
                if confidence > self.confidence:
                    box = detection[0:4] * np.array([iw, ih, iw, ih])
                    (centerX, centerY, width, height) = box.astype("int")
                    x = int(centerX - (width / 2))
                    y = int(centerY - (height / 2))
                    boxes.append([x, y, int(width), int(height)])
                    confidences.append(float(confidence))
                    classIDs.append(classID)

        idxs = cv2.dnn.NMSBoxes(boxes, confidences, self.confidence, self.threshold)

        results = []
        if len(idxs) > 0:
            for i in idxs.flatten():
                x, y = (boxes[i][0], boxes[i][1])
                w, h = (boxes[i][2], boxes[i][3])
                id = classIDs[i]
                confidence = confidences[i]

                results.append((id, self.labels[id], confidence, x, y, w, h))

        return iw, ih, inference_time, results


def detect_objects(our_image):
    st.set_option('deprecation.showPyplotGlobalUse', False)

    col1, col2 = st.beta_columns(2)
    
    try:
        yolo = YOLO("yolov3/yolov3_custom.cfg", "yolov3/yolov3_custom1_1000.weights", ["Fire"])
    except:
        st.success("Model Loaded!!")
        
    col1.subheader("Original Image")
    st.text("")
    plt.figure(figsize = (15,15))
    plt.imshow(cv2.cvtColor(our_image, cv2.COLOR_BGR2RGB))
    col1.pyplot(use_column_width=True)

##    new_img = np.array(our_image.convert('RGB'), np.float32)
##    our_img = cv2.cvtColor(new_img,1)
##    our_image = cv2.imread(our_image)
    width, height, inference_time, results = yolo.inference(our_image)
    if(results==[]):
        cv2.putText(our_image, 'No Fire', (0, 160), cv2.FONT_HERSHEY_SIMPLEX,1, (0, 255, 255), 2)
    else:
        for detection in results:
            id, name, confidence, x, y, w, h = detection
            color = (0, 255, 255)
            cv2.rectangle(our_image, (x, y), (x + w, y + h), color, 2)


    st.text("")
    col2.subheader("Object-Detected Image")
    st.text("")
    plt.figure(figsize = (15,15))
    plt.imshow(cv2.cvtColor(our_image, cv2.COLOR_BGR2RGB))
    col2.pyplot(use_column_width=True)


def object_main():
    """OBJECT DETECTION APP"""

    st.title("Object Detection")
    
    choice = st.radio("", ("Show Demo", "Browse an Image"))
    st.write()

    if choice == "Browse an Image":
        st.set_option('deprecation.showfileUploaderEncoding', False)
        image_file = st.file_uploader("Upload Image", type=['jpg','png','jpeg'])

        if image_file is not None:
            our_image = Image.open(image_file)
##            our_image = cv2.imread(image_file)
            detect_objects(our_image)

    elif choice == "Show Demo":
##        our_image = Image.open("images/fire7.jpg")
        our_image = cv2.imread("images/fire8.jpg")
        detect_objects(our_image)

if __name__ == '__main__':
    object_main()
