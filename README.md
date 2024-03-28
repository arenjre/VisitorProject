# VisitorProject

## Setup on local

Dillinger requires [Python 3.12.2](https://www.python.org/downloads/release/python-3122/)  to run.

Clone the project from github repository
```sh
cd VisitorProject
docker-compose up database -d
docker-compose up server
done!
```

Now create a superuser to login in admin pannel 
```sh
open new console
docker ps
docker exec -sh <container-id> sh
python manage.py createsuperuser
Add the information of superuser
```

Now you can login into admin pannel and add some data, such as Worker, Unit, Visit

APIs...

| API | url path |
| ------ | ------ |
| Get list of units(get method) | http://127.0.0.1:8000/api/units/?phone_number=9008900599 |
| Make a visit(post method) | http://127.0.0.1:8000/api/visit/ |
payload for make a visit API
        {
          "phone_number": "9008900599",
          "unit_pk": 6,
          "coordinates": {
            "latitude": 40.7128,
            "longitude": -74.0060
          }
        }

