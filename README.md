# chess_world
Exploring chess


# Creating env
python3.8 -m venv env
source env/bin/activate

# Creating adding .env
printf "\n# Adding this command to read local .env file" >> env/bin/activate
printf "\nexport \$(grep -v '^#' .env | xargs)" >> env/bin/activate