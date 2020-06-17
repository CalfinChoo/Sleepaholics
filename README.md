# Pictionary by Sleepaholics

Project Demo - https://youtu.be/VtDzaOfFopg

**ROSTER** <br>
Calvin Chu - Project Manager, SVG/Game Handler <br>
Jeff Lin - Websockets, Frontend <br>
Jackson Zou - Backend, Frontend <br>
Derek Leung - SVG/Game Handler <br><br>

**DESCRIPTION** <br>
A playable Pictionary game between multiple players. The game will be constantly reloaded to keep track of inputs from multiple users, and allow for a real-time game. 

<br><br>
**HOW TO RUN THE PROJECT**
<br>Before you run: <br>
Download flask from home directory
```
$ python3 -m venv [insert hero]                          #creates virtual environment
$ . hero/bin/activate                                    #activates virtual environment
(hero)$ pip install -r doc/requirements.txt              #installs all required packages
(hero)$ deactivate                                       #deactivates the virtual environment (do after you finish testing)
```

Running the project:
1. Clone the repository
```
git clone https://github.com/CalfinChoo/Sleepaholics.git
```
2. Run the main python program
```
python3 app/__init__.py
```
3. Copy and paste the local url into your browser (<http://127.0.0.1:5000/>)
