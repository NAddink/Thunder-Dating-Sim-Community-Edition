# WELCOME to Thunder Dating Simulator- Community Edition:
If you're reading this, you've taken interest in *Thunder Dating Simulator*- enough that Noah decided he might actually pursue rebooting the project that was imagined in October 2023.
<br><br>
### Thanks for thinking this extremely wack idea is a cool one. Here is some info about the old project:
- Thunder Dating Simulator is a visual novel type game. That is very dialogue heavy, and played almost exclusively by selecting action/dialogue options.
- TDS is written in *Ren'Py*, a visual novel engine built on the python programming language. It's actually the same engine that Doki Doki Literature Club used.
- Since this is literally named the Community Edition, I am ***very*** open to suggestions, comments, ideas. It's not as if I just coded this, so scrapping and changing things doesn't feel like a loss.

Below is the Dialogue document, also made back when I originally did this stuff. It's very barebones.

[Dialogue Document](https://docs.google.com/document/d/10ckp_Utvbeq8JK4584tTMq91LJHOO5WwZh3Eap90syo/edit?usp=sharing)

Lastly, I may end up making a discord server for TDS-CE, let me know if you guys would be interested in that. 

# Below is more detailed information regarding the original TDS:
There is also a minimal roadmap showing what was accomplished and what would still be missing. So basically just code is there and nothing else. 

# General structure
###### In it's current form (subject to change)

### Premise:
There are 4 thunder 'variants', AKA different actors wearing the thunder costume. 
- Puppy Thunder
- Suave Thunder
- Aggro Thunder
- Flirty Thunder

The game consists of 5 weeks where you pick a location and run into a thunder, where you then have to make dialogue choices in order to secure a date with that thunder. 

The thunders are in costume when you interact with them during normal events. After successfully answering dialogue, and going on the date, the thunder will show up out of costume. Once you reach the date it is revealed which thunder you went on a date with. 

After successfully going on 4/5 date opportunities with one thunder you will reach the success ending (4/5 is a bit arbitrary and may be subject to change)


### Route System:
- Events (5 regular events, 1 final event) and date opportunities are separate
  - Events are where you meet (pick) the Thunder you want to interact with
    - i.e. you meet Aggro Thunder at the Esports lounge
  - The dialogue you choose while in the event with that Thunder will determine whether you have a date opportunity with him following the event
    - There will be 3 chances to successfully complete the event; you must pick at least 2 correct dialogue options in order to secure it
    - If unsuccessful, a default scene will play, in which you return to your dorm.
  - If successful in appealing to that particular Thunder, you will receive a  date opportunity immediately following that event
    - In date opportunities, you can choose between 4 locations to hang out with Thunder at
      - This includes Taco Bell
    - In those scenarios, location will not matter EXCEPT for if you choose Taco Bell. If you consistently choose dialogue options that discuss or interact with the Taco Bell worker, ████, you will unlock the secret ████ route.
  - Dates will end with an affection point for the Thunder you spent it with
    - In other words, if you successfully get the date opportunity with that Thunder after an event, you’re assured gaining affection with that Thunder and the dialogue is mostly flavor text
  - The final event will be a big occasion (a game, pep rally, etc. -undetermined yet)
    - You can choose which final event to go to, but whether or not that event is followed by the good ending for that Thunder is determined by how many successful weeks you’ve achieved with that Thunder
      - i.e. you had 3 completed weeks with AT and 2 completed weeks with PT. If you choose PT’s final event, it concludes with an unsuccessful ending. If you choose AT’s final event, it will conclude in the successful ending because you spent the majority of weeks with him.

### Current Issues:
- Assuming it takes 5 weeks to completely know a Thunder’s backstory and character, what do we do if the player only does 3 weeks of that Thunder, since you only need a minimum of 3 weeks to secure his successful ending?
  - Possible solutions include increasing the minimum number of weeks to land a successful ending to 4
    - To keep it fun, we can change the locations for each event so that players really have to think in order to predict where the Thunder they’re going for is at
    - IDEA: Players can unlock the perfect ending for their Thunder by completing 5 weeks with that specific Thunder and attending his respective final event; this will entail knowing all of Thunder’s backstory and understanding his personality, as well as gaining further closure on his primary conflict
- Being able to find the same thunder for dates following the first one is sort of up to chance, since players *might* be able to guess where their thunder will be, but if they were to guess wrong they would completely miss that date opportunity.
  - Perhaps thunder will say on dates hints of where he will be next week.

# Roadmap: 
### Legend:

✅ Completed
\
🛠️ Partially done
\
⏰ Planned

<hr>


## 👾 Code
- ✅ Basic code structure
- ✅ Week point system
- ⏰ Possible additional features

<hr>


## 💬 Dialogue 
- ⏰ Puppy Thunder dialogue<br>
- ⏰ Suave Thunder dialogue<br>
- ⏰ Aggro Thunder dialogue<br>
- ⏰ Flirty Thunder dialogue<br>

<hr>


## 🎨 Art
- ⏰ Puppy Thunder<br>
  - ⏰ Emote Variants<br>
- ⏰ Suave Thunder<br>
  - ⏰ Emote Variants<br>
- ⏰ Aggro Thunder<br>
  - ⏰ Emote Variants<br>
- ⏰ Flirty Thunder<br>
  - ⏰ Emote Variants<br>
