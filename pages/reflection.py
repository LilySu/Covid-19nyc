# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app



onSelfReflectionCenter = dbc.Col(
    [
        html.Center(
            children=[
                html.Img(src=app.get_asset_url('onSelfReflection.jpg'), style={'marginTop':60,'display': 'block', 'width':'60%'}),
                html.Br(),
                html.Span(' ', className='mr-1'),
                html.Div(
                    [
                        dbc.Card(
                            dbc.CardBody(
                            [
                                html.H4("Self-Reflection as a Fundamental Activity",className="card-text",style={'fontSize':32, 'marginTop':40, 'marginBottom':55}),
                                html.P(
                                    "Approaching the second week of self-isolation has felt momentous. The first week was filled with anxiety of the unknown and the flurry of stocking up at the supermarket and pharmacy. But now having found some semblance of a routine - grocery shopping once a week, rotating working areas within the apartment to keep things stimulating, taking up new hobbies, and reconnecting with friends and family, this all feels a bit more bearable. ",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "But more time indoors has meant more time for introspection. This means getting reacquainted with the self, all of the neuroses, nagging thoughts, and feelings. For many, life is just too busy to allow for moments of self-reflection. Coming face to face with your own thoughts is also not easy. But now that we have more time and less distractions to hide behind, we are being forced to do so. Remember that one time you tried to meditate? Yes, I mean sitting with ALL of your thoughts and feelings and letting them go. Even on a normal day this is difficult to do. But worries are running higher than normal around the well-being of family, job security, parenting and working from home, and general uncertainty of the future.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "We need to understand that the only way is working through these complex thoughts and feelings. The truth is, this is a great time for self-reflection as individuals and as humanity. Are you living your best self? What do you truly value? What should we as humanity value? What is fundamentally broken in our society? How can we fix it? What is our civic role and duty in society? What does it mean to be interconnected? Perhaps this introspection will mean we can be better sons and daughters, mothers and fathers, citizens, citizens of the world when we emerge from the other side.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "I have resolved to embrace this moment in time. To view this as a profound lesson. Rather than fighting feelings of anxiety, depression, or loneliness, accept them, learn from them and let them go. I invite you to join me to do the same! My hope is that this moment in time will be a great learning opportunity for individuals. Embrace yourself and others. Be kind to one another in awareness that we are all going through a difficult time together.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Here are some ways to ease into a mindset that is open to self-reflection:",className="card-text",style={'text-align':'left'}
                                ),
                                html.H5("Meditation",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),

                                html.P(
                                    "As mentioned, the ultimate practice for sitting with the self is meditation. There are some amazing apps, my favorite being Insight Timer, for home meditation. ",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "If you find it difficult to meditate alone, set aside time with those you live with or schedule a session virtually with friends! For beginners who find it difficult to sit in one place for a long time, you can easily adopt other mindfulness practices including mindful eating and mindful walking in the local park.",className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("More on Insight Timer", href="https://insighttimer.com/", style={'color':'#16849c'}),
                                dbc.CardLink("Helpful Link for Mindful Eating", href="https://www.health.harvard.edu/staying-healthy/8-steps-to-mindful-eating", style={'color':'#16849c'}),
                                dbc.CardLink("Helpful Link for Mindful Walking", href="https://chopra.com/articles/mindful-walking-practice-how-to-get-started", style={'color':'#16849c'}),
                                html.H5("Journaling",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                                html.P(
                                    "Whether you are a seasoned journaler or not, writing out your thoughts and feelings can be a therapeutic way to decompress. What can be helpful is setting aside a time to write regularly around the same time. For instance, every Sunday evening before bed. Keeping a gratitude journal of sorts can help as well. For those who struggle with writing you can write one sentence daily on what you are grateful for. ", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("On Keeping a Gratitude Journal", href="https://greatergood.berkeley.edu/article/item/tips_for_keeping_a_gratitude_journal", style={'color':'#16849c'}),
                                html.H5("Walking",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                                html.P(
                                    "Getting outside in the fresh air for a short while (preferably alone) can be helpful. If there is a garden or park nearby take advantage of it and soak in the spring breeze! Walking has been known to improve creativity and the thought process according to a study by Stanford University. You can opt to walk with a companion but considering the number of restrictions in many countries regarding self-isolation this is not advised unless you live with them. That being said, solo is probably best so you can focus on your thoughts.", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("Study on the Correlation Between Walking & Creativity", href="https://news.stanford.edu/2014/04/24/walking-vs-sitting-042414/", style={'color':'#16849c'}),
                                html.H5("Exploring Happiness",className="card-text",style={'fontSize':26, 'marginTop':35, 'marginBottom':35}),
                                html.P(
                                    "Lots of people have the misconception of what happiness means. For many it is something that is a sustained state to aspire to. But in reality, happiness is constantly in a flux and related to self-resilience. Resilience means building the muscle to allow for living joyfully while in full awareness of life’s inherent ups and downs. This is a great moment in time to exercise that muscle! Two great resources include “The Happiness Project” by Gretchen Rubin and a free Coursera module, “The Science of Well-Being,” taught by Professor Laurie Santos at Yale University.", className="card-text",style={'text-align':'left'}
                                ),
                                dbc.CardLink("Article on How Resilience is Tied to Happiness", href="https://qz.com/1289236/resilience-is-the-new-happiness/", style={'color':'#16849c'}),
                                html.Hr(),
                                html.P(
                                    "Written by:",style={'fontSize':14, 'marginTop':40, 'marginBottom':0},
                                    className="card-text"),
                                dbc.Button('Jenny Kai', color="link",href = "https://www.linkedin.com/in/jenny-a-kai-06b89329/", size="sm",style={'marginBottom':0, 'marginTop':0}), 
                            ]), color="light"
                        )
                    ])
                ]
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
            dbc.Row([onSelfReflectionCenter]),  ############################
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