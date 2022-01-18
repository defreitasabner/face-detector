<h1 align="center">Real-time Face Detector</h1>

<p align="justify">A simple real-time face detection software developed in Python 3 using module OpenCV with CascadeClassifier method.</p>

<h2>About this project</h2>
<p align="justify">I start the develop of this project after I watched one <a href="https://www.youtube.com/watch?v=h5z8jrW9CtY&list=RDCMUCEn6kONg6EC_Ylh0RlInsMw&index=4">video about face detection</a> 
from the brazilian Youtube's channel "<a href="https://www.youtube.com/channel/UCEn6kONg6EC_Ylh0RlInsMw">Universo Discreto</a>" by Lucas Lattari 
(<a href="https://github.com/lucaslattari">lucaslattari</a>). The base code made by Lucas could be find 
<a href="https://github.com/lucaslattari/UniversoDiscreto/blob/master/OpencVLOG/OpenCVLOG%2011.1/visualizaFaceDetectada.py">here</a>. 
It was developed just to put my coding skills into practice.</p>

<h2>How it works?</h2>
<p align="justify">The base code made by Lucas Lattari from "Universo Discreto", which 
was made to detect faces in a input image file. However, 
I introduce as input, not the image file, but the image from webcam to make a real-time 
face detection. The webcam images are converted to gray-scale and 
Cascade Classifier, from module OpenCV, try to match the models (specified in .xml file)
with the input images. When the Cascade Classifier's models matches with a face, a rectangle 
is drawn around the face.</p>

<h2>How to use it?</h2>
<ol>
    <li><p>Download this repository's folder.</p></li>
    <li><p>Run python file (.py) on console.</p></li>
    <li><p>If it works, a system window with webcam's image will open. 
    Faces recognized will be marked by red rectangles.</p></li>
    <li><p>Press ESC to quit application.</p></li>
</ol>

<h2>Possible problems</h2>
<ol>
    <li><p align="justify"><b>False face detection:</b> Sometimes objects could 
be detected as faces. It mistake probably occurs because 
the code need more improvements. It not ghosts, I swear.</p></li>
    <li><p align="justify"><b>Missing necessary modules:</b> The code try to download 
and install the necessary modules, but if it fails, 
the software will break. Try to install necessary modules by command line.</p></li>
</ol>

<h2>Acknowledgement</h2>
<p align="justify">I would like to thanks <a href="https://github.com/lucaslattari">Lucas Lattari</a> and his collaborators by 
spread knowledge with their amazing Youtube's channel <a href="https://www.youtube.com/channel/UCEn6kONg6EC_Ylh0RlInsMw">Universo Discreto</a>.</p>
