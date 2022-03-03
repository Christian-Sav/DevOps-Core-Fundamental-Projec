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
