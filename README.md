# acciGone_June
![Sample GUI](/documentation_img/img1.png)
# Folder distribution :<br>
gui_v3 >> elements_v2[for image repo]<br>
gui_v3 >> cars_v2.xml,visionary.net_pedestrian_cascade_web_LBP.xml , overtaking_lane_v3.wav[sound]<br>
# Function documentation: <br>
serverData() ----> Receives data from arduino , seperated into ',' delimeter and stores in respective named variables <br>
|-----> serverData() utilizes the initialization variable ser. use proper COM port and bauds to start the code. It is recommended to add a try-except if there is no arduino available<br>
gui(img, status, warning) -----> receives resized image , status and warnings. Uses Opencv image wrapper to produce frames and overlay warinings<br>
resizer(img) -----> resize images for background and all other warning sings to fit in any ratio frame <br>
correct_lane() ----> calls gui() with warning code 0. that means only background with no warning overlay and sound <br>
ped_warning(): ----> calls gui() with warning code 1. that means to overlay middle pedstrian warning icon overlay and sound <br>
ped_warning_left(): ----> calls gui() with warning code 3. that means to overlay left pedstrian warning icon overlay and sound <br>
ped_warning_right(): ----> calls gui() with warning code 4. that means to overlay right pedstrian warning icon overlay and sound <br>
collision_warning(): ----> calls gui() with warning code 2. that means to overlay center collision warning icon overlay and sound <br>
cap = cv2.VideoCapture(2) ---> use your camera number here 
                      
# miscellaneous
the Arduino code for receiving data using blurtooth module has been provided in folder read_data_arduino
