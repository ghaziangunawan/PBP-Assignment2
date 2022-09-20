# Platform-Based Development Assignments

# Assignment 2

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

We use virtual environments to have a lightweight and isolated environment for packages and versions so that it does not "pollute" your main package directory and vice versa. Although you can create a django web application without virtual environments it is not recommended because it may create environment issues between your production environment and other environment that is hard to fix.


**3.Explain how did you implement the steps on point 1 to point 4 above**
1. Copying template repository https://github.com/pbp-fasilkom-ui/assignment-repository and clone it to local repository
2. Implement view.py function that stores the data from models, context dictionary, and returns render function that combines katalog.html and the given context dictionary
3. Implement urls.py to create the routing to the views function and register the app in another urls.py located project_django folder
4. change the fill me! in katalog.html to {{name}} and {{student_id}} respectively also adding code to iterate list_item
5. push changes to github 
6. create new heroku application and copy-paste the HEROKU_API_KEY and HEROKU_APP_NAME to the repository secret
7. rerun the failed workflow and the application will be deployed in heroku

# Assignment 3
### Heroku Hyperlink : https://pbd-katalog.herokuapp.com/mywatchlist/ <br>
/html = https://pbd-katalog.herokuapp.com/mywatchlist/html/ <br>
/xml  = https://pbd-katalog.herokuapp.com/mywatchlist/xml/ <br>
/json = https://pbd-katalog.herokuapp.com/mywatchlist/json/

**1. Explain the difference between JSON, XML, and HTML!**<br>

**HTML**<br> HTML which stands for Hyper Text Markup Language is the standard markup language for building web pages/ web applications. HTML describes the structure of web pages and gives the browser the information how to display the content for the web page. HTML consists of series of elements where that elements label the parts of the contents <br>

**XML**<br> XML which stands for eXtensible Markup Language. Just like HTML, XML is also a markup language, but its made for storing and transporting data unlike HTML which are built for the structure of web pages. XML does not do anything but solely just for carrying data where its content is the information with tags<br>

**JSON**<br> 
JavaScript Object Notation or JSON is commonly used for data storage and transfer, in JSON, it is similiar with HTML but it serves different purpose where HTML serves for making the structures of web pages while JSON is for storing and transfering data where everything is represented as an object consisting of attribute–value pairs and arrays in JSON.

**2. Explain why we need the data delivery in implementing a platform!**<br>
Data delivery is crucial when implementing a platform. It is an essential way for sending, fetching, and storing datas for that platforms that is needed for that applications to operate correctly such as displaying some tables, texts, graphics, etc.

**3. Explain why we need the data delivery in implementing a platform!**<br>








