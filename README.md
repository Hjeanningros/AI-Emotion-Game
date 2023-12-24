# IA Emotion Game

The goal of this mini-game is to imitate the emotion prompted by the program based on a given event example. The program uses the front camera of your laptop as an image input and detects your emotion with an AI model. The available emotions are Surprise, Neutral, Anger, Happy, and Sad. To detect the faces, the program uses the library available at https://github.com/ageitgey/face_recognition.

## How to run the mini-game

### Install libraries

- Install dlib; to do this, follow the instructions in this repository: https://gist.github.com/ageitgey/629d75c1baac34dfa5ca2a1928a7aeaf
- Install the libraries from the requirements.txt file; you can use the command `pip3 install requirement.txt`.


### Start

- Run `python main.py` or `python3 main.py` based on which environnement you are using. 

## Add prompt example

In the file src/situations.py, you will find a JSON containing all the example prompts. You can add sentences to vary the game.