# Elevator_pitch
A Flask application that allows users to submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

#### By [Annabel Micheni](https://github.com/AnnabelNkir) 
##### **{November 9, 2021}**

## Requirements

This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found here;

## Setup/Installation Requirements

To view the app, ensure you have the required modules installed. Here is a run through of how to set up the application:
```
Step 1 : Clone this repository using git clone https://github.com/AnnabelNkir/Elevator_pitch.git, or downloading a ZIP file of the code.

Step 2 : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened.

Step 3 : Open the terminal, go to the project directory and run the following commands: chmod +x manage.py and ./start.sh respectively to launch the program.

To view the app, open the live site link provided below on the README. Here is a run through of how to set up the application:

Step 1 : Clone this repository using git clone https://github.com/AnnabelNkir/Elevator_pitch.git, or downloading a ZIP file of the code.
Step 2 : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
Step 3 : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:

 + pip install virtualenv
 + virtualenv virtual
 + source virtual/bin/activate
 
Note that you can exit the virtual environment by running the command deactivate
Step 4 : Download the all dependencies in the requirements.txt using pip install -r requirements.txt
```
Note that you can exit the virtual environment by running the command deactivate
Step 4 : Download the all dependencies in the requirements.txt using pip install -r requirements.txt


## User stories

The user is expected to navigate seamlessly through the application.
```
+ As a user, I would like to see the pitches other people have posted.
+ As a user, I would like to vote on the pitch they liked and give it a downvote or upvote.
+ As a user, I would like to be signed in for me to leave a comment
+ As a user, I would like to receive a welcoming email once I sign up.
+ As a user, I would like to view the pitches I have created in my profile page.
+ As a user, I would like to comment on the different pitches and leave feedback.
+ As a user, I would like to submit a pitch in any category.
+ As a user, I would like to view the different categories.

```
## Business Driven Development(BDD)

```

|  Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Signing up | Fill your credentials in the form in the signup page | Redirects to the login page after sign up |
| Signing in | Fill in the form in the signin page | Redirects to the home page |
| ```post pitch``` Button | In the home page, enter your pitch in text, select a category in the drop down menu and hit Post Button! | Reloads the page with the pitch as the newest pitch |
| Liking a pitch | Press the thumbs up button | Adds a like |
| Disliking a pitch | Press the thumbs down button | Adds a dislike |
| ```Comment``` | Type the comment on the text area field in the pitch page, and hit post comment | Reloads the page and posts the comment. The comments will be shown from the most recent |
| Viewing user profile | Click on the users name eg: ```Bella__``` | Redirects the user to the clicked user profile |
| Uploading a photo | Click on the choose file button and choose file | The page will be refreshed with the profile photo updated |
| Editing the bio | Click on the ```edit bio``` button and enter your bio  | Redirects the page back to the profile page with an updated bio |
```
## Technologies
```
.Flask
.Git
.HTML5 & CSS
.Bootstrap
.Python 3.8
.Heroku

```
## Known Bugs
There are no unresolved bugs in this code.

## Support and contact details

Incase of any query, need for collaboration or issues with this code, feel free to reach me at annabel.micheni@student.moringaschool or nkiroteannabel@gmail.com.


### MIT License

```
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

```

#### Copyright (c) [2021] [Annabel Micheni](https://github.com/AnnabelNkir)  ####

## Acknowlegment
I acknowledge the amazing Moringa School fraternity, supportive TM and peers who have been making my learning experience better for which i am truly grateful for.
