<img src="https://github.com/ZanClifton/100-days-of-code/blob/main/images/100-days-code.png" width=250px align=right alt="100 Days of Code"/>

# 100 Days of Code x2

### Day 1: Jan 22 2023, Sunday

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/snek.png" width=225px align=left alt="Snake Game Over screen"/>

**Activity:** Snek

**Thoughts:** Guided by 100 Days of Python, here is my version of 'Snake'. I'm getting better at Python classes, but still feel confused at times. This uses the in built Turtle module to display the game graphics. The limitations of using this module are exposed at slower speeds as it takes so long to 'draw' the snake and to respond to the keyboard commands as a result.  

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/02-snek) | [Replit](https://replit.com/@ZanClifton/snek?v=1) |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/pong.png" width=250px align=right alt="Pong game in progress"/>

### Day 2: Jan 23 2023, Monday

**Activity:** Pong

**Thoughts:** Created a screen, two paddles, and a ball for Pong. At the moment, you can't press and hold the paddle keys, expecting movement to continue, as the second key press interrupts the first. Although that might not matter so much as you'll only really move your paddle when you know where the ball is travelling towards you, probably.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/03-pong) | [Replit](https://replit.com/@ZanClifton/pong?v=1) |

#

### Day 3: Jan 24 2023, Tuesday

**Activity:** Pong

**Thoughts:** Not time for much this morning. Added the bounce method to the Ball class to get it to change direction when it strikes the top or bottom of the screen. Sadly that's probably it for the day, but something is better than nothing, I guess.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/03-pong) | [Replit](https://replit.com/@ZanClifton/pong?v=1) |

#

### Day 4: Jan 25 2023, Wednesday

**Activity:** Pong

**Thoughts:** I finished up the game but am a little disappointed about some of the functionality. Holding a move key down for a paddle seems to prevent the other player from moving their own paddle, as can queuing up a whole bunch of key presses (I think this is to do with the `time.sleep` command for refreshing the screen and is therefore a quirk of the way it combines with the Turtle module). Happy it's done, though, and it's even kind of fun playing yourself. 

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/03-pong) | [Replit](https://replit.com/@ZanClifton/pong?v=1) |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/turtle-crossing.png" width=250px align=right alt="Turtle Crossing"/>

### Day 5: Jan 28 2023, Saturday

**Activity:** Turtle Crossing

**Thoughts:** Put together 'Turtle Crossing', an absolute knock off of Crossy Road made with Python and the Turtle module and of course the graphics are atrocious. It's also buggy as hell in Replit, which is super annoying. I've always found Replit to be pretty reliable till now but it's not always resetting the turtle to the bottom of the screen. Not happy about it. Although a thought has just occurred to me! It might be to do with holding down the up arrow key meaning the turtle skips across the reset point. I'll make a note and refactor it sometime this week coming.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/04-turtle-crossing) | [Replit](https://replit.com/@ZanClifton/turtle-crossing?v=1) |

#

<img src="https://user-images.githubusercontent.com/96394256/215429243-62e18aa4-b998-4477-81f6-e436a7e4a667.png" width=250px align=left alt="Snek"/>

### Day 6: Jan 29 2023, Sunday

**Activity:** Snek

**Thoughts:** Added a high score to Snek and made it so the high score is written to, and retrieved from,  a text file each time the game is played. There's also no game over message any more; the game continually loops. I'm pretty happy with that.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/02-snek) | [Replit](https://replit.com/@ZanClifton/snek?v=1) |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/mail-merge.png" width=300px align=right alt="Mail Merge"/>

### Day 7: Jan 30 2023, Monday

**Activity:** Mail Merge

**Thoughts:** Using the [readlines](https://www.w3schools.com/python/ref_file_readlines.asp), [replace](https://www.w3schools.com/python/ref_string_replace.asp) and [strip](https://www.w3schools.com/python/ref_string_strip.asp) methods, I used a list of names and a pre-written letter to create a mail merge. The list and the letter were in separate files and needed to be combined, then each personally addressed letter written to its own file named after the recipient. This was a pleasant and methodical task, and although I've done more complex things already (perhaps my Python + SQL projects shouldn't have been put in with the 'basic' projects and I should probably separate them out) it's good to revise the fundamentals.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/05-mail-merge) | None |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/us-states.png" width=400px align=right alt="US States Game"/>

### Day 8: Feb 05 2023, Sunday

**Activity:** US States Game

**Thoughts:** Turtle is back, and with it, the pandas library. I did a little bit of playing around with it yesterday, but not really with any particular focus or project in mind, but today, I used the pandas library to read a csv file for the data in my game, and quickly put together a game that fills in a US map with the names of the States. I abstracted some of the code out to a separate class (which now, finally, feels completely natural) and the whole thing came together with much less effort than I expected.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/06-us-states) | [Replit](https://replit.com/@ZanClifton/us-states?v=1) |

#

### Day 9: Feb 08 2023, Wednesday

**Activity:** List Comprehension and the US States Game

**Thoughts:** I worked on [list comprehension](https://realpython.com/list-comprehension-python/) and did some exercises to cement my understanding. This is a wonderful example of [syntactic sugar](https://medium.com/analytics-vidhya/syntactic-sugar-in-python-3e61d1ef2bbf) and is probably my favourite thing in Python to date. Python is a sexy beast of a language. I then refactored a little bit of code from the US States Game to take advantage of it. I love it!

![image](https://user-images.githubusercontent.com/96394256/217489475-a8d9b41b-5da8-4a38-ba39-340e86a189a2.png)

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/06-us-states) | [Replit](https://replit.com/@ZanClifton/us-states?v=1) |

#

### Day 9: Feb 10 2023, Friday

**Activity:** Dictionary Comprehension

**Thoughts:** Dictionary comprehension is just as lovely as list comprehension. 

![image](https://user-images.githubusercontent.com/96394256/218272535-fca23105-0217-484b-9351-8225f018552a.png)

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/07-nato-alphabet-translator) | [Replit](https://replit.com/@ZanClifton/nato-alphabet-translator?v=1) |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/nato-alphabet-translator.png" width=400px align=right alt="Nato Phonetic Alphabet Translator"/>

### Day 11: Feb 11 2023, Saturday

**Activity:** Nato Phonetic Alphabet Translator

**Thoughts:** Used a little dictionary comprehension with a for loop to create a program that'll take a word and give you the phonetic code for it. 

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/07-nato-alphabet-translator) | [Replit](https://replit.com/@ZanClifton/nato-alphabet-translator?v=1) |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/miles-to-km.png" width=400px align=right alt="Miles to Km Converter"/>

### Day 12: Feb 19 2023, Sunday

**Activity:** Miles to Km Converter

**Thoughts:** Messed around on and off with the Tkinter module for most of the week, but didn't produce an actual project until today. It converts miles (floating point number) into kilometers (also a float with 2 decimal places). The maths and code isn't hard, but the syntax for Tkinter isn't hugely intuitive and it employs classes with *args and **kwargs, which is the first time I've come across this. For the first time in a while I decided I needed to keep references for how these things work for later.

| Project Repo | Project Demo |
|:-------------|:-------------|
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/08-miles-to-km) | [Replit](https://replit.com/@ZanClifton/miles-to-km?v=1) |

#

<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/09-pomodoro/tomato.png" width=200px align=right alt="Pomodoro"/>

### Day 13: Feb 20 2023, Monday

**Activity:** Pomodoro

**Thoughts:** Created the user interface for a pomodoro timer, but none of the functionality as yet. I worry that I'm way too slow at things when it takes me an hour to put something like this together. It's kind of exciting to see the interface building up from a blank window, though. I think I'm getting the hang of various commands now, but finding some of the more obscure kwargs is a challenge.

| Project Repo | Project Demo |
|:-------------|:-------------|i
| [GitHub](https://github.com/ZanClifton/intermediate-python-projects/tree/main/09-pomodoro) | Not yet! Patience, young padawan! |

#
