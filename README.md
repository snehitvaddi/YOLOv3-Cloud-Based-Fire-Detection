## YoloV3 Fire Detection model
A Project on Fire detection using YOLOv3 model. This repo consists of code used for training and detecting Fire using custom YoloV3 model. I trained my custom detector on existing yolov3 weights trained to detect 80 classes. <br>
The Dataset is collected from google images using [Download All Images](https://chrome.google.com/webstore/detail/download-all-images/ifipmflagepipjokmbdecpmjbibjnakm) chrome extension. Tool for Dataset labelling [Label Img](https://github.com/tzutalin/labelImg).<br>
Find some readily labelled datasets are available here @[Google's Open Image Dataset v5](https://storage.googleapis.com/openimages/web/index.html).
#### Note:
**I have made `Fire-Implementation.ipynb` private for personal reasons, contact me @v.snehith999@gmail.com for complete directory ✌**<br>
|  🧾 Colab Notebook  |   📂 Dataset with Labels   | 🔑 Trained Model Weights |  ✍ LabelImg |
|------------|-------------|-----------|-----------|
| [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://drive.google.com/file/d/1O1tlwjbt4dUWBct2Jv0vHXPNe_fcMCa_/view?usp=sharing) | [Dataset with Labels](https://drive.google.com/file/d/1O1tlwjbt4dUWBct2Jv0vHXPNe_fcMCa_/view?usp=sharing) | [Download Weights](https://drive.google.com/file/d/1-0mACyQvwGSpaxXS57Z1L6wdHutpuFRE/view?usp=sharing) | [Label Img ](https://github.com/tzutalin/labelImg)  |

### 📥 Web-Interface using Streamlit 
<center><img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Based-Fire-Detection/blob/master/UI.PNG" width="500" /></center><br>

###### Streamlit library makes it easy to create and share beautiful, custom web apps for machine learning and data science applications.
 * For executing Streamlit application, install streamlit using `pip install streamlit --user`.
 * Open Command Prompt, and execute `streamlit run UI.py`.
 * A Streamlit server gets started and opens up web UI in the default browser.

### 🧬 Sample outputs from Custom YOLOv3 model
  |    Input   |   Output   |
  |------------|-------------|
  | <img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/images/fire1.jpg" width="300"> | <img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/result-images/predictions%20(1).jpg" width="300"> |
  | <img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/images/fire3.jpg" width="300"> | <img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/result-images/predictions%20(2).jpg" width="300"> |
  | <img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/images/fire7.jpg" width="300"> | <img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/result-images/predictions%20(3).jpg" width="300"> |
****************************************************************************************************************************************

## 📈 Training Performance Chart
Here is the chart to describe how my performed during entire training process. It shows average loss vs. iterations. For a model to be 'accurate' you would aim for a loss under 2.<br>
<img src="https://github.com/snehitvaddi/YOLOv3-Cloud-Custom-Object-Detection/blob/master/result-images/chart.png" width="450" height="450"/>
****************************************************************************************************************************************
### 📂 Files Required :
* Darknet repository
* Labeled Custom Dataset
* Custom .cfg file
* obj.data and obj.names files
* train.txt file (test.txt is optional here as well)

I referenced this tutorial from an [YouTube Video](https://www.youtube.com/channel/UCrydcKaojc44XnuXrfhlV8Q) by TheAIGuy channel.
You can follow a step-by-step walkthrough of video and the code here: https://www.youtube.com/watch?v=10joRJt39Ns

You can download the yolov3 pretrained weights by clicking [here](https://pjreddie.com/media/files/yolov3.weights) and yolov3-tiny [here](https://pjreddie.com/media/files/yolov3-tiny.weights)
****************************************************************************************************************************************

### ⚡ Colab Hack: ⭐
If you are a student like me, and unable to pay such amount, here is a jugad for you. 😉<br>

👉Step 1: In colab notebook, type CTRL + SHIFT + I (Inspect element)<br>
👉Step 2: Go to the console tab and paste the code given in the image below.<br>

`function ClickConnect(){`<br>
`console.log("Working"); `<br>
`document.querySelector("colab-toolbar-button#connect").click() `<br>
`}`<br>
`setInterval(ClickConnect,60000)`<br>
****************************************************************************************************************************************
## 🧠 Further Ideas
* Integrate the model with IOT and leverage Cloud services for real-time monitoring and alerting system.

## References: 
**Streamlit Yolo Deployment** - https://srishti.hashnode.dev/object-detection-app-using-yolov3-opencv-and-streamlit-1<br>
**YoloV3 Custom Model taining** - https://www.youtube.com/channel/UCrydcKaojc44XnuXrfhlV8Q<br>

#### 💡 Need Help.
I'm facing bugs with uploading images through Streamlit and Displaying them using OpenCV. Any kind of suggestions will be appriciable. 
