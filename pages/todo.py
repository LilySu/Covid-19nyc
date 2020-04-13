# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app



thingstodoCenter = dbc.Col(
    [
        html.Center(
            children=[
                html.Img(src=app.get_asset_url('todo.png'), style={'marginTop':40,'display': 'block', 'width':'30%'}),
                html.Br(),
                html.Span(' ', className='mr-1'),
                html.Div(
                    [
                        dbc.Card(
                            dbc.CardBody(
                            [
                                html.H4("10 Things To Do While Quarantined",className="card-text",style={'fontSize':32, 'marginTop':40, 'marginBottom':55}),
                                html.P(
                                    "So you’ve watched everything there is to watch on Netflix, Hulu, and Amazon Prime. You could go through the second run-through of Tiger King. But who wants to expose themselves to Carole Baskins again?",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Thankfully, I’ve conjured up a list of activities that may help you through this stay-at-home marathon.",className="card-text",style={'text-align':'left'}
                                ),


                                html.H5("1. Read a Book ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),



                                html.P(
                                    "If you’re anything like me, a self-professed book hoarder, you’ve stacked up enough reading material to open up your own private library branch. (Not including ebooks.) The only problem arising out of this obsessive quest has been the pursuit of time. With the distraction that is social obligations, adulting responsibilities, and the task of accruing enough money to pay the bills, having time to do anything outside of the aforementioned parameters is a luxury.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "This luxury has only been awarded to a few of us, including Mr. Henry Bemis of the infamous Twilight Zone episode, “Time Enough at Last.” And since we’ve practically dove headfirst into the Twilight Zone at the start of this decade, it’s only fitting that we acclimate ourselves with a great novel, self-help book, comic book, or non-fiction book. After all, there’s enough time at last. ",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "What if you don’t have a stack of physical books, though? Here are two of my favorite resources that can help you.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "If you have a library card, you should download the Libby app (available for most iOS, Android, and Windows devices) which will give you free access to ebooks and digital audiobooks that you can borrow.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "The Internet Archive also has free ebooks available in many formats that you can download to your smartphones, kindles, and tablets. All you have to do is sign up for an account with them and dive in.",className="card-text",style={'text-align':'left'}
                                ),


                                dbc.CardLink("Libby App", href="https://libbyapp.com/welcome", style={'color':'#16849c'}),
                                dbc.CardLink("Internet Archive", href="https://archive.org/", style={'color':'#16849c'}),


                                html.H5("2. Learn a New Skill",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),


                                html.P(
                                    "Aziz Ansari didn’t need to tell us that we, as Millenials, are a generation who pride ourselves as the masters of none. It’s not completely our fault that we have a history of unstable relationships with employers. The American Dream just abandoned us. It left us to make do with what we could achieve and services we could provide.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "But there’s only so many matcha lattes you could make and emails you could write before you realize this is going nowhere. Take this as a sign telling you that it’s time to make changes that may, hopefully, with patience and focus, improve your life. Time to learn a new skill for the resume! ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "YouTube University is a very real place. I’ve learned how to make a beat, tie a tie, purchase a suit, brew tea properly, create essential oils, how to distill water, buy and sell sneakers online, and improve my photoshop skills. Most of what I’ve learned here has helped me in my everyday life or improved my skills in personal interests. However, there’s not enough I can learn on YouTube that can be applicable, skill-wise, from an academic standpoint, for prototypical industry positions.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "That’s what Coursera is for!", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Coursera provides free online courses from top universities from around the world, including Yale, Stanford, Columbia, and leading tech companies like Google and IBM. The only fee you’d have to pay is for accreditation for the courses you’ve completed.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Go on now! Learn new skills so you could pay your bills! ", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("Coursera", href="https://www.coursera.org/", style={'color':'#16849c'}),


                                html.H5("3. Cook Your Own Food ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),



                                html.P(
                                    "GrubHub has made take out so easy. And Instagram has us going out to restaurants so we could take pictures of the food. I don’t have the numbers but I’m sure they’re the reason many of us don’t cook. It’s not that I think we cannot cook, I believe we choose not to do it.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "It’s great that you’d like to support your local restaurants and delivery guys. But staying home and making your own great creations will be all the more rewarding. Plenty of chefs are doing live streaming demonstrations and, unlike the Food Channel, you can ask them questions.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "A great source for recipes can be found on Tastespotting. Whether you’re in the mood for a hummus vegetable salad, or you’re looking to create your own bread, but you’re in need of a wild sourdough recipe, you’ll find something for your innovative kitchen needs here.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Even setting aside and portioning your vitamins, protein powders, health food powders, and dried and frozen fruits in ziplock baggies help when you’re creating smoothies, yogurts, and juice combinations. ", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("Tastespotting", href="http://www.tastespotting.com/", style={'color':'#16849c'}),


                                html.H5("4. Talk to Family and Friends",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),


                                html.P(
                                    "One of my colleagues confessed that she was suffering from a lack of socialization just two days into the quarantine in New York City. In an attempt to console her through her isolation, I advised her to reconnect with her brothers and sisters via FaceTime or Skype. “Ahh, yes,” she responded. “Technology! What would we do without it?”", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "This pandemic has given us all an opportunity to reconnect with family and friends. The unfortunate aspect is the distance that is keeping us apart, no pun intended. So it has become crucial to reach out to our loved ones. Normally, I’d hear from my immediate family about once every two to three months. Recently, I’ve been in touch with them nearly every day. The same goes for my friends.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Smart devices have introduced a myriad of problems into the world, including the exploitation of our narcissism. Therefore it’s refreshing that we could use this technology to stay connected at a time where we’re practicing physical isolation, a behavior that goes against our natural desire to commune.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Zoom has exploded on the scene as the app has been most utilized during this pandemic, although Google Hangouts, Skype, FaceTime, Instagram Live, and Facebook Live, are all also capable video chat apps and in-app features that can keep you in touch with friends and family.", className="card-text",style={'text-align':'left'}
                                ),

                                html.P(
                                    "A Google Calendar schedule can optimize your time spent reaching out for video chats, especially if you keep a large social circle. You can spend the daytime chatting with family over lunch, and at night you can share a long-distance glass of wine with a friend. And that’s what can help make these chats fun.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "None of these video chats have to be bound to just conversation. You can still exercise with your gym buddies, listen to tunes with your fellow music aficionados, and still hold your book club meeting without missing a step.", className="card-text",style={'text-align':'left'}
                                ),


                                html.H5("5. Exercise",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),



                                html.P("Since gyms have been closed to prevent the spread of infection, many people have opted to exercise in the parks. The most recent action taken by New York City officials, to combat social gatherings of this kind has been to remove the basketball rims from public parks across the city.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Reactions across social media, from fitness enthusiasts to beach-body boasters have ranged from mild annoyance to the postponement of their summer bodies until the following year.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("However, instead of quitting, a local Crossfit gym in Brooklyn met this obstacle with creativity by live-streaming their classes for their members. Something that the popular health club chains may not have at their disposal, yet. ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Those members have been relegated to outdoor workouts. And although I have witnessed many people still jogging outside, it’s probably safer for everyone to keep the cardio indoors, even at the risk of angering your downstairs neighbor.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Once again, YouTube University comes to the rescue! Doing a quick search of bodyweight exercises will help you maintain, and perhaps enhance your strength. You will also find plenty of yoga, pilate, and qigong instructors, with plenty of routines that will cater to your level of conditioning. Instagram is also a great source for fitness instructors and specialists, who spotlight exercises designed to work on a specific area of your body.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("If space is not an issue in your household you can take your creativity to task by designing your own DIY gym setup. Reddit is littered with folks sharing everything from back extension setups weighted by cinder blocks inside a metal bucket to a hand-built bench press made from plywood.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("And who says you can’t have fun or experience pleasure while you break a sweat? Sex is one of the most enjoyable workouts we practice. The more acrobatic positions like the wheelbarrow, which porn stars periodically practice, can work your arms and abdominal muscles. You can remix a traditional position like doggystyle by incorporating a plank for endurance. But if you’re practicing alone, traditional positions like cowgirl/boy can still help you focus on your abdominals, buttocks, and thighs.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("It’s important not to remain sedentary during this quarantine. Health experts have expressed that an inactive lifestyle may lead to higher risks of diabetes, heart disease, high blood pressure, and increased feelings of depression and anxiety. None of which you need right now. ", className="card-text",style={'text-align':'left'}
                                ),


                                html.H5("6. Organize",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),



                                html.P("As much as we’d all like to think that we’re on top of everything, the reality is that we’re not. To claim that we’re not disorganized in some area in our life would be a lie. Even if that disorganization just exists in your contacts list or emails, there is some order to be had. ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Of course, you’d find it difficult to walk into a Container Store to purchase storage units for your promising new set up at home. So it’s best to do the best that you can with the space you have and, possibly, with the help of Marie Kondo, declutter your space.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Organizing tips are abundant online. Stick to housekeeping and home-style blogs for organizational tips at home, and if you’re currently doubling as a home office you can also check out office design blogs. But if you don’t know where to begin you can always start small by matching up all your socks and even mending holes in your clothes. Take advantage of the time we have that will allow you to focus on one area of your home each day.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Keep a list of errands you will need to run during and after the quarantine. This will help you tackle necessities in your life that need priority.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("For those of us that do not have the choice to stay at home, it is important to plan for a worst-case scenario trip to the hospital. Just as a couple who prepares for the mother to go into labor keeps a packed bag ready, so should you. If an in-home quarantine is needed, either from yourself or another sick person in the home, keep the items you would need in your room. ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Imagine if you were to emerge from this quarantine with a better hold on your life. Even greater is the possibility that throughout this stay-in-home order you would have been able to develop good habits. ", className="card-text",style={'text-align':'left'}
                                ),


                                html.H5("7. Develop Good Habits",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),


                                html.P("The popular consensus tells us that it takes 21 days to develop a new habit. According to psychologist and author Barbara Markway, this would be “setting ourselves up for failure.”", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("In a piece written in 2014 for Psychology Today, she lays out six stages and 16 tips for developing good habits. “Think a good new habit you’d like to develop,” she states. “With that in mind, read through each stage and the tips to move you from one stage to the next.”", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Sounds simple enough. Good luck! ", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("Psychology Today Article on Developing Good Habits", href="https://www.psychologytoday.com/us/blog/shyness-is-nice/201406/6-stages-and-16-tips-developing-good-habits", style={'color':'#16849c'}),



                                html.H5("8. Become Financially Literate ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),


                                html.P("Although this is an arduous task, even Scrooge McDuck would admit that this would be rewarding knowledge to possess. We can all agree that this is something that should have been taught in schools, however, that may not have been a choice for many of us.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Similarly, the choice to be working is not one that millions of Americans can currently exercise. Making this the best time to learn frugality and financial literacy. ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("You’ve traded hours of your life to make your money. Why not trade a few more to learn how to utilize it as a tool or learn to cut unnecessary spending? Sure, it becomes a daunting task when you’re hit with terminology you don’t understand, complex rules, and deceptive terms and agreements, but you must learn to protect yourself. ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Sites like NerdWallet and Investopedia are great places to start. AskSebby and Credit Shifu are great channels on YouTube for credit card information, and for investment knowledge, Earn Your Leisure and Invest Like A Boss are two great podcasts. ", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("NerdWallet", href="https://www.nerdwallet.com/", style={'color':'#16849c'}),
                                dbc.CardLink("Investopedia", href="https://www.asksebby.com/", style={'color':'#16849c'}),
                                dbc.CardLink("AskSebby", href="https://thecreditshifu.com/", style={'color':'#16849c'}),
                                dbc.CardLink("Credit Shifu", href="https://www.earnyourleisure.com/", style={'color':'#16849c'}),
                                dbc.CardLink("Earn Your Leisure", href="https://www.psychologytoday.com/us/blog/shyness-is-nice/201406/6-stages-and-16-tips-developing-good-habits", style={'color':'#16849c'}),
                                dbc.CardLink("Invest Like A Boss", href="http://www.investlikeaboss.com/", style={'color':'#16849c'}),


                                html.H5("9. Listen to Music & Podcasts ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),



                                html.P("Depending on the season, I typically have about 20 albums and 3 personally customized playlists in rotation. With the exception of my days off from work, I get lazy and fail to make time for new music, despite the hundreds of albums I have saved for later.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("I’m guilty of letting episodes of my favorite podcasts add up, too. Podcasts are out there in abundance and there are so many good ones that touch on the subject matters and interests that speak to you. In the beginning, the best suggestion would be to find one that allows you to feel as if you’re hanging out with a group of people who you aspire to be like.", className="card-text",style={'text-align':'left'}
                                ),


                                html.H5("10. Spend Time With Yourself ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),


                                html.P("According to an article recently released on Bloomberg, this quarantine has the potential to be liberating for introverts through the rejuvenation of energy, due to social distancing, which will be helping those creative juices flow. And judging by the impatience being voiced through memes and the defiant socializing others are still practicing, it appears that those who lean towards extroversion have a difficult time being alone. But it doesn’t have to be that way once you stop looking at time spent alone as a punishment.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Spending time alone can be an eye-opening experience. If we can learn to put our devices away for, at least, ten minutes a day we would have a better sense of who we are as an individual. Have you ever wondered how we became the person we are today? Have you ever taken a moment to think about how crazy the journey has been? ", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("Have fun with it! Try out a radical new hairstyle. Think about it: how many people are going to see it? Experiment with your makeup and facial hairstyles, too! Make yourself feel sexy with that luxe lace lingerie you only wear on special occasions and combine them with your favorite heels.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("If you have an upcoming birthday, don’t feel down. Dress up, make yourself a candlelit dinner with some wine and cake, put on some music, and dance the night away.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("But as the revelry softens and your new, unconventional look stares back at you, recognize that there is a profound undertaking that needs to be engaged with your current self.", className="card-text",style={'text-align':'left'}
                                ),
                                html.P("It’s hard to face ourselves. I know. We’re not facing an easy moment either. In fact, this is one of the most difficult moments in our entire lives, and we have a chance to truly get to know ourselves (the good and the bad) and make peace, without the need to pretend that everything is alright. Instead of worrying about whether or not things will get worse or normalize tomorrow, take some time to love yourself again.", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("Bloomberg Article on the Effects of the Quarantine on Introverts ", href="https://www.bloomberg.com/opinion/articles/2020-03-28/coronavirus-for-introverts-quarantine-can-be-a-liberation", style={'color':'#16849c'}),




                                html.Hr(),
                                html.P('Written by:',style={'fontSize':14, 'marginTop':40, 'marginBottom':0},className="card-text"),
                                dbc.Button('Enrique Grijalva', color="link",href = "https://www.linkedin.com/in/enrique-grijalva-15833059", size="sm",style={'marginBottom':0, 'marginTop':0}),  
                            ]), color="light"
                        )
                    ])
                ]
            )
    ],
    md=12,
)



# tab1_data_content = dbc.Card(
#     dbc.CardBody(
#         [
#             dbc.NavItem(dbc.NavLink("", href="/index", className='nav-link')),
#         ]
#     ),
#     className="mt-3",
# )



nav = dbc.Col(
    [
        dbc.Nav(
            [
                dbc.NavItem(dbc.NavLink("Things To Do", href="/todo", className='nav-link')),
                dbc.NavItem(dbc.NavLink("On Self-Reflection", href="/reflection", className='nav-link')),
                dbc.NavItem(dbc.NavLink("On Peace Within", href="/peace", className='nav-link')),
                dbc.NavItem(dbc.NavLink("Mindfulness Shopping", href="/shopping", className='nav-link')),
            ],fill=True
        )
    ],md=12
)

tab2_actions_content = dbc.Card(
    dbc.CardBody(
        [
            dbc.Row([nav]), 
            dbc.Row([thingstodoCenter]),  
        ]
    ),
    className="mt-3",
)


tabs = dbc.Tabs(
    [
        dbc.Tab(tab2_actions_content, label="ACTIONS", label_style={'fontSize':24}, labelClassName="text-info"),
        # dbc.Tab(tab1_data_content, label="DATA", label_style={'fontSize':24}, labelClassName="text-info"),
    ]
)




singleColumn = dbc.Col([],md=1)
doubleColumn = dbc.Col([],md=2)

navbar = dbc.Col([
    dbc.Nav([dbc.NavItem(tabs)],fill=True)
],md=10)

layout = [
        dbc.Row([singleColumn, navbar, singleColumn]),  
        ]