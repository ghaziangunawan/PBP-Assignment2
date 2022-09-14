# Platform-Based Development Assignment 2

### Heroku Hyperlink : https://pbd-katalog.herokuapp.com/katalog/

**1. Create a diagram containing client request to the Django web application and its response. Also explain the flow of the diagram and how the urls.py, views.py, models.py and HTML files connected each other.**

![diagram (1)](https://user-images.githubusercontent.com/112075463/190153814-6d89d315-51e1-4774-84a2-be6bc434a0f4.png)

Flow of diagram:
1. User fetch/request data that will go to django framework
2. a specific file with mappings called url will sends routing of data to a View
3. View goes to model to retrieve data from the database
4. View also goes to template to retrieve the correct template
5. Views then renders back to user with the the correct template and data 

**2. Explain why do we use virtual environments? Let's say, if we do not use the virtual environments, can we still create a Django web application?**



