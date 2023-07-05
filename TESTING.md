# Testing

## Code Validation

The [Tennis Buddies](https://tennis-buddies.herokuapp.com/) webpage was thouroughly tested. HTML code was reviewed in the [W3C HTML Validator](https://validator.w3.org). The CSS code was validated in the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the JS file was check in [JS Hint](https://jshint.com/). Python files were tested in [Python Linter](https://pep8ci.herokuapp.com/#).  

<!-- All errors were corrected and HTML, JS and CSS files currently have no errors. -->
### HTML Testing
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
| Buddy Details | [Buddy Details Validation](./testing-images/buddy_details_html_no_errors.png)  |
| Edit Buddy | [Edit Buddy Validation](./testing-images/edit_buddy_html_no_errors.png) |
| Delete Buddy | [Delete Buddy Validation](./testing-images/delete_buddy_html_no_errors.png) |
| Sign In | [Sign In Validation](./testing-images/sign_in_html_no_errors.png) |
| Sign Up | [Sign Up Validation](./testing-images/sign_up_html_no_errors.png) |
| Sign Out | [Sign Out Validation](./testing-images/sign_out_html_no_errors.png) |
| 404 Error Page |[404 Error Page Validation](./testing-images/404_html_no_errors.png)
| 403 Error Page | [403 Error Page Validation]() | [403 Page Errors](./testing-images/403_page_errors.png) | [f0a1efc](https://github.com/lucia2007/tennis_buddies/commit/f0a1efca45e32d496e99c98b589809b23a7ae347)

I could not check the source for 500 Error page, because when I tried to look at the source code in devtools, I had to Confirm Form Resubmission and thus my html code no longer applied.


## Browser Compatibility
## Responsiveness Test
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

## Unfixed Bugs

Bug: The Staff link is highlighted also when the user is on bookings/list/own, even though it should be highlighted only when the staff user is on bookings/list/all.

There is a bug in the browser console: 
[Browser error](/testing-images/browser_error.png)

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


### User Stories Testing