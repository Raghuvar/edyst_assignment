### A Simple flask app that counts words in given URL.
 
 ## Setup
Following steps assume that you have python3 installed and created a virtual enviroment on your computer.

1. Create a virtual env
 If you don't have virtualenv installed do install with:
	`virtualenv -p python <name_of_env>`

2. Activate the virtual env using `source <name_of_env>/bin/activate` and navigate to the root directory of app.
 ### Install the dependencies using
	`pip install -r requirements.txt`
 
3. Run redis worker

	`python worker.py`
  
	> Note: Keep this *worker* running in background.
 
4. Create Database
	In a new terminal window (In your virtualenv) run the create_db.py file to build the database configuration 
		`python create_db.py`
 
5. Run the application server
	In new teminal window run the app using
		`python app.py`

## Open your browser and browse: http://localhost:5000/ or http://127.0.0.1:5000/

### Sample Tests
	Open a new window in virtual environment, then run tests using
		`python tests.py`



