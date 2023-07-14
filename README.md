# Tennis Buddies
![Tennis Buddies](/readme-images/amiresponsive.png)

Tennis Buddies is an application which can be used in real life by smaller tennis clubs across the country. Its main purpose is for new but also current members of the club to find a suitable partner for tennis practice. It also enables the players to book a court to play on.

I was inspired to develop this app by two local tennis clubs back home. If I wanted to make a booking in one of them, I would have to do it by phone. In the other one, I would have to go physically to a pub connected to the tennis facilities, find the person who was the owner of a notebook where the bookings were noted down, and thus make a reservation. Both of these processes are quite incovenient. I believe this app will make booking a court a much more pleasant and smoother experience.

The other functionality revolves around finding a tennis buddy. When a new player joins a club, they often encounter difficulties in finding a suitable hitting partner. Many people already have their regular games set up and it's hard to approach them. On the other hand, there are other players who are available and willing to play, but they usually don't know about each other. Some players are looking for hitting practice, others are looking to practice for matches, still others are looking to play socially and to have fun. This app will enable the registered users to search in the club's database and hopefully find a great tennis buddy.

The app was developed for a fictional tennis club called Nebu Tennis Club, inspired by the two above mentioned clubs.

You can access the Tennis Buddies app here:
[Tennis Buddies](https://tennis-buddies.herokuapp.com/)

[Back to top](#contents)

# Contents

- [Tennis Buddies](#tennis-buddies)
- [Contents](#contents)
- [Project](#project)
  - [Objective](#objective)
  - [Site User's Goal](#site-users-goal)
  - [Site Owner's Goal](#site-owners-goal)
- [User Experience (UX)](#user-experience-ux)
  - [Primary Goal](#primary-goal)
  - [Visitor Goals](#visitor-goals)
    - [First Time Visitor](#first-time-visitor)
    - [Returning Visitor](#returning-visitor)
    - [Frequent Visitor](#frequent-visitor)
  - [User Stories](#user-stories)
- [Creation Process](#creation-process)
  - [Design Prototype (Wireframes)](#design-prototype-wireframes)
    - [Desktop Wireframes](#desktop-wireframes)
    - [Tablet Wireframes](#tablet-wireframes)
    - [Mobile Wireframes](#mobile-wireframes)
  - [Project Management](#project-management)
    - [Sprint #1 - 08/05 -12/05](#sprint-1---0805--1205)
    - [Sprint #2 - 15/05 - 19/05](#sprint-2---1505---1905)
    - [Sprint #3 - 22/05 -26/05](#sprint-3---2205--2605)
    - [Sprint #4 + #5 - 29/05 - 09/06](#sprint-4--5---2905---0906)
    - [Sprint #6 - 12/06 - 16/06](#sprint-6---1206---1606)
    - [Sprint #7 - 19/06 - 23/06](#sprint-7---1906---2306)
    - [Sprint #8 - 27/06 - 30/06](#sprint-8---2706---3006)
    - [Sprint #9 + #10- 03/07 - 14/07](#sprint-9--10--0307---1407)
    - [GitHub Projects Board](#github-projects-board)
    - [Moscow Prioritization](#moscow-prioritization)
    - [Milestones](#milestones)
    - [Epics](#epics)
    - [User Stories](#user-stories-1)
  - [Database Schema (ERD)](#database-schema-erd)
  - [Site Structure](#site-structure)
- [Design Choices](#design-choices)
  - [Typography](#typography)
  - [Color Scheme](#color-scheme)
- [Features](#features)
  - [Site Responsive Navigation Bar](#site-responsive-navigation-bar)
  - [Carousel](#carousel)
  - [Footer](#footer)
  - [Home Page](#home-page)
  - [Find the Perfect Buddy Page](#find-the-perfect-buddy-page)
    - [Buddy Search](#buddy-search)
    - [Future Features for Buddy Search](#future-features-for-buddy-search)
    - [Buddy Details](#buddy-details)
    - [Future Features for Buddy Matching](#future-features-for-buddy-matching)
  - [Booking of the courts](#booking-of-the-courts)
    - [Booking requirements](#booking-requirements)
    - [Making a reservation](#making-a-reservation)
    - [Edit/Delete Functionality](#editdelete-functionality)
    - [Staff Dashboard](#staff-dashboard)
    - [Bookings in the past](#bookings-in-the-past)
    - [Future features for Booking](#future-features-for-booking)
  - [Contact Us page](#contact-us-page)
    - [Inquiry Confirmation Message](#inquiry-confirmation-message)
    - [Future Features for Contact Us](#future-features-for-contact-us)
      - [CLI Message](#cli-message)
  - [Profile Icon](#profile-icon)
    - [Contact Info](#contact-info)
      - [Add Contact Info](#add-contact-info)
      - [View Added Contact Info](#view-added-contact-info)
      - [Edit Contact Info](#edit-contact-info)
      - [Delete Contact Info](#delete-contact-info)
    - [Buddy Profile](#buddy-profile)
      - [Add Buddy Profile](#add-buddy-profile)
      - [View Added Buddy Details](#view-added-buddy-details)
      - [Edit Buddy Details](#edit-buddy-details)
      - [Delete Buddy Details](#delete-buddy-details)
    - [Your Bookings](#your-bookings)
  - [Sign Up Page](#sign-up-page)
  - [Sign In Page](#sign-in-page)
  - [Logout Page](#logout-page)
    - [Future Features Sign in functionality](#future-features-sign-in-functionality)
  - [403, 404 and 500 Error Pages](#403-404-and-500-error-pages)
  - [Future Features](#future-features)
- [Technologies Used](#technologies-used)
  - [Languages](#languages)
  - [Frameworks and Software](#frameworks-and-software)
- [Python Packages](#python-packages)
- [Testing](#testing)
    - [Manual testing](#manual-testing)
    - [External Testing](#external-testing)
    - [Automated Testing](#automated-testing)
- [Project Deployment](#project-deployment)
  - [Create a new GitHub Repository from CI template](#create-a-new-github-repository-from-ci-template)
  - [Install Django and the supporting libraries](#install-django-and-the-supporting-libraries)
  - [ElephantSQL Database](#elephantsql-database)
  - [Cloudinary API](#cloudinary-api)
  - [Heroku Deployment](#heroku-deployment)
  - [To fork the repository on GitHub](#to-fork-the-repository-on-github)
  - [To create a local clone of a project](#to-create-a-local-clone-of-a-project)
- [Credits](#credits)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgements](#acknowledgements)

[Back to top](#contents)

# Project

## Objective

I used to play tennis as a child. But due to my knee problems, unfortunately, I had to stop playing at a young age. When we moved to Ireland couple years ago, my children started playing tennis in the local tennis club. I never thought I wwould go back to tennis, but I tried and discovered that my physical limitations were gone. I had rediscovered my love and passion for tennis and have been playing frequently ever since. I was lucky to find a great hitting partner right at the beginning, but in those two years I have seen many people struggle in that respect. My local club has a great website which provides the booking functionality and I thought combining these two features and perhaps making them available to smaller local clubs would be beneficial.

When developing this project, my goal was to put my knowledge of HTML, CSS, JavaScript, Python, Bootstrap and Django Framework to use.

As the main objective was to apply CRUD functionality to custom made models and use a backend framework, I did not quite get my booking system or the search functionality to where I wanted them to be. But I have several custom models with full CRUD functionality in place, and I plan to improve both of my main features in the next version of this project.

## Site User's Goal

The Tennis Buddies site user is a tennis aficionado. They want to find a suitable and compatible tennis partner for their practice. Also they want to be able to make a reservartion of a court to play on.
## Site Owner's Goal

As the site owner, I want to provide a platform where new tennis club members can meet and organize games, no matter what their tennis level or goals are. I also want to make booking a court a simple, straightforward, fast experience.

# User Experience (UX)

## Primary Goal

The primary goal of this application is to enable member of a tennis club to find a tennis buddy and to make court reservations.

## Visitor Goals

As a visitor, I want to easily find a tennis partner to practise with and make a court reservation for a suitable time. I also want to be able to get in touch with the tennis club in case of any inquiries.

### First Time Visitor

  - A user sees the three main features of the app on the welcome page: Find a buddy, Book a court, Contact us
  - A user can register, log in and logout.
  - A user can see Buddy profiles on Find the perfect buddy page. 
  - A user can see details of buddies including an email address when they have signed in.
  - A logged in user can avail of the search bar to search for a buddy when on Find the Perfect Buddy tab.
  - A logged in user can click on Buddy card and be presented with their details (level, availability, preferences etc). They can also contact the chosen buddy by email to make arrangements.
  - A user can see the booking calendar and choose different dates to see court availability if not signed in.
  - A signed in user can click on a link in the booking calendar and make a reservation on the following page with the prefilled date/time/court information.
  - A signed is user can choose an opponent/s to play with when making a reservation. They can choose maximum 3 players.
  - A user is informed if they had not chosen the correct number of opponents.
  - A user is informed about a successful booking and about having made a reservation in the past if that's the case.
  - A user can add/edit/delete their contact information which can be accessed from the Profile Icon on the right (Contact Info). They are informed about having created, updated or deleted their Contact info.
  - A user can add/edit/delete their buddy information which can also be accessed from the Profile Icon (Profile).
  - Lastly, a user can see and manage their own bookings available under the Profile Icon (Your Bookings).
  - A user can contact the tennis club by filling in a form.
  - A user can easily see the location of the club on the Contact Us page.
  - A user can access useful information in the footer:
    - Links to social media
    - Opening hours
    - Site navigation
    - Recommendations for improvement
    - Contact information
  
### Returning Visitor

  - A user can easily sign in and access majority of the features of the website.
  - A user with filled in Contact info can also make court reservations.
  - A user can easily find a tennis buddy and contact them.

### Frequent Visitor

  - A user can easily make a court reservation or look for a new buddy.

[Back to top](#contents)
## User Stories
- As a **user**, I would like to **view the apps homepage** so that I can **learn about the app and see what services it provides**.
- As a **user** I can **locate the navigation area** so that I can **easily access different parts of the website**
- As a **user**, I can **access relevant information about opening hours, contact information and social media links without having to scroll back to the top of the page** so that I can **visit the club, contact the club and follow the club online**.
- As an **unregistered user** I want to be able **to sign up onto the website** so that I can **access websites functionality and content**.
- As a **registered user** I want to be able **to sign in into my account** so that I can **get access to the website's functionality and options**.
- As a **signed in user** I want to be able **to sign out of my account** so that I can **keep my account private and safe**.
- As a **user** I can **enter my personal details** so that I can **create an account with Tennis buddies and be contacted in case of need**
- As a **signed in user with an active profile** I can **create a buddy profile** so that **I can use the search functionality to find the best tennis partner**
- As a **user**, I can **edit my buddy profile** to **update my preferences regarding the style of play/practice**.
- As a **registered user** I can **press delete button on my buddy profile form** so that I can **delete all provided information regarding my preferences for a tennis partner, including pictures**
- As a **registered user** I can **press delete button on my user profile/contact form** so that I can **delete all provided information regarding my contact details**.
- As a **user**, I can **edit my user profile** to **update my personal details**.
- As a **user** I can **visit the Find Your Perfect Buddy page** so that I can **find the perfect match for my tennis practice**.
- As a **user** I can **reserve a court** so that I can **play at a time that suits me and can avoid come to a full club**.
- As a **signed in user/staff member** I can **view all the bookings** so that I can **see when other people are playing/the courts are busy**.
- As a **registered user/superuser** I can **press delete button on my booking details** so that I can **delete my/any user's booking**.
- As a **user**, I can **edit my bookings** to **update my preferences regarding the day/time/court/opponents**.
- As a **user/staff** I can **see the list of all bookings (staff)/my own bookings (current user)** so that I can **be reminded of my reservations, but also to be able to update them or delete them**.
- As a **user** I can **be visually attracted to the app and see the main site features on the moving carousel** so that I can **quickly get an idea what the app offers**.
- As a **user I want to be informed about different user actions** so that I can **be sure that the itended action took place**.
- As a **user** I can **view the contact us page** so that I can **get in touch with the club by filling in a contact form and also see the clubs location and opening hours**.
- As a **user** I can **not add a picture to my buddy profile** so that I can **protect my privacy**.
- As a **signed in user** I can **search among the buddies** so that I can **find the best partnert to play with**.
- As a **user** I can **enjoy browsing the webpage while looking for information** so that **I don't feel compelled to leave**.
- As a **user** I can **easily see which courts are available for booking in a calendar** so that I **don't have to randomly look for free date/time/court combinations**.
- As a **signed in user** I can **easily see which courts are free on a given day** so that I **don't have to keep guessing a combination of court/time/date which would be free**.
- As a **user** I want to **press a cancel button which will take me to the previous page** so that I **don't have to use the Back button**.
- As a **user** I can **easily understand what the table lables mean** so that I can **avoid any unnecessary confusion**.
- As a **user** I **can clearly see that I made a booking in the past** so that I can **be made aware of the fact**.
- As a **site owner** I want **the user to provide their phone number in valid format** so that I can **contact them if necessary**.
- As a **site owner** I can **restrict the number of bookings per user per day** so that all players **get a chance to book a court**.
- As a **site owner** I can **make sure that the user enters valid information** so that **they can be contacted in time of need**.

[Back to top](#contents)
# Creation Process

When I started creating the web application, I had a very clear idea of what I wanted to achieve. My tennis club has a very good booking system which served as an inspiration for me. The club's booking system can be viewed [here](https://clubmanager365.com/CourtCalendar.aspx?club=shankill&sport=tennis). I liked the calendar view where a user can easily see which courts are free and make a reservation by clicking on a free cell. The club's system is of course more sophisticated and more advanced, but I tried to simulate as many of the features as possible.

[Back to top](#contents)
## Design Prototype (Wireframes)

I started by creating wireframes which is always a great process because it helps me think in much more detail about what I want to accomplish. As you will see from my wireframes I had hoped to create a much more sophisticated search system for my "Find a Perfect Buddy" functionality, but I will have to do that in the next version due to time constraints. My booking system is almost where I wanted it to be, but it definitely needs more logical restrictions to function faultlessly and to avoid invalid reservations (more on that in Future Features).

The wireframes include a view for desktop, tablet and mobile to take responsives into accout. Many of the simple pages look the same on all devices (sign in, sign up, logout, forms,...). For those whose layout is different on smaller devices, I created a sample wireframe. The main difference in smaller screen is a collapsed NavBar accessible at the hamburger icon and the footer where the items stack up. The number of displayed tennis buddies and other relevant features also responds to the size of the screen.

I used [Figma](https://www.figma.com) which is an excellent tool for making wireframes.

[Back to top](#contents)
### Desktop Wireframes

<details><summary><b>Home Page</b></summary>
   
![Home Page](/readme-images/homepage_desktop.png)
</details><br />

<details><summary><b>Find a Perfect Buddy</b></summary>
   
![Find a Perfect Buddy](/readme-images/findbuddy_desktop.png)
</details><br />

<details><summary><b>Buddy Details</b></summary>
   
![Buddy Details](/readme-images/buddydetails_desktop.png)
</details><br />

<details><summary><b>Booking Calendar</b></summary>
   
![Booking Calendar](/readme-images/bookcourt_desktop.png)
</details><br />

<details><summary><b>Make a Booking</b></summary>
   
![Make a Booking](/readme-images/makebooking_desktop.png)
</details><br />

<details><summary><b>Staff Dashboard</b></summary>
   
![Staff Dashboard](/readme-images/staffdashboard_desktop.png)
</details><br />

<details><summary><b>Contact Us</b></summary>
   
![Staff Dashboard](/readme-images/contactus_desktop.png)
</details><br />

<details><summary><b>Sign Up</b></summary>
   
![Sign Up](/readme-images/signup_desktop.png)
</details><br />

<details><summary><b>Sign In</b></summary>
   
![Sign In](/readme-images/signin_desktop.png)
</details><br />

<details><summary><b>Add/Edit Contact Info</b></summary>
   
![Add/Edit Contact Info](/readme-images/add_edit_contact_desktop.png)
</details><br />

<details><summary><b>Add/Edit Buddy Profile</b></summary>
   
![Add/Edit Buddy Profile](/readme-images/add_edit_buddy_profile_desktop.png)
</details><br />

[Back to top](#contents)
### Tablet Wireframes

<details><summary><b>Home Page</b></summary>
   
![Home Page](/readme-images/homepage_tablet.png)
</details><br />

<details><summary><b>Find a Perfect Buddy</b></summary>
   
![Find a Perfect Buddy](/readme-images/findbuddy_tablet.png)
</details><br />

### Mobile Wireframes

<details><summary><b>Home and Find Buddy Page</b></summary>
   
![Home and Find Buddy Page](/readme-images/homebuddy_mobile.png)
</details><br />

[Back to top](#contents)
## Project Management

I have been using GitHub projects for organizing my project, tracking user stories and epics. It is a very helpful tool which enabled me to keep all my PBIs in one place and to tackle them gradually.

At the beginning of the project, I spent a fair amount of time on project planning, on thinking it through. I created wireframes and a sketch of my models first. Having the wireframes and the ERD model to refer to when working on the project was both essential and very helpful. Any time I was getting lost or confused, I could consult them and figure out how to proceed.

Later I jotted down as many PBIs as I could think of. I also started writing my Epics and User Stories to an excel file. Subsequently, I started using the Kanban board in Projects for organizing the PBIs into Epics and User stories and assigning them to Milestones, which also served as my sprint trackers. 

At first I did not know how many story points to assign to each user story and how to organize them into sprints (milestones), so the first two to three sprints were more experimental, where I would retrospectively note down how many story points each user story took, to see how many of user story points I could do in one sprint. As am a novice at this, I am taking this as a practice run for the future projects. When I am finished with this project, I plan to make an average of the points I did in each sprit, to have a better idea how to organize my next project.

I used Milestones for organizing my sprints. I know it is not ideal, but the Project tool does not have a great alternative to tracking sprints. Thus, I would create my milestones, give them a description, assign Epics and User stories to them and add a finish date for each Milestone. My sprints were usually one week long Monday to Friday, but sometimes I had to move some issues to the next sprint due to a problem which took me longer to solve than I had expected. As I was expecting setting of the booking system to be more challenging, I planned out to do it in two sprints.

As you will see from my progress, I have always kept MVP in mind. At first I made sure the backend functionality was in place, then I started working on other crucial elements and when I had some extra time, I added some nice to have features, but always keeping in mind meeting the core project requirements first. This is visible especially with my booking system, which at first was very basic, but functional. When I assumed I would have enough time to implement the more complicated and advanced version of the booking system, I expanded on the original. When that was done, I went back to the core requirements - documentation and testing and when I felt I had a bit of time, I added a few should-haves/could-haves. Overall, primarily, I focused on completing majority of the must-haves, in later stages of the product development I would consider some should and could-haves. At the same time, I was identifying user stories which would have to change into won't haves.

Breaking up the project in Epics, User stories and essentially into tasks has been very helpful and enabled me to tackle the project in managable bite-size steps. Using acceptance criteria as a part of my user stories helped me define what was necessary to achieve before I could consider the user story done. Each user story also contained detailed tasks which had to be fulfilled before labeling the story as done.

Each of the user stories would get labels such as: must have, should have, could have, won't have; story points; epic number; user story/dev task/bug; high/medium/low priority. Each user story would be assigned to its respective epic and milestone (sprint).

[Back to top](#contents)

My sprints were planned out as follows:

### Sprint #1 - 08/05 -12/05

In the first milestone my main goal was to get the project's framework set up and running and do an early deployment.  I also added Login/Registration functionality using django-allauth. Most of this sprint was about setting up the backend and the tasks were labeled as Dev Task (DT). The following tasks where a part of this sprint:

- DT Install of Django Environment
- DT Create Django Project
- DT Set Up Heroku
- DT Set Up Cloudinary
- DT Deployment
- DT Set Up Django allauth
- DT Create an admin panel
- DT Create Database models from ERD
  
[Back to top](#contents)
### Sprint #2 - 15/05 - 19/05

Create models, general site structure and navigation elements (navbar and footer) based on the original wireframes. In this sprint I moved from the backend to setting up the basic frontend features of the app and to user stories (US). I had to fix a few crucial bugs in this sprint (BF).

- US Homepage Setup
- US Navigation
- US Footer
- US Sign Up
- US Log In
- US Log Out
- US Create User Profile
- US Create Buddy Profile
- US Edit Buddy Profile
- US Delete Buddy Profile
- DT Install Django Crispy Forms
- BF Crispy Filter not working 
- BF Set up user profile in views.py and save into database
- BF Set up Buddy profile in views.py and save into database

[Back to top](#contents)
### Sprint #3 - 22/05 -26/05

Finish CRUD functionality for Contact Details (user_profile), for buddy profile

- US Delete User Profile (Contact Info)
- US Edit User Profile
- US View Buddies (ListView)
- DT Readme Forking/Cloning

[Back to top](#contents)
### Sprint #4 + #5 - 29/05 - 09/06

The goal is to create a booking CRUD functionality which will enable the user to book a court, view, edit and delete a booking. In the meantime, add carousel and improve basic style of the app, add messages to main user actionas (CRUD). These tasks were split into two sprints due to their complexity.

- US Create Booking
- US View all Bookings (ListView)
- US Delete Booking
- US Edit Booking
- US Alternate List View depending on current user/staff
- US Add Carousel
- US Display messages upon user action
- DT Write up all the bugs until now

[Back to top](#contents)
### Sprint #6 - 12/06 - 16/06

The goal is to finish adding the main features: search functionality, contact form, improve styling of main elements.

- US Contact Us page
- US Add placeholder picture for Buddy
- US Basic Search Functionality
- US Improve website's style
- BF Favicon not loading

[Back to top](#contents)
### Sprint #7 - 19/06 - 23/06

Make a more advanced booking system, deploy with css and images, make progress with Readme. Connect the AddBooking form to a visual calendar which will inform the user about the court availability.

- US Make a more sophisticated visual booking system
- US Booking Calendar
- US Add Cancel button to edit/delete forms
- US Change column desctription in booking calendar
- US Inform the user when they have made a booking in the past (started in sprint #7, finalized in sprint #8)
- BF Heroku not loading css file
- BF When add booking is approached from the booking calendar, the information about date/time/court is lot

[Back to top](#contents)
### Sprint #8 - 27/06 - 30/06

Make progress with Readme and fix small bugs encountered during testing. Add phone number validation.

- BF Correct the flow for admin when editing/deleting a booking
- BF Fix hrefs for sign in and sign up pages
- US Restruct number of bookings per user to one per day
- US Phone number validation
- DT Readme Project management, Features, User Stories

[Back to top](#contents)
### Sprint #9 + #10- 03/07 - 14/07

Perform manual testing of HTML, CSS, Python, JS, LightHouse, responsivness, browser compatibility, user story testing. Add custom error pages. Add input validation. Make minor improvements and fix bugs. Again, this milestone took two sprints to complete.

- DT Readme Deployment
- DT Add customized 403, 404 and 500 error pages
- US Add validators for user inputs
- DT Readme: Technologies and packages used, Testing, ERD, Credits, Error Pages sections
- DT Do thorough testing of all aspects of the application to make sure everything works seamlessly and write up the documentation


[Back to top](#contents)

### GitHub Projects Board

I used Projects tool inbuilt in GitHub, [GitHub's Projects](https://github.com/users/lucia2007/projects/6/views/1), to help me manage the scope of the project, to track my progress and record bugs, but also to jot down any ideas that were relevant for the application development. These ideas were either later applied in the code or dismissed if they did not seem to enhance the user's experience or improve the development process.

Whenever I had an idea related to the project, I would jot it down in the "Backlog section/Brainstorming" section. Then I would go through the tasks and assign them to the current Milestone I was working on. I would convert the simple ideas into proper User Stories with acceptance criteria and necessary tasks and move them to the To Do section. I would label each User Story with the following labels: MoSCoW lables, story points, relevant Epic and Milestone, priority, user story/dev task/bug-fix. The developed tasks were usually centered around the backend part of the project, getting the frameworks set up and functional, or fixing bugs, writing documentation or testing.

When my Milestone with its deadline was set up (Sprint), I would assign relevant Epics with their User Stories to it. On a day-to-day basis, each morning, I would choose 2, max 3 things that were currently being worked on and I would place them in the "In Progress" section. If I became stuck on a task for whatever reason or depended on external input, I moved it to "Blocked". At last, when a task was completed, I would one more time check against the acceptance criteria, tick each of the finished tasks and move it to the "Done" section. I also made sure to work on my Readme file regularly in order to avoid having to tackle it all at once at the end. 

The Project tool has been very benefitial for my development process, especially because I could rely on having all the relevant information in one place. I would write down the sources to be credited, or bugs to be fixed or ideas on how to improve some part of the application, so I did not have to worry about having forgotten something crucial.

In the future, I should able to surmise the amount of story points for each Epic/User story more easily and thus plan my Sprints more effectively. Also I would like to improve my process for reporting bugs in Project and connecting them to their commits. At the moment I usually took note of a bug, but only retrospectively made it into an issue. In the future I would like to use a similar process as with user stories, with acceptance criteria and tasks and connect the issue to the commit message with solved it.

[Back to top](#contents)
### Moscow Prioritization

I had tried to apply MoSCoW principles in my development but more on a project basis than on a sprint basis. In my first sprints I solely focused on meeting must-have user stories and when most of my necessary features were in place, only then did I start incorporating should-haves or could-haves. As I went along, I also indentified won't-haves which were either to be fully abandoned or left for future development.

- Must Have: must be delivered (max 60% of user stories)
- Should Have: add significant value, but not crucial (20% of stories)
- Could Have: small impact if not implemented (20% of stories)
- Won't Have: not crucial for this iteration

Unfinished user stories can be found in either to-do or the won't have section of my project board.

[Back to top](#contents)
### Milestones

I split up my project development into the following milestones:

1. Set up project's framework, do an early deployment, add django allauth.
2. Create models, general site structure and navigation elements (navbar and footer) based on the original wireframes.
3. Finish CRUD functionality for Contact Details (user_profile) and for buddy profile.
4. Basic Booking functionality, improve app content/style, add user messages.
5. Search Functionality, Contact Form, Improve Styling of Main Elements.
6. Make a more advanced booking system, deploy with css and images, make progress with Readme.
7. Make progress with Readme and fix small bugs encountered during testing
8. Manual Testing, Readme Completion

[Back to top](#contents)
### Epics

Each milestone was split into epics. Looking back at it, my epics copy milestones quite a bit and I probably should have split them into more detailed ones. Some milestones contain just one epic, others contain more. For details please look into my [Projects](https://github.com/users/lucia2007/projects/6/views/1) where you can see which epic was a part of which milestone.

1. Setup development environment, install dependencies and packages, early deployment. Install Allauth.
2. Create genereal site structure and navigation elements based on wireframes.
3. Enable CRUD functionality for User_profile and Buddy.
4. Enable CRUD functionality for Booking.
5. Add Carousel and improve website styling.
6. Add messages to user actions.
7. Add search functionality, contact form and other small embelishments.
8. Make a more advanced Booking system.
9. Fix bugs encountered during testing.

[Back to top](#contents)
### User Stories

Each epic would contain several user stories. Each user story has a description, acceptance criteria and tasks which had to be done before the user story could be closed and moved to done. For details as to which user story was a part of a particular epic/milestone and for the acceptance criteria/tasks, please refer to my [Projects](https://github.com/users/lucia2007/projects/6/views/1) where all the details can be found.

The above listed user stories above had all been finished. There are several user stories which had not been done and are postponed for future development, others were moved into "won't do" category. For more details see Future Features in each respective section.

I realize that my attempt at agile project development was not perfect and I know I will do several things differently in the future, but it has definitely been an enriching experience which helped me manage the project's scope. In the future I plan to make more detailed Epics and to plan my sprints according to user story points, as now I have a better idea how long different tasks take me and I can make better, if imperfect, estimates.

[Back to top](#contents)
## Database Schema (ERD)

Before I started writing any code, I spent a lot of time on planning and thinking things through. One part on which I spent a considerable amount of time, was creating the ERD diagram and designing each model and their relationships. I used [Lucid Charts](https://lucidchart.com/) to create my ERD schema.

![ERD Diagram Lucid Charts](/readme-images/erd_diagram_lucidcharts.png)

Later when I needed to understand realtionships with django models better, I installed graphviz and related packages with which I could generate the schema below.

<details><summary><b>ERD Schema graphviz</b></summary>
   
![ERD Schema graphviz](/readme-images/model2.png)
</details><br />

This ERD schema was instrumental for creating all the necessary models for this app. Creating this schema helped me realize the relationships between different apps and models and clarified what kind of fields each of the model components would need. Later I followed [this link](https://www.youtube.com/watch?v=6F7QMoIc_dM) to generate an extensive model of all my project apps, including the Django inbuilt models which helped me clarify some of the relationships.

Models used in this project:
- UserProfile - used to collect contact information for users - full CRUD functionality
- Buddies - used to create/view/edit and delete buddy profiles with user's preferences and contact information
- Booking - used for making a court reservation - full CRUD functionality
- allauth - used for sign in/out/up functionality of the site
- Court - used for entering courts, not full CRUD
- Event - left for future development
- Club - not used

[Back to top](#contents)

## Site Structure

The Tennis Buddies site takes its form depending on if the user is signed in or not. If the user is not signed in, they can see a Register/Login buttons, whereas if they are sign in, they can see a Profile Icon/Logout buttons. If sstaff member is signed in, they can also see a Staff tab in the NavBar. More details can be found in the NavBar feature section.

There are different features which become available for only a signed in user, or for a user with filled in contact information. These restrictions are described more deeply in revelant sections.

[Back to top](#contents)
# Design Choices

The goal for the site was to make it simple, easily understandable, yet attractive. I kept the used colors to a minimum and used just three images for the carousel to make the site more lively.

[Back to top](#contents)
## Typography

Originally I wanted to change the provided font-type, but in the end after playing around with different fonts, I was quite happy with the original bootstrap one and so I did not make any alternations.

[Back to top](#contents)

## Color Scheme

As regards the color scheme, I normally would use a color scheme/wheel, but here I used only one main yellow/green color for the body and only altered the color of the pop up messages to match it. I chose colors which are associated with tennis. I kept the header and footer white to give the site a clean look.

[Back to top](#contents)

# Features
## Site Responsive Navigation Bar

![NavBar Login](./readme-images/navbar_login.png)

The site contains a simple but effective NavBar which simplifies the movement of the user on the site. The following links are available:
- Logo - the tennis buddy logo which evokes friendship and companionship is clickable and takes the user to the home page.
- Home - the home button takes the user to the home page.
- Find the ideal Buddy - this link takes the user to the buddies.html where the user can see a catalouge of players from which they can choose a player to engage with.
- Conditional Search functionality - if the user is signed in, they can see a search bar on the right. They can enter values like "beginner/advanced/intermediate", or "morning/afternoon/both morning and afternoon", or "hitting practice/match practice", or "singles/doubles", or "male/female".
  
[Back to top](#contents)

![Search Feature](./readme-images/conditional_search.png)  

- Booking - this link takes the user to the bookingcalendar.html where they can see which courts are available on a particular day.
- Contact us - the contact.html page lets the user get in touch with the club and provides information about the location of the club.
- Register/Login - when the user is not logged in, they can see "Register/Login" buttons which allow then to create an accout if they don't already have on or to log in, if they already have an account.
- User Profile Icon/Logout - when the user is logged in, the links on the right change to the "Profile Icon/Logout".

[Back to top](#contents)

![Profile Icon](./readme-images/profile_logout.png)  

- Conditional Profile icon appears, when the user is logged in. The user can access the following features through this icon:
  - Contact details - the user can either add their contact details through this link, or edit/delete them if the contact details had already been provided
  - Profile - the user can either create their buddy profile here, or they can edit/delete the profile if they already have one
  - Your bookings - here the user can see all of their bookings, which they can edit/delete, or they are informed about having no bookings in their name.

[Back to top](#contents)

![Staff Tab](./readme-images/condition_profile_icon.png)

- Conditional Staff link - if the user is admin/staff, when they log in, "Staff" link appears which lets them access the bookings/list/all where they can see/edit/delete everybody's bookings.

When a user is on a particular page, the link is becomes bold to make it clear to the user which page they are on.

The NavBar is responsive and is available in its full version on large screens only. When the screen size diminishes, the NavBar is collapsed into a clickable Hamburger.

![Hamburger](./readme-images/hamburger_collapsed.png)

<details><summary><b>Hamburger Open</b></summary>
   
![Hamburger open](./readme-images/hamburger_open.png)
</details><br />

<details><summary><b>Hamburger Profile</b></summary>
   
![Hamburger Profile](./readme-images/hamburger_profile.png)
</details><br />


[Back to top](#contents)
## Carousel

I used a moving carousel with three hero images to highlight the main features of the site easily accessible:
- The first image of a tennis ball on a tennis court makes the theme/content of the page clearly tennis related for any visiting user. The user can access sign in and sign up functionalities on this image.

![Welcome Image](./readme-images/carousel_welcome_image.png)

- The second image evokes friendship and companionship. It provides links to finding a new tennis buddy.

![Find Your Perfect Buddy](./readme-images/carousel_find_buddy.png)

- The third image of outdoor tennis courts shows the clubs layout and provides a shortcut to the booking system.

![Book a Court](./readme-images/carousel_tennis_courts.png)

[Back to top](#contents)

I created an overlay effect over the images for better legibility and accessibility. It also bring the text forward. The details of the images are not so important, as they are mainly to convery the main ideas and intentions.

The carousel also contains arrows and "dashes"/buttons to take the user to the desired carousel-image. 

On smaller screens, the text disappears to avoid making the images cluttered.

<details><summary><b>Welcome Small</b></summary>
   
![Welcome Small](./readme-images/carousel_tennis_ball_small.png)
</details><br />

<details><summary><b>Find a Perfect Buddy Small</b></summary>
   
![Find a Perfect Buddy Small](./readme-images/carousel_buddies_small.png)
</details><br />

<details><summary><b>Book a Court Small</b></summary>
   
![Book a Court Small](./readme-images/carousel_courts_small.png)
</details><br />


[Back to top](#contents)

## Footer

The user can find all necessary information in the footer. There is information about the opening hours of the club, there is site navigation which takes the user quickly to a desired part of the app, there are links to tips for self-improvement and lastly, there are contact details for getting in touch with the club. The footer also contains links to social media. The footer is site responsive and the items are stacked on top of each other for smaller screens, whereas they are next to each other for larger screens. 

![Footer](./readme-images/footer.png)

<details><summary><b>Footer Small Screens</b></summary>
   
![Footer small screens](./readme-images/footer_small_screens.png)
</details><br />

[Back to top](#contents)

## [Home Page](https://tennis-buddies.herokuapp.com/)

The home page contains basic information about the main features of the application. There are links to Find the Perfect Buddy, Booking and Contact us pages. 

![Home Page](./readme-images/homepage.png)

[Back to top](#contents)
## [Find the Perfect Buddy Page](https://tennis-buddies.herokuapp.com/buddies/)

On this page the user can see a display of players who are looking for a hitting partner. You can see their picture, or a placeholder picture if they did not provide one, their name and a brief description. If they want to see a player's details, they need to be signed in.

![Find the Perfect Buddy Page](./readme-images/findbuddy.png)

[Back to top](#contents)
### Buddy Search

In order to avail of the buddy search functionality, the user must be registered and signed in. They can search for terms like: "beginner/advanced/intermediate", or "morning/afternoon/both morning and afternoon", or "hitting practice/match practice", or "singles/doubles", or "male/female". Once the user has narrowed down the players to those who match their search criteria, they can click on the card and are taken to a page where the chosen buddy's details are presented.

### Future Features for Buddy Search

Originally, the buddy search was intended to be more sophisticated and more straightforward. As a first approximation, there should at least be a pop up modal which would give the user a hint which values they can search for. As the next step, I would like to do a more complex search functionality, where the user would be able to pick different values in each of the categories. 

[Back to top](#contents)
### [Buddy Details](https://tennis-buddies.herokuapp.com/accounts/login/?next=/buddies/"pk")

The link above should have a particular buddy's "pk" at the end of the link. The link in this form does not work. I did not provide a particular profile number, as the profile might get deleted and the link would not work.

![Buddy Detail Page](/readme-images/buddy_details.png)

Here the user can see the player's details such as their level, availability, preferences etc. Also an email address is displayed at the bottom of the form so that the user can contact the player and arrange a game with them.

If the signed user is also the owner of the buddy profile, when they click on their own card, they can see "Edit/Delete" buttons at the bottom of their card. These buttons are not present if the profile belongs to someone else.

<details><summary><b>Buddy Detail Page Owner</b></summary>
   
![Buddy Detail Page Owner](./readme-images/buddydetails_owner.png)
</details><br />

[Back to top](#contents)
### Future Features for Buddy Matching

- The admin will have to approve a profile before it can be added.
- The user can indicate if their status is active or not. If inactive, their profile would not be displayed on this page.
- The search functionality is to be more sophisticated: the user should be able to click on different available criteria and search for a combination of values, e.g. beginner + morning + doubles.
- Only the users which had created a buddy profile, will be able to search for a tennis buddy.
- The email of the registered users needs to be verified, so that the contact email address is a valid one and not a made up one which the user might have used at the registration.

[Back to top](#contents)  
## [Booking of the courts](https://tennis-buddies.herokuapp.com/bookingcalendar/)

![Booking Calendar](./readme-images/bookingcalendar.png)

The booking page consists of a date picker and a table with court availability on a particular day.
### Booking requirements

In order to book a court, the user must have a registered account and must be signed in. The user also must have created a user profile where they add their contact information. This is because the club staff wants to be able to give the user a quick phone call in case of a late cancelation, last minute change, or an emergency.

### [Making a reservation](https://tennis-buddies.herokuapp.com/bookings/add/?date=2023-06-01&time=15:00%20-%2016:00&court=three)

When the user clicks on a Booking link in NavBar or approaches it from the carousel or the footer, they are taken to bookingcalendar.html. Here the user is informed which courts are booked/free for the current date, or on the date they had chosen in the datepicker. The courts which are free contain a hyperlink. 

When the user clicks on a particular "Book now" link, the information about the chosen date/time/court combination is carried over to the bookings/add.html page. The user only has to choose an opponent/(s). At this point, they could still edit the time/date/court, but they would not be sure if the combination had already been booked by someone else.

The user can choose min 1 and max 3 opponents. The user chooses multiple opponents by holding shift or control. The user can also choose themselves if they want to e.g. practice their serve on their own. The user gets a warning if they choose more than 3 opponents.

[Back to top](#contents)

![Make a Booking](./readme-images/makebooking.png)

![Opponents Warning](./readme-images/opponents.png)

The user can see a pop up message which informs them about the successful reservation at the top of the page.

![Booking Success](./readme-images/bookingsuccessful.png)

[Back to top](#contents)

Any user can make maximum one booking per day. This is to prevent one user from reserving too many courts on any given day and gives other users a chance to make their own reservations. If a user tries to make a booking on a day when they already have a court booked, they get a warning message about maximum number of bookings and are taken back to the booking calendar, where they can choose a different date.

![Max Booking Warning](/readme-images/max_bookings_warning.png)

### [Edit/Delete Functionality](https://tennis-buddies.herokuapp.com/bookings/list/own/)

When the user has created a booking, they are taken to bookings/list/own.html where they can view, edit or delete their own bookings. This page can also be accessed through the Profile icon, under the "Your Booking" tab. Edit and delete features are available only for the owner of the bookings. A regular user can't edit or delete somebody else's booking. 

If a user deletes their contact info and wants to see their bookings (even though there are currently none as they got deleted with the profile), the user is prompted to enter their contact details.

![Your Bookings](./readme-images/yourbookings.png)

[Back to top](#contents)

![Edit Booking](./readme-images/edit_booking.png)

When the user has updated their booking, they can see a success message at the top of the page.

![Update Booking Success](./readme-images/edit_booking_success_message.png)

[Back to top](#contents)

![Delete Booking](./readme-images/booking_delete_confirmation.png)

![Delete Booking Success](./readme-images/booking_delete_success_message.png)

[Back to top](#contents)
### [Staff Dashboard](https://tennis-buddies.herokuapp.com/bookings/list/all/)

If the user is admin/staff/superuser, they will also see a "Staff" option in their NavBar through which they can access all the bookings of all the members. The staff user can edit or delete a booking of any of the users. If they access their own booking, they are taken to their booking list, but it they edit/delete somebody else's booking, the staff user is taken to staff dashboard.

![Staff Dashboard](./readme-images/staffdashboard.png)

[Back to top](#contents)
### Bookings in the past

The users are allowed to create bookings in the past as well. This is due to the fact that the club requires exact information about the court usage and the members sometimes don't make a booking and just come and use a court that is free or they don't update the opponents on the booking. The club needs the information about the players in case something was damaged, or somebody got hurt (insurance reasons) or e.g. in case of the recent Covid Pandemic, they could inform the players if one them had turned Covid positive. When a booking in the past gets created, the user gets a messages about its successful creation, but is informed about having made a booking in the past.

![Booking in the Past ](./readme-images/bookingpast.png)

[Back to top](#contents)
### Future features for Booking

There are several ways how the booking system could/should be improved:
- Make the bookings accessible for e.g. next week only, so that the users can't make a booking e.g. two years in advance. 
- At the moment, the combination of date/time/court is unique, but the system should also be checking if the user had not been entered as an opponent for that particular time/date combination.
- The user should be sent an email after they create a booking.
- The users which were chosen as opponents should also get a confirmation and the reminder email.
- The user/opponent should also be getting an email when a booking which they are a part of has been edited or deleted.
- The user could get a confirmation email when their reservation is coming up.
- When the user approaches the booking system from the calendar, they can clearly see which courts are available. However, when they are editing their booking, they don't see anymore which courts are free on the new desired date/time combination. In the future, the user should be either taken back to the calendar or get some suggestion about which courts are free so they wouldn't have to keep guessing. Maybe the user should be able to just edit the opponents and when they want to change the date/time or court, they would have to cancel the booking and add a new one through the calendar link.
- The booking calendar could display who the owner/opponents are for a particular booking instead of just "Booked".
- In the future I should differentiate between a superuser and staff members and adjust the conditional statements.
- A modal window should pop up when the user is chosing opponents with an information to hold shift or control buttons for choosing multiple players.
- One of the features I did not manage to do, was to create a separate booking system for staff members, where they would be able to book multiple courts on the same day for multiple hours, much more in advance in the future for special events. (This was taking into account restrictions which are not yet in place for the user booking either e.g.: bookings only one week in advance.) And of course a staff member should be able to make a booking in anybody's name.

[Back to top](#contents)

## [Contact Us page](https://tennis-buddies.herokuapp.com/contact/)

This page contains two main sections: a form which a client can fill in if they want to get in touch with the tennis club and a Google map which shows them an exact position of the club. When the user fills in the form, they see a message about the inquiry having been sent. However, this is not fully functional yet and will be taken care of in the next version. 

![Contact Us](./readme-images/contactus.png)

The input in the contact form is validated. First name and last name fields don't accept numbers and other unusual characters. For email validation, the front-end validator is a bit less strict than the backend validator. For example, according to the front-end this address would be acceptable: a@a, but the form would still be invalid. Therefore, I added a warning for the user that the email address is not valid and in what format it should be submitted. This is just a temporary workaround.

![Invalid Email Warning](/readme-images/invalid_email_warning.png)

[Back to top](#contents)
### Inquiry Confirmation Message

![Inquiry Confirmation Message](./readme-images/inquiry.png)

[Back to top](#contents)

### Future Features for Contact Us

At the moment, when the user fills in the form, they get a message about the inquiry being sent, but no email is delivered. I need to set this functionality up. At the moment, only a message in CLI/terminal appears, but this is available only in development environment.

[Back to top](#contents)
#### CLI Message

![CLI Message](./readme-images/cli_message.png)

[Back to top](#contents)
## Profile Icon

A profile Icon appears when the user is signed in. When the user clicks on the icon, they see the following options:

### Contact Info

Here the user can either [add their contact information](https://tennis-buddies.herokuapp.com/profiles/add/) if they had not done so before, or they can edit/delete the information. Contact Info is required in case the user wants to make a booking, view bookings or wants to add a buddy profile.

The user is informed about each action with a message that appears at the top of the page. Before deleting the profile, the user is asked to confirm the action. The user has an option to cancel edit/delete action in which case they are taken back to the previous page. 

[Back to top](#contents)
#### Add Contact Info   

![Add Contact Info](./readme-images/add_contact_details.png)

![Add Contact Success Message](./readme-images/add_contact_success.png)

The user has to enter the phone number in a desired format: +353xxxxxxxxx. If the number is not valid, a warning is displayed and a prompt is shown to help the user enter the number correctly.

![Phone Validation Warning](./readme-images/phone_number_validation.png)

[Back to top](#contents)

#### View Added Contact Info

![Contact Added](./readme-images/contact_added.png)

[Back to top](#contents)

#### Edit Contact Info

![Edit Contact Info](./readme-images/edit_contact.png)

![Edit Contact Success Message](./readme-images/contact_update_success.png)

[Back to top](#contents)

#### Delete Contact Info

![Delete Contact Info](./readme-images/contact_confirm_delete.png)

![Delete Contact Success Message](./readme-images/contact_delete_success_message.png)

[Back to top](#contents)

### Buddy Profile

A user can choose to fill in their buddy/profile details if they want to be contacted by other players to arrange a game. They are either taken to [add profile](https://tennis-buddies.herokuapp.com/profiles/add/?next=/buddies/add/) or to edit/delete profile if they had previously filled in the information. Again, the user is asked if they are sure about deletion or they can cancel edit/delete and go back to the previous page. All user actions are accompanied by a success message which appears at the top of the page. 

[Back to top](#contents)
#### Add Buddy Profile   

All fields in the form are prefilled or have placeholder text to aid the user in filling in the form. As regards the image, if the user does not provide one, a placeholder image will be used.

The user can choose their level, availability, type of game, etc. In the future, they will also be able to say that their profile is not to appear in the catalogue (inactive profile) or in the searches (the backend functionality is not currently in place.) Also in the next version, the admin will have a right to approve a buddy profile and dismiss those that violate the code of conduct as defined by the club.

![Add Buddy Profile](./readme-images/add_buddy_details.png)

![Add Buddy Success Message](/readme-images/add_buddy_success_message.png)

[Back to top](#contents)

#### View Added Buddy Details

When the user approaches their own buddy details either from Profile Icon or from Find the Perfect buddies, they can see edit/delete buttons underneath their profile. These are only present when the owner of the profile is the same as the current logged in user. 

![Buddy Details](./readme-images/buddy_details.png)

[Back to top](#contents)

#### Edit Buddy Details

![Edit Buddy Details](./readme-images/edit_buddy_details.png)

![Edit Buddy Success Message](./readme-images/edit_buddy_success_message.png)

[Back to top](#contents)

#### Delete Buddy Details

![Delete Buddy Details](./readme-images/buddy_delete_confirmation.png)

![Delete Buddy Success Message](./readme-images/buddy_delete_success_message.png)

[Back to top](#contents)

### Your Bookings 

Under Your Bookings the user can see/edit/delete their own bookings if they have made some, or they see a message that they have no bookings. More details above.

[Back to top](#contents)
## Sign Up Page

Sign up Page has a simple design. The user has to enter their email and the password twice. This is due to defensive programming principle where we try to avoid unnecessary errors caused by small typos.

All sign in functionalities are a result of using django-allauth. Using this package has enabled me to set this functionality up quickly and easily.

[Back to top](#contents)

![Sign Up Page](./readme-images/sign_up_page.png)

![Sign Up Success](./readme-images/sign_up_success_message.png)

[Back to top](#contents)

## Sign In Page
![Sign In Page](./readme-images/sign_in_page.png)

![Sign In Success](./readme-images/sign_in_success_message.png)

[Back to top](#contents)
## Logout Page

![Sign Out Page](./readme-images/sign_out_page.png)

![Sign Out Success](./readme-images/sign_out_success_message.png)

[Back to top](#contents)

### Future Features Sign in functionality

In the next version I would like to enable registration with social account sign in as this functionality makes the registration process much quicker and easier. Users are often dissuaded from signing up to new apps and this could facilitate the process.

At the moment, the email is not being verified and user can use a made up email. In the future I definitely want to add email verification as this is important for other features in the app, like contacting a buddy to organize a game or for contacting users in case of need by staff.

[Back to top](#contents)

## 403, 404 and 500 Error Pages

If a user navigates to a page that does not exist, a customized 404 error page will appear.

If a user attempts to do something they are not authorized to do, they will get a 403 Error page.

If a user navigates to a page and there is a server related issue/error, they will be shown a customized 500 error page.
    
![404 Error Page Image](readme-images/404_error_page.png) 

![403 Error Page Image](readme-images/403_error_page.png) 

![500 Error Page Image](readme-images/500_error_page.png) 

[Back to top](#contents)
## Future Features

Apart from the already mentioned future features in each relevant section, I would like to add a possibility to book a professional hitter/coach. Since Find your perfect buddy has an aspect of social media, I might have to add some restrictions to the buddies, e.g. if someone didn't want to be contacted by a particular player, they should be able to block them out, or younger players might want to be contacted only by players in their age category.

Also I would like to add automated testing, as at this point I relied thoroughly on manual testing.

[Back to top](#contents)

# Technologies Used
## Languages

- [Python](https://www.python.org/) - Used for adding functionality to the application.
- [HTML5](https://en.wikipedia.org/wiki/HTML) - Provides the content and structure for the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS) - Provides the styling for the website.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript) - Provides interactive elements of the website

## Frameworks and Software

- [Bootstrap](https://getbootstrap.com/) - A CSS framework that helps building solid, responsive, mobile-first sites.
- [Django](https://www.djangoproject.com/) - An MVT framework used to create the Tennis Buddies site.
- [Figma](https://figma.com) - Used to create wireframes.
- [Github](https://github.com/) - Used for hosting the repository.
- [Projects in GitHub](https://github.com/lucia2007?tab=projects) - Used for project managament.
- [Heroku](https://heroku.com/) - Used for deploying the application.
- [Gitpod](https://www.gitpod.io/#get-started) - Used for developing the application.
- [Markdown Table Generator](https://www.tablesgenerator.com/markdown_tables) - Used to generate tables in Markdown.
- [Favicon Converter](https://favicon.io/favicon-converter/) - used to create a favicon in correct format.
- [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) - Used to test performance of site.
- [Responsive Design Checker](https://www.responsivedesignchecker.com/) - Used for responsiveness check. 
- [Google Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used for debuggin and test responsiveness. 
- [Cloudinary](https://cloudinary.com/) - A service for hosting all static files in the project.
- [HTML Validation](https://validator.w3.org/) - Used to validate HTML code
- [CSS Validation](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- [CI Python Linter](https://pep8ci.herokuapp.com/#) - Used for validation python code.
- [Regex Pattern Checker](https://regex101.com/) - used to check my regex expression for phone number validation.
- [Lucid Charts](https://lucidchart.com/) - for creating my ERD Diagram

[Back to top](#contents)

# Python Packages

Following packages and libraries were installed and are located in requirements.txt or requirements-graphviz.txt. 
- asgiref==3.6.0
- black==23.3.0
- click==8.1.3
- cloudinary==1.32.0
- crispy-bootstrap5==0.7
- dj-database-url==0.5.0
- dj3-cloudinary-storage==0.0.6
- Django==3.2.19
- django-allauth==0.41.0
- django-crispy-forms==2.0
- django-extensions==3.2.1
- django-stubs==4.2.0
- django-stubs-ext==4.2.0
- django-summernote==0.8.20.0
- django-tables2==2.5.3
- graphviz==0.20.1
- gunicorn==20.1.0
- oauthlib==3.2.2
- pathspec==0.11.1
- psycopg2==2.9.6
- PyJWT==2.6.0
- python3-openid==3.2.0
- pytz==2023.3
- requests-oauthlib==1.3.1
- sqlparse==0.4.4
- types-dj-database-url==1.3.0.3
- types-pytz==2023.3.0.0
- types-PyYAML==6.0.12.9

- pydot==1.4.2
- pygraphviz==1.10
- pyparsing==3.0.9
- urllib3==1.26.16
- graphviz==0.20.1

[Back to top](#contents)
# Testing

For testing the application, I used manual testing and external validators. Both manual and external testing are a part of a separate testing [file](/TESTING.md).

### Manual testing

  - I used manual testing throughout the whole development phase of the project. Mainly:
    - I deployed early to avoid any last minute issues and checked my local and life site periodically. With the live site, I could check responsivness from early on on different devices.
    - I attended to any errors which I came across during development process.
    - I used validators to check my HTML, CSS and backend code.
    - For each of the user stories I wrote down clear acceptance criteria and tasks which had to be done to meet those criteria. Only after I had met all the conditions, did I move the user story to done.

### External Testing

  All external testing is a part of a separate testing [file](/TESTING.md).

### Automated Testing

I had not managed to do automated testing for this application, but I want to make it a regular part of my development process in my future projects.

[Back to top](#contents)

# Project Deployment

## Create a new GitHub Repository from CI template

- Create a GitHub repository from the [Code Institute template](https://github.com/Code-Institute-Org/gitpod-full-template) by following the link and then click 'Use this template'.

<details><summary><b>Create GitHub Repository</b></summary>

![Create GitHub Repository](readme-images/heroku_step_1.png)
</details><br />

- Fill in the needed details as stated in the screenshot below and then click 'Create Repository From Template'. The name you choose must be unique.

<details><summary><b>Choose Repository Name</b></summary>

![Repository Name](readme-images/heroku_step_2.png)
</details><br />

- When the repository is created, click the green 'Gitpod' button as stated in the screenshot below.

<details><summary><b>Click Green GitPod Button</b></summary>

![Click Green GitPod Button](readme-images/heroku_step_3.png)
</details><br />

[Back to top](#contents)
## Install Django and the supporting libraries

- To install Django and the supporting libraries, type the commands below.

* ```pip3 install 'django<4' gunicorn```
* ```pip3 install dj_database_url psycopg2```
* ```pip3 install dj3-cloudinary-storage```

<details><summary><b>Install Supporting Libraries</b></summary>

![Install Supporting Libraries](readme-images/heroku_step_4.png)
</details><br />

- When Django and the libraries are installed we need to create a requirements file.

* ```pip3 freeze --local > requirements.txt``` - This will create and add required libraries to requirements.txt

<details><summary><b>Create Requirements File</b></summary>

![Step 5](readme-images/heroku_step_5.png)
</details><br />

- Create the project.

* ```django-admin startproject YOUR_PROJECT_NAME .``` - This will create your project

<details><summary><b>Create Project</b></summary>

![Create Project](readme-images/heroku_step_6.png)
</details><br />

- When the project is created, we can now create the application.

* ```django-admin startapp APP_NAME``` - This will create your application

<details><summary><b>Create Application</b></summary>

![Create Application](readme-images/heroku_step_7.png)
</details><br />

- To create a superuser type in the following code:
`python3 manage.py createsuperuser`

You will be asked to enter credentials after which the superuser is created.  

- We now need to add the application to settings.py

<details><summary><b>Add Application to settings.py</b></summary>

![Add Application to settings.py](readme-images/heroku_step_8.png)
</details><br />

- Now do your first migration and run the server to test that everything works as expected. This is done by writing the commands below.

* ```python3 manage.py migrate``` - This will migrate the changes.
* ```python3 manage.py runserver``` - This runs the server. To test it, click the 'open browser' button that will be visible after the command is run.

- Create `env.py` file at the root level and include the following environment variables. Don't forget to add the `env.py` file in the `.gitignore` in order to keep your secret information from becoming unsafe:

`import os`

`os.environ["CLOUDINARY_URL"] = "insert your own Cloudinary API key here"`

`os.environ["DATABASE_URL"] = "insert your own ElephantSQL database URL here"`

`os.environ["SECRET_KEY"] = "this can be any random secret key"`

`os.environ["DEVELOPMENT"] = '1'`

The last variable is for local development only and must not be included in production/deployment/config vars in Heroku.

- In the `settings.py` add the following code under `from pathlib import Path`:

`import os`

`import dj_database_url`

`if os.path.isfile("env.py"):`

`import env`

* Replace the original unsafe SECRET_KEY with the following code:

`SECRET_KEY = os.environ.get('SECRET_KEY')`

* Set `DEBUG = "DEVELOPMENT" in os.environ`. This allows us to have DEBUG set to True when developing locally, but set to False when deployed to Heroku.

* Replace the original `DATABASES` code with the following lines (this allows us to use the postgress database instead of the sqlite3 databases):

`
DATABASES = {
    'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
  }
`

- Save all the files and migrate the changes:
`python3 manage.py migrate`

* Add Cloudinary Libraries to the "INSTALLED_APPS" in the following order (the order must be adhered to):

![Cloudinary Libraries added to Installed Apps](/readme-images/cloudinary_installed_apps.png)

* Add the following rows to the settings.py file for Django to be able to use and store static files:

![Static Settings](/readme-images/static_settings.png)

* Link the file to the Heroku templates directory:

![TEMPLATES_DIR](/readme-images/templates_directory.png)

* Update the TEMPLATES array with the following code:

![Template array update](/readme-images/templates_array_update.png)

* Add Heroku app and localhost to ALLOWED_HOSTS so the application can work through Heroku

![ALLOWED_HOSTS](/readme-images/allowed_hosts.png)

* Create the following folders at the top level directory:
  * media
  * static
  * templates
  
* Create a file called **Procfile** and add the following line in it:
`web: gunicorn PROJ_NAME.wsgi`

* Save all the files and do the first commit and push to GitHub:
  * `git add .`
  * `git commit -m "Deployment Commit"`
  * `git push`

[Back to top](#contents)
## ElephantSQL Database

[ElephantSQL](https://www.elephantsql.com/) is used for the PostgreSQL database in this project.

To create your own PostgreSQL database, sign-up with your GitHub account and follow these steps:
- Click **Create New Instance** to initiate a new database.
- Choose a name, usually the name of the project.
- Select **Tiny Turtle(Free)** plan.
- Leave the **Tags** blank.
- Select **Region** and **Data Center** closest to you.
- Afterwards, click on the new database name, where you can view the db URL and Password. Copy the URL and enter the address into your **config vars in Heroku** and into your `env.py` file.

[Back to top](#contents)
## Cloudinary API

[Cloudinary API](https://cloudinary.com/) is used to store media assets online.

In order to retrieve your Cloudinary API key, you must create an account and log in.
- Choose 'Programmable Media for image and video API' for 'primary interest'.
- Copy your **API Environment Variable** from your Cloudinary Dashboard.
- Remove the `CLOUDINARY_URL=` from the API value and use the key in **config vars in Heroku** and in your `env.py`.

[Back to top](#contents)
## Heroku Deployment

The project was deployed to [Heroku](https://www.heroku.com). To deploy, please follow the process below:

Create the application on Heroku, attach a database, prepare the `env.py` and `settings.py` file and setup the **Cloudinary storage** for static and media files. To do all this, follow the steps above.

* Go to [Heroku](https://www.heroku.com/) and sign in (or create an account if needed).

* Once signed in, click the button "New" in the top right corner, below the header and choose "Create new app". The name you choose must be unique. Choose a region which is closest to you.

<details><summary><b>Create New App</b></summary>

![Create New App](/readme-images/heroku_step_9.png)
</details><br />

<details><summary><b>Choose Name and Region</b></summary>

![Choose Name and Region](/readme-images/heroku_step_10.png)
</details><br />

- This brings you to the "Deploy" tab. From here, click the "Settings" tab and scroll down to the "Config Vars" section and click on "Reveal Config Vars". In the KEY input field, enter "PORT" and in the VALUE input field, enter "8000". After that, click the "Add" button on the right.

- Also add the `CLOUDINARY_URL`, `DATABASE_URL` and the `SECRET_KEY`. The values are identical to those entered into the `env.py` file.

- `DISABLE_COLLECTSTATIC` variable is needed only for the initial deployment, later this variable must be removed.

<details><summary><b>Config Vars</b></summary>

![Config Vars](/readme-images/config_vars.png)
</details><br />


Heroku needs two additional files in order to deploy properly:
- `requirements.txt` (see above)
- `Procfile` - this file can be created with the following command: `echo web: gunicorn app_name.wsgi > Procfile`. Replace 'app-name' with the name of your primary Django app/project name.

- Scroll back to the top of the page and choose the "Deploy" tab. Then choose "GitHub" as Deployment method.
   
<details><summary><b>Deployment method</b></summary>

![Deployment method](/readme-images/deploy.png)
</details><br />

Go to "Connect to GiHub" section, search for the repository name and then click "Connect".
   
<details><summary><b>Connect to GitHub</b></summary>

![Connect to GitHub](/readme-images/connect_repository.png)
</details><br />

- In the "Automatic Deploys" section, choose your preferred method for deployment. At first, I used the manual deployment option, and later I changed it to automatic deploys. Afterwards, click "Deploy Branch".
   
<details><summary><b>Automatic Deploys</b></summary>

![Automatic Deploys](/readme-images/automatic_deploys.png)
</details><br />

Alternatively, you can follow these steps:
- In the Terminal/CLI connect to Heroku by typing in: `heroku login -i`
- Set the remote for Heroku: `heroku git: remote -a app_name` (replace app_name with your app name)
- After doing Git `add`, `commit`, `push` to GitHub, you can type in: `git push heroku main`

The project should now be deployed to Heroku.

The link to the the live site can be found here - https://tennis-buddies.herokuapp.com/.
The link to the GitHub repository can be found here - https://github.com/lucia2007/tennis_buddies.


[Back to top](#contents)
## To fork the repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. This copy can be viewed and changed without affecting the original repository. Take the following steps to fork the repository:

1. Log in to **GitHub** and locate the [repository](https://github.com/lucia2007/tennis_buddies).
2. On the top right hand side of the page is a button called **'Fork'**. Click on the button to create a copy of the original repository in your GitHub Account.

![GitHub forking process image](/readme-images/forking_process.png)

[Back to top](#contents)

## To create a local clone of a project

Take the following steps to create a clone of a project:

1. Click on the **Code** button in the left top corner.
2. Next to the green **GitPod** button, click on **Code** drop-down menu.
3. In the **HTTPS** section, click on the clipboard icon to copy the displayed URL.
4. In your IDE of choice, open **Git Bash**.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone``, and then paste the URL copied from GitHub.
7. Press **enter** and the local clone will be created.
8. Install requirements to get the project to work by typing in this command:
   `pip3 install -r requirements.txt`
   This command downloads and installs all the required dependencies as found in `requirements.txt file`.
9. Set up environment file (`env.py`) so that the project knows what variables are needed to make it work. For retrieving the Cloudinary API key and the ElepahtnSQL url, please follow the steps in the subsequent sections. Then add the following code to your file. 
    
`import os`

`os.environ["CLOUDINARY_URL"] = "insert your own Cloudinary API key here"`

`os.environ["DATABASE_URL"] = "insert your own ElephantSQL database URL here"`

`os.environ["SECRET_KEY"] = "this can be any random secret key"`

`os.environ["DEVELOPMENT"] = '1'`

These variables are usually hidden due to sensitivity of the information. You must not push the `env.py` file to GitHub. You will achieve this by adding the `env.py` to the `.gitignore-file`. The variables that are declared in the `env.py` also need to be added to the **Heroku config vars** apart from the ["DEVELOPMENT"] variable, for detailes see above. (For setting up your CLOUDINARY and ElephantSQL please follow the steps detailed in the deployment section.)

10.  Make all the relevant migrations before running the server by:
    - `python3 manage.py migrate` - this makes the necessary migrations
    - `python3 manage.py runserver` - enables the project to live locally 
    - `python3 manage.py createsuperuser` - this creates a superuser after you provide credentials

![Github cloning process image](/readme-images/cloning_process.png)

[Back to top](#contents)

# Credits

## Content
- I followed [this link](https://www.youtube.com/watch?v=6F7QMoIc_dM) to generate an extensive model of all my project apps, including the Django inbuilt models which helped me understand the relationships
- Readmes to follow: https://github.com/worldofmarcus/project-portfolio-4/blob/main/README.md#deployment, https://github.com/amylour/FreeFido_v2, https://github.com/adamgilroy22/tribe/tree/main#deployment, https://github.com/worldofmarcus/project-portfolio-4/blob/main/README.md
- Table structure in Staff Dashboard was created following [this tutorial](https://www.youtube.com/watch?v=gXGQmt_U9Ao&t=65s).
- [Filtered booking list](https://www.django-rest-framework.org/api-guide/filtering/#filtering-against-the-current-user)
- [To query according to url+filter](https://docs.djangoproject.com/en/4.2/topics/db/queries/)
- [CRUD functionality was done following Dee Mc's Recipe tutorial](https://www.youtube.com/watch?v=sBjbty691eI&list=PLXuTq6OsqZjbCSfiLNb2f1FOs8viArjWy)
- [Boutique Ado](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+EA101+2021_T1/courseware/eb05f06e62c64ac89823cc956fcd8191/3adff2bf4a78469db72c5330b1afa836/) inspired me to use "includes" for header.html and footer.html.
- Features section of the home page was inspired by [this site](https://easy-eater.herokuapp.com/).
- [Restrict the number of opponents](https://stackoverflow.com/questions/20203806/.limit-maximum-choices-of-manytomanyfield/20230270#20230270)
- [Update Owner to current user](https://docs.djangoproject.com/en/2.0/topics/class-based-views/generic-editing/#models-and-request-user)
- [Messages](https://learn.codeinstitute.net/login?next=/courses/course-v1%3ACodeInstitute%2BFST101%2B2021_T1/courseware/b31493372e764469823578613d11036b/ae7923cfce7f4653a3af9f51825d2eba/%3Fchild%3Dfirst) - to display messages
- [Delete Message](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown) - to display deletion message in Class based views
- [Search Functionality](https://www.youtube.com/watch?v=LsU79aY79UA) - to enable search functionality on the Find the Perfect buddy page.
- [Contact Page Functionality](https://www.youtube.com/watch?v=w4ilq6Zk-08&list=PLCC34OHNcOtrZnQI6ZLvGPUWfQ6oh-D6H&index=7&t=2s) - to send an email to CLI in developer mode
- [Contact Form](https://ordinarycoders.com/blog/article/build-a-django-contact-form-with-email-backend) - for contact form structure and google maps
- [If not for loop last](https://www.reddit.com/r/django/comments/13p2uuz/is_there_a_way_to_if_not_forlooplast/)
- [Check if superuser](https://stackoverflow.com/questions/65421561/how-can-i-check-if-an-user-is-superuser-in-django)
- [Image overlay](https://www.w3schools.com/howto/howto_css_overlay.asp)
- [Check if date is not in the past](https://stackoverflow.com/questions/73260028/how-can-i-check-if-date-is-passed-from-django-model)
- [TestIfUserProfile Mixin](https://stackoverflow.com/a/42193610/15098344)
- [Placeholder time=now](https://docs.djangoproject.com/en/4.2/ref/templates/builtins/#now)
- [Split string and get 1st element](https://bobbyhadz.com/blog/python-split-string-and-get-last-element#split-a-string-and-get-the-first-element-in-python)
- [Convert string to datetime](https://www.freecodecamp.org/news/python-string-to-datetime-how-to-convert-an-str-to-a-date-time-with-strptime/)
- [Get success url with pk](https://stackoverflow.com/questions/26548018/how-to-feed-success-url-with-pk-from-saved-model)
- [Prepopulate AddBooking Form](https://stackoverflow.com/questions/22083218/django-how-to-pre-populate-formview-with-dynamic-non-model-data)
- [Generate HTML in Django](https://twitter.com/AdamChainz/status/1504231031574040578)
- [Url encode](https://stackoverflow.com/questions/64538729/how-to-url-encode-in-django-views)
- [Characters not to be included for name validation](https://salesforce.stackexchange.com/questions/41153/best-regex-for-first-last-name-validation)
- [Disable html warning](https://html-validate.org/usage/index.html#inline-configuration)
- [Disable class Deletion warning](https://stackoverflow.com/a/75724709/15098344)
- [Check if url contains a certain string](https://stackoverflow.com/a/12877568/15098344)

[Back to top](#contents)
## Media
- https://www.istockphoto.com/photos/tennis-friends
- https://www.coachhousevets.com/meet-the-team/the-team/no-photo-icon-22/
- [Tennis Buddies image](https://www.google.com/search?q=tennis+buddies+icon&tbm=isch&ved=2ahUKEwivzZKN0LD_AhU2SEEAHdYeCk4Q2-cCegQIABAA&oq=tennis+buddies+icon&gs_lcp=CgNpbWcQAzIECCMQJzoFCAAQgAQ6BggAEAcQHjoGCAAQCBAeOgYIABAFEB46CwgAEIAEELEDEIMBOgQIABAeOgcIABAYEIAEUP4GWP0iYIIlaABwAHgAgAFoiAGKDpIBBDE3LjOYAQCgAQGqAQtnd3Mtd2l6LWltZ8ABAQ&sclient=img&ei=VzCAZO_FJLaQhbIP1r2o8AQ&bih=1441&biw=2844&rlz=1C1CHBF_csIE1041IE1041#imgrc=XSMFqBMnwoaIKM)

[Back to top](#contents)
## Acknowledgements
- Extra help and guidance was received from my mentor Precious Ijege, from my husband Sam and fellow colleagues from the Code Institute. I was especially thankful for my mentor's last minute feedback when I was getting weary and was becoming unattentive to detail.

Thank you all for your support and encouragement. I couldn't have done it without you.

[Back to top](#contents)

