# facebook-posts-retriever
This code is to show how you can group posts from your timeline and write it to a word file. More in "Readme.md" file

Download your Posts activity from Facebook:

1.	Login to your Facebook account on a browser.
2.	Click on the ‘Drop down arrow’ at the top right corner.
3.	Click on “Settings and Privacy” and navigate to “Settings”.
4.	Select “Your Facebook Information” and then on the right-side menu, select “Download your information”.
5.	After step 4, you will be taken to a menu. Select “Format” as Json which was HTML as default.
6.	Then straight to the “Your Information” menu, there is an option “Deselect all”
7.	After deselecting, apply “tick” mark to the first option that is “Posts”.
8.	Then “Create File”.
File creation will start and after some time you will be notified that the file generation is complete.
9.	Now, click on that notification or follow steps 2 to 4 if you are not on the same menu after step 8. Select “Available Files” and download your file. Downloading file requires Password!
Extract the zip file to a folder and store the Json file in posts and the code file in the same folder to avoid complexity in code.

Installing required python packages:
pip install python-docx
pip install translate
pip install DateTime
pip install jsonlib

Fuctionalities:
1. Read data from json data file.
2. Convert the latin unicoded string to original text. (In case you have written your posts in other languages)
3. Write to a word file.
