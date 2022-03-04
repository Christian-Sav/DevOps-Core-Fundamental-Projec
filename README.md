# DevOps Core Fundamental Project - School Enrollment App
Within this repository are my deliverables for the DevOps Core Fundamentals project.

## Contents:
* [Project Brief](#Project-Brief)  
* [App Design](#App-Design)
* [CI Pipeline](#CI-Pipeline)  
* [Risk Assessment](#Risk-Assessment)
* [Testing](#Testing)
* [The App](#The-App)
* [Updates](#Updates)
* [Current Issues](#Current-Issues)
* [Future-Plans](#Future-Plans)

## Project Brief:  
In the brief provided, we were required to design and produce a web app using. The web app needed to use CRUD functionality (CREATE, READ, UPDATE, DELETE), needed to be bults using the Flask micro-framework and had to be able of storing information in a database using MYSQL consisting of atleast 2 tables sharing a one to many relationship.

## App Design:
For my app I have chosen to build a school enrollment app that allows the user to add students, classes and enrollments (adhearing to the CREATE functionality), view the students, classes and enrollments (adhearing to the READ functionality), update the students, classes and enrollments (adhearing to the UPDATE functionality) and delete students, classes and enrollments (adhearing to the DELETE functionality). The database for this project comprises of a Students table, a Classes table and an Enrollments table, with the Enrollments table being the join table (or child table) between Students and Classes assossiating one student with multiple enrollments and multiple classes with multiple enrollments (two one-to-many relationships). The ERD for this is shown below:

![ERD](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/ERD%20Version%201.png)

The future goal for the project is the ability to add grades A* to F within the program for each student in each class, to do this it would result in a very similar table to the enrollments table with the addition of the grades funciton, a proposoal of this is below:

![updateERD](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/ERD%20Version%202.png)

## CI Pipeline: 
As well as the requirements outlined already, the project also required the implementation of multiple stages of a typical CI pipeline. We were required to include project tracking, version contol, development enviroment and a build server. 

For project tracking I used a scrum based project tracker on Jira, on this items were assigned story points with MoSCoW prioritisiation, they were then moved from project backlog to sprint backlog to To Do then to In Progress and eventually to done as the project was progressed. The board at the beginning of sprint one looked like this:

![jiraboard](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/sprint.png)

For version control I used git with the project repository being hosted on github, using git for Version control allowed for easy access to the commit history for access to earlier versions whilst changes are being made and committed to the project. GitHub as a repository hosting service means that the actual repositoy for the project is sotred far away from the development environment this as well as providing webhooks which send http POST requests to the build server to automate building and testing made GitHub a valuable choice.

A python3 virtual enviroment or venv was used as the development enviroment which was hosted on a google cloud platform virtual machine running Ubuntu 20.04. I used python as Flask is a python-based framework. I used a venv as it allows pip installs to be used and for the app to be run without conflicting with any existing installs on the host machine. 

Jenkins was used as the build server which provided automation of both building and testing. The automation is achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit to the dev branch. The full CI pipeline for this project is:

![CI Pipeline](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/CI%20Pipeline.png)

## Risk Assessment
Before even starting the build of the app, risk assessment was taken to identify risks and to propose control measures that can be used in order to reduce them. These measures could then be implemented into the app or advised to users. The inital risk assessment is shown here: 

![RiskAssessment](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Risk%20Assessment.png)
 

## Testing:  
Testing the app was an essential part of the development process.

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. These tests are automated using Jenkins via webhooks whenever I commit to the Dev branch.Below is a  successful build, in which all tests passed:  

![Build](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Build%20tests%20pass.png)

As well as this I have included the functionality of outputing a coverage report as a HTML file to be archived as an artifact after the build is completed, for the above build this is the corresponding coverage report:

![Coverage](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/CI%20Coverage.png)

This is a 97% overall coverage on tests. To be classed as a sucessful build all tests included MUST pass, even a single failed test would result in the build being classed as a failure.

## The App:

When first navigating to the app you will be greated with the home screen which shows you your current students and your current classes with the functionality to update or delete them:
 ![Home](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Home%20Page.png)
 
 Using the navigation bar you can select to either add students, classes or enrollments and view your currenrt enrollments and are then taken to the respective pages :
 
 ![ADDSTUD](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Add%20Student.png)
 
 The user adds the student by filling out the respective form with the students first and surname, house number and postcode.
 
 ![ADDCLASS](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Add%20Class.png)
 
 Similar to the student page classes are added by filling out the form with the class name and description.
 
 ![ADDENROLL](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Add%20Enrollment.png)
 
 However unlike the other pages the Enrollment page is filled using a drop down list consisting of all of the availiable students and classes.
 
 ![ViewEnroll](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/View%20Enrollments.png)
 
The view enrollments page allows you to see your current enrollments with the functionality to update or delete them.

![Updates](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Update.png)

The Updates page re-uses the add page with a dynamic title changed by using the update link.
 
 ## Updates:
 * 04/03/2022
     * Background slightly changed to rgb(219, 245, 241) a more relaxing baby blue.
 
 ## Current Issues:
* Currently the same enrollment can be added twice, allowing for the same student in  the same class more than once.
* Other than having a different address a student with the same name would be indistinguishable from another on the enrollments page.

## Future Plans:
* As outlined earlier I currently have plans to impliment a grading system from A* to F into the enrollment app for further school functionality.
