Chartifier v0.1.0

Randomly generates a chord chart and strum pattern for you to play.

Chartifier is heavily inspired by www.michaelfogleman.com/phrases/ which is an incredible writing 
tool I love to use when writing songs. However, sometimes I want some musical inspiration as well. 
So I made a Random Chord Chart Generator complete with random strum patterns too. The strum patterns 
are not displayed on html page yet but all of the tricky math is implemented.

Chartifier.html generates a new random chord chart every time you load it. v0.1.0 is basically a 
demo site, I will polish the html/css as I go forward. Right now it's just the 12 bar blues in a 
random key but I'm going to expand the random harmony algorithms after launch.

I'm also going to add some radio buttons so users can select any key they want, as well as rhythmic
choices, and a 'New Chords' button.

I will also add a way to save chord charts you like (maybe as a pdf?). But that feature won't be before
version 0.2.0

Since this project is pretty data heavy I will be modeling my algorithms in python first and then converting
all the sick python builtins into js as I go.


LICENSE

    This project is not licensed because it is mostly stolen code and I'm not going
    to relicense someone else's code. You can use this project in any way you want so 
    long as you also don't distribute/relicense the code. It would be illegal to relicense
    code you do not own.

    I did write 100% of the python so you can do something with that if you want.


TESTING

    I'm not writing any tests at the moment because I don't have a need to test anything.
    I will make sure to document major changes to the algorithms so that if you prefer an
    older version of Chartifier they will be available.