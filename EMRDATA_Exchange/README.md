# EMRDATA_EXCHANGE
a Electronic Medical Record  Application which is a bi-directional interface using the FHIR Standard for seamless sharing and retrieval of electronic medical records (EMRs) among healthcare providers

# Follow The steps to run the project 
1.First you have to create an virtual environment .<br>
2.Create virtual environment in the base directory and put the whole project into the other folder.

python -m venv {Environment_name}             # command for creating virtual env<br>

3.install this packages :

pip install asgiref==3.7.2                    # to install asgiref==3.7.2<br>
pip install Django==5.0.1                     # to install Django==5.0.1<br>
pip install sqlparse==0.4.4                   # to install sqlparse==0.4.4<br>
pip install tzdata==2023.4                    # to install tzdata==2023.4<br>


4.After installing the below packages you to mention it into the setting.py (INSTALLED_APPS):

pip install djangorestframework               # to install  Djnago rest Framework<br>
pip install djangorestframework-simplejwt     # to  install JWT module<br>


5.After Creating the virtual environment ,you have to go to Scripts folder and activate the Scripts (in virtual environment)<br>
6.And now go to the project Directory and start the local server

python manage.py runserver                     # to start the server<br>
python manage.py createsuperuser               # to create Admin Interface<br>
python manage.py makemigrations                # to migrate models of the database<br>
python manage.py migrate






















