import numpy as np
import cv2
import time
import pyglet
import random
import datetime
import serial

ser = serial.Serial('COM8', 19200, timeout=0, parity=serial.PARITY_NONE,

                    stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)

car_cascade = cv2.CascadeClassifier('cars_v2.xml')
ped_cascade = cv2.CascadeClassifier('visionary.net_pedestrian_cascade_web_LBP.xml')

overtaking_sound = pyglet.media.load("overtaking_lane_v3.wav", streaming=False)
correct_lane_img = cv2.imread('elements_v2/dash_v4.png', cv2.IMREAD_UNCHANGED)
pedestrian_front = cv2.imread('elements_v2/pedestrian_front.png')
pedestrian_left = cv2.imread('elements_v2/pedestrian_left.png')
pedestrian_right = cv2.imread('elements_v2/pedestrian_right.png')
collision = cv2.imread('elements_v2/collision.jpg')
x, y, w, h = 0, 0, 1000, 60


event = 'Loading...'
egine_heat_index = 'Loading...'
temp = 'Loading...'
humidity = 'Loading...'
rain = 'Loading...'
speed = '000'
flag = 0


def serverData(): #Serves as Bluetooth data
    global Event_name,egine_heat_index_name,temp_name,humidity_name,speed_name,rain_name
    nbytes = ser.inWaiting()
    x = str(ser.readline(nbytes))
    x = x.lstrip("b")
    x = x.strip("'")
    x = x.rstrip("\\r\\n")
    #print(x)
    y = x.split(',')
    for a in y[0:1]:
        Event_name = a
    for a in y[1:2]:
        egine_heat_index_name = a
    for a in y[2:3]:
        temp_name = a
    for a in y[3:4]:
        speed_name = a
    for a in y[4:5]:
        humidity_name = a
    ser.flushInput()
    rain_name='0'
    return Event_name, egine_heat_index_name, temp_name, humidity_name, rain_name , speed_name


