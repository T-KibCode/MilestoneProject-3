![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# App Deployment Link: 
- https://news-flash.herokuapp.com/ 
# GitHub Repository link: 
- https://github.com/T-KibCode/MilestoneProject-3 

# Introduction

This project is the third one I've undertaken as part of the Full Stack Software Diploma course at [Codeinstitute.net](https://www.CodeInstitute.net).

NewsFlash! - Social Media Website
Welcome to NewsFlash!, a social media website where users can share their impressions of the world and real-life experiences. This README will provide you with detailed information about the project, its original goal, and the new direction it has taken.

After careful consideration, I  decided to move the project in this direction. I recognized the need for a platform where individuals could share their personal experiences, opinions, and thoughts about everyday affairs, similar to other social media websites. This led us to the development of NewsFlash!, a social media website that encourages users to express themselves and connect with others through their real-life experiences.

If running the app locally, please run python run.py or python3 run.py respectively.

# First Time Visitor Goals

Key Features of NewsFlash!
NewsFlash! offers a range of features designed to foster engagement and facilitate meaningful conversations:

Personal Stories: Users can share their own stories and experiences, whether they are heartwarming, funny, inspiring, or thought-provoking. 

Impressions: NewsFlash! allows users to express their impressions of various topics, such as current events, social issues, entertainment, travel, and more. Users can post their thoughts, opinions, and viewpoints, initiating conversations and encouraging others to share their perspectives.

Interaction on the site: Users can engage in discussions by commenting on stories and impressions. This fosters a sense of community and enables users to connect with others who have similar interests or opinions, as well as research further into the topics reported.

Personal Profiles: Each user has a personal profile which can be created against an email address, allowing the user to post on the website for their given subject matter/story. In order to do so, they will need to create a User account at the Register page. This will then allow the user to post their story/news report to the website so that other users can see. 

Technologies Used
To build NewsFlash!, I utilized the following technologies:

Frontend: The frontend of NewsFlash! was developed using HTML5, CSS3, JavaScript, and the Flask-Bootstrap library.
  
Backend: We used Flask, a Python web framework, along with various libraries and packages including bcrypt, blinker, cachetools, certifi, cffi, chardet, charset-normalizer, click, cryptography, distlib, dnspython, dominate, email-validator, env.py, filelock, Flask-Bcrypt, Flask-Bootstrap, Flask-Login, Flask-Mail, Flask-SQLAlchemy, Flask-WTF, google-api-core, google-api-python-client, google-auth, google-auth-httplib2, google-auth-oauthlib, googleapis-common-protos, greenlet, gspread, itsdangerous, Jinja2, jwt, MarkupSafe, mysql, mysqlclient, numpy, oauthlib, odict, optional-django, packaging, pandas, pgsql, Pillow, platformdirs, pluggy, plumber, protobuf, psycopg2-binary, pyasn1, pyasn1-modules, pycparser, PyJWT, pyodbc, pyOpenSSL, pyparsing, pytest, python-dateutil, pytz, PyYAML, requests, requests-oauthlib, rsa, six, SQLAlchemy, svgwrite, touch, Tree, typing_extensions, tzdata, uritemplate, urllib3, values, virtualenv, visitor, Werkzeug, wget, WTForms, zope.component, zope.deferredimport, zope.deprecation, zope.event, zope.hookable, zope.interface, zope.lifecycleevent, and zope.proxy.

The Use of the multiple backend packages was to deal with the initial building blocks of the backend database when planning which packages would be used. However as I ran out of time towards the end of the project, I have had to strip back my intial ideas that I wanted to put into this project, and will instead talk about them as if they were to be implemented within a future release.

These include the ability for users to comment on other user's posts, whilst maintaining the security of each individual contribution to that post. This would allow each user to ability to #CREATE their post( or a comment on someone else's post), #READ the post along with the date and time that comment/post was made, #UPDATE their post/ comment that the individual has contributed securely, and #DELETE their comment/post if the user wishes to do so, there fulfilling the CRUD function needed within the app.


# User Stories
  
### First Time Visitor Goals

  As a first-time visitor, I want:  

- the layout of the website function to be clear, front and center  
- to be able to easily create and log in to a user account. 
- to be able for each user to be able to delete and create posts as they wish. 
- to be able to look at other users posts. 
  
### Website's Owner Goals

  As the developer I want:


- to create a comments section that allows users to leave posts following the CRUD format.
- to lead the user down a pseudo-constructed path, in order to provide a semi-streamlined experience with the website.
- to create a separate database for the users to write to i.e. comments/reviews etc, (in this case utilizing sqlite3).


