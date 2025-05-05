# University_Ranking
This app provides university rankings for 1) Climate, 2) Social Justice 3) Gender and 4) Overall Ranking for universities from USA, UK, Ireland, Australia, New Zealand and Canada.  

All universities from Russel Group (UK) and Ivy League (USA) are also included.

[Access data Dashboard here!](https://uniranking.streamlit.app/)   

<b>This is a work in progress.</b>     
  
<b>Method/ Methodology</b>  
Publicly available text from websites of all universities in USA, UK, Ireland, Australia, New Zealand and Canada are used to determine the rankings.  
Maximum 15 pages are used from the official website of each university.  The pages were checked during Easter break 2025.  
Further, links are used from each homepage, and links in resulting pages may also be used (up to max 15 pages in total for each university) to analyze text.  

Universities with less than 4000 words in their webpages are discarded. Non-english websites (about 18 from Canada) are also excluded.

Rankings are based on the number of occurrences of various words (shown below) along each of the 3 dimensions, scaled by the total number of words in the respective university's webpage. Then the "Overall Rank" is based on the sum of the three scores.  

The words associated with each dimension are provided  below.

<b>1) Climate:</b>  
carbon capture,
carbon footprint,
climate action,
climate catastrophe,
climate change,
climate crisis/es,
climate emergency,
climate justice,
climate pledge,
climate policy,
climate resilience,
climate solution,
emission,
green new deal,
greenhouse,
netzero,
sustainable/bility,



<b>2) Social justice:</b>    
affirmative action,
antiracism/t,
bipoc ,
black lives matter,
 blm ,
critical race,
 decolonisation/zation,
 dei ,
 deib ,
diversity,
 edi ,
equitable,
equity,
inclusive ,
inequity,
intersectional\ality,
latinx,
microaggression,
pay gap,
refugee,
 reparation,
safe space,
systemic racism,
unconscious bias,
undocumented,
white privilege,
white supremacy/cist



<b>3) Gender:</b>     
cisgender,
gender discrimination/tory,
gender diverse/sity,
gender equality/ies,
gender equity,
gender expression,
gender history,
gender identity/ties,
gender inclusive/usion,
gender justice,
gender neutral,
gender pay,
gender policy,
gender restroom,
genderqueer,
 lgb ,
 lgbt ,
nonbinary,
patriarchy,
queer,
toxic masculinity,
transgender




