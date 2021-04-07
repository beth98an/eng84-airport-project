# Airport App
Python Project for SpartaGlobal Engineering 84 DevOps Stream.

## Table of Contents
- [User Stories](#user-stories)
- [Documentation](#documentation)
- [Project Structure](#project-structure)


## User Stories
- As an airport assistant, I want to be to create passengers with name AND passport number, so that I can add them flight.
- As an airport assistant, I want to be able to assign or change flight destinations or departure dates with user passwords.
- As an airport assistant, I want to create a flight trip with a specific destination.
- As an airport assistant, I want to be able to generate a flight_attendees_list_report that lists passengers' names and passports to check identity.
- As an airport assistant, I want to be able to add passengers to a flight so I can sell tickets to them


## Documentation
Prerequisites:
- python 3.7+
- git cli

To work on the project, clone it in your local machine:
```bash
git clone https://github.com/conjectures/eng84-airport-project.git
```
Change directory to the downloaded folder:
```bash
cd eng84-airport-project
```
It is highly recommended to use a virtual environment to install the python packages.

When the virutal environment is activated, run
```bash
python -m pip install -r requirements.txt
```
> *Note: Might need to substitude `python` with `python3` in certain linux distributions. If `python --version` outputs a python version of 3.x+ then the above snippet will work properly.*

After all the requirements are installed, the app will be almost ready to run. Change directory to the `app/` folder, then enter the following commands sequentially.
```bash
python manage.py makemigrations
python manage.py migrate
```
As the database is not tracked in the github repository, you need to create a new `sqlite3` database on your machine. With the above commands, the database is initialised with the models required.

If you already have a previous version of the project, some conflicts will arise with the database. It might be more beneficial to remove `db.sqlite3` and try again, if the issue cannot be resolved via the commandline.

After the migrations are complete, it is time to run the project on a localhost:
```bash
python manage.py runserver
```
The above command will run a localhost server on port 8000 on your machine. To view the app, open any browser and type on the URL `127.0.0.1:8000` or `localhost:8000` for your convenience.

## Project Structure
The project is organised as follows:

```python
# Repository folder. Contains all project files.
eng84-airport-project/
  # Files required for git tracking
  .git/
  ...
  ...
  # Files for the Django project
  app/
    # Temporary database
    db.sqlite3
    # Django App 'starter' file
    manage.py
    # Project files and settings are stored here:
    airportapp/
      ...
      ...
      settings.py
    # All the functionality is stored here.
    core/
      ...
      ...
      ...
      # The html templates are stored here.
      templates/
```
