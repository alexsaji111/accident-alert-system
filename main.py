import socket

import sys

import random

# Create a TCP/IP socket

import cv2

import time

import smtplib

import os

import serial

 

import RPi.GPIO as GPIO     

GPIO.setmode(GPIO.BCM)  

GPIO.setwarnings(False)

GPIO.setup(25, GPIO.IN)  

GPIO.setup(24, GPIO.OUT)  

ser = serial.Serial('/dev/ttyACM0')

#ser = serial.Serial('/dev/ttyACM0')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

 

server_address = ('192.168.225.41', 8081)

camera_capture = cv2.VideoCapture(0)

 

print('starting up on {} port {}'.format(*server_address))

sock.bind(server_address)

sock.listen(1)

count = 91

 

while True:

# Wait for a connection

print('waiting for a connection')

connection, client_address = sock.accept()

try:

print('connection from', client_address)



while True:

count = count+1

line = ser.readline()

line = line.decode('ascii')

print (line)

if '0' in line:

        data = connection.recv(300)

        print(data)

        GPIO.output(24, 1)

        print('received {!r}'.format(data))

        data = data.decode('utf-8')

        data = str (data)

        print (data)

        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

        server.login("alexsaji010@gmail.com", "alexsaji111")

        server.sendmail(

                    "alexssaji010@gmail.com",

                    "alexsaji111@gmail.com",

                    data)

        success, im = camera_capture.read()



cv2.imwrite('test.png',im)

        os.system('python3 sosemail1.py')

        os.system ('python3 sossms.py')

        GPIO.output(24, 0)





        time.sleep(5)



finally:

print('closing socket')

sock.close()