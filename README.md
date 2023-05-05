# Introduction
This project is the third one I've undertaken as part of the Full Stack Software Diploma course at [Codeinstitute.net](https://www.CodeInstitute.net).

It is a user interactive movie review website.  The aim is to have users be able to search up movies, read a shot description and have the ability (if registered) to leave a comment/review on the page for that particular movie.  
The goal is to have a gently guided experience for the user towards this goal with intuitive design of the project, starting from the search function being the main draw of their attention, the ability for them to find information on the film, both spoiler and spoiler free, create a registered account in order to be able to leave user scores after seeing a film, and to be able to edit any previous posts made by the user.

The reason for my choosing of this project specifically, is because I wanted the user experience to be a social one in relation to the films, both being able to find a film to watch in a specific genre, whilst also allowing the user to leave their own thoughts on the site for others to see. This will allow me to use a variety of different language models to achieve this and should hopefully demonstrate the skills within the project.

# User Experience/User Interface (UX/UI)

<details>
  
  <summary>User Experience/User Interface (UX/UI)</summary>
  
  ### User Stories
  
  ##### First Time Visitor Goals
  As a first time visitor I want:  
  - the search function for movie reviews to be clear, front and center  
  - to be able to filter by multiple fields, such as genre, year of release, age rating   
  - to be able to create user account to interact with other users 
  
  ##### Return/frequent Visitor Goals.
  As a return/frequent visitor I want:  
  - to be able to score films/movies I have seen.
  - to be able to save movies to a personal favourites page to keep personal track.
  - to be able to leave comment reviews on individual movie pages with the ability to edit the comments.
  - to allow the registered user to be able to filter if they see user reviews or not. 
  
  ##### Website's Owner Goals.
  As the developer I want:
  - to correctly create a relational database that pulls the information the user requires of their search i.e after searching a certain parameter, being able to filter down the returned results such as, release date filter being applied when searching the horrow genre to find movies released in a certain window whether that be annual or seasonal.
  - to create a comments section that allows user's to leave word-limited reviews following the CRUD format. 
  - to lead the user down a pusedo-constructed path, in order to provide a semi-streamlined experience with the website.
  - to either create a database, or use an available API call for a pre-existing movie database that can be used to pull names, lead actors, directors, release dates and series links in to the site. 
  - to create a seperate database for the users to write to i.e comments/reviews etc, movies scores etc.



# Initial template build process - understanding functions available

<details>
  <details>Proof of testing rendered functions</details>

  ### Initial test processes.
  In my initial commits within the repository, I had issues intially getting my Flask modules to be recognised and for the app.py python file to render to the html file. 
  []

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


![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


