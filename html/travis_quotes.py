#!/usr/bin/python

from random import choice

quote_list = [
  "it's really tiring watching people play tennis.",
  "oh! this is stuff we're supposed to have done already.",
  "everything i do is that self-explanatory",
  "i don't deliver on most of my promises when it comes to timeline",
  "it's really hard to motivate people around test plans",
  "this may be one of those things i shouldn't say",
  "i haven't been here long enough to be bitter",
  "it's ok for us to miss bugs",
  "i love lucy is some the purest americana we have",
  "i have this problem where i lose track of time when i get in front of people",
  "there are two sides of this. there's the cynic side... let's call it the inga side",
  "we want to be the voice of caution and paranoia",
  "i don't even like babies",
  "you don't just let the jaguar sit in the driveway and take the honda out",
  "i mean not good but... good",
  "let's not start rumors. or if we do let's blame them on brandon.",
  "then we can sue cisco which I've always wanted to do",
  "jax unplugged some customer service headphones but fortunately they still think he's fluffy and awesome.",
  "i've been having this problem lately where i'm saying things and i don't know i'm saying them",
  "there are probably errors there, but they haven't been uncovered because we're not that high-functioning",
  "i've been here for 3 months without making fun of anyone's name. time to start.",
  "that was probably one of those inappropriate comments",
  "someday they'll be sentient and take over the world, but not yet",
  "i manage upward like flesh-eating bacteria",
  "the tamagachi is your friend",
  "the bar is not very high so don't worry about it",
  "odds are wee are a little under-handed. i mean short-handed.",
  "you seem like you want to say something. you want me to shut up.",
  "we've got jim somebody coming in maybe",
  "i wanna know why you don't like me",
  "we're QA so we stick with our teams! kinda like those birds that follow the water buffalo",
  "i lack the interpersonal skills to convince people they're going to be happy where they're sitting",
  "my brain is only capable of having 6 people on my team",
  "ok we talked about burning man. that was definitely one of my agenda items.",
  "you don't care. well, you care like you care about people in a distant land having problems with their computers.",
  "i don't know all your names.",
  "i dunno if they're gonna be as cool as i am. i doubt it."
  ]

print "Content-type: text/html\n\n";
print "<html>"
print "<head>"
print "<style>a{text-decoration:none;}</style>"
print "<style type=\"text/css\">"
print "html, body   { height: 100%; margin: 0; padding: 0; text-align: center; }"
print "div#centered { border: 0; height: 50%; width: 50%; position: absolute; left: 25%; top: 25%;}"
print "</style>"
print "</head>"
print "<body>"
print "<div id=\"centered\"><p id=\"content\"><a href=\"travis_quotes.py\"><font style=\"font-size: 42pt;\">" + choice(quote_list) + "</font></a><br>click for another one.</p></span>"

print "</body>"
print "</html>"








