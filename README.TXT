Chartifier v0.9.9

Randomly generates a chord chart and strum pattern for you to play.

Chartifier is heavily inspired by https://www.michaelfogleman.com/phrases/ which is an incredible
writing tool that I love to use when writing songs. However, sometimes I want some musical inspiration 
as well. So I made a random chord chart generator complete with random strum patterns too. 

I started with the strum patterns and in fact the math for strum patterns is much more intense than the
math for chords but I consider rhythm and harmony equally important to the generation of random charts.

Chartifier generates a new random chord chart in a random key every time you refresh the page or click New Chords.
There are also dropdown menus that allow you to select a mode and a key (you need to select both) and then the
New Chords button will use your chosen key. You can also choose a number of eighth notes for the generated strum 
pattern (this is called "count" and has it's own dropdown menu).

This is my first time working on a web app and I don't yet have a place to host Chartifier. If you've
read this far and you'd like to try using Chartifier it's extremely simple to run on any computer with
a web browser.

All you need to do is download the dist/ directory and place it anywhere on your pc. 
Then you right click on Chartifier.html and choose open in web browser. 
You can even bookmark Chartifier.html so it's easier to return to.

Chartifier is really simple and does not need an internet connection to run. It can be used in a fully 
offline sandbox or in private browsing. There is no data collection, or phoning home. Just pure, fun, 
javascript functions.

The total size of the Chartifier v0.7.5 src directory is 27.3 kB, and the dist directory is 13.6 kB. 
While I do expect this project to grow a bit, it will never use cookies, 
communicate with a server, or do anything remotely sketchy with your CPU cycles. This is a webapp meant for 
a more nostalgic time when the web was neat!

The only code I didn't personally write is random.js from https://github.com/oittaa/random-browser-js/
and is licensed under MIT. The random.js module defines a couple handy functions, and does not communicate
with the outside world. It's a really nice addition to the project.

Along with the src directory you can find a screenshots directory that aims to show what Chartifier.html
renders into. This will also eventually document different versions of the algorithm for historical purposes.

This project was originally written in python, and a current documented version of the python code is in the
python directory. That source code might be of particular interest to musicians/programmers who are the most
likely people to have read this far. 

I have written a neat/fast algorithm to find a large amount of rhythmic variations which seem simple but can
be implemented in as many complex ways as the musician desires. You could even generate multiple rhythms, and
overlay them, or you could subdivide them in interesting ways. This project exists to inspire creativity, and
not to limit it!


LICENSE

Chartifier is licensed under MIT to match the license of https://github.com/oittaa/random-browser-js/
which is the lovely script that enables Chartifier to exist. I personally prefer a more copyleft style license 
like GPL, but I am happy to share this project under MIT so that other cool music projects can be created.

The work I have already done for rhythm and harmony generation should be enough to help a lot of other music
generation projects get off the ground. If for instance you wanted to write a midi program to play these rhythms 
or chords, this code gets you 90% of the way there. So please enjoy using the Chartifier code in any projects 
you are inspired to create! 


TESTING

I'm not writing any tests at the moment because I don't have a need to test anything.
I will make sure to document major changes to the harmony algorithms so that if you prefer an
older version of Chartifier It will be available.
