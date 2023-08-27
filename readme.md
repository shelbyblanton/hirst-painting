# Hirst Painting Recreation

## **[100 Days of Code: The Complete Python Pro Bootcamp for 2023](https://www.udemy.com/course/100-days-of-code/)**

By Dr. Angela Yu

*Day 18 of 100:* Turtle and the Graphical User Interface (GUI)

## Project Specs

Using **[Turtle](https://docs.python.org/3/library/turtle.html)**, Screen, and **[Colorgram](https://pypi.org/project/colorgram.py/)**, program an app that recreates one of **[Damien Hirst's Dot Paintings](https://www.artsy.net/artist-series/damien-hirst-spots)** that sell for thousands of dollars each:

![alt text](https://github-readme.s3.us-west-1.amazonaws.com/hirst-painting.jpg)

Using the same color hues as in the provided image, we programmatically "paint" the canvas. 

This application is written with Python 3.11.

![alt text](https://github-readme.s3.us-west-1.amazonaws.com/HirstPainting-screenshot.png)

### Main Features
This application extracts the dot colors from one of Damien Hirst's paintings, then draws a white screen and moves the turtle cursor 225 degrees to the southwest where it paints a 20-pixel dot every 50 pixels.  

Once a row of 10 dots has been painted, the cursor starts a new row of 10 dots 50 pixels above the previous row, until 10 rows of dots are painted to complete the canvas.

## Usage & Requirements

This application uses one library package that will need to be installed from PyPi:

- **[Colorgram](https://pypi.org/project/colorgram.py/)**

### Workflow
Start the application, and watch it paint the canvas.

# Getting Started

All of the commands below should be typed into the Python terminal of your IDE (I use PyCharm for my Python Development).

First, clone the repository from Github and switch to the new directory:

    $ git clone git@github.com:shelbyblanton/hirst-painting.git
    
Then open the project in PyCharm.

Open the Python Console and type the following to install the `Colorgram` package:

    >>> pip install colorgram.py

**Setup is complete!** 

Click Run in PyCharm to see the app in action.


# Author & Credits

Programmed by **[M. Shelby Blanton](https://www.linkedin.com/in/shelbyblanton/)** under the instructional guidance of **[Dr. Angela Yu](https://www.udemy.com/user/4b4368a3-b5c8-4529-aa65-2056ec31f37e/)** via **[Udemy.com](udemy.com)**.
