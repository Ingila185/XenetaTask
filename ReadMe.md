**Database Setup**

- Setup the database from the docker image in the repository https://github.com/Ingila185/XenetaTaskDbSetup. Follow instructions in Readme.md.


**Backend API Setup**

- Clone the repo https://github.com/Ingila185/XenetaTask.git

- Create Virtual Environment


    ```py -m venv venv```

- Activate the virtual environment using

    ```venv\Scripts\Activate```


- Install all requirements 

    ```pip install requirements.txt```


- Run the application using 


    ```py manage.py runserver```

- Test the applicatiion using the endpoints:

***Port to Port***

    http://127.0.0.1:8000/rates/?date_from=2016-01-01&date_to=2016-01-31&origin=CNSGH&destination=BEZEE

***Port To Region***

    http://127.0.0.1:8000/rates/?date_from=2016-01-01&date_to=2016-01-31&origin=HKHKG&destination=scandinavia

***Region to Port***

    http://127.0.0.1:8000/rates/?date_from=2016-01-01&date_to=2016-01-31&origin=china_south_main&destination=NOBVK

***Region to Region***

    http://127.0.0.1:8000/rates/?date_from=2016-01-01&date_to=2016-01-31&origin=china_south_main&destination=north_europe_main



