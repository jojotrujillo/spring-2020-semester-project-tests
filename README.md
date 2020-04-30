# 3900860s2020team1-tests

@jojotrujillo
- ran "change password" tests using WSL (virtualenvs are easier to build)
  - if you choose to do the same, file paths are different, i.e. /mnt/c/users/... /documents/team1-tests
 
  - driver .exe needs to be in venv/bin

- used JSON file to hold variable values

- folder structure of tests mirrors project folder structure
  - in django terms, each app should have it's own tests; we have the account app and the images app
  
  @mpopelka
  For Social Media Authentication, in the interest of privacy, no usernames nor passwords were hard-coded into the tests. 
  To properly use the test scripts, replace the appropriate fields with your information.
    -for example, for the Twitter test, you would replace "Your Twitter Username" with your Twitter username.
  Google has an automated feature that detects and prohibits the use of an automated test to login to a Google account.
  This means that Google rejects Selenium's automation to use a Gmail account to log in.
