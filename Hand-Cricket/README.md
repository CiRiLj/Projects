# hand-cricket

## **Software Requirements**
1) opencv-python 4.5.5.64 or above
2) mediapipe 0.8.9 or above
3) numpy 1.20.0

## **Hardware Requirement**
1) Webcam

## **Project Info**

### Game Info
Hand Cricket is a game that many children used to play in their school days. In this game two players show moves on their respective fingers. If the moves are equal, the batsman is declared out. Else, the move of the batsman is added to the total runs of the batting team. Once the first player is out the second player starts batting and their goal is to beat the score of first player.(This game is explained in this instructibles.com article https://www.instructables.com/How-to-Play-Hand-Cricket/)

## **Move Set**
There are 7 valid moves in this game. They depict 0,1,2,3,4,5,6 runs respectively.

![alt text](https://github.com/wasdac9/hand-cricket/blob/main/move_set.png?raw=true)

*Image: Move with respect to the number they depict.*

In this version of Hand Cricket, the first player is a real person and the second player is the computer. The player throws one of these moves in front of the webcam as per their choice which is converted into its respective number between 0 and 6, and simultaneously the computer selects a number between 0 and 6 randomly. If both(player and computer) throw the same number, the batsman is out!.

In the first innings, the person always bats first and computer bowls first and unless the computer takes the wicket of the person, the score of the person keeps on adding as per their move. When the computer takes the wicket of the person, the computer starts batting and adding up its score and the person has to take the wicket of the computer before they beat the person's score.

## **Interface**

![alt text](https://github.com/wasdac9/hand-cricket/blob/main/complete_screen.PNG?raw=true)

The interface is a opencv window which consists of some game details in text format and the webcam feed.(This interface pops up on running HandCricket.py)

1) The first line of the text based game details displays the move the player chose and the move the computer chose.
(Here the player made the move 5 which was converted into its respective number 5 and hence on the first line it displays "You: 5". And since the computer chose the number 1 randomly between the numbers 0 and 6, it displays "Computer: 1"
2) The second line of game details displays the total running score(while batting) of the player on the left side and the total running score(while batting) of the computer on the right side seperated by "|"(the pipe).
3) The third line of game details displays the state of the player. In the beginning the player is always in the "Batting" state. When the computer takes the player's wicket, the state of player changes to "Bowling".
4) The rest of the screen is the webcam feed with landmark detection of the hand displayed on the window.(The landmark detection is done by mediapipe library)

Note: 
1) The interface updates every 2 seconds. This feature exists to give some time for the player to make their move.
2) The computer only makes its move when there is a hand detected in the frame. When there is no hand in the frame, there is no change in the score.

### **Out Screen**

![alt text](https://github.com/wasdac9/hand-cricket/blob/main/out_screen.PNG?raw=true)

When the computer takes the wicket of the player, a out screen is displayed. This screen displays some details like the score computer needs to win and the changed state of the player to "Bowling". (Here the player's score is 18, and the computer needs to beat this score to win.)

### **End Screen**

![alt text](https://github.com/wasdac9/hand-cricket/blob/main/end_screen.PNG?raw=true)

This is the end screen. This screen displays the final winner and the final scores of both players. (Here we can see that the player made a score of 18 in the batting stage and got out, and then when the computer was batting, the  player managed to take computer's wicket at a score of 12. And hence the Player won.)

## **Code**

1) HandTrackingModule.py is a helper module that does all the landmark detection, and landmark drawing on the hands.(Since the screen only updates every 2 seconds while in the game, this module can be ran to see the real FPS and accuracy of hand detection in a live webcam feed.)
2) HandCricket.py is the main module that calls HandTrackingModule. It handles all the move set, turns, opencv window and game details logic required for hand cricket.

## **Summary**
1) Mediapipe is a very powerful open source library created by Google. 
2) Mediapipe does all its computation on CPU and still manages to give good FPS (around 20 FPS).
3) Mediaipe can do various other tasks such as Face Detection, Pose Estimation, etc.

