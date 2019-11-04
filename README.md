# Online Cook Book



The brief for this code Institute data Centric Project was to build a back-end applicaiton using Flask framework.
The site should support the user to be able to create, edit and delete recipes from the front end.  The back end logic should support a well designed database schema for the user to have interactive control.

# UX

When designed this application, the main focus was to make the site navigation and ease of recipe building easy and quick.  Therefore, some functionality in terms of uploading images to the database were ignored and instead replaced with a json file of pre-loaded images which are automatically inserted if a condition is met.  Furthermore, this application has maintained minimal html pages to support user navigation and remain focused on the objective of finding recipes, creating recipes and editing recipes.

  - As a user I would like to enter the site and see available recipes which are clearly marked in terms of what the recipe is
  - As a user I would like to see visual images which describe the recipe before reading too much about the recipe.
  - As a user when creating a recipe, I dont want the process to be a time consuming exercise.  I dont want to have to take photos and upload, and i dont want too many fields to enter.  
  - As a user I just want a snapshot of a recipe idea that i am interested in so that i can get a basic understanding of the ingredients and preperation.

# Wireframes

Available in project directory

# Features

The features of this application were mostly biult from [materializecss.com].  The features were;
 - Cards - a nice way of displaying the recipes in a clean and user friendly manner
 - Buttons / a link - the buttons are well displayed for the user to see and action
 - Forms - the user is able to fill out forms to add and edit 
 - Dropdown - populated recipe dropdown link is available for the user to quickly and easily start creating recipes

# Features left to implement

As a starter application, the content and user intergration is limited.  Therfore, future implementations would be to biuld on the existing site to make it more interactive by developing more user stories and looking at how to allow the user full control and protection when creating recipes.
 - User login - when logged in the user can create, edit and delete recipes.  The user can only edit or delete recipes they created.
 - User can create their own food categories - this functionality was not included as the current set up is designed to populate a specfic image when a category is selected - reasons exlplained in user stories.  
 - Potential to develop the form fields more to allow specific recipe considerations such as allergen issues.  The user can add notes however the current site does not support users who may want to know more detailed information about the orgin of the food etc or other spefic food health considerations.
 - Paigination and Search options - Search options could be as specific as ingredients / food category / recipe name / most popular 

# Technologies Used


* [HTML 5](https://html.spec.whatwg.org/) - basic templating language
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference) - site styling
* [Materialize](materializecss.com/) - HTML structure for mobile first navigation
* [JQuery](https://code.jquery.com/) - front end site functionality
* [JavaScript](https://www.keycdn.com/support/javascript-cdn-resources) - front end 
* [Flask](http://flask.palletsprojects.com/en/1.1.x//) - python platform for project
* [Python](https://www.python.org/) - backend functionality
* [AWS](https://aws.amazon.com/) - devlopment platform 
* [MongoDB](https://cloud.mongodb.com//) - database
* [Heroku](https://dashboard.heroku.com/) - site hosisting platform


### Testing

Recipe displays correctly in index.html
 - When recipe was created through MDB, it was tested that it rendered correctly and was then styled.
 - Functionality was then biult to add recipe through front end and tested.
 - Multiple recipes were created to test page layout and user viewing in all screen resolutions
 - When a recipe was created, the image laded from the json file was tested that the correct images were linked to the recipe category
 
 Recipe can be edited
  - Functionality was biult to allow a specific recipe to be edited.
  - Tested that no duplicates were created and that all changes made saved correctly and re-populated tot he html page
  - Tested that after submission, the site returns to index.html
 
 Recipe can be deleted
  - functionality built to allow user to delete a recipe 
  
Testing considerations when designed the site for the user
- When editing a recipe the format looks the same as creating a recipe - this was done so that the user is familiar with the process.
- The buttons are clearly visable and well placed so that the user can see that an action is available or required.
- To ensure that the site information looks full - yet without overloading the site with content - field values were allocated to keep text input minimal or required.
- Page styling - the site orginally had a full imgae background but there were some rendering site responsiveness issues therefore it was removed.
- The same processes were followed when creating the review sections.

Testing flow

Generally, testing of the site in terms of the functionality, styling, layout and user story expereince was completed at each stage of the project and committed.

Initial Project Testing

Before the project the initialised, the required dependencies, important passwords and settings for Heroku were implmeneted and tested so that the project would be ready to be published on completion.

  
### Site Responsive

As the site used Materalize for the html grid layouts, the formatting styled the site similar to bootstrap.  Media queries were written in the CSS file for more specific details.  This was in part because it was easier to write in CSS than learn the new typography, color styling that materialize has - generally, the site has incorporated abit of both.

### Debugging

I tested having a gallery.html page to install the images but decided to create a json file instead and create a python if statement.  The biggest challnages i had was creating a pagination for the application.  In the future, creating more forms and then biulding routes would make it easier to build pagination for the application.


### Deployment

The project was started on AWS 9 and a repository was created on GitHub.  After settig up the required requirments.txt dependencies and Procfile the project was then master git origin to heroku.  Heroku settings and AWS passwords settings were dealt with at the beginning of the application.
Upon completion of the project, the final push to GitHub is the same project as is deployed on Heroku
> URI database saved to bashrc file and added to local convig vars in Heroku
> git add .
> git commit -m
> git push heroku master



### Credits

- Basic functionality of the code comes from the Code Institute learning course Data Centrics - further guidance was found from the CI Slack community - especially when reading up on Pagination and Search fields
- Stack Overflow - Sort in HTML
- Stack Overflow - JS code for the mobile versoning header text

### Media
- Unsplash - https://unsplash.com/
