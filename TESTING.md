# Testing

## Code Validation

The [Tennis Buddies](https://tennis-buddies.herokuapp.com/) webpage was thouroughly tested. HTML code was reviewed in the [W3C HTML Validator](https://validator.w3.org). The CSS code was validated in the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) and the JS file was check in [JS Hint](https://jshint.com/). Python..........  All errors were corrected and HTML, JS and CSS files currently have no errors.

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

## Unfixed Bugs

## Additional Testing
### Lighthouse

The application was also tested using [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) in Chrome Developer Tools. The following aspects were tested:

- Performance - reveals how the site performs during loading
- Accessibility - shows if the site if accessible for all users and suggests ways to improve it
- Best Practices - indicates if the site conforms to industry best practices
- SEO - Search Engine Optimisation - shows if the site is optimised for search engine result rankings

### Results from Lighthouse

### User Stories Testing