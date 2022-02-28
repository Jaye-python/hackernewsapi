# hackernewsapi
## This project is to synchronize a database with news provided by [Hackernews API](https://hackernews.api-docs.io/).
### Tasks to be done:
1. Sync the published news from hackernews to the DB every 5 minutes (this was accomplished using Celery)
2. Implement a view to list the latest news with pagination
3. Create a detail view to see news items in detail
4. Create a filter box to allow filtering by the type of item
5. Implement a search box for filtering by text
6. Create a GET request API to consume DB objects (this was accomplished using Django Rest Framework APIVIEW)
7. Create a POST request API to add news items to the DB
8. Items created via hackernews sync should not be deletable, only items created via API should be allowed to be deleted (this was accomplished by first creating a DB Boolean field titled: **'API_CREATED'** with a default value of **'False'**. When a news item is created via API, this field is set to **'True'** at the view level. Only objects with **True** for this field are allowed to be deleted

#### To implement (Note: These are Linux commands):
1. Navigate to your desktop
```
$ cd Desktop
```
2. Create new folder/directory
```
$ mkdir hackernews
```
3. Navigate into this new folder
```
$ cd hackernews
```
4. Create new Python Virtual environment
```
$ python3 -m venv ./venv
```
5. Activate this new virtual environment
```
$ source venv/bin/activate
```
6. Clone this git repo
```
$ git clone https://github.com/Jaye-python/hackernewsapi.git
```
7. Move into the hackernews folder 
```
$ cd hackernews
```
8. Install dependencies
```
$ pip install -r requirements.txt
```
9. Run
```
$ ./manage.py runserver
```
See ss.png:
! [Django Project Creation_Jaye] (/ss.png)
