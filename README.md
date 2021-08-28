# Recipe, Set, Go! - SYNCSHACK 2021

# Inspiration
Food wastage is becoming an increasingly prevalent issue in a world challenged by depleting resources and malnourished populations. In Australia, 7.3 million tonnes of food is wasted - and households are the biggest contributors (Foodbank, 2021). Comparatively, in 2019, nearly 1 in 10 people in the world were exposed to severe levels of food insecurity (Food and Agriculture Organisation of the United Nations, 2019). Evidently, becoming more mindful of the social impact of food consumption is crucial in our society’s future, particularly in the habits of over-purchasing and over-consumption. As a result, households have a necessary role in reducing their impact on food waste, particularly through making conscious decisions to utilise the food they have already purchased, as opposed to instinctively buy more. It would thus be greatly beneficial if solutions were developed allowing households to best utilise the ingredients present within their home already, to connect them with recipes they are able to create without the necessity of purchasing more food than they already have access to.

# What it does
Our solution is a website where the user can input a list of spare ingredients they have at home, and the program will search a database and suggest recipes that use the given ingredients. This provides a quick, easy, and user-friendly solution for the average person to limit the amount of food they waste/throw away by giving them a comprehensive list of recipes, across different cuisines and meal-types. To make the experience more user-friendly, after inputting the ingredients, the website will prompt the user to choose from a selection of cuisines and meal-types (i.e. breakfast, lunch, dinner, desserts) to narrow down the list of recipes they may be able to use.

The program provides an abundance of different recipes stemming from over 22 geo-cultural World Regions, including; Japan, Greece, Mexico and Scandinavia. This allows the user to quickly and easily discover a recipe to satisfy their palate, regardless of where they are or what they feel like eating.

# How we built it
When creating this project, we first needed to find a database of recipes which we could then filter based on ingredients (and cuisines if we wanted). We implemented this with a python script that parses the recipe data from csv files. We then used the python module flask to host a web server, with the UI handled by html files.

# Challenges we ran into
One of the primary challenges that we confronted during this time was the conflict between ideation and reality. While our ideation phase was majorly positive and saw a significant level of cooperation on ideas, our original idea was far too broad in scope, as we were unable to narrow down the specific aspect of food wastage that was most crucial to address. However, through further ideation, and the recognition of the necessity of making our solution defined and specific to the issue of household over-purchasing and food wastage, we confronted this issue. Thus, we were able to make headway in producing a viable, individualised solution to this specific problem that we identified.

Having limited coding experience, the group struggled to get a working program, as we ran into issues reading the csv files we were using to store the recipe/ingredient data. Similarly, the majority of the group had never used html before, and none of us had ever used GitHub, so there was a somewhat steep learning curve on that front. However, after working together and doing ample research, we managed to produce a viable program that we were able to submit on GitHub with minimal issues.

# Accomplishments that we're proud of
We are mostly proud of our attitude in confronting this project. As a group of beginner coders with only a semester or so of python coding behind us, we were enthusiastic but nervous at the start of the project. Despite running into various barriers throughout our ideation process, predominantly due to the constraint of our still-developing skills, we persisted through this to come up with a solution that suited our coding abilities while also addressing the problem that we identified. This persistence was definitely what we were most proud of!

What we learned
As a team with beginner level coding experience, this project helped us to be able to build our coding skills, particularly in a collaborative environment. This introduced us to many of the features of project design and development - ideation, prototyping, and implementation. The experience also enabled us to familiarise ourselves with systems such as Github repositories.

# What's next for Recipe, Set, Go!
There are several additional features that could be implemented within Recipe, Set, Go!, predominantly in terms of improving user experiences. As one of the primary goals of our site was to tailor our recipes and suggestions to the user’s preference, the obvious next step would be to incorporate various dietary-requirement friendly options. Hopefully, this will increase the accessibility of our product, while also increasing its personalisation features and optimising each individual’s experience.

Improvements to personalisation and the UI could include allowing the user to create an account with which they can connect with friends/neighbours and be able to see what ingredients other people have and recipes that combine them with ingredients the user has. Each person could also customise their account to include pantry staples that they regularly have so they don’t have to constantly input the same few ingredients every time they use the site. Over time, the website would be slowly transitioned into an app for better accessibility and a more user friendly interface, as well as implementing a system similar to OLIO, in which the user can contact other users and give away unwanted food so it doesn’t go to waste.

# How to use this
1. Simply run server.py and then go to 127.0.0.1:5000 on your browser of choice.
2. Enter the ingredients you want to use in the text box, separated by spaces, and hit enter.
3. Choose which cuisine you want to make a recipe from and click submit.
4. Enjoy your meal suggestions :)