def gui(img, status, warning):
    global event, flag, egine_heat_index, temp, humidity, rain , speed
    e = datetime.datetime.now()
    now = time.time()
    sec = int(now % 60)
    if (sec % 5 == 0 & flag == 0):
        event, egine_heat_index, temp, humidity, rain , speed = serverData()
        flag=1
    else:
        flag=0
    # Draw black background rectangle
    #cv2.rectangle(img, (x, x), (x + w, y + h), (0, 0, 0), -1)

    status_x_offset = 800
    status_y_offset = 220

    date_x_offset = 800
    date_y_offset = 8

    event_x_offset = 120
    event_y_offset = 530

    engine_heat_x_offset = 120
    engine_heat_y_offset = 115

    temp_x_offset = 120
    temp_y_offset = 250

    trip_x_offset = 120
    trip_y_offset = 380

    speed_x_offset = 825
    speed_y_offset = 100

    speed_unit_x_offset = 1015
    speed_unit_y_offset = 100

    speed_limit_x_offset = 950
    speed_limit_y_offset = 150

    speed_limit_text_x_offset = 880
    speed_limit_text_y_offset = 150

    humidity_x_offset = 100
    humidity_y_offset = 400

    rain_x_offset = 100
    rain_y_offset = 360

    cv2.putText(img, "Cruise Date: %s-%s-%s" % (e.day, e.month, e.year),
                (date_x_offset + int(w / 28), date_y_offset + int(h / 1)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2)
    #cv2.putText(img, "Status: " + status, (status_x_offset + int(w / 28), status_y_offset + int(h / 1)),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(img, event, (event_x_offset + int(w / 28), event_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2) #Event Notification
    cv2.putText(img,egine_heat_index+"C",
                (engine_heat_x_offset + int(w / 28), engine_heat_y_offset + int(h / 1)), cv2.FONT_HERSHEY_SIMPLEX, 0.7,
                (255, 255, 255), 2) #Engine Heat
    cv2.putText(img,temp+"C", (temp_x_offset + int(w / 28), temp_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2) # feels Like temp
    cv2.putText(img,"3 Km", (trip_x_offset + int(w / 28), trip_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)  # feels Like temp
    cv2.putText(img,speed, (speed_x_offset + int(w / 28), speed_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_TRIPLEX, 3, (255, 255, 255), 3) #spped
    cv2.putText(img, "Kmph", (speed_unit_x_offset + int(w / 28), speed_unit_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2) #speed Unit
    cv2.putText(img, "Limit: ", (speed_limit_text_x_offset + int(w / 28), speed_limit_text_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)  # speed Limit text
    cv2.putText(img, "60"+" Kmph", (speed_limit_x_offset + int(w / 28), speed_limit_y_offset + int(h / 1)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)  # speed Limit text
    #cv2.putText(img, "Humidity: " + humidity, (humidity_x_offset + int(w / 28), humidity_y_offset + int(h / 1)),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    #cv2.putText(img, "Rain: " + rain, (rain_x_offset + int(w / 28), rain_y_offset + int(h / 1)),
                #cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)


    ped_x_offset = 490
    ped_y_offset = 250

    ped_left_x_offset = 400
    ped_left_y_offset = 250

    ped_right_x_offset = 600
    ped_right_y_offset = 250

    coli_x_offset = 400
    coli_y_offset = 50



    if warning == 1:
        img[ped_y_offset:ped_y_offset + pedestrian_front.shape[0],
        ped_x_offset:ped_x_offset + pedestrian_front.shape[1]] = pedestrian_front
        time.sleep(0.25)
    elif warning == 3:
        img[ped_left_y_offset:ped_left_y_offset + pedestrian_left.shape[0],
        ped_left_x_offset:ped_left_x_offset + pedestrian_left.shape[1]] = pedestrian_left
        time.sleep(0.25)
    elif warning == 4:
        img[ped_right_y_offset:ped_left_y_offset + pedestrian_right.shape[0],
        ped_right_x_offset:ped_right_x_offset + pedestrian_right.shape[1]] = pedestrian_right
        time.sleep(0.25)
    elif warning == 2:
        img[coli_y_offset:coli_y_offset + collision.shape[0],
        coli_x_offset:coli_x_offset + collision.shape[1]] = collision
        #overtaking_sound.play()
        time.sleep(0.25)
    return img


def resizer(img):
    scale_percent = 60
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    # dsize
    dsize = (width, height)
    # resize image
    img = cv2.resize(img, dsize)
    return img


def correct_lane():
    img = correct_lane_img
    img = resizer(img)
    img = gui(img, 'Safe', 0)  # img , status
    cv2.imshow('acciGone || Drive Safe', img)


def ped_warning():
    img = correct_lane_img
    img = resizer(img)
    img = gui(img, 'Pedestrian ahed', 1)  # img , status
    cv2.imshow('acciGone || Drive Safe', img)
def ped_warning_left():
    img = correct_lane_img
    img = resizer(img)
    img = gui(img, 'Pedestrian at left', 3)  # img , status
    cv2.imshow('acciGone || Drive Safe', img)
def ped_warning_right():
    img = correct_lane_img
    img = resizer(img)
    img = gui(img, 'Pedestrian at right', 4)  # img , status
    cv2.imshow('acciGone || Drive Safe', img)

def collision_warning():
    img = correct_lane_img
    img = resizer(img)
    img = gui(img, 'Look for cars', 2)  # img , status
    cv2.imshow('acciGone || Drive Safe', img)


cap = cv2.VideoCapture(2)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.25)
cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, -13)
while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 5)
    pedestrians = ped_cascade.detectMultiScale(gray, 1.3, 5)
    if len(cars) > 0:
        for (p, q, r, s) in cars:   #x,y,w,h
            img = cv2.rectangle(img, (p, q), (p + r, q + s), (255, 255, 0), 2)
            #print(r * s)
            val = 2
    elif len(pedestrians) > 0: #x,y,w,h
        for (a, b, c, d) in pedestrians:
            img = cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 255), 2)
            print(a)
            if(a<200):
                val = 3
            elif(a<400):
                val = 1
            elif(a<600):
                val = 4
    else:
        val = 0
    # print(val)
    if val == 0:
        correct_lane()
    elif val == 1:
        ped_warning()
    elif val == 3:
        ped_warning_left()
    elif val == 4:
        ped_warning_right()
    elif val == 2:
        collision_warning()
    else:
        print('nothing to show')
    cv2.imshow('img', img)  # ***********display******
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()