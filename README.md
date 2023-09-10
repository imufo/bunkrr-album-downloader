# bunkrr-album-downloader
This is a simple app written in python with python libraries to download a bunkrr album.
---------------------------------------------------------------------------[overview]---------------------------------------------------------------------------
This is a python app for downloading all images inside a bunkrr album.
This version is just a prototype and only works for bunkrr album links with top level domain .su

-------------------------------------------------------------------------[requirements]------------------------------------------------------------------------
Interpreter: python3.7 or above

required python libraries:
              [requests, beautifulsoup4, urllib3, tqdm]
              If one of above was not installed yet you can install it white pip
              Ex: pip install requests
              You can also install them using [pip install -r requirements.txt] in the same directory which requirements.txt exists,
               this will install exactly versions which I have used (It would be best using a virtual environment)

-------------------------------------------------------------------------[how to use]---------------------------------------------------------------------------
After that you were satisfied and installed requirements just run the script with python interpreter.
prompt will ask you for the album link, copy and paste album link
Ex:
> Enter gallery URL: https://bunkrr.su/a/0vkji0xx
Then number of images will be enumerated and announced to you and will ask you if you want to continue.
just pres Enter or if you want to quit pres [Ctrl + C] to break

Ex:
> Almost 1839 files will be downloaded!
> Wanna continue?


![Image](https://user-images.githubusercontent.com/60540316/266840008-dfa6d23f-468e-447f-951c-da4ca6947282.png)

You will have two progress bar:
First one for all images and second one for each individual image.
Files will be saved in [downloaded_images] directory in the current folder as running program, if it didn't exits program will make it.
After all images were downloaded program will finish and quit.



![Image](https://user-images.githubusercontent.com/60540316/266841006-5924726e-f8c2-4069-953c-ed9e46410eb8.png)


-------------------------------------------------------------------------[considerations]------------------------------------------------------------------------
First of all this will only work for bunkrr.su albums.
Second, due to fast changing of bunkrr.su web site it is possible that it doesn't work properly.
Until the writing date of this readme [2023-9-10] works fine.
and last but not the least, I am new to this kind of programs. I will continue to develop and maintain this program and more features will be added with more abilities.

Thank you for Reading :)
