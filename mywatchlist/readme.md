# Assignment 3
### Heroku Hyperlink : https://pbd-katalog.herokuapp.com/mywatchlist/ <br>
/html = https://pbd-katalog.herokuapp.com/mywatchlist/html/ <br>
/xml  = https://pbd-katalog.herokuapp.com/mywatchlist/xml/ <br>
/json = https://pbd-katalog.herokuapp.com/mywatchlist/json/

**- Explain the difference between JSON, XML, and HTML!**<br>

**HTML**<br> HTML which stands for Hyper Text Markup Language is the standard markup language for building web pages/ web applications. HTML describes the structure of web pages and gives the browser the information how to display the content for the web page. HTML consists of series of elements where that elements label the parts of the contents <br>

**XML**<br> XML which stands for eXtensible Markup Language. Just like HTML, XML is also a markup language, but its made for storing and transporting data unlike HTML which are built for the structure of web pages. XML does not do anything but solely just for carrying data where its content is the information with tags<br>

**JSON**<br> 
JavaScript Object Notation or JSON is commonly used for data storage and transfer, in JSON, it is similiar with HTML but it serves different purpose where HTML serves for making the structures of web pages while JSON is for storing and transfering data where everything is represented as an object consisting of attribute–value pairs and arrays in JSON.

**- Explain why we need the data delivery in implementing a platform!**<br>
Data delivery is crucial when implementing a platform. It is an essential way for sending, fetching, and storing datas for that platforms that is needed for that applications to operate correctly such as displaying some tables, texts, graphics, etc.

**- Explain how you can implement the checklists above**<br>
1. Creating and configuring mywatchlist app and its models by running "python manage.py startapp mywatchlist in local repository", adding mywatchlist in the installed apps in settings.py, adding the models in models.py, and migrating it <br>
2. making folder fixtures and adding "initial_watchlist_data.json" and its data content of 10 datas <br>
3. configuring views.py by adding the necessary functions <br>
4. Creating folder templates and adding watchlist.html and its content along with configuring some css styles<br>
5. Making routings by creating urls.py for the views function and adding path to urls.py located in project_django folder

**Postman Screenshots**<br>
<img width="1060" alt="Screen Shot 2022-09-20 at 21 29 23" src="https://user-images.githubusercontent.com/112075463/191285670-0f5d252a-06fc-4f58-89dc-34731993381a.png"> <br>

<img width="1060" alt="Screen Shot 2022-09-20 at 21 29 33" src="https://user-images.githubusercontent.com/112075463/191285950-f88aabbf-de5e-4edf-9c07-ea6550bb32e3.png"><br>


<img width="1060" alt="Screen Shot 2022-09-20 at 21 29 42" src="https://user-images.githubusercontent.com/112075463/191286136-e4c4b83f-d1a0-4ec1-896b-5d5b4f241135.png"><br>
