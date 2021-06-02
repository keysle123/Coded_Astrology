import random
ZODIAC ="Your constellation is"
#Constant to create print statement which Zodiac Sign is found

#Generated list for random trait according to zodiac sign
aries = ['Adventuerous and energetic', 'Pioneering and courageous', 'Enthusiastic and confident',
             'Dynamic and quick-witted', 'Selfish and quick-tempered', 'Impulsive and impatient', 'Foolhardy and daredevil']
taurus =['Patient and reliable', 'Warmhearted and loving', 'Persistent and determined', 'Placid and security loving',
         'Jealous and possessive', 'Resentful and inflexible', 'Self-Indulgent and greedy']

gemini = ['Adaptable and versatile', 'Communicative and witty', 'Intellectual and eloquent', 'Youthful and lively',
          'Nervous and tense', 'Superficial and inconsistent', 'Cunning and inquisitive']
cancer = ['Emotional and loving', 'Intuitive and imaginative', 'Shrewd and cautious', 'Protective and sympathetic',
          'Changeable and moody', 'Overemotional and touchy', 'Clinging and unable to let go']
leo = ['Generous and warmhearted', 'Creative and enthusisatic', 'Broad-minded and expansive', 'Faithful and loving',
       'Pompous and patronizing', 'FABULOUS and AMAZING!', 'Bossy and interfering', 'Dogmatic and intolerant',
       'LIFE OF THE PARTY!', 'BEST DRESSED AND DRESSED TO IMPRESS!']

virgo = ['Modest and shy', 'Meticulous and reliable', 'Practical and diligent', 'Intelligent and analytical',
         'Fussy and a worried', 'Overcritical and harsh', 'Perfectionist and conservative']
libra = ['Diplomatic and urbane', 'Romantic and charming', 'Easygoing and sociable', 'Idealistic and peaceable',
         'Indecisive and changeable', 'Gullible and easily influenced', 'Flirtatious and self-indulgent']

scorpio = ['Determined and forceful', 'Emotional and intuitive', 'Powerful and passionate', 'Exciting and magnetic',
           'Jealous and resentful', 'Compulsive and obsessive', 'Secretive and obstinate']

sagittarius = ['Optimistic and freedom-loving', 'Jovial and good-humored', 'Honest and straightforward',
               'Intellectual and philosophical', 'Blindly optimistic and careless', 'Irresponsible and superficial',
               'Tactless and restless']
capricorn = ['Practical and prudent', 'Ambitious and disciplined', 'Patient and careful', 'Humorous and reserved',
             'Pessimistic and fatalistic', 'Miserly and grudging']

aquarius = ['Friendly and humanitarian', 'Honest and loyal', 'Original and inventive', 'Independent and intellectual',
            'Intractable and contrary', 'Perverse and unpredictable', 'Unemotional and detached']

pisces = ['Imaginative and sensitive', 'Compassionate and kind', 'Selfless and unworldly', 'Intuitive and sympathetic',
          'Escapist and idealistic', 'Secretive and vague', 'Weak-willed and easily led']

def main():
    zodiac()



def zodiac():
    print("Astrology is the study of patterns and relationships - planets in motion and our birth chart. \nLet's find your astrological sign, constellation, and traits!")
    while True:
        try:
            day = int(input("Input birthday (e.g. 1 - 31): "))
            month = input("Input month of birth (e.g. march, july etc): ")
            #.lower() lets the user write the zodiac sign in multiple ways
        except ValueError:
            #when a user doesn't enter a valid entry it will return this statment
            print("Sorry, that is an invalid entry. \nEnter a numeric value for day. \nSpell out the your birth month.")
            #try again and return to start of the loop
            continue
        else:
            #we'e ready to exit the loop.
            break
    #user input will categorize them by months and use int of dates to store in variable astro_sign
    if month.lower() == 'december':
	    astro_sign = 'Sagittarius' if (day < 22) else 'Capricorn'
    elif month.lower() == 'january':
	    astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month.lower() == 'february':
	    astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month.lower() == 'march':
	    astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month.lower() == 'april':
	    astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month.lower() == 'may':
	    astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month.lower() == 'june':
	    astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month.lower() == 'july':
	    astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month.lower() == 'august':
	    astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month.lower() == 'september':
	    astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month.lower() == 'october':
	    astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month.lower() == 'november':
	    astro_sign = 'scorpio' if (day < 22) else 'Sagittarius'
    print("Your Astrological sign is :", astro_sign)

#choice function allows to random generate for a list
    if astro_sign == "Sagittarius":
        print(ZODIAC + ' the Archer')
        print('Traits:', random.choice(sagittarius))
    elif astro_sign == 'Capricorn':
        print(ZODIAC + ' the Goat')
        print('Traits:', random.choice(capricorn))
    elif astro_sign == 'Aquarius':
        print(ZODIAC + ' the Water Carrier')
        print('Traits:', random.choice(aquarius))
    elif astro_sign == 'Pisces':
        print(ZODIAC + ' the Fish')
        print('Traits:', random.choice(pisces))
    elif astro_sign == 'Aries':
        print(ZODIAC + ' the Ram')
        print('Traits:', random.choice(aries))
    elif astro_sign == 'Taurus':
        print(ZODIAC + ' the Bull')
        print('Traits:', random.choice(taurus))
    elif astro_sign == 'Gemini':
        print(ZODIAC + ' the Twins')
        print('Traits:', random.choice(gemini))
    elif astro_sign == 'Cancer':
        print(ZODIAC + ' The Crab')
        print('Traits:', random.choice(cancer))
    elif astro_sign == 'Leo':
        print(ZODIAC + ' the Lion')
        print('Traits:', random.choice(leo))
    elif astro_sign == 'Virgo':
        print(ZODIAC + ' the Maiden')
        print('Traits:', random.choice(virgo))
    elif astro_sign == 'Libra':
        print(ZODIAC + ' the Scales')
        print('Traits:', random.choice(libra))
    elif astro_sign == 'Scorpio':
        print(ZODIAC + ' the Scorpion')
        print('Traits:', random.choice(scorpio))






if __name__ == '__main__':
    main()