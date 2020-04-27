# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app


selectedWritingsHeaderCenter = dbc.Col(
    [
        html.Center(
            children=[
                #html.Img(src=app.get_asset_url('Covid19-Website-R7-000_0038_Layer-28.png'), style={'display': 'block', 'width':'100%'}),
                html.Img(src=app.get_asset_url('mindfulnessShopping.gif'), style={'display': 'block', 'width':'80%', 'marginTop':30}),
                html.Br(),
                html.Span(' ', className='mr-1'),
            ]
        )
    ],
    md=12,
)


collapseEniqueArticle = dbc.Col(
    [
        html.Center(
            html.Div(
                [
                    dbc.Card(
                        dbc.CardBody(
                        [
                            html.H4("Mindfulness When Shopping",className="card-text",style={'fontSize':32, 'marginTop':40, 'marginBottom':55}),
                            html.P(
                                "It’s difficult to stay home during this crisis if we’re ill-prepared. We have to stock up on food, snacks, vitamins, hand sanitizer and, of course, toilet paper. It’s important to have a clean booty during a pandemic.",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "That’s why shopping for quarantine life has become an event. Thanks to the hours of predictive programming instilled into our minds by post-apocalyptic movies centering on societal collapse, we haven’t been reduced to chaotic creatures. However, as someone who is still assisting customers, both young and old, I have noticed an array of mindfulness and lack thereof when it comes to shopping. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "So here are a few tips you can use to protect yourself and others when shopping.",className="card-text",style={'text-align':'left'}
                            ),
                            html.H5("Mask & Gloves ",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "Seriously. We’re at a point where you have to assume someone has touched the item you just grabbed, whether it’s an employee or another customer. It helps you, the employees, fellow customers, and your loved ones. The addition of the mask can help ease any anxieties that employees may have, and it adds a layer of protection for you, too. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "According to the Centers for Disease Control and Prevention (CDC), It is recommended to use nitrile gloves, natural rubber gloves, or polychloroprene gloves, as they provide higher elasticity than vinyl gloves. ",style={'text-align':'left'}
                            ),
                            html.P(
                                "For masks, as you may already know, the N-95 Respirator comes highly recommended, for its tight fight and ability to reduce 95 percent of the wearer’s exposure to small particles and large droplets. A surgical mask may work in a pinch, however, it will not provide the needed protection against smaller airborne particles.",style={'text-align':'left'}
                            ),
                            html.P(
                                "Ideally, it is suggested that these masks be thrown away after each use. But given the current deficiencies of Personal Protective Equipment (PPE) that hospitals are facing, it would be considerate if you did not hoard masks, which could be accomplished by giving each individual mask a longer service life.",style={'text-align':'left'}
                            ),
                            html.P(
                                "If possible, you can help by reaching out to local hospitals and donating masks. ",style={'text-align':'left'}
                            ),
                            html.H5("What to Do",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "One store will not operate like the other, especially if you are frequenting independent pharmacies, grocery stores, and food processors. Make an attempt to learn their style of operations, checkout procedures, payment options, hours, and safety precautions.For example, Stop and Shop allow senior citizens (60-year-olds and over) to shop between 6-7:30 am, while Trader Joe’s is only allowing 30 customers in the store at one time.",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "Generally, you can avoid the crowds during the early mornings, because as the saying goes: the early bird catches the worm. Just pay attention to any updates that shops may have via their social media accounts, or call ahead if you’re not sure.",className="card-text",style={'text-align':'left'}
                            ),
                            html.H5("Know What You Want",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "For real, this isn’t the time to be window shopping. With the ever-increasing descent upon grocery stores and pharmacies, it’s imperative to have a list of the items you will be needing. ",style={'text-align':'left'}
                            ),
                            html.P(
                                "The quicker you are the quicker the checkout line will move, which will result in shorter exposure times. If you need help figuring out how to shop, refer to the god-awful film, “Jingle All the Way” starring Arnold Schwarzenegger and Sinbad.",className="card-text",style={'text-align':'left'}
                            ),
                            html.H5("Gimme Some Space",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "People are touching, smiling, and not respecting your personal space. The whole time my mind is thinking, 'Gimme some space, bro!' ",style={'text-align':'left'}
                            ),
                            html.P(
                                "Do you people even understand what’s happening out here? I’m not trying to add to the fear-mongering tactics some have accused the media of using, but if we don’t take this seriously we will be risking people’s health by extending this pandemic’s life span.",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "Please practice social distancing. Communicate clearly and thoroughly from the recommended six-foot distance. Keep in mind, that if you’re on a possible collision course with someone waving is one of the best non-verbal cues that you can rely on if you’re having trouble commanding a person’s attention.",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "Remember, if you can smell someone’s breath, cologne, or body odor you are too close.",className="card-text",style={'text-align':'left'}
                            ),
                            html.H5("Wipe Everything Down",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "Once you’re home, it’s important to wipe down any of the items you may have purchased, whether it’s packaged food products, produce, or home supplies. If it’s possible, designate an area at home that will be used to place outside items on. Wipe down this area after everything is put away. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "A thorough cleaning of fruits and veggies is crucial before they are stored away, even for fruits that are protected by an out layer, like oranges, bananas, and melons. A simple soak/wash in a bowl of water with vinegar (apple cider vinegar or white vinegar) and a gentle scrub with soap would suffice.",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "For those of you that use reusable bags, especially those made from cloth, it’s also essential to clean the bag, too. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.H5("R-E-S-P-E-C-T",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                            html.P(
                                "In America, we live in such a desensitized society that people watch police killings on their phones while eating their avocado toast. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "We lack empathy.", className="blockquote"
                            ),
                            html.P(
                                "You don’t care about my plight or the social injustices that affect me? Whatever. That was before this new situation engulfed America, and now we’re in this together.",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "So you may have looked down on or ignored the so-called low-skilled workers two months ago, but now we’re the ones you seek for cleanliness, supplies, food, transportation, education, and the normality that dissolved, due to this pandemic, yet you still yearn for to calm your anxieties. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.P(
                                "We don’t want to be out here, but we are. We’re risking our own health and that of our loved ones, which is making your life easier. Please take the time to show your appreciation in a non-condescending fashion. We are essential workers. ",className="card-text",style={'text-align':'left'}
                            ),
                            html.Hr(),
                            html.P(
                                "Written by:",style={'fontSize':14, 'marginTop':40, 'marginBottom':0},
                                className="card-text"),
                            dbc.Button('Enrique Grijalva', color="link",href = "https://www.linkedin.com/in/enrique-grijalva-15833059", size="sm",style={'marginBottom':0, 'marginTop':0}), 
                            ]
                        ), color="light"
                    )
                ]
            )
        )
    ],
    md=12,
)

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
            dbc.Row([selectedWritingsHeaderCenter]),
            dbc.Row([collapseEniqueArticle]),  ############################
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
        dbc.Row([singleColumn, nav, singleColumn]),  
        dbc.Row([singleColumn, selectedWritingsHeaderCenter, singleColumn]),  
        dbc.Row([singleColumn, collapseEniqueArticle, singleColumn]),  
        ]