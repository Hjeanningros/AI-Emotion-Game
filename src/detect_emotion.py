import cv2 as cv
import numpy as np
import tensorflow as tf
from src.display_info import display_informations, display_instructions
import face_recognition
import random
from src.situations import emotions_sentences

class Detect_Emotion():
    def __init__(self):
        self.model = tf.keras.models.load_model('models/emotion_modelv2.h5')
        self.dictionnary = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad']
        self.emotion_to_detect = random.choice(self.dictionnary)
        self.sentence = random.choice(emotions_sentences[self.emotion_to_detect])

    def detect(self, frame):
        locations = []
        emotions_states = []

        face_locations = self.detect_face(frame)
        for top, right, bottom, left in face_locations:
            
            # Scale back up face locations since the frame we detected in was scaled
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            # Crop the image where the head is located
            roi = frame[top:bottom, left:right]
            gray_roi = cv.cvtColor(roi, cv.COLOR_BGR2GRAY)
            # Resize to np.array of shape(48,48,1), this is the input shape of the model
            cropped_roi = np.expand_dims(np.expand_dims(cv.resize(gray_roi, (48, 48)), -1), 0)

            # Predict the emotion with the model 
            predictions = self.model.predict(cropped_roi, verbose=0).argmax()
            state = self.dictionnary[predictions]

            locations.append([top, bottom, left, right])
            emotions_states.append(state)

        return emotions_states, locations
    
    def display_info(self, emotions, locations, frame):
        frame = display_informations(emotions, locations, frame)
        frame = display_instructions(frame, self.sentence, self.emotion_to_detect)
        return frame

    def detect_face(self, frame):
        small_frame = cv.resize(frame, (0, 0), fx=0.50, fy=0.50)
        face_locations = face_recognition.face_locations(small_frame)
        return face_locations

    def check_player_emotion(self, state_emotion):
        if state_emotion:
            if state_emotion[0] == self.emotion_to_detect:
                self.emotion_to_detect = random.choice(self.dictionnary)
                self.sentence = random.choice(emotions_sentences[self.emotion_to_detect])
                print("GOOD JOB BIG BOY")
        
        