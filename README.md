
---
![PokerBlog](../blog-poker/documentation/pokerblog_logo.jpg)

My poker blog is about tracking my journey on improving at the game of poker. It allows blogs to be posted under 3 distinct categories ("Session summaries, "Progress Reports" & "Interesting Spots"). Furthermore it allows me to track my poker results by adding session statistics to a bespoke page for "sessions". This shows my wins & losses for different poker sessions played over different locations.


## User Stories

 - As a user I want to be able to post stories to a blog so that I can document my journey as a poker player

 - As a user I want to be able to categorise posts between different types, so that I can show collections of different posts and organise the content into clear areas ("Session summaries, "Progress Reports" & "Interesting Spots")
 
 - As a user I want to be able to create progress update posts so that I can provide reflective updates to users on the journey that I am undertaking to becoming a poker champion
 
 - As a user I want to be able to create session summary posts so that I can provide details on a particularly fun or interesting games of poker that I've played
 
 - As a user I want to be able to create interesting spot posts so that I can provide updates for users on key hands or learnings that I have made on my journey
 
 - As a user I want to be able to comment & like posts so that I can provide feedback to the blog writer
 
 - As a user I want to be able to view a full list of sessions that I have undertaken so that I track results by being able to see the length, venue, profit/loss of each session and any notes that shows what happened
 
 - As a user I want to be able to add sessions to the session list so that I can record every session that has been undertaken


## Features

### Main Blog Area

The home page includes a header, with a list of the most recent blogs and navigation:

![Home Page](../blog-poker/documentation/pokerblog_home.jpg)
![Navigation](../blog-poker/documentation/pokerblog_navigation.jpg)

A user can navigate to different categories and session result tracking:

![Category Navigation](../blog-poker/documentation/pokerblog_category_navigation.jpg)

Each post is shown on a separate page:

![Post Area](../blog-poker/documentation/pokerblog_post.jpg)

A comment & like section is inlcuded on the post page:

![Comment & Like](../blog-poker/documentation/pokerblog_comment_like.jpg)

The session section shows results of poker games tracked in order:

![Session](../blog-poker/documentation/pokerblog_session_table.jpg)

New sessions can be added in the session input area on this page:

![Session](../blog-poker/documentation/pokerblog_session_input.jpg)

---
## Technologies Used

- [BootStrap](https://startbootstrap.com/template/blog-home) was used as the foundation of the site front end
    - [HTML](https://startbootstrap.com/template/blog-home) was used as part of Bootstrap.
    - [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - was used as part of Bootstrap.
- [Django](https://www.djangoproject.com/) was used as the foundation of the back end and site middleware.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the site data.
- [Cloudinary](https://cloudinary.com/) was used host the blog pictures.
- [GitPod](https://gitpod.io/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.

## Django Technology Used

The Django Framework was the core technology for the back end and middleware components of the site. This can be accessed in GitPod via the following commands: `pip3 install 'django<4' gunicorn`

The blog uses several Django models in order to manage site data:

  - A "Post" model (including a Comment Model) to manage the creation of posts. This was adapted from the CI Django Blog.

  - A "Session" Model (orginal & bespoke) to manage the creation of the session trcking history.

The following libraries were used in the creation of the project in Django:

![Django requirements:](../blog-poker/documentation/pokerblog_django_requirements.jpg)

---

## Testing

In order to confirm the correct functionality, responsiveness, and appearance:

+ The website was tested on the following browsers: Chrome, Firefox, Brave.

+ The functionality of the blog was checked as well by different users.

---
## Validator testing
+ ### HTML
  #### Main Page
  - No errors or warnings were found when passing through the official W3C validator.

![W3C Checker](../blog-poker/documentation/pokerblog_nuhtmlchecker.jpg)

+ ### Lighthouse Report: Accessibility and performance 
  - Using lighthouse in devtools I confirmed that the website is performing well, accessible and colors and fonts chosen are readable.

![Lighthouse](../blog-poker/documentation/pokerblog_lighthouse.jpg)
---
## Deployment

- The site was deployed to Heroku, and can be accessed [here](https://blog-poker-2e9e23ce2538.herokuapp.com/).

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/t0bes1/blog-poker).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/t0bes1/blog-poker.git`


### To deploy the project to Heroku so it can be run as a remote web application:

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `gh repo clone t0bes1/poker-blog`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`

  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).

  1. Go to [Heroku](https://dashboard.heroku.com/apps) account, navigate to the "New" option

  ![Heroku deployment](../blog-poker/documentation/heroku_deployment1.jpg)

  1. In the settings tab, update the "config variables" with the following CRED / PORTs. This includes the contents of the creds.json file (not on GiHub).

  ![Heroku deployment](../blog-poker/documentation/heroku_deployment2.jpg)

  1. Then link the GitHub repo () and "enable" automatic deploys:

  ![Heroku deployment](../blog-poker/documentation/heroku_deployment3.jpg)

  1. From the source section drop-down menu, select the **Main** Branch and click "Deploy Branch":

  ![Heroku deployment](../blog-poker/documentation/heroku_deployment4.jpg)

  1. The page will be automatically updated when commits are pushed to the GitHub repo.

---
## Credits

+ #### Content

  - All content has been created personally, with assistance from [Google Bard](https://bard.google.com/chat)
---

## Acknowledgments

- [Code Institute](https://codeinstitute.net/) tutors and Slack community members for their support and help.
- [Code Institute's Django Blog](https://github.com/Code-Institute-Solutions/Django3blog) was adapted for some of the sites blog & comment/like functionality
- [Bootstrap template](https://startbootstrap.com/template/blog-home) used was "Start Bootstrap - Blog Home v5.0.9" as the foundation of the site's front end
---