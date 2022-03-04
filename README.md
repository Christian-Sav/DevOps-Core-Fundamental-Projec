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
* [Current Issues](#Current Issues)

## Project Brief:  
In the brief provided, we were required to design and produce a web app using. The web app needed to use CRUD functionality (CREATE, READ, UPDATE, DELETE), needed to be bults using the Flask micro-framework and had to be able of storing information in a database using MYSQL consisting of atleast 2 tables sharing a one to many relationship.

## App Design:
For my app I have chosen to build a school enrollment app that allows the user to add students, classes and enrollments (adhearing to the CREATE functionality), view the students, classes and enrollments (adhearing to the READ functionality), update the students, classes and enrollments (adhearing to the UPDATE functionality) and delete students, classes and enrollments (adhearing to the DELETE functionality). The database for the MVP for this project comprises of a Students table, a Classes table and a Enrollments table, with the Enrollments table being the join table between Students and Classes assossiating one student with multiple enrollments and multiple classes with multiple enrollments (two one-to-many relationships). The ERD for this MVP is shown below 

![ERD](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/ERD%20Version%201.png)

## CI Pipeline: 
As well as the requirements outlined already, the project aslso required the implementation of multiple stages of a typical CI pipeline. We were required to include project tracking, version contol, development enviroment and a build server. 

For project tracking I used a scrum based project tracker on Jira, on this items were assigned story points, their criteria for acceptance and MoSCoW prioritisiation, they were then moved from project backlog to sprint backlog to in progress and eventually to done as the project was progressed. The board at the beginning of sprint one looked like this:

![jiraboard]

For version control I used git with the project repository being hosted on github, using git for Version control allows for easy access to the commit history for access to earlier versions whilst changes are being made and committed to the project. GitHub as a repository hosting service allows the repository to be stored away from the development environment, as well as providing webhooks, which send http POST requests to the build server to automate building and testing.

A python3 virtual enviroment or venv was used as the development enviroment which was hosted on google cloud platform virtual machine running Ubuntu 20.04. I used python as Flask is a python-based framework. I used a venv as it allows pip installs to be used and for the app to be run without conflicting with any existing installs on the host machine. 

Jenkins was used as the build server, providing automation of building and testing. The automation is achieved by setting up a freestyle project which executes the test.sh script when it recieves a webhook from github upon pushing a commit to the dev branch. The full CI pipeline for this project is:

![CI Pipeline](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/CI%20Pipeline.png)

##Risk Assessment
Before even starting the build of the app, risk assessment was taken to identify risks and to propose measures that can be used in order to control them. These measures could then be implemented into the app. The inital risk assessment is shown here: 

![RiskAssessment](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Risk%20Assessment.png)

Some of the control measures implemented in the project as a result of the risk assessment are as follows:  
* User profiles were decided to be too big of a risk for the app as this would require sending some form of authentication over an unsecured connection.  
* SQLAlchemy was used with Flask to prevent SQL commands being sent directly to the database.  
* Any credentials have been stored as secret texts on my Jenkins VM and exported as environment variables to avoid accidentally publishing confidential details. 

##Testing:  
Testing the app was an essential part of the development process. Two types of testing were implemented:  
* Unit testing tests _units of functionality_ (i.e functions) within the app. Unit tests were written for create, read, update and delete functionality, to ensure that these worked as intended.
* Integration testing tests the function of the app in an as-live environment, being able to simulate keyboard input and mouse clicks to ensure that these elements of the app function as intended. Integration tests were written for many of the forms employed in the app.  

As this is not a production app, tests such as security tests and performance tests were not part of the scope of this project; only testing for functionality was performed. These tests are automated using Jenkins via webhooks whenever I commit to the Dev branch.Below is a  successful build, in which all tests passed:  

![Build](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/Build%20tests%20pass.png)

As well as this I have included the functionality of outputing a coverage report as a HTML file to be archived as an artifact after the build is completed, for the above build this is the corresponding coverage report:

![Coverage](https://github.com/Christian-Sav/QA_Project/blob/feature/Figures/CI%20Coverage.png)

This is a 97% overall coverage on tests. To be classed as a sucessful build all tests included MUST pass, even a single failed test would result in the build being classed as a failure.

##The App:

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
 
 ##Updates:
 * 04/03/2022
     * Background slightly changed to rgb(219, 245, 241) a more relaxing baby blue
 
 ##Current Issues:
* Currently the same enrollment can be added twice, allowing for the same student in  the same class more than once.
* Other than having a different address a student with the same name would be indistinguishable from another on the enrollments page
