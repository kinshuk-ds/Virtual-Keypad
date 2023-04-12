# Project Virtual Keyboard with Mediapipe and OpenCV
This project is a virtual keyboard that can be controlled using hand gestures, implemented with the help of Mediapipe and OpenCV libraries in Python. The project allows the user to type in text using the virtual keyboard, by hovering over the buttons with their hands and making a certain gesture to select the button.

## How it works
The project uses the HandDetector class from the cvzone module, which uses Mediapipe to detect and track the user's hand in real-time. The hand landmarks are then used to determine if the hand is hovering over a button on the virtual keyboard.

The virtual keyboard is represented by a list of Button objects, each of which has a position, size, and a label (i.e. the text on the button). When the user's hand hovers over a button, the corresponding label is displayed in a rectangle. When the user selects the button by making a certain gesture, the label is added to the final text and the corresponding character is "typed" as if it was typed on a physical keyboard.

## Installation:
To use this program, you will need to install several Python libraries. You can do this using pip, by running the following commands in your terminal:

pip install opencv-python

pip install mediapipe

pip install pynput

pip install cvzone

## Usage:
1. Run the program in your Python environment.
2. Position your hand in front of the camera so that it is fully visible.
3. Hover your index finger over the key you want to press.
4. Pinch your index finger and thumb together to "press" the key.
5. The character you pressed will be displayed on the virtual screen.

## Customization:
You can customize the layout of the virtual keyboard by modifying the "keys" list in the program. Each sublist represents a row of keys, and each string represents a key's character. You can also modify the appearance of the virtual keyboard by modifying the drawALL function.

## Contributing:
If you would like to contribute to this project, feel free to fork the repository and submit a pull request.

## License:
This project is licensed under the MIT License.
