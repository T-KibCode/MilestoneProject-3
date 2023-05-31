![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# App Deployment Link: 
- https://news-flash.herokuapp.com/ 
# GitHub Repository link: 
- https://github.com/T-KibCode/MilestoneProject-3 

# Introduction

This project is the third one I've undertaken as part of the Full Stack Software Diploma course at [Codeinstitute.net](https://www.CodeInstitute.net).

NewsFlash! - Social Media Website
Welcome to NewsFlash!, a social media website where users can share their impressions of the world and real-life experiences. This README will provide you with detailed information about the project, its original goal, and the new direction it has taken.

Original Project Idea
Originally, the project aimed to create a movie review website that would allow users to leave comments and reviews on various movies. The website was designed to utilize PostgreSQL as the movie database and SQLite for the user database. Users would have been able to browse and search for movies, read and write reviews, and engage in discussions related to their favorite films.

Pivot to NewsFlash!
However, after careful consideration and feedback from users, I  decided to pivot the project in a new direction. We recognized the need for a platform where individuals could share their personal experiences, opinions, and thoughts beyond just movie reviews. This led us to the development of NewsFlash!, a social media website that encourages users to express themselves and connect with others through their real-life experiences.

If running the app locally, please run python run.py or python3 run.py respectively.

# First Time Visitor Goals

Key Features of NewsFlash!
NewsFlash! offers a range of features designed to foster engagement and facilitate meaningful conversations:

Personal Stories: Users can share their own stories and experiences, whether they are heartwarming, funny, inspiring, or thought-provoking. They can write detailed accounts, attach relevant images or videos, and add tags to categorize their stories.

Impressions: NewsFlash! allows users to express their impressions of various topics, such as current events, social issues, entertainment, travel, and more. Users can post their thoughts, opinions, and viewpoints, initiating conversations and encouraging others to share their perspectives.

Interaction on the site: Users can engage in discussions by commenting on stories and impressions. This fosters a sense of community and enables users to connect with others who have similar interests or opinions, as well as research further into the topics reported.

Personal Profiles: Each user has a personal profile which can be created against an email address, allowing the user to post on the website for their given subject matter/story. In order to do so, they will need to create a User account at the Register page. This will then allow the user to then post their story/news report to the website that other users can see. 

Technologies Used
To build NewsFlash!, we utilized the following technologies:

Frontend: The frontend of NewsFlash! was developed using HTML5, CSS3, JavaScript, and the Flask-Bootstrap library.
  
Backend: We used Flask, a Python web framework, along with various libraries and packages including bcrypt, blinker, cachetools, certifi, cffi, chardet, charset-normalizer, click, cryptography, distlib, dnspython, dominate, email-validator, env.py, filelock, Flask-Bcrypt, Flask-Bootstrap, Flask-Login, Flask-Mail, Flask-SQLAlchemy, Flask-WTF, google-api-core, google-api-python-client, google-auth, google-auth-httplib2, google-auth-oauthlib, googleapis-common-protos, greenlet, gspread, itsdangerous, Jinja2, jwt, MarkupSafe, mysql, mysqlclient, numpy, oauthlib, odict, optional-django, packaging, pandas, pgsql, Pillow, platformdirs, pluggy, plumber, protobuf, psycopg2-binary, pyasn1, pyasn1-modules, pycparser, PyJWT, pyodbc, pyOpenSSL, pyparsing, pytest, python-dateutil, pytz, PyYAML, requests, requests-oauthlib, rsa, six, SQLAlchemy, svgwrite, touch, Tree, typing_extensions, tzdata, uritemplate, urllib3, values, virtualenv, visitor, Werkzeug, wget, WTForms, zope.component, zope.deferredimport, zope.deprecation, zope.event, zope.hookable, zope.interface, zope.lifecycleevent, and zope.proxy.

The Use of the multiple backend packges was to deal with the initial building blocks of the backend database when planning which packages would be used. However as I ran out of time towards the end of the project, I have had to strip back my intial idea's that I wanted to put into this project, and will instead talk about them as if they were to be implmented within a future release.

These include: The ability for users to comment on other users post, whilst maintaining the security of each individuals contribtions to that post. This would allow each user to ability to #CREATE their post( or a comment on someone else's post), #READ the post along with the date and time that comment/post was made, #UPDATE their post/ comment that the individual has contributed securely, and #DELETE their comment/post if the user wishes to do so, there fufilling the CRUD function needed within the app.
  
However, it should be noted, that I would like to expand this in future instances to be closer to the original vision of this app as a movie/tv show social website with the following User stories and aims;

# User Stories
  
### First Time Visitor Goals

  As a first time visitor I want:  

- the search function for movie reviews to be clear, front and center  
- to be able to filter by multiple fields, such as genre, year of release, age rating
- to be able to create user account to interact with other users
  
### Return/frequent Visitor Goals

  As a return/frequent visitor I want:  

- to be able to score films/movies I have seen.
- to be able to save movies to a personal favourites page to keep personal track.
- to be able to leave comment reviews on individual movie pages with the ability to edit the comments.
- to allow the registered user to be able to filter if they see user reviews or not.
  
### Website's Owner Goals

  As the developer I want:

- to correctly create a relational database that pulls the information the user requires of their search i.e after searching a certain parameter, being able to filter down the returned results such as, release date filter being applied when searching the horrow genre to find movies released in a certain window whether that be annual or seasonal.
- to create a comments section that allows user's to leave word-limited reviews following the CRUD format.
- to lead the user down a pusedo-constructed path, in order to provide a semi-streamlined experience with the website.
- to either create a database, or use an available API call for a pre-existing movie database that can be used to pull names, lead actors, directors, release dates and series links in to the site.
- to create a seperate database for the users to write to i.e comments/reviews etc, movies scores etc.


# Initial template build process - understanding functions available


### Initial test processes

  In my initial commits within the repository, I had issues intially getting my Flask modules to be recognised and for the app.py python file to render to the html file.
  [/]

  I cited an external resource in order to solve the issue of routing which was at the following link on youtube.
  [https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH].
  Using this allowed me get through the majority of my build process following the guidiance within these instructional videos.

I've had to use an online conversion tool in order to convert a movie database from a tsv.gz file , to uncompress the file into .tsv format, and to convert it using a website named [https://www.convertsimple.com/convert-tsv-to-sql-insert-statement/]

This was used to create a demo sql table for me to call information within my request function within my javascript page.
The issues I faced during this process where a variety of a few not limited to:

- My instance os VsCode (chosen IDE enviroment) having compatability issues due to my machine only being able to run OSX 10.13.6 (High Sierra) at its highest version causing issues when attempting to install mysql and mongosh commands through the terminmal commands whether that be through the Homebrew function, of that be through the pip3 install function.

- Having to code across multiple IDE instances depending upon where I was when working on my project (a seperate macbook again circa 2010-2012 that I keep at my parents house) and therefore not always having access to my creds.json information.

- Attempting to create a custom sql table to call information from as I was unable to connect to my postgresql database within my machine instace (again due to OSX compatibiliy issues).

- due to an older instructional video and updates to security measures, as well as my computers outdated OS system, I was unable to complete the email security function portion of this part of the instructional video. However I will highlight the areas of improvement for future work and future projects going forward.

# Online Validators

### W3 HTML 
- The W3 HTML validator only returned one Error in the validation error of missing alt tag within my <img> profile for users photos that are uploaded to use for their profiles. This was resolved with only a minor warning of a *main* element tag being returned as unnescessary, however this does not hinder the function of the app in anyway shape or form. 

### W3 C3S

- The W3 C3S validator returned a number of errors due to the use of the CDN link of bootstrap within my project file. These however do not affect the interaction of the webapp in anyway and are sometimes returned with using both custom CSS and CDN CSS from an external libary within the same project. 

### PEP8 Validator
- When running my python code through the validator, it returned an average score of 56%, so I looked for tools that I could use online in order to improve my valdation score on the code itself. I then found the website *Online Python Formatter* {https://www.tutorialspoint.com/online_python_formatter.htm} and using this website, I was able to correct indentation errors in my code to make it both more readable, but also ensure the python code reaches 100% validation through the PEP8 syntax checker. 

Any Python code that does not run through this validator within my project is redundant, though I have kept it present for the sake of showing my initial planning before the step change within my project. 

### Javascript validator
- As this project did not use any javascript outside of the Bootstrap CDN link, there was no need to run any JS through an external validators. 


# Website Theme/Designs
The Website uses a simple Scroll Method Gradient, however in future iterations when the ability to comment on movie and tv series is introduced ( in line with my original idea's for the website) , There will then be a more focused branding and colour to focus the theme of the website and the users. 

![Screen Shot 2023-05-31 at 23 06 33](https://github.com/T-KibCode/MilestoneProject-3/assets/110776212/28663a78-c9d1-4fca-94c1-26adad509182)

Once the Secondary database utilising PostgreSQL to arrange a movie database witha relational table between actors and the movies they star is, is implmented and arranged, I would then use the following Database Scheme to plan this out and implement this: 

![drawSQL-movie-database-export-2023-05-19](https://github.com/T-KibCode/MilestoneProject-3/assets/110776212/57aa0b15-45f9-40e6-8014-ca77d8701a4e)

These were the initial sketch plans of how I wanted the movie app to beging to take shape and look at, but I found I was lacking in time, hence the simpified the version of app has been used in this case:

![Screen Shot 2023-04-11 at 20 29 44](https://github.com/T-KibCode/MilestoneProject-3/assets/110776212/0a7b6ae9-d298-409e-9a35-7dba0e414aa1)

# Mobile Responsive

The App I've designed is fully mobile responsive for all users and has been tested within multiple browers to ensure its effectiveness. 

# Special Thanks

I would like to give thanks for Code Institute for providing this course that has allowed me learn the skills I have developed up to this point.

I would also like to thank my class mates that have helped me look at other key area's to understand where I have been going wrong. 

I would also like to thank my Mentor *Ronan*, of whom has helped highlight area's where my prevous projects have been lacking in order to help me develop as an individual during this journey.

And most of all, I would like to thank my Class tutor *Mohamed* of whom has been extremely patient with my personal circumstancces over the last 6 months, and has allowed me to be able to finish this project in order to complete my studies in this area, whilst providing support as best as he can for me, all at a time when public funding of our education, healthcare and public services area being stress tested and managing more of a workload then initially envisioned. 
