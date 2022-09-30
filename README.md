# Globant Techical Test Quickstart - Python Pokeberry API

This is a Pokeberry API app project developed for the Python developer Globant Techical Test. It uses the [Flask](https://flask.palletsprojects.com/en/2.0.x/) web framework. Please follow the instructions below to get set up.

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository

   ```git
   $ git clone https://github.com/ben-tiki/globant-technical-exercise.git
    ```

3. Navigate into the project directory

   ```bash
   $ cd globant-technical-exercise
   ```

4. Create a new virtual environment

   ```bash
   $ python -m venv venv
   $ . venv/Scripts/activate
   ```

5. Install the requirements

   ```bash
   $ pip install -r requirements.txt
   ```

6. Run the app

   ```bash
   $ flask run
   ```

You should now be able to access the app at [http://localhost:5000](http://localhost:5000)! 

## API Documentation
Endpoint: /allBerryStats

Method: GET

Description: Returns all the berries and their growth time stats in JSON format.

Example response:

![image](https://user-images.githubusercontent.com/101474762/193174745-bbe1a763-92f5-4f08-977c-90e72a8872fb.png)

---
Endpoint: /allBerryDashboard

Method: GET

Description: Returns the information in plain HTML format. Displaying a table with all the berries and their growth time stats, side by side with a histogram of the growth time.

Example response:
![image](https://user-images.githubusercontent.com/101474762/193161384-f5b1b349-f1c5-4e92-bf30-62327710595a.png)

---
Endpoint: /berries

Method: GET

Description: Returns all berry names in plain HTML as list items.

Example response:
![image](https://user-images.githubusercontent.com/101474762/193161622-ba7af5f1-7606-43bd-9dae-b4441be3c865.png)

---
