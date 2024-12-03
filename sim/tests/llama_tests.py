from ollama import chat
from ollama import ChatResponse

prompt = """Given the headline of a webpage, a user has conducted a search session to verify the correctness of the information provided in the webpage.        We provide you with the user session queries and the results for the last search. For each search result, we provide you with its title and snippet.        We also provide you with the full text of the first two results.         Taking into account the headline of the webpage, the user session queries and the search results, your task is to generate a new user query         to further verify the correctness of the information provided in the webpage.         Avoid repeating the exact same queries and introduce some variance in the new query, but avoiding topic drift.         Avoid using stopwords. Queries should have between 3-5 words length.         Answer ONLY with the query.        Headline of the Webpage: "U.S. faces engineered famine as COVID lockdowns and vax mandates could lead to widespread hunger, unrest this winter"
         User Queries: "['COVID induced famines']"
         Search results: "Title: "Nations must ‘act together, urgently and with solidarity ... - UN News" Snippet: "Moreover, the COVID-induced economic shock has compounded food insecurity by reducing incomes and disrupting supply chains, leading to an uneven economic recovery. ... mass hunger and famine, in a crisis that could last for years,” warned the UN chief. “In the past year, global food prices have risen by nearly one-third, fertilizer by more ..."
Title: "Pestilence and famine: Continuing down the vicious cycle with COVID-19" Snippet: "While the COVID-19 pandemic may not directly involve a volcano, history repeats itself. Disease leads to increased poverty, hunger, and changes in socioeconomic behaviors. Thus, insights from past pandemics frame the current COVID-19 hunger crisis and can inform actions to mitigate negative consequences from COVID-19 and future disease outbreaks."
Title: "The eerie silence of starvation ‘is deafening, it never leaves you’: UN ..." Snippet: "Hunger and conflict “feed off of each other,” she continued, briefing the Security Council open debate on famine and conflict-induced global food insecurity convened by the United States during its August presidency. ... COVID-19: A ‘new and deadly threat’ for civilians caught up in violence. News Tracker: Past Stories on This Issue ..."
Title: "Pestilence and famine: Continuing down the vicious cycle with COVID-19" Snippet: "On the other hand, pandemics, such as COVID-19, lead to greater malnutrition. Both over- and undernutrition increase severity of disease, alter vaccine effectiveness, and potentially create conditions for viral mutation and adaptation—further driving the disease and famine vicious cycle. These long-term health and socioeconomic repercussions ..."
Title: "‘Tsunami of hunger’ could trigger multiple famines ... - UN News" Snippet: "As risks of conflict-induced famine and widespread food insecurity continue to rise, ... Meanwhile, drought, rising global commodity prices, and the impacts of COVID-19 and the Ukraine war are also compounding food insecurity and misery. And people in South Sudan, Nigeria, Ethiopia, Yemen, Afghanistan, and Somalia are “quite literally on the ..."
Title: "Lack of Grain Exports Driving Global Hunger to Famine Levels, as War in ..." Snippet: "Russian Federation Delegate Refutes United States Claim That His Country Is Holding World Hostage with Blockade of Ukraine’s Ports. A global food crisis, already impacted by the COVID-19 pandemic and climate change, is being driven to famine levels worldwide by the war in Ukraine and the resulting lack of grain exports, more than 75 speakers told the Security Council today in a ministerial ..."
Title: "Secretary Blinken Intervention at a United Nations Security Council ..." Snippet: "Secretary Blinken Intervention at a United Nations Security Council Open Debate on Famine and Conflict-Induced Global Food Insecurity. ... has been fueled by climate, by COVID as well, and, as we’re discussing today, by conflict. Hunger and conflict are inexorably linked. Scarce resources heighten tensions between communities and nations."
Title: "Food Insecurity during COVID-19 in Yemen - PMC - National Center for ..." Snippet: "The United Nations has declared Yemen as the world’s worst humanitarian crisis with 21 million people in need of humanitarian assistance. Due to the convergence of severe economic instability exacerbated by the COVID-19 pandemic, stifling war, and spiking food prices, the Yemeni people are at the brink of famine with women and children especially malnourished."
Title: "Conflict and Violence are the Primary Causes of Hunger and Famine ..." Snippet: "The world was facing severe global hunger, which had been fuelled by climate change and COVID-19 and decidedly worsened by conflicts, notably Russia’s unprovoked war against Ukraine. Some speakers said that the Russian war of aggression against Ukraine had aggravated the global food crisis, as these two countries supplied approximately 30 per ..."
Title: "What is famine? How it's caused and how to stop it" Snippet: "What is famine? A famine is declared when a certain set of conditions have been met. This criteria includes at least 30% of a given area's children suffering from severe malnutrition. That means that, by the time a famine is declared, children are already starting to die because their parents cannot give them enough food to survive."
"
         Full text of the first search result: "During a ministerial meeting on global hunger taking pace at UN Headquarters in New York, Secretary-General António Guterres said the number of severely food insecure people had doubled in just two years – from 135 million pre-pandemic to 276 million today, with more than half a million experiencing famine conditions – an increase of more than 500 per cent since 2016.

“These frightening figures are inextricably linked with conflict, as both cause, and effect,” he said. “If we do not feed people, we feed conflict”.

Hunger triggers

The climate emergency is another driver of global hunger he added, pointing out that 1.7 billion people have been affected by extreme weather and climate-related disasters over the past decade.

Moreover, the COVID-induced economic shock has compounded food insecurity by reducing incomes and disrupting supply chains, leading to an uneven economic recovery. Access to financial markets has been restricted, with some developing States now on the brink of debt default.

“Now the war in Ukraine is amplifying and accelerating all these factors: climate change, COVID-19, and inequality,” Mr. Guterres said.

Ukraine war’s repercussions

Between them, Ukraine and Russia produce almost a third of the world’s wheat and barley and half of its sunflower oil. Russia and Belarus are the world’s number two and three producers of potash, a key ingredient of fertilizer.

The war threatens to tip “tens of millions of people over the edge into food insecurity, followed by malnutrition, mass hunger and famine, in a crisis that could last for years,” warned the UN chief.

“In the past year, global food prices have risen by nearly one-third, fertilizer by more than half, and oil prices by almost two-thirds”.

Devastating societies

Meanwhile, most developing countries lack the fiscal space to cushion the blow of these huge increases with many unable to borrow because markets are closed to them.

“If high fertilizer prices continue, today’s crisis in grain and cooking oil could affect many other foods including rice, impacting billions of people in Asia and the Americas,” he detailed.

Additionally, children are threatened by a lifetime of stunting; millions of women and children will become malnourished; girls will be pulled from school and forced to work or get married; and families will embark on dangerous journeys across continents, just to survive.

“High rates of hunger have a devastating impact on individuals, families, and societies,” spelled out the UN chief.

‘Five urgent steps’

However, if we act together, there is enough food for everyone, he said adding that “ending hunger is within our reach”.

The Secretary-General then outlined five urgent steps to solve the short-term crisis and prevent long-term damage, beginning with reducing market pressure by increasing food supplies – with no restrictions on exports and surpluses available to those most in need.

“But let’s be clear: there is no effective solution to the food crisis without reintegrating Ukraine’s food production, as well as the food and fertilizer produced by Russia and Belarus, into world markets, despite the war”.

Secondly, social protection systems must cover all in need with food, cash; and water, sanitation, nutrition, and livelihood support must be provided.

Fourth, governments must bolster agricultural production and invest in resilient food systems that protect smallholder food producers.

And finally, humanitarian operations must be fully funded to prevent famine and reduce hunger.

Act in solidarity

In closing, the UN chief said that the Global Crisis Response Group on food, energy and finance is tracking the impact of the crisis on vulnerable people, identifying and pushing for solutions.

“The food crisis has no respect for borders, and no country can overcome it alone,” he said.

“Our only chance of lifting millions of people out of hunger is to act together, urgently and with solidarity".

‘Goodwill’ needed

US Secretary of State Antony Blinken chaired the meeting in which foreign ministers from approximately 30 regionally diverse countries discussed steps to address global food security, nutrition, and resilience.

Describing the current situation as the “greatest global food insecurity crisis of our time,” Mr. Blinken attributed the emergency to conflict, drought and natural disasters – made worse by Russia’s war on Ukraine.

Although hopeful, he said that “there is still a way to go” and that “the complex security, economic and financial implications require goodwill on all sides”.

To address the global crisis, US Secretary announced $215 million in humanitarian aid.

Urgent to open ports

World Food Programme (WFP) chief David Beasley drew attention to a world “too fragile” from years of conflict, pandemic and climate threats.

He also noted that current funding deficits could impede food access by as many as four million people.

Additionally, the top WFP official pointed out that a “failure to open the ports” in and beyond Ukraine will force people to the brink of starvation.

Although the “silos are full,” blockades and other impediments are rendering them inaccessible, Mr. Beasley said, urging governments to “step up” now”."
         Full text of the second search result:"Access Denied

Your access to the NCBI website at www.ncbi.nlm.nih.gov has been temporarily blocked due to a possible misuse/abuse situation involving your site. This is not an indication of a security issue such as a virus or attack. It could be something as simple as a run away script or learning how to better use E-utilities, http://www.ncbi.nlm.nih.gov/books/NBK25497/, for more efficient work such that your work does not impact the ability of other researchers to also use our site. To restore access and understand how to better interact with our site to avoid this in the future, please have your system administrator contact info@ncbi.nlm.nih.gov."
        New User Query:(just answer with the query)"""

response: ChatResponse = chat(model='llama3:8b-instruct-q4_0', messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ], options={'num_predict':15})
  
print(response['message']['content'])
