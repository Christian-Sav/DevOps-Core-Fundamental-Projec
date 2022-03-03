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


