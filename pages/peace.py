# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app


restoringPeaceCenter = dbc.Col(
    [
        html.Center(
            children=[
                html.Img(src=app.get_asset_url('restoringPeace.png'), style={'marginTop':60,'display': 'block', 'width':'80%'}),
                html.Br(),
                html.Span(' ', className='mr-1'),
                html.Div(
                    [
                        dbc.Card(
                            dbc.CardBody(
                            [
                                html.H4("Restoring Peace Within Yourself",className="card-text",style={'fontSize':32, 'marginTop':40, 'marginBottom':55}),
                                html.P(
                                    "We understand how a pandemic can create anxiety, panic and stress, especially with how fast the worldwide spread has been. We would like to help you restore peace of mind within yourself by introducing the mindfulness practice taught by Thich Nhat Hanh, the father of mindfulness. The following comes from the chapter “Restoring Peace Within Yourself” from his book True Love.",className="blockquote",style={'text-align':'left'}
                                ),
                                html.P(
                                    "During the day, if you practice walking meditation, each step brings you back to the present moment; each step enables you to touch what is beautiful, what is true. And in this way, after a few weeks of practice, joy will become something possible, you will be able to undo many knots within yourself, and you will be able to transform negative energies into joy and peace. The Buddha said this: “The object of your practice should first of all be yourself. Your love for the other, your ability to love another person, depends on your ability to love yourself.” If you are not able to take care of yourself, if you are not able to accept yourself, how could you accept another person and how could you love him or her? So it is necessary to come back to yourself in order to be able to achieve the transformation.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Each of us is a king who reigns over a very vast territory that has five rivers. The first river is our body, which we do not know well enough. The second is the river of sensations. Each sensation is a drop of water in this river. There are pleasant sensations, others that are unpleasant, and neutral sensations. To meditate is to sit down on the bank of the river of sensations and identify each sensation as it arises. The third is the river of perceptions, which it is necessary to observe. You must look deeply into their nature in order to understand. The fourth is the river of mental formations, of which there are fifty-one. And finally, the fifth is the river of consciousness.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Our territory is really very vast, but we are not responsible kings or queens. We always try to dodge away and we do not keep up a real surveillance of our territory. We have the feeling that there are immense conflicts there, too much suffering, too much pain—that is the reason we are very hesitant to get back to our territory. Our daily practice consists in running away. If we have a moment free, we will make use of it to watch television or read a magazine article so we will not have to go back to our territory. We are afraid of the suffering that is inside us, afraid of war and conflicts.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "The practice of mindfulness, the practice of meditation, consists of coming back to ourselves in order to restore peace and harmony. The energy with which we can do this is the energy of mindfulness. Mindfulness is a kind of energy that carries with it concentration, understanding, and love. If we come back to ourselves to restore peace and harmony, then helping another person will be a much easier thing.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "Caring for yourself, reestablishing peace in yourself, is the basic condition for helping someone else. So that the other can stop being a bomb, a source of pain for ourselves and others, you really have to help him to defuse the bomb. To be able to provide help, we have to have a little calm, a little joy, a little compassion in ourselves. This is what we get from mindfulness in everyday life, because mindfulness is not something that is only done in a meditation hall; it is also done in the kitchen, in the garden, when we are on the telephone, when we are driving a car, when we are doing the dishes.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "If you can do it this way, three weeks are enough to transform the pain inside you, to bring back your joy in living, to cultivate the energy of compassion with which you can help the person you love. The practice of being there with what is beautiful and with what is healing is something we should do every day, and it is possible to do this in everyday life.",className="card-text",style={'text-align':'left'}
                                ),
                                html.P(
                                    "In order to support your mindfulness practice, you might be interested in trying some mobile apps, such as Insight Timer, Calm, Headspace, with which you can practice mindfulness wherever you go. Hope peace of mind and love be with you, especially in this extraordinarily challenging time!", className="blockquote",style={'text-align':'left'}
                                ),
                                dbc.CardLink("More on Insight Timer", href="https://insighttimer.com/", style={'color':'#16849c'}),
                                dbc.CardLink("More on Calm", href="https://www.calm.com/", style={'color':'#16849c'}),
                                dbc.CardLink("More on Headspace", href="https://www.headspace.com/", style={'color':'#16849c'}),
                                html.Hr(),
                                html.P('Excerpt from Zen Master Thich Nhat Hanh. "True Love: A Practice for Awakening the Heart."Penguin Random House, 2004. Chapter 8.',style={'fontSize':14, 'marginTop':45}, className="card-text"),
                                html.P('Intro and Afterword by',style={'fontSize':14},className="card-text"),
                                dbc.Button('Wen Ping Lin', color="link",href = "https://www.linkedin.com/in/wenpinglin", size="sm",style={'marginBottom':0, 'marginTop':0}), 
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
            dbc.Row([restoringPeaceCenter]),  ############################
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