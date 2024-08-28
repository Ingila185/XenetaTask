**Database Setup**

- Setup the database from the docker image in the repository https://github.com/Ingila185/XenetaTaskDbSetup. Follow instructions in Readme.md.


**Backend API Setup**

- Clone the repo https://github.com/Ingila185/XenetaTask.git

- Create Virtual Environment


    ```py -m venv venv```


- Install all requirements 

    ```pip install requirements.txt```


- Run the application using 


    ```py manage.py runserver```

- Test the applicatiion using the endpoints:


    http://127.0.0.1:8000/rates/?date_from=2016-01-01&date_to=2016-01-31&origin=CNSGH&destination=BEZEE



