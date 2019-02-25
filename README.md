# django-moreViews-cw

### Exercise 1
- Create a "hello" route that takes a name in the URL and returns a response with "hello [NAME]".
- Create a "times2" route that takes an argument in the URL and returns a response with "The product times 2 is: [ANSWER]"
- Create a "total" route that takes an integer in the URL and returns a response with "The sum of all numbers from 0 to the integer is: [SUM]"

### Exercise 2
Using the Cup model/schema create
Create a Cup model/schema with name, material, and manufacturerDate attributes. Create 3 entries using 3 different methods (admin site, create method using an endpoint, and class construtor using an endpoint).

Create an 'all/' endpoint that prints out all entry purchaseTimes and create another new endpoint to change the material text of cups manufactured after 2012 to be "Slightly New".

### Exercise 3
Using the same project/app from Exercise 2, create a django template for the route URL. Do the following in the template:
- Display your name in large letters at the top
- Display all entries in the database as an HTML list
- Display "Here are all of the cups manufactured after 2012"
- Display all cups manufacturered after 2012
<hr>
2 points.
