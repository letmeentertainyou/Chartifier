Chartifier v0.3.1

Randomly generates a chord chart and strum pattern for you to play.

Chartifier is heavily inspired by www.michaelfogleman.com/phrases/ which is an incredible writing 
tool I love to use when writing songs. However, sometimes I want some musical inspiration as well. 
So I made a Random Chord Chart Generator complete with random strum patterns too. The strum patterns 
are not displayed on html page yet but all of the tricky math is implemented.

Chartifier.html generates a new random chord chart every time you load it. v0.1.0 is basically a 
demo site, I will polish the html/css as I go forward. Right now it's just the 12 bar blues in a 
random key but I'm going to expand the random harmony algorithms after launch.

(Now Chartifier generates random chords)

Starting with v0.2.0 I will be backing up old versions of the chord algorithms so that any users
who prefer the chords of an older version can use it. The backups won't show up until version 0.3.0
ships to github.

***

I'm also going to add some radio buttons so users can select any key they want, as well as rhythmic
choices, and a 'New Chords' button. I will also add a way to save chord charts you like (maybe as a pdf?).

Since this project is pretty data heavy I will be modeling my algorithms in python first and then converting
all the sick python builtins into js as I go. I'm compiling tools like xrange and deepCopy in js/tools.js feel
free to grab any of them for other projects. The tools that are stolen from the internet are clearly marked. 


LICENSE

    I had to write a custom permutations algorithm, so now the only borrowed code is random.js so I will double check what license that user, and then pick a compatible license for this project.


TESTING

    I'm not writing any tests at the moment because I don't have a need to test anything.
    I will make sure to document major changes to the algorithms so that if you prefer an
    older version of Chartifier they will be available.