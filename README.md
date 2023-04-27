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

  I cited an external resource in order to solve the issue of routing which was at the following link on youtube.

  
I've had to use an online conversion tool in order to convert a movie database from a tsv.gz file , to uncompress the file into .tsv format, and to convert it using a website named [https://www.convertsimple.com/convert-tsv-to-sql-insert-statement/]

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome T-KibCode,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
