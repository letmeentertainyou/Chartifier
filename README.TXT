Chartifier v0.3.2

Randomly generates a chord chart and strum pattern for you to play.

Chartifier is heavily inspired by www.michaelfogleman.com/phrases/ which is an incredible writing 
tool I love to use when writing songs. However, sometimes I want some musical inspiration as well. 
So I made a random chord chart generator complete with random strum patterns too. 

I started with the strum patterns and in fact the math for random strum patterns is much more intense 
than the math for random chords but I consider rhythm and harmony equally important to the generation
of random music.

Chartifier.html generates a new random chord chart every time you load it. I am planning on adding
some nice features to the UI like radio buttons to select what key you want.

There are aspects of this project that are pretty data heavy and have been originally written in python
so I am keeping a copy of the python source in the github repo, but all you need to run Chartifier locally
is Chartifier.html and the js folder.


LICENSE

This project is licensed under MIT to match the license of https://github.com/oittaa/random-browser-js\
which is the lovely script that enables Chartifier to exist. I personally prefer a more copyleft style license 
like GPL, but I am happy to share this project under MIT so that other cool music projects can be created.

The work I have already done for rhythm and harmony generation should be enough to help a lot of other music
generation projects get off the ground. If for instance you wanted to write a midi program to play these rhythms 
or chords, this code gets you 90% of the way there. So please enjoy using the Chartifier code in any projects 
you are inspired to create! 


TESTING

I'm not writing any tests at the moment because I don't have a need to test anything.
I will make sure to document major changes to the harmony algorithms so that if you prefer an
older version of Chartifier they will be available.