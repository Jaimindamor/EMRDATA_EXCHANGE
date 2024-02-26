# EMRDATA_EXCHANGE
a Electronic Medical Record  Application which is a bi-directional interface using the FHIR Standard for seamless sharing and retrieval of electronic medical records (EMRs) among healthcare providers

# Follow The steps to run the project 
1.First you have to create an virtual environment and you have to install this packages.<br>
2.Create virtual environment in the base directory and put the whole into the other folder.

python -m venv {Environment_name}             # command for creating virtual env

pip install asgiref==3.7.2                    # to install asgiref==3.7.2
pip install Django==5.0.1                     # to install Django==5.0.1
pip install sqlparse==0.4.4                   # to install sqlparse==0.4.4
pip install tzdata==2023.4                    # to install tzdata==2023.4


3.After installing the below packages you to mention it into the setting.py (INSTALLED_APPS):

pip install djangorestframework               # to install  Djnago rest Framework
pip install djangorestframework-simplejwt     # to  install JWT module


4.After Creating the virtual environment ,you have to go to Scripts folder and activate the Scripts (in virtual environment)<br>
5.And now go to the project Directory and start the local server

python manage.py runserver                     # to start the server
python manage.py createsuperuser               # to create Admin Interface
python manage.py makemigrations                # to migrate models of the database
python manage.py migrate






















