#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3
from random import *
# @adjective @race @dclass from @location who @backstory
# adapted from http://whothefuckismydndcharacter.com/


def vowel_check(string):
    capital = False
    if string == '':
        if capital:
            return 'A '
        else:
            return 'a'

    vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
    for char in vowels:
        if string[0] == char:
            if capital:
                return 'An '
            else:
                return 'an'
    if capital:
        return 'A '
    else:
        return 'a'

def backstory_creator():
    adjectives = ['bigoted', 'bitchy', 'blunt', 'boisterous', 'bossy', 'brave', 'callous', 'cautious', 'charming', 'cheerful', 'churlish', 'cold', 'composed', 'conceited', 'condescending', 'confident', 'conscientious', 'cool-headed', 'courageous', 'crabby', 'crass', 'critical', 'cruel', 'cunning', 'curious', 'cynical', 'decisive', 'dependable', 'determined', 'driven', 'fearless', 'flamboyant', 'flirtatious', 'friendly', 'gruff', 'headstrong', 'hot-headed', 'lazy', 'loud', 'Machiavellian', 'moody', 'philosophical', 'pompous', 'pretty chill', 'romantic', 'selfish', 'sensitive', 'tactless', 'thoughtful', 'wary', 'depressed', 'delightful', 'demure', 'diligent', 'disruptive', 'discerning', 'dramatic', 'dutiful', 'frank', 'funny', 'fussy', 'generous', 'gentle', 'gloomy', 'grave', 'grouchy', 'guarded', 'hateful', 'helpful', 'hot-headed', 'hypercritical', 'level-headed', 'mean', 'methodical', 'meticulous', 'miserable', 'motivated', 'morose', 'naive', 'nosy', 'peaceful', 'pensive', 'plain-speaking', 'playful', 'plucky', 'positive', 'proud', 'prejudiced', 'quick-tempered', 'reliable', 'reluctant', 'resentful', 'resourceful', 'respectful', 'restless', 'sassy', 'sentimental', 'short-tempered', 'snobby', 'sombre', 'sophisticated', 'spiteful', 'soulless', 'stern', 'stoic', 'surly', 'sweet', 'suspicious', 'talented', 'warm-hearted', 'wary', 'well-intentioned', 'adventurous', 'agreeable', 'ambitious', 'anxious', 'apathetic', 'argumentative', 'assertive', 'attentive', 'impulsive', 'intolerant', 'inventive', 'overemotional', 'unpredictable', 'eager', 'easy-going', 'egotistical', 'emotional', 'enterprising', 'enthusiastic', 'excitable', 'impatient', 'impetuous', 'inconsiderate', 'insensitive', 'irritable', 'obnoxious', 'old-fashioned', 'outgoing', 'outspoken', 'unbalanced', 'unstable', 'absent minded', 'melodramatic', 'paranoid', 'chipper', 'passive-aggressive', 'amicable', 'broad-minded', 'compassionate', 'considerate', 'diplomatic', 'faithful', 'hard-working', 'modest', "patriotic", "easy-going", "rebellious", "manipulative", "witty", "sarcastic", "rebellious", "humble", "eccentric", "frank"]

    locations = ['a tiny village', 'the smallest mountain in the world', 'the local forests', 'the city sewers', 'the gutter', 'a large family', 'a orphanage workhouse', 'an extremely religious upbringing', 'a mid-level cult', 'a commune', 'the desert', 'an unchartable island', 'a small family farm', 'a taverneless village', 'the slave fighting pits', 'a company of sellswords', 'a mercenary company', 'a nocturnal town', 'a city that never slept', 'a travelling carnival with a freak show', 'an impure bloodline', 'a strict monastery', 'a local street gang', 'a now ruined city', 'a haunted castle', 'a bustling city', 'a highly guarded prison', 'a floating city', 'an underground city', 'a theatre company', "the guard's academy", 'the royal bank', 'a travelling band', 'a fishing village', 'the pirate infested isles', 'a fallen kingdom', 'the inner city slums', 'a mining town', 'a tourist town in the mountains', 'an oasis village', 'the tundra', 'the nice part of a bad town', 'a peaceful coastal town ', 'the wilds', 'a pompous wizard school', 'a string of terrible places to live', 'a laid back beach town', 'a place only they can pronounce', 'an extremist temple', 'a sheltered upbringing', 'a sunken city', 'a tropical paradise', 'a recently erupted volcano village', 'a small town where nothing ever happened', 'a town of Outlaws', 'a war-torn city', 'an isolated monastery ', 'an affluent upbringing', 'a backwater village', 'a small town wizarding school', 'a cliff-side village', 'a quiet woodland hut', 'a small town on the border', 'a broken home', 'a thriving seaport town', 'a small farm in the grasslands', 'the city of lights', 'the City of Ten Thousand Flags', 'a city with towers that rival the clouds', 'the wetlands', 'a destitute plantation', 'an aristocratic family', 'a line of fallen royalty', 'a boarding school', 'the assassins guild', 'a disgraced family of knights', 'the city watch', 'a dysfunctional marriage', 'a poorly run orphanage', 'a bustling city market', 'a secret order of monks', 'the imperial army']

    backstorys = ['hates wearing their glasses', 'finds it impossible to speak to girls', 'has always wanted to open their own tavern', 'has a huge debt to pay back', 'was raised by ghosts', 'suffers from claustrophobia', 'makes inappropriate jokes at the worst times', 'is afraid of heights', "doesn't understand the concept of politeness", 'always alliterates their anecdotes', 'has a bad gambling problem', 'wants everyone to like them', 'never takes their armour off, just in case', 'always wanted to learn magic but struggled with it', 'always needs to be the centre of attention', 'has no other family but the party', "was left out of their father's will", 'is writing an autobiography', 'has a drinking problem', 'is completely colour blind', 'gets nervous speaking in front of crowds', "can't swim", 'is afraid of fire', 'distrusts all authority', 'mistrusts anyone smaller than them', 'hates the monarchy', 'has anger problems', 'always romanticised adventure', "can't read", 'deserted the army', 'always takes first watch', 'constantly watches their back', 'always keeps their promises', 'wants to be famous, no matter what', 'is trying to get out of the adventuring business to settle down', "can't stand the sight of blood", 'secretly became an adventurer to impress a love interest', 'has twenty-seven siblings to provide for', 'has nothing left to lose', "doesn't know their own strength", 'is just trying to get by', 'is trying to avoid a prophecy', "forever picking fights to 'win back honour'", "can't stand silence", 'bangs on about their genealogy to everyone', 'gets easily attached to people', 'insists they are the reincarnation of a legendary warrior', 'adds a notch to their sword every night', 'prefers to fight drunk', 'is searching for a rare fertility herb', 'is a compulsive liar', 'wants to one day own their own ship ', 'is a lookalike of the local monarch', 'is pretty tight fisted with their gold', 'is the only surviving member of their previous adventure party', 'was disowned by their family', 'carries a cryptic treasure map they won in a tavern bet', 'seeks to end a family feud', 'has accepted death as an inevitability', 'has been on the run for over three years', "can't stand children", 'was beaten and imprisoned for their religious beliefs', 'acts shallow but only to hide their insecurities', 'makes all minor decisions by flipping a coin', 'wants to become a famous singer', 'always gives the good news first', 'used to work as a tavern bouncer', 'tries to be a friend to everyone', 'left their home in disgrace', "doesn't understand sarcasm", 'suffers from night terrors', 'has a burning hatred for pirates', 'aims to learn every language in the land', 'owes money to the wrong people', 'was drafted into the army at fourteen', 'loves to haggle', 'suffers from a recurring nightmare', 'came out of retirement for this adventure', 'is dealing with a midlife crisis', 'has delusions of grandeur', 'was born in a different body', 'suffers from vertigo', "carries a charmed locket that they can't open", 'is getting too old for all this', 'ran away at the age of eleven', 'carries the scars of an attempted suicide', 'hates being made to wait', 'seems to think they know everyone', 'was badly burnt by a sorcerer', 'was written out of their family will', 'is planning to retire next year', 'exaggerates everything they talk about', 'is quick to take credit and assign blame', "refuses to admit they're past their prime", 'only has two more years before a demon comes back to claim their soul']

    adjective = adjectives[randint(0, len(adjectives))]
    location = locations[randint(0, len(locations))]
    backstory = backstorys[randint(0, len(backstorys))]

    choice = randint(0,3)
    if choice == 0:
        return("You're", vowel_check(adjective), adjective, "character who comes from", location, "who", backstory)
    elif choice == 1:
        return("Listen here, you", adjective, "son of a bitch, I don't care if you're from", location+',', "saying you're someone who", backstory, "still won't get you in here")
    elif choice == 2:
        return("Have you heard about that", adjective,"fellow? I heard that they're from", location+".", "Even worse, they", backstory+".", "Isn't that interesting?")
    elif choice == 3:
        return("This is your cover story. You're from", location, "and if someone asks you for your history, just say that you", backstory+".", "Always try to get across that you're", adjective+".")



# Listen here, you adjective son of a bitch, I don't care if you're from location, saying you're someone who backstory still won't get you in here
# Have you heard about that adjective fellow? I heard that they're from location, even worse, they backstory. Isn't that strange?
# This is your cover story. You're from location and if someone asks you for your history, just say that you're backstory. Always try to get across that you're adjective.
