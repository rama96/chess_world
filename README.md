# chess_world
Exploring chess


# Creating env
python3.8 -m venv env
source env/bin/activate

# Creating adding .env
printf "\n# Adding this command to read local .env file" >> env/bin/activate
printf "\nexport \$(grep -v '^#' .env | xargs)" >> env/bin/activate

# Installing requirements
pip install -r requirements/base.txt


# To Do 

## Python 

 Create a Class for the following points --
 1. TO make a move
 2. Store the current board at any point of time 
 3. A button to reset teh board
 4. A function that returns the chessboard on whos turn it is

## HTML

Create a template which basically accepts the FEN arg from the user and returns/displays the board on teh website
Create a template which basically accepts the FEN arg from the user and returns/displays the board on teh website