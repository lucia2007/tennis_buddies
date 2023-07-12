# Testing
- [Testing](#testing)
  - [Code Validation](#code-validation)
    - [HTML Testing](#html-testing)
    - [Python Testing](#python-testing)
    - [JavaScript Testing](#javascript-testing)
    - [CSS Testing](#css-testing)
  - [Browser Compatibility](#browser-compatibility)
  - [Responsiveness Test](#responsiveness-test)
  - [Fixed Bugs](#fixed-bugs)
  - [Unfixed Bugs](#unfixed-bugs)
  - [Additional Testing](#additional-testing)
    - [Lighthouse](#lighthouse)
    - [Results from Lighthouse](#results-from-lighthouse)
    - [User Stories Testing](#user-stories-testing)
    - [Manual Testing](#manual-testing)

## Code Validation

The [Tennis Buddies](https://tennis-buddies.herokuapp.com/) webpage was thouroughly tested. HTML code was reviewed in the [W3C HTML Validator](https://validator.w3.org). The CSS code was validated in the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the JS file was check in [JS Hint](https://jshint.com/). Python files were tested in [Python Linter](https://pep8ci.herokuapp.com/#).  

All errors were corrected and HTML, JS and CSS files currently have no errors.

[Back to top](#testing)
### HTML Testing
In order to validate my HTML code I had to extract it from "View page source" which is available upon a right mouse click on the respective html page. This is due to the fact that I have been using Jinja syntax and form|crispy and not all of my code would be validated if I just copied my own html code.

During HTML validation I encountered a number of errors in my file. In order to avoid verbosity, I'm attaching the original validation message and a commit number where the errors were corrected. 

| Page | Current Errors and Warning (No Errors) | Original Errors and Warnings | Bug-Fix (Commit #)
| ---- | ---------- | --------- |  ---------- |
| Home | [Home Page validation](./testing-images/index_html_no_errors.png) | [index.html Errors](./testing-images/homepage_html_validation_errors.png)  | [2c843fa](https://github.com/lucia2007/tennis_buddies/commit/2c843fa7a82dca807c5b41020fd5433524763c75), [522bb31](https://github.com/lucia2007/tennis_buddies/commit/522bb3181c1df4854706dbbc2a55d40e24438dd2)  |
| Find the Perfect Buddy | [Find Perfect buddy validation](./testing-images/perfect_buddy_no_errors.png) | [Find Buddy Errors](testing-images/perfect_buddy_no_errors.png)  | [0dd4f0d](https://github.com/lucia2007/tennis_buddies/commit/0dd4f0d99bacc93a8cd09d5bcc8bb4af4a5e7bb7) |
| Booking Calendar | [Booking Validation](./testing-images/booking_calendar_html_no_errors.png) |  [Booking Errors](testing-images/booking_calendar_html_validation_errors.png) | [915dd87](https://github.com/lucia2007/tennis_buddies/commit/915dd87d5b811a77238837d4c9b7dd11ffdd1cff)
| Add Booking | [Add Booking Validation](./testing-images/add_booking_html_no_errors.png) |
| Your Bookings | [Your Bookings Validation](./testing-images/your_bookings_html_no_errors.png) |
| Edit Booking | [Edit Booking Validation](./testing-images/edit_booking_html_no_errors.png)
| Delete Booking | [Delete Booking Validation](./testing-images/delete_booking_html_no_errors.png)
| Contact Us | [Contact Us Validation](./testing-images/contact_us_html_no_errors.png) |
| Staff | [Staff Validation](./testing-images/staff_html_no_errors.png) | [Staff Warnings](./testing-images/staff_html_validation_errors.png) | [b8701f0](https://github.com/lucia2007/tennis_buddies/commit/b8701f0bc0e4ca7d0ff80c6d359e60cba6bc2586)
| Add Profile | [Add Profile Validation](./testing-images/add_profile_html_no_errors.png) | [Add Profile Errors](testing-images/add_booking_html_validation_errors.png) |[c384b01](https://github.com/lucia2007/tennis_buddies/commit/c384b01e1bab7c0ff42ee35e859859aa6765ae53)
| Edit Profile | [Edit Profile Validation](./testing-images/edit_profile_html_no_errors.png) |
| Delete Profile | [Delete Profile Validation](./testing-images/delete_profile_html_no_errors.png) |
| Add Buddy  | [Add Buddy Profile Validation](./testing-images/add_buddy_html_no_errors.png) |
| Buddy Details | [Buddy Details Validation](./testing-images/buddy_details_html_no_errors.png)  | [Buddy Details Errors](/testing-images/buddy_details_errors.png) | [cc08499](https://github.com/lucia2007/tennis_buddies/commit/cc084997fe7a60423879d193b698e38eb28a4fae)
| Edit Buddy | [Edit Buddy Validation](./testing-images/edit_buddy_html_no_errors.png) |
| Delete Buddy | [Delete Buddy Validation](./testing-images/delete_buddy_html_no_errors.png) |
| Sign In | [Sign In Validation](./testing-images/sign_in_html_no_errors.png) |
| Sign Up | [Sign Up Validation](./testing-images/sign_up_html_no_errors.png) |
| Sign Out | [Sign Out Validation](./testing-images/sign_out_html_no_errors.png) |
| 404 Error Page |[404 Error Page Validation](./testing-images/404_html_no_errors.png)
| 403 Error Page | [403 Error Page Validation]() | [403 Page Errors](./testing-images/403_page_errors.png) | [f0a1efc](https://github.com/lucia2007/tennis_buddies/commit/f0a1efca45e32d496e99c98b589809b23a7ae347)

I could not check the source for 500 Error page, because when I tried to look at the source code in devtools, I had to Confirm Form Resubmission and thus my html code no longer applied.

[Back to top](#testing)

### Python Testing

[CI Python Linter](https://pep8ci.herokuapp.com/#) was used to validate the Python files which were created or edited by me.

|        | admin.py| forms.py | models.py | urls.py | views.py | tables.py |
| ------ | ---------- | ------------- | --------- | -------- | --------------- | --------------- |
| bookingcalendar | na   | na         | na      | [no errors](/testing-images/bookingcalendar_urlspy.png)      | [no errors](/testing-images/bookingcalendar_viewspy.png)         | [no errors](/testing-images/bookingcalendar_tablespy.png)         |
| bookings | [no errors](/testing-images/bookings_adminpy.png)      | [no errors](/testing-images/bookings_formspy.png)          | [no errors](/testing-images/bookings_modelspy.png)     | [no errors](/testing-images/bookings_urlspy.png)    | [no errors](/testing-images/bookings_viewspy.png)           | na          |
| buddies | [no errors](/testing-images/buddies_adminpy.png)      | [no errors](/testing-images/buddies_formspy.png)          | [no errors](/testing-images/buddies_modelspy.png)      | [no errors](/testing-images/buddies_urlspy.png)    | [no errors](/testing-images/buddies_viewspy.png)          | na            |
| contact | na     | [no errors](/testing-images/contactform_formpy.png)        | na      | [no errors](/testing-images/contactform_urlspy.png)     | [no errors](/testing-images/contactform_viewspy.png)            | na            |
| home | na      | na          | na      | [no errors](/testing-images/home_urlspy.png)     | [no errors](/testing-images/home_viewspy.png)           | na            |
| profiles | [no errors](/testing-images/profiles_adminpy.png)      | [no errors](/testing-images/profiles_formspy.png)           | [no errors](/testing-images/profiles_modelspy.png)      | [no errors](/testing-images/profiles_urlspy.png)     | [no errors](/testing-images/profiles_viewspy.png)         | na     
| settings.py | [no errors](/testing-images/tennisbuddies_settings.png)         | na          | na     | na    | na            | na     
| tennisbuddies | na       | na          | na      | [no errors](/testing-images/tennisbuddies_urlspy)     | na            | na     

In a few cases I used "# noqa" in order to be able to keep the lines over 80 characters without getting an error. This was done only in cases where the code legibility would suffer if I broke the code apart.

I also used "# type: ignore" for an internal django bug, which is decribed [here](https://stackoverflow.com/a/75724709/15098344). I also used this expression for "missing library stubs or py.typed marker [import] mypy", [explanation](https://mypy.readthedocs.io/en/stable/running_mypy.html).

[Back to top](#testing)

### JavaScript Testing

I used only one small JS function for closing a message window after 2000 miliseconds. The code is without errors.

[JS Validation Result](/testing-images/js_timeout.png)

[Back to top](#testing)

### CSS Testing

[W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) was used to validate my CSS file. External CSS for Bootstrap, provided by CDN was not tested. No errors were found.

[CSS Validation Result](/testing-images/css_validation_no_errors.png)

[Back to top](#testing)

## Browser Compatibility

The website was tested on the following browsers: Google Chrome, Safari, Microsoft Edge and Mozilla Firefox. There were no errors discovered in the functionality of the site or the individual features.

| App | Browser Compatibility |
| ---- | ---------- |
| Google Chrome | &check; | 
| Safari | &check; | 
| Microsoft Edge| &check; | 
| Mozilla Firefox| &check; | 

[Back to top](#testing)

## Responsiveness Test

Testing of responsive design was carried out manually by utilizing [Google Chrome DevTools](https://developer.chrome.com/docs/devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).

|        | S Galaxy 5 | iPhone 6/6S/7 | iPad Mini | iPad Pro | Display <1200px | Display >1200px |
| ------ | ---------- | ------------- | --------- | -------- | --------------- | --------------- |
| Render | pass       | pass          | pass      | pass     | pass            | pass            |
| Images | pass       | pass          | pass      | pass     | pass            | pass            |

The only tricky page is where user's bookings are displayed (bookings/list/own or /all) on very small devices (below 375px). But since my focus was on devices >= 375px, I did not decrease the size of the content further to keep the text legible.

[Back to top](#testing)

## Fixed Bugs

|                                        BUG                                       | WHERE |                                      HOW                                      |                   COMMIT                   |
|:--------------------------------------------------------------------------------:|:-----:|:-----------------------------------------------------------------------------:|:------------------------------------------:|
| Buddy profile was not saving.                                                    | buddies/views.py  | I had to add a related name to UserProfile model. Add DOB to the form and change form_valid()| [b616b94](https://github.com/lucia2007/tennis_buddies/commit/b616b9436146f435f4df4fe6318a580a01364792)  |
| User_profile form was not saving/form_valid() was not correctly defined          | profiles/views.py | I had to change `form.instance.user_profile` and add a related name.| [946720c](https://github.com/lucia2007/tennis_buddies/commit/946720c1e774fdb4be1f857466e5ecd9fd478b50)  |
| Crispy filter now working/not being applied                                      | login.html        | I had copied the allauth templates into templates/allauth/templates instead of templates/allauth, so the crispy filter and other changes could not be applied.                                                   | [d706a2b](https://github.com/lucia2007/tennis_buddies/commit/d706a2b5b50d20f392f361e8ec42966fd6f9c85f)  |
| My success url for AddUserProfile was not working                                | profiles/views.py | get_success_url() needed success_url to be declared (added it back)| [c51e1ef](https://github.com/lucia2007/tennis_buddies/commit/c51e1efa9f88281ca5e17c890f0f55e6e49f1247)
| I changed values from false/true and back in some my models and the migrations failed  | buddies    | I had to squash the bad migration with its reversal                 | [9521f88](https://github.com/lucia2007/tennis_buddies/commit/9521f886d05014ce8aa90b643f2126d869f49c08)  |
| Deployment not working due to graphviz                                           | requirements.txt  | I had to take out graphviz requirements into a separate file (not needed for deployment.)                                                  | [bb8530b](https://github.com/lucia2007/tennis_buddies/commit/bb8530b42a94f0f6434e5e89ae1d529178bbb315)  |
| Booking-detail url would not display, as it was satisfied by an earlier url case | Bookings/urls.py  |  I changed the order of the urls.                                  | [088bed5](https://github.com/lucia2007/tennis_buddies/commit/088bed5865f233ec00542c085b8ba66a7ba12e6c)  |
| bookings/list/all was asking for user_profile which is not needed in this case   | bookings/views.py | I moved line 37 into the else branch of the condition              | [fc3f324](https://github.com/lucia2007/tennis_buddies/commit/fc3f3245cf1bf0cdbf2e4ab6b42f87578bdac351)  |
| Automatic profile creation was causing all sorts of issues (e.g. after I register, I get a bug Field 'id' expected a number but got 'AnonymousUser'.)     | profiles/models.py     | I deleted the post_save() and signals functionality and reversed to the original code | [91daf23](https://github.com/lucia2007/tennis_buddies/commit/91daf2333f91048b728944962bcaa9763c03e418)  |
| When the site was deployed, the css or the images would not show/be applied.     | Heroku/live site  | I used absolute paths for the css file and the images/icons. I had to remove the first slash. | [a1691a8](https://github.com/lucia2007/tennis_buddies/commit/a1691a8d23e04f8391af204889abdc47572105db)  |
| Booking details were getting lost if the user had no user profile                |  bookingcalendar.html    |  I had to use the get_full_path() to keep all the booking details | [08d1a63](https://github.com/lucia2007/tennis_buddies/commit/08d1a6303bea935cbcf4b75d41de59632bf635ce)  |
| Similar as the previous bug, not all booking information was being carried over  |  bookingcalendar.html    |  I had to use the urlencode() to keep all the booking details | [08d1a63](https://github.com/lucia2007/tennis_buddies/commit/08d1a6303bea935cbcf4b75d41de59632bf635ce)  | [d5a3ae7](https://github.com/lucia2007/tennis_buddies/commit/d5a3ae7148f9d0b1e5bb37de101fbc1319007621)
| The favicon was not loading properly                                             |  base.html   |  I had to move the favicon.ico file to the static folder and update the path in base.html  |[65c2731](https://github.com/lucia2007/tennis_buddies/commit/65c27313286e41ee3a22b13eabb22f0d8cdf7cc8)
| When I accessed any of the Home, Find the buddy, Booking or Contact pages from the NavBar, the sign in and sign up buttons on the carousel would not take me to the desired pages.      |  all pages   | I had to change the href reference for them to work on any of the given pages.   |[ae15a3d](https://github.com/lucia2007/tennis_buddies/commit/ae15a3daab39b7201c2f3f81aa94bf8072c2546f)
| When I edited or deleted bookings as an admin, it would take me 'bookings/list/own' instead of 'bookings/list/all'  |  edit/delete booking pages   | I had to create conditions for get_success_url() and introduce a condition around "Cancel" button on edit/delete booking pages. |[1bf5cf5](https://github.com/lucia2007/tennis_buddies/commit/1bf5cf5f23787d7ee08663e49e1257bb9f792dc1)
Lines > 80, other minor errors     |  many different files, mostly python   | I shortened most of the lines in python files, except for those where I felt the readability of the code would suffer if the code were split to numerous lines |[74fed1e](https://github.com/lucia2007/tennis_buddies/commit/74fed1e47c47c90f3a9fba0e81a5891acb64d383)
| When I made a booking at a future date, but the time has passed, I would get a warning about booking in the past. |  views.py bookings   | I had to change the condition check for time in the past |[9aa7a16](https://github.com/lucia2007/tennis_buddies/commit/9aa7a160ba0560cb9ccf5e625de5b3cc1f76c078)
| Staff tab was highlighted even when I was on bookings/list/own |  header.html   | I had to change the condition to look for the url path and not for url_name |[525c0fd](https://github.com/lucia2007/tennis_buddies/commit/525c0fdfededbb510e0223c77aeb22f88d6a0ee1)

[Back to top](#testing)

## Unfixed Bugs

I have tried to fix the following errors but have not managed to do so in the provided timeframe. I definitely plan to fix these errors in the next version.

1. In my Edit Buddy form the "currently" image field is empty, even though it should display the path to the image. I had not managed to make the path appear. Neverthless, this does not affect the functionality and the user is able to edit the image without any problems.
[Missing Image description](/testing-images/missing_image_description.png)

2. There is a bug in the browser console related to the imported JS which handles the appearance of messages. The same error appears in most browsers.
[Browser error](/testing-images/browser_error.png)

[Back to top](#testing)

## Additional Testing
### Lighthouse

The application was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools. The following aspects were tested:

- Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse
| Page | Validation Results |
| ---- | ---------- |
| Home | [Home Page Score](./testing-images/lighthouse_homepage.png) | 
| Find the Perfect Buddy | [Find Perfect Buddy Score](./testing-images/lighthouse_buddies.png) |
| Booking Calendar | [Booking Calendar Score](./testing-images/lighthouse_booking_calendar.png) |
| Add Booking | [Add Booking Score](./testing-images/lighthouse_bookings_add.png) |
| Your Bookings | [Your Bookings Score](./testing-images/lighthouse_bookings_list_own.png) |
| Edit Booking | [Edit Booking Score](./testing-images/lighthouse_booking_edit.png)
| Delete Booking | [Delete Booking Score](./testing-images/lighthouse_booking_delete.png)
| Contact Us | [Contact Us Score](./testing-images/lighthouse_contactus.png) |
| Staff | [Staff Score](./testing-images/lighthouse_bookings_list_all.png) | 
| Add Profile | [Add Profile Score](./testing-images/lighthouse_profile_add.png) | 
| Edit Profile | [Edit Profile Score](./testing-images/lighthouse_profile_edit.png) |
| Delete Profile | [Delete Profile Score](./testing-images/lighthouse_profile_delete.png) |
| Add Buddy  | [Add Buddy Profile Score](./testing-images/lighthouse_profile_add.png) |
| Buddy Details | [Buddy Details Score](./testing-images/lighthouse_buddy_detail.png)  |
| Edit Buddy | [Edit Buddy Score](./testing-images/lighthouse_buddy_edit.png) |
| Delete Buddy | [Delete Buddy Score](./testing-images/lighthouse_buddy_delete.png) |
| Sign In | [Sign In Score](./testing-images/lighthouse_login.png) |
| Sign Up | [Sign Up Score](./testing-images/lighthouse_signup.png) |
| Sign Out | [Sign Out Score](./testing-images/lighthouse_logout.png) |

All of my scores for all of the pages were above 90, often close to 100. On a couple of pages the "Best Practices" score is slightly lower, due to an error which is logged into the console and seems to be caused by JSDelivr CDN for the close button on messages. I have not managed to fix this error. Details are in the bug section.

[Back to top](#testing)

### User Stories Testing
Before any user story could be moved to "done", clear acceptance criteria were defined and necessary tasks were listed. Only after all the criteria were met and all tasks were finished, did I consider a user story finished. The only exception was, if some of the features were moved into "won't do" category. In that case, that feature would be extracted from the user story and labeled as "won't do"

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | As a **user**, I would like to **view the apps homepage** so that I can **learn about the app and see what services it provides**.
| &check; | As a **user** I can **locate the navigation area** so that I can **easily access different parts of the website**
| &check; | As a **user**, I can **access relevant information about opening hours, contact information and social media links without having to scroll back to the top of the page** so that I can **visit the club, contact the club and follow the club online**.
| &check; | As an **unregistered user** I want to be able **to sign up onto the website** so that I can **access websites functionality and content**.
| &check; | As a **registered user** I want to be able **to sign in into my account** so that I can **get access to the website's functionality and options**.
| &check; | As a **signed in user** I want to be able **to sign out of my account** so that I can **keep my account private and safe**.
| &check; | As a **user** I can **enter my personal details** so that I can **create an account with Tennis buddies and be contacted in case of need**
| &check; | As a **signed in user with an active profile** I can **create a buddy profile** so that **I can use the search functionality to find the best tennis partner**
| &check; | As a **user**, I can **edit my buddy profile** to **update my preferences regarding the style of play/practice**.
| &check; | As a **registered user** I can **press delete button on my buddy profile form** so that I can **delete all provided information regarding my preferences for a tennis partner, including pictures**
| &check; | As a **registered user** I can **press delete button on my user profile/contact form** so that I can **delete all provided information regarding my contact details**.
| &check; | As a **user**, I can **edit my user profile** to **update my personal details**.
| &check; | As a **user** I can **visit the Find Your Perfect Buddy page** so that I can **find the perfect match for my tennis practice**.
| &check; | As a **user** I can **reserve a court** so that I can **play at a time that suits me and can avoid come to a full club**.
| &check; | As a **signed in user/staff member** I can **view all the bookings** so that I can **see when other people are playing/the courts are busy**.
| &check; | As a **registered user/superuser** I can **press delete button on my booking details** so that I can **delete my/any user's booking**.
| &check; | As a **user**, I can **edit my bookings** to **update my preferences regarding the day/time/court/opponents**.
| &check; | As a **user/staff** I can **see the list of all bookings (staff)/my own bookings (current user)** so that I can **be reminded of my reservations, but also to be able to update them or delete them**.
| &check; | As a **user** I can **be visually attracted to the app and see the main site features on the moving carousel** so that I can **quickly get an idea what the app offers**.
| &check; | As a **user I want to be informed about different user actions** so that I can **be sure that the itended action took place**.
| &check; | As a **user** I can **view the contact us page** so that I can **get in touch with the club by filling in a contact form and also see the clubs location and opening hours**.
| &check; | As a **user** I can **not add a picture to my buddy profile** so that I can **protect my privacy**.
| &check; | As a **signed in user** I can **search among the buddies** so that I can **find the best partnert to play with**.
| &check; | As a **user** I can **enjoy browsing the webpage while looking for information** so that **I don't feel compelled to leave**.
| &check; | As a **user** I can **easily see which courts are available for booking in a calendar** so that I **don't have to randomly look for free date/time/court combinations**.
| &check; | As a **signed in user** I can **easily see which courts are free on a given day** so that I **don't have to keep guessing a combination of court/time/date which would be free**.
| &check; | As a **user** I want to **press a cancel button which will take me to the previous page** so that I **don't have to use the Back button**.
| &check; | As a **user** I can **easily understand what the table lables mean** so that I can **avoid any unnecessary confusion**.
| &check; | As a **user** I **can clearly see that I made a booking in the past** so that I can **be made aware of the fact**.
| &check; | As a **site owner** I want **the user to provide their phone number in valid format** so that I can **contact them if necessary**.
| &check; | As a **site owner** I can **restrict the number of bookings per user per day** so that all players **get a chance to book a court**.
| &check; | As a **site owner** I can **make sure that the user enters valid information** so that **they can be contacted in time of need**.

[Back to top](#testing)

### Manual Testing

In addition to tests stated above I have performed a series of manual tests. Below is a list of tests that have been conducted. These test are in addition to checking against acceptance criteria of each user story and fulfilling all of the relevant tasks.

| Status | **Main Website - User Logged Out**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page is restricted to a particular user (delete own booking e.g.) loads a forbidden page
| &check; | Clicking the nav logo loads the home page
| &check; | Clicking the Home button on the nav bar loads the home page
| &check; | Clicking the Find the Perfect Buddy button on the nav bar shows buddy catalogue
| &check; | Clicking the Booking button on the nav bar takes the user to booking calendar page
| &check; | Clicking the Contact Us button on the nav bar lists takes the user to the contact us page
| &check; | Clicking the Log In / Sign Up loads the sign in/sign up page
| &check; | In the Buddies catalogue, if the user clicks on a buddy card, no details are shown
| &check; | A moving carousel with three main images is displayed, with links which take the user to relevant pages.
| &check; | Clicking the Instagram link in the footer area opens Instagram in a new window
| &check; | Clicking the YouTube link in the footer area opens YouTube in a new window
| &check; | Clicking the LinkedInlink in the footer area opens LinkedIN in a new window
| &check; | Clicking the Twitter link in the footer area opens Twitter in a new window
| &check; | Clicking the Home, Find a Buddy, Booking, Contact us in the footer, takes the user to the respective pages
| &check; | Clicking the Serve, Grand strokes, Volleys, Strategy takes the user to sites with information about respective topics. The site opens in a new
| &check; | Clicking the envelope opens an app to send an email.

| Status | **Main Website - User Logged In**
|:-------:|:--------|
| &check; | Typing in a incorrect URL on the page loads the 404 error page
| &check; | Pasting page that checks object ownership loads a forbidden page
| &check; | When clicking on Find the Perfect Buddy icon, a search field appears on the right.
| &check; | The user can search for level, game type, availability, practice type and gender. If looking for a different keyword, the user is informed to change the search.
| &check; | When clicking on a cell in booking calendar which says free, the user can add a booking if they had filled in their contact details before. If not, they are first taken to fill in their contact details.
| &check; | A Profile Icon appears for a signed in user on the right next to the Logout button.
| &check; | A Profile Icon lets the user access their Contact Info, Buddy Profile and their bookings.
| &check; | The user can add/edit/delete their booking.
| &check; | The user can add/edit/delete their contact information.
| &check; | The user can add/edit/delete their buddy information.
| &check; | The user with filled in contact info, can see their bookings under "Your Bookings" under Profile Icon.
| &check; | The user is informed by a message appearing at the top of the screen about each add/edit/delete action.
| &check; | The user is asked to confirm deletion of booking, contact info or buddy details.
| &check; | If the user deletes their contact info (user profile), their buddy information and bookings are deleted as well.
| &check; | The user can click a Cancel button if they decide not to edit/delete their booking/contact info or buddy details. They are taken back to the previous page.

| Status | **Main Website - Admin Logged In**
|:-------:|:--------|
| &check; | When a staff member/superuser logs in, a Staff button appears which leads to a list of all bookings made by all members.
| &check; | A staff member can edit/delete anybody's booking. If they delete their own booking, they are taken to bookings/own, if they delete someone else's booking, they are taken to bookings/all.
|  | When a bookings/all is displayed, Staff button is highlighted. However, this button is highlighted also, when the admin user goes to "Your booking". This is a bug and has been documented above.

 Status | **Create A Booking - User Logged In and has a User Profile**
|:-------:|:--------|
| &check; | All elements are required.
| &check; | When user approaches add booking from booking calendar, date, time and court are prefilled.
| &check; | User can choose max 3 opponents.
| &check; | If user makes a booking in the past, they get a warning message.
| &check; | User can make maximum one booking per day.

Status | **Create A User Profile - User Logged Out**
|:-------:|:--------|
| &check; | First name is required and has to contain must not contain numbers or special characters outside of the commonly used characters.
| &check; | Last name is required and has to contain must not contain numbers or special characters outside of the commonly used characters.
| &check; | Phone number is required and is validated to be provided in the following format: +353xxxxxxxxx.

Status | **Create A Buddy Detail Form - User Logged In and has a User Profile**
|:-------:|:--------|
| &check; | All fields in the form are required, only in case of the picture, of the user does not provide an image, a placeholder picture is used.

Status | **Create A Contact Form - User Logged In and has a User Profile**
|:-------:|:--------|
| &check; | First name is required and has to contain must not contain numbers or special characters outside of the commonly used characters.
| &check; | Last name is required and has to contain must not contain numbers or special characters outside of the commonly used characters.
| &check; | Email is required and must contain "@" and some characters before and after the sign.
| &check; | When the user fills in correct information, a message appears that the Inquiry was sent successfully. At the moment, a message appears in the CLI in developement mode, as email functionality is not yet set up.

[Back to top](#testing)
