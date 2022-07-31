# Django_Querysets_and_Managers

* Create a new virtual environment in that folder named venv.  Activate it and install the Django python package (Hint: `pip install Django).

* Also, install the Django rest framework (pip install djangorestframework)

* We want users of our API to view all active links. We also want to provide users with an endpoint to view Links created during the week.

* Create a new file, managers.py in your links app folder. Replace the content of links/managers.py with this starter file https://github.com/TobeTek/Zuri/blob/main/starter-files/Querysets-and-Managers/managers.py  

 

* Add the following attributes to your Link model in links/models.py

```
objects = models.Manager()

public = ActiveLinkManager()
```

* On to the views. Copy the ActiveLinkView and RecentLinkView from  https://github.com/TobeTek/Zuri/blob/main/starter-files/Querysets-and-Managers/views.py to links/views.py.

* Add the following new URL paths in links/urls.py.

```
path("active/", ActiveLinkView.as_view(), name=’active_link’)

path("recent/", RecentLinkView.as_view(), name=’recent_link’)
```

* Stage and Commit your Django project and push your changes to your GitHub repository.
