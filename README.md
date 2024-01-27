
---
![PokerBlog]()

My poker blog is about tracking my journey on improving at the game of poker. It allows blogs to be posted under 3 distinct categories ("Session summaries, "Progress Reports" & "Interesting Spots"). Furthermore it allows me to track my poker results by adding session statistics to a bespoke page for "sessions". This shows my wins & losses for different poker sessions played over different locations.


## User Stories

 - As a user I want to be able to post stories to a blog so that I can

 - 


## Features

### Main Blog Area

The single page includes a header, with a clickable info button showing the rules:

![Header]()

When clicked, the rules are shown as follows:

![Modal]()

A main game area shows 3 cards for the player and 3 cards for the house in the main game area:

![Game Area]()

There is a section showing the players bet, their bankroll, the game action buttons and a message box:

![Score Area]()

The page includes a footer, with a link to my github:

![Footer]()

---
## Technologies Used

- [BootStrap](https://startbootstrap.com/template/blog-home) was used as the foundation of the site front end
    - [HTML](https://startbootstrap.com/template/blog-home) was used as part of Bootstrap.
    - [CSS](https://developer.mozilla.org/en-US/docs/Web/css) - was used as part of Bootstrap.
- [Django](https://www.djangoproject.com/) was used as the foundation of the back end and site middleware.
- [ElephantSQL](https://www.elephantsql.com/) was used to store the side data
- [GitPod](https://gitpod.io/) was used as the main tool to write and edit code.
- [Git](https://git-scm.com/) was used for the version control of the website.
- [GitHub](https://github.com/) was used to host the code of the website.

---

## Testing

In order to confirm the correct functionality, responsiveness, and appearance:

+ The website was tested on the following browsers: Chrome, Firefox, Brave.

+ The functionality of the blog was checked as well by different users.

### Manual testing

| feature | action | expected result | tested | passed | comments |
| --- | --- | --- | --- | --- | --- |
| Game Play | | | | | |
| Initial Game State | Refresh page and review set up | All cards are shown face down, a bankroll of 100 & scores at 0 | Yes | Yes | - |
| Stake not set | No entry is made in the stake box, but "Deal" button pressed  | A message appears showing the user that they can't bet nothing and a new deal is offered | Yes | Yes | - |
| Stake greater than Bankroll | Player chooses a stake higher than the Bankroll available  | A message appears showing the user that they can't bet this amount and a new deal is offered | Yes | Yes | - |
| Initial Deal | Enter a valid stake and click on the "Deal" button | The player receives 2 cards, the correct total is shown on the player score and the Hit/Stand choice is offered | Yes | Yes | - |
| Player chooses "Hit" |The "Hit" button is clicked |The player receives a third card, the correct total is calcuated and the house is dealt its cards |Yes |Yes | |
| Player chooses "Stand" and Busts |The "Stand" button is clicked |The player does not receive a third card, the result of the game is calculated as a loss, with the house cards not shown |Yes |Yes | |
| Player chooses "Stand" and scores 21 or lower |The "Stand" button is clicked |The player does not receive a third card, the house hand is dealt correctly, the game result is calculated correctly |Yes |Yes | |
| Hand result is calculated correctly |The hand is concluded after "Hit" or "Stand" |The player score is shown correctly, the house score is show correctly, a win or lose message is displayed correctly |Yes |Yes | |
| Hand outcome of a win is shown correctly |A hand is concluded |The Bankroll is updated to reflect the win, in line with the bet amount |Yes |Yes | |
| Hand outcome of a loss is shown correctly |A hand is concluded |The Bankroll is updated to reflect the loss, in line with the bet amount |Yes |Yes | |
| Game outcome of a win is shown correctly |The player reaches a bankroll of 200 or greater after as many hands as necessary |A congratulations message is shown, a celebration sound is played, the user is offered a restart option |Yes |Yes | |
| Game outcome of a loss is shown correctly |The player reaches a bankroll of 0 after as many hands as necessary |A commiseration message is shown, a commiseration sound is played, the user is offered a restart option |Yes |Yes | |
| Modal | | | | | |
| Game rules are shown  |The "i" button is clicked | The rules of the game are shown to the player |Yes |Yes | |
| Game rules are hidden |The screen is clicked when the modal is open | The rules of the game are no longer shown to the player and the game is playable |Yes |Yes | |
| Sound | | | | | |
| Sound plays  |The sound toggle is clicked on | Sounds play when hands are won or lost |Yes |Yes | |
| Sound does not play |The sound toggle is left off  | Sounds do not play when hands are won or lost |Yes |Yes | |
| Footer | | | | | |
| Github icon in the footer | Click on the Github icon | The user is redirected to the Github page | Yes | Yes | - |

---
## Validator testing
+ ### HTML
  #### Main Page
  - No errors or warnings were found when passing through the official W3C validator.

![W3C Checker]()
    
+ ### CSS
  - No errors were found when passing through the official W3C (Jigsaw) validator:

![W3C CSS Checker]()

+ ### Lighthouse Report: Accessibility and performance 
  - Using lighthouse in devtools I confirmed that the website is performing well, accessible and colors and fonts chosen are readable.

![Lighthouse]()
---
## Deployment

- The site was deployed to Heroku, and can be accessed [here](https://everett-rovers-u9y-15b7dda34125.herokuapp.com/).

### To deploy the project as an application that can be **run locally**:

*Note:*
  1. This project requires you to have Python installed on your local PC:
  - `sudo apt install python3`

  1. You will also need pip installed to allow the installation of modules the application uses.
  - `sudo apt install python3-pip`

Create a local copy of the GitHub repository by following one of the two processes below:

- Download ZIP file:
  1. Go to the [GitHub Repo page](https://github.com/t0bes1/football-stats).
  1. Click the Code button and download the ZIP file containing the project.
  1. Extract the ZIP file to a location on your PC.

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `git clone https://github.com/t0bes1/football-stats.git`


### To deploy the project to Heroku so it can be run as a remote web application:

- Clone the repository:
  1. Open a folder on your computer with the terminal.
  1. Run the following command
  - `gh repo clone t0bes1/football-stats`

  1. Create your own GitHub repository to host the code.
  1. Run the command `git remote set-url origin <Your GitHub Repo Path>` to set the remote repository location to your repository.

  1. Push the files to your repository with the following command:
  `git push`

  1. Create a Heroku account if you don't already have one here [Heroku](https://dashboard.heroku.com).

  1. Go to [Heroku](https://dashboard.heroku.com/apps) account, navigate to the "create app option"

  ![Heroku deployment]()

  1. In the settings tab, update the "config variables" with the following CRED / PORTs. This includes the contents of the creds.json file (not on GiHub).

  ![Heroku deployment]()

  1. Then link the GitHub repo () and "enable" automatic deploys:

  ![Heroku deployment]()

  1. From the source section drop-down menu, select the **Main** Branch and click "Deploy Branch":

  ![Heroku deployment]()

  1. The page will be automatically updated when commits are pushed to the GitHub repo.

---
## Credits

+ #### Content

  - All content has been created personally
---

## Acknowledgments

- [Code Institute](https://codeinstitute.net/) tutors and Slack community members for their support and help.
- [Code Institute's Django Blog](https://github.com/Code-Institute-Solutions/Django3blog) was adapted for some of the sites blog & comment/like functionality
- [Bootstrap template](https://startbootstrap.com/template/blog-home) used was "Start Bootstrap - Blog Home v5.0.9" as the foundation of the site's front end
---