# Initial template build process - understanding functions available


### Initial test processes

  In my initial commits within the repository, I had issues initially getting my Flask modules to be recognized and for the app.py python file to render to the HTML file.
  [/]

  I cited an external resource in order to solve the issue of routing which was at the following link on youtube.
  [https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH].
  Using this allowed me to get through the majority of my build process following the guidance within these instructional videos.

This was used to create a demo sql table for me to call information within my request function within my javascript page.
The issues I faced during this process were a variety of a few not limited to:

- My instance os VsCode (chosen IDE environment) having compatibility issues due to my machine only being able to run OSX 10.13.6 (High Sierra) at its highest version causing issues when attempting to install mysql and mongosh commands through the terminal commands whether that be through the Homebrew function, of that be through the pip3 install function.

- Having to code across multiple IDE instances depending upon where I was when working on my project (a separate Macbook again circa 2010-2012 that I keep at my parent's house) and therefore not always having access to my initial creds.json information.

- Attempting to create a custom SQL table to call information from as I was unable to connect to my Postgresql database within my machine instance (again due to OSX compatibility issues).

- due to an older instructional video and updates to security measures, as well as my computer's outdated OS system, I was unable to complete the email security function portion of this part of the instructional video. However, I will highlight the areas of improvement for future work and future projects going forward.

# Online Validators

### W3 HTML 
- The W3 HTML validator only returned one Error in the validation error of missing alt tag within my <img> profile for users' photos that are uploaded to use for their profiles. This was resolved with only a minor warning of a *main* element tag being returned as unnecessary, however, this does not hinder the function of the app in any way shape or form. 

### W3 C3S

- The W3 C3S validator returned a number of errors due to the use of the CDN link of Bootstrap within my project file. These however do not affect the interaction of the web app in anyway and are sometimes returned with using both custom CSS and CDN CSS from an external library within the same project. 

### PEP8 Validator
- When running my python code through the validator, it returned an average score of 56%, so I looked for tools that I could use online in order to improve my validation score on the code itself. I then found the website *Online Python Formatter* {https://www.tutorialspoint.com/online_python_formatter.htm} and using this website, I was able to correct indentation errors in my code to make it both more readable, but also ensure the Python code reaches 100% validation through the PEP8 syntax checker. 

Any Python code that does not run through this validator within my project is redundant, though I have kept it present for the sake of showing my initial planning before the step change within my project. However in a fully commercial production environment, these would be deleted/removed. 

### Javascript validator
- As this project did not use any javascript outside of the Bootstrap CDN link, there was no need to run any JS through an external validator. 


# Website Theme/Designs
The Website uses a simple Scroll Method Gradient, however in future iterations when the ability to comment on other users' posts, There will then be a more focused branding and color to focus the theme of the website and the users. 

![Screen Shot 2023-05-31 at 23 06 33](https://github.com/T-KibCode/MilestoneProject-3/assets/110776212/28663a78-c9d1-4fca-94c1-26adad509182)

These were the initial sketch plans of how I wanted the movie app to beging to take shape and look at, but I found I was lacking in time, hence the simpified the version of app has been used in this case:

![Screen Shot 2023-04-11 at 20 29 44](https://github.com/T-KibCode/MilestoneProject-3/assets/110776212/0a7b6ae9-d298-409e-9a35-7dba0e414aa1)

# Mobile Responsive

The App I've designed is fully mobile responsive for all users and has been tested within multiple browsers to ensure its effectiveness.

# Deployment

The App has been deployed using Heroku and can be found at the following link: https://news-flash.herokuapp.com/.
I used the following steps to deploy the app to Heroku:
- Log into the Heroku website and create a new app.
- Select the region closest to you.
- Click on the Deploy tab and select Heroku Git as the deployment method.
- Install the Heroku CLI and log into your account using the command heroku login -i.
- Create a requirements.txt file using the command pip3 freeze > requirements.txt.
- Create a Procfile using the command echo web: python app.py > Procfile.
- Add and commit the files to Git using the commands git add . and git commit -m "Initial commit".
- Add the Heroku app as a remote using the command heroku git:remote -a <news-flash>.
- Push the files to Heroku using the command git push heroku master.
- Set the IP and PORT environment variables in the Heroku Config Vars.
- Click on the Deploy Tab and click on Enable Automatic Deploys.
- Link the App to the GitHub repository using the Connect to GitHub option.
- Click on Deploy Branch to deploy the app to Heroku.
- Check that the app now deploys when a commit is made to github.


