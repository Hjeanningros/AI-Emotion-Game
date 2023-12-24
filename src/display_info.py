import cv2 as cv


def display_informations(emotions, locations, frame):
    for emotion, location in zip(emotions, locations):
        # Draw Rectangle all around the head detected 
        frame = cv.rectangle(frame, (location[2], location[0]), (location[3], location[1]), (0, 0, 255), 2)
            
        # Display the emotion detected
        frame = cv.rectangle(frame, (location[2], location[0] - 20),
            (location[3], location[0]), (0, 0, 255), -1)
        frame = cv.putText(frame, emotion, (location[2] + 3, location[0] - 5),
            cv.FONT_HERSHEY_SIMPLEX, 0.7,
            (255, 255, 255), 1,
            cv.LINE_AA)
    return frame

def display_instructions(frame, sentence, emotion_to_detect):
    frame = cv.putText(frame, f"Situation: {sentence}", (20, 20),
        cv.FONT_HERSHEY_SIMPLEX, 0.7,
        (0, 0, 0), 1,
        cv.LINE_AA)
    frame = cv.putText(frame, f"Emotion to detect: {emotion_to_detect}", (20, 40),
        cv.FONT_HERSHEY_SIMPLEX, 0.7,
        (0, 0, 0), 1,
        cv.LINE_AA)
    return frame