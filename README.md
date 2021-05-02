# Lottocracy Playground

A Lottocracy scratchpad and playground

## Introduction

Hello all of you lovely people! I'm starting a thing, and rushing into it without giving it really too much thought.
It's a special thing though, and it's designed so that you don't really need to know much about it in order to
participate. It's called a Lottocracy (or a Sortition), and it's a form of governance. The idea is to randomly select
people from a population and have them act, in official capacity, as representatives for the entire population. The
underlying thought is that those who are randomly selected will want to make decisions that are best for the whole
group, since next time they probably won't be making the decision. It's a cooperative game where everybody contributes
(this is famously [the key](https://en.wikipedia.org/wiki/Shapley_value) where cooperative games fall apart).

I want to experiment with this in the same way that I was introduced to Democracy as a kid -- through games and
play-pretend that has stakes as high or as low as my friends and I want to go. So the goal is to understand
Lottocracies. That seems like a thing that I could use a Lottocracy for...

The game of a "Lottocracy for understanding Lottocracies" will start with these very arbitrary rules:

1) Create a Facebook group dedicated solely to this game. It's open to the public; the more the merrier; there are no
   rules except to play in good faith.
2) I'd create a super simple open-source tool that would serve to administer the Lottocracy. This has two motivations:
    1) Capture the history of how the Lottocracy evolves. A system is defined by how it works and it's underlying
       ideology. The social part of the Lottocracy will start off being administered mostly by Facebook (that's kinda
       scary). The administration portion (how we actually get things done) will be captured by this app.
    2) Good games are played more than once. Let's make that easy ;-)

   To start, the app would just have functionality to group people.
3) The first grouping would be our Deliberation Day groups. We'd ask everyone participating in the Lottocracy to group
   up randomly and hop on a video call for an hour to just talk.
4) The second grouping would be the people in power. They could change these rules any way they see fit. They have full
   control over the app and Facebook groups. They could add checks & balances, they could change direction of the group
   by deciding it has a new purpose, they could create more Lottocracies to solve more complicated problems, they could
   choose to disband the group entirely! Who knows, the idea is to play it out and see how it goes.

What do y'all think? Wanna play a game?

## Getting Started With The App

Ok, so this gets a bit into the hairy details of software development. Eventually, we might want to move this to a legit
phone app and go through the App Review process with Facebook, but that entry bar is too high for this at the moment. So
here's what you do:

### Windows Installation

Linux users can figure out their own commands...

Launch the Command Prompt program by going to the search bar at the bottom left, and putting in `cmd` and pressing
enter. Then copy and paste (right click in the command prompt) the commands below to download this source code, so you
and run the app.

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
lottocracy -h
```

When you press enter after the last command, you should see:
```
Lottocracy playground

    Usage:
        lottocracy [options] <command> [<args>...]

    Commands:
        facebook      Manage your lottocracy in a Facebook group

    Options:
        -h --help     Show this screen.
        --version     Show version.
```

You can also get the help info for subcommands:
```
lottocracy facebook -h
Lottocracy Facebook playground

    Usage:
        lottocracy facebook <access_token>
        lottocracy facebook <access_token> batch [<answers>...]

    Options:
        -h --help     Show this screen.
        --version     Show version.
```

When you run the Facebook command, it requires a debugger access_token. This is something that's normally returned to 
an app through the login process. For now, we're developing and figuring out how this should look, so you need to learn
how to use the Facebook developer tools, which unfortunately requires some expertise and your willing consent to give 
access to the app. Therefore, I won't put those instructions here until things are more settled.

# Usage
The app is designed as a workflow. It'll ask you questions about what you want to do, and help you do it. If the app 
can't help you administer the Lottocracy in the way that's agreed upon by the group in power, it should be updated!

Here's the original use case of running a lottery on Facebook groups (with my personal info removed)
```
lottocracy facebook somereallyreallylongsetofcharactersthatmakesupmydevelopmentaccesskey
? What do you want to do?
  1) Run Lottery On Facebook Group
  Answer: 1
<I press enter and the screen updates>
? What do you want to do?  Run Lottery On Facebook Group
? Which group should the lottery be run on?  (Use arrow keys)
 ❯ Lottocracy: The Social Experiment - Test Group
   Washington Hikers and Climbers
   Bioluminescence Experience: PNW
   Seattle Trans & Nonbinary Community
<I use the up and down arrows to select the group>
? What do you want to do?  Run Lottery On Facebook Group
? Which group should the lottery be run on?  Lottocracy: The Social Experiment - Test Group
Found 1 members
? What is the maximum group size that should be used? 5
[{'name': 'Samantha', 'id': '<numbers>'}]
<It displays lists of people who have been randomly assigned to groups...
 I'm the only one right now, so it's kinda lonely>
```
From here, we could add all sorts of new features. Maybe it creates Facebook events for each group? Maybe it creates a 
post to the group with the info? Maybe it messages people to see if they can commit this week? ¯\_(ツ)_/¯