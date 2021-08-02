# acciGone_June
Folder distribution : gui_v3 >> elements_v2[for image repo]<br>
&nbsp&nbsp&nbsp&nbsp&nbsp  gui_v3 >> cars_v2.xml,visionary.net_pedestrian_cascade_web_LBP.xml , overtaking_lane_v3.wav[sound]<br>
Function documentation: <br>
serverData() ----> Receives data from arduino , seperated into ',' delimeter and stores in respective named variables <br>
gui(img, status, warning) -----> receives resized image , status and warnings. Uses Opencv image wrapper to produce frames and overlay warinings<br>
resizer(img) -----> resize images for background and all other warning sings to fit in any ratio frame <br>
correct_lane() ----> calls gui() with warning code 0. that means only background with no warning overlay and sound <br>
ped_warning(): ----> calles gui() with warning code 1. that means to overlay middle pedstrian warning icon overlay and sound <br>
                                                                                              
                      
