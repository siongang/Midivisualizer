import cv2
import os
import pygame as pg

frames_dir = 'frames'
output_file = 'yes.mp4'
frame_rate = 60
WIDTH = 1280
HEIGHT = 720

def constructor(width, height):
    WIDTH = width
    HEIGHT = height

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(output_file, fourcc, frame_rate, (WIDTH, HEIGHT))

def vid_generator (frame):
    pg.image.save(frame, "frames/frame.jpeg")    
    img = cv2.imread(os.path.join(frames_dir,'frame.jpeg'))
    if img is None:
        print("Failed to load image.")
    video.write(img)
