
# Assignment 4
### Heroku Hyperlink : https://pbd-katalog.herokuapp.com/todolist/<br>
**- What does {% csrf_token %} do in the form element? What happens if there is no such "code snippet" in the form element?**<br>
CSRF (cross-site request forgery) token is token that is unique to every user session which is used to prevent a CSRF attack, an attack where the attacker 'hijacks' the user session when the user clicks on a malicious links and submits a form on the malicious links then the ongoing site session is used by the malicious link. To create this token, Django will use the get_token() function in the ../Middleware/csrf.py file to encode the real csrf token so that it cannot be seen by other websites. without this csrf token django will throw a 403 client error "csrf verification failed" because it is enabled by default in the settings.py which means if we use an unsafe methode such as POST,PUT, and delete csrf token must be used as without csrf token there will be no security against CSRF attack


**- Can we create the form element manually (without using a generator like form.as_table ? Explain generally how to create form manually.**<br>
Yes we can create form element manually. To do this we need to add form tag with method such as POST and GET and the csrf token tag and then we can create the inputs and buttons. After that we need to configure the views.py file using request."form-method".get("input name")


**- Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.**<br>
user initial request will be routed to views.py, then views will route it to the html file using return render(request, 'file_name.html',context), after html form is received by the user, the user will fill the form and submit it. then the submission will be returned back to views.py which will be prosessed with the if request.method == "POST" code block and then returned a response accordingly back to the user
  
**- Explain how you implement the checklist above.**<br>
1. Run the python3 manage.py startapp todolist command and then add todolist in the installed application in settings.py and urls in urls.py in project_django folder<br>
  
2. Create class task and add user,date,title, and description models in models.py and then run python3 manage.py makemigrations and python3 manage.py migrate <br> 
  
3. Implement the registration, login, and logout forms and its routing by following the lab 3 tutorial<br>

4. creating the create-task page by adding new_task function in views.py, routing in urls.py and the new_task.html file in template folder<br>

5. add, commit, and push to github and github will automatically deploy the changes in the repository
  

