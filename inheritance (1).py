#!/usr/bin/env python
# coding: utf-8

# In[3]:


class country:
    def info(self):
        x=["INDIA","RUSSIA","USA"]
        for k in x:
            print(k)

class india(country):
    def state(self):
        y=["Rajasthan","Delhi","punjab"]
        for k in y:
            print(k)
    
    def rajasthan(self):
        print("\nRajasthan")
        print('''Rajasthan is a state in northern India. It covers 342,239 square kilometres or 10.4 percent of India's total geographical area. It is the largest Indian state by area and the seventh largest by population.''')
    def delhi(self):
        print("\nDelhi")
        print('''Delhi, India’s capital territory, is a massive metropolitan area in the country’s north. In Old Delhi, a neighborhood dating to the 1600s, stands the imposing Mughal-era Red Fort, a symbol of India, and the sprawling Jama Masjid mosque, whose courtyard accommodates 25,000 people. Nearby is Chandni Chowk, a vibrant bazaar filled with food carts, sweets shops and spice stalls''')
    def punjab(self):
        print("\nPunjab")
        print('''Punjab, a state bordering Pakistan, is the heart of India’s Sikh community. The city of Amritsar, founded in the 1570s by Sikh Guru Ram Das, is the site of Harmandir Sahib, the holiest gurdwara (Sikh place of worship). Known in English as the Golden Temple, and surrounded by the Pool of Nectar, it's a major pilgrimage site. Also in Amritsar is Durgiana Temple, a Hindu shrine famed for its engraved silver doors''')

class russia(country):
    def state1(self):
        y=["moscow","saint_petersburg"]
        for k in y:
            print(k)
    def moscow(self):
        print("\nMoscow")
        print('''Moscow, on the Moskva River in western Russia, is the nation’s cosmopolitan capital. In its historic core is the Kremlin, a complex that’s home to the president and tsarist treasures in the Armoury. Outside its walls is Red Square, Russia's symbolic center. It's home to Lenin’s Mausoleum, the State Historical Museum's comprehensive collection and St. Basil’s Cathedral, known for its colorful, onion-shaped domes.''')
    def saint_petersburg(self):
        print("\nsaint_petersburg")
        print('''Saint Petersburg received over 15 million tourists in 2018. It is considered an important economic, scientific, and tourism centre of Russia and Europe. In modern times, the city has the nickname of being "the Northern Capital of Russia" and is home to notable federal government bodies such as the Constitutional Court of Russia and the Heraldic Council of the President of the Russian Federation.''')
        
class USA(russia):
    def state2(self):
        y=["california","texus","florida"]
        for k in y:
            print(k)
    def california(self):
        print("\ncalifornia")
        print('''California, a western U.S. state, stretches from the Mexican border along the Pacific for nearly 900 miles. Its terrain includes cliff-lined beaches, redwood forest, the Sierra Nevada Mountains, Central Valley farmland and the Mojave Desert. The city of Los Angeles is the seat of the Hollywood entertainment industry. Hilly San Francisco is known for the Golden Gate Bridge, Alcatraz Island and cable cars.''')
    def texus(self):
        print("\ntaxus")
        print('''Texas is a state in the South Central region of the United States. At 268,596 square miles, and with more than 30 million residents in 2023, it is the second-largest U.S. state by both area and population''')
    def florida(self):
        print("\nflorida")
        print('''Florida is the southeasternmost U.S. state, with the Atlantic on one side and the Gulf of Mexico on the other. It has hundreds of miles of beaches. The city of Miami is known for its Latin-American cultural influences and notable arts scene, as well as its nightlife, especially in upscale South Beach. Orlando is famed for theme parks, including Walt Disney World. ''')
    


# In[4]:


obj.info()


# In[5]:


x=input("enter the country name:-")
if x=="india":
    obj=india()
    obj.state()
    obj.rajasthan()
    obj.delhi()
    obj.punjab()
elif x=="russia":
    obj=russia()
    obj.state1()
    obj.moscow()
    obj.saint_petersburg()
elif x=="USA":
    obj=USA()
    obj.state2()
    obj.california()
    obj.texus()
    obj.florida()
else:
    print("wrong option")


# In[52]:


x=input("enter the country name:-")
if x=="india":
    obj=india()
    obj.rajasthan()
    obj.delhi()
    obj.punjab()
elif x=="russia":
    obj=russia()
    obj.moscow()
    obj.saint_petersburg()
elif x=="USA":
    obj=USA()
    obj.california()
    obj.texus()
    obj.florida()
else:
    print("wrong option")


# In[ ]:




