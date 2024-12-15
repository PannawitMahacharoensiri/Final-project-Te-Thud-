# Project : Te-THUD !!!!
( the name came from Tetris + sound of object got crushed “THUD!!”)
“Doged the block above you or you LOST”
This project was developed as part of 01219114/01219115 Programming 1
Section 450, Academic Year 2567 at "Kasetsart University"


## Introduction
Good Morning Everyone, I am excited to present my video game project titled "Te-Thud!!!". Before I go further, I would like to acknowledge that I did not develop the original code for the game entirely from scratch. Rather, I modified and adapted existing code from a classic "Tetris" game. I would like to extend my gratitude to Christian Thompson for his contributions, which served as the foundation for this project.

You can find his original Python code at the following link:
    https://github.com/wynand1004/Projects/blob/master/Tetris%2Ftetris.py
Additionally, Christian can be found on Twitter @tokyoedtech.
Thank you for your attention, and I hope you enjoy the game!


## Project description
- My project  is a Tetris-inspired video game  where the player controls a square block that must avoid falling obstacles. Unlike traditional Tetris, the player does not manipulate the obstacles but instead navigates the game environment to dodge them. The objective is to prevent obstacles from landing on the player's block, as doing so results in losing the game.
- The game features a grid-based design, meaning updates occur block by block rather than with smooth framerate transitions. Despite this, the core mechanics are fully implemented, including player movement (left, right, and jumping), automatic clearing of rows when they are completely filled, and the random generation of obstacles. These mechanics ensure an engaging and enjoyable experience for players.
``` | Control |
Move left : Key left
Move right : Key Right
Jump : Key Up
```


## How to install and run the project
My video game is developed using Python's turtle module and can be run directly from an integrated development environment (IDE). To play, users need an IDE that supports Python and provides access to standard libraries such as turtle, random, and time. The game is launched by simply running the source file within the IDE.
Step by step:
1. An IDE capable of accessing Python's external modules.
2. The ability to execute the source file directly from the IDE.


## Usage 
[TeTHUD demo video](https://youtu.be/YganM5vVIUM)


## Project design and implementation
-  UML class diagram : https://lucid.app/lucidchart/0eb1a408-46f5-407c-a79f-0226788f450d/edit?viewport_loc=-251%2C-141%2C2560%2C1184%2C0_0&invitationId=inv_53a46a61-07b2-4ca6-ae34-975f9579f89e
- Player Class: Responsible for constructing the player object and managing player movement.
- Obstacles Class: Serves as a blueprint for creating obstacle objects whenever they are instantiated.
- Game Class: The main class that handles the core game logic, including setting up the screen, processing user input, and coordinating interactions between objects from other classes.

### Interaction Between Objects:
The majority of the program’s functionality is managed within the Game class. When the Game class needs to modify the state or attributes of an object from another class (e.g., Player or Obstacles), it invokes the appropriate methods of that class and passes the required values. This ensures that each class operates cohesively while maintaining clear separation of responsibilities.
- Firstly, I utilize code introduced in class, such as the ball_bouncing_sim program, as a case study and example to understand the capabilities of the turtle module.
- To create animations that depict movement, I apply the logic of updating the visual display frame by frame. This involves continuously modifying the attributes of objects, which, in turn, update the screen to create the appearance of motion with each frame.

### Testing :
I primarily test my code by running it for 5–10 minutes to verify that it performs the intended mechanics as expected that include
1. Build screen open window (turtle module)
2. change grid to picture that can interact
3. player movement : left/right and jump
4. Object and player fall behaviour
5. random new block continually
6. Clear row when the row are full
7. check timer
8. check collision and game error screen 
Based on my testing so far, I have not encountered any bugs, and the program functions as intended with 100% accuracy.