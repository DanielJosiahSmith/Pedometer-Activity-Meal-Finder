<h1>Pedometer Activity Meal Finder</h1>

<p>Want some meal options for dinner?  But also want to stay within a calorie range depending on your walking activity? Try the Pedometer Activity Meal Finder!</p>

<h3>Getting Started</h3>
<p>1. Clone repository</p>
<p>2. Run docker compose up</p>

<h3>Endpoint</h3>

DINNER OPTIONS <br><br>
&nbsp;&nbsp;<strong>GET</strong> http://127.0.0.1:8000/dinner_options <br><br>
&nbsp;&nbsp;<strong>PARAMS </strong><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>name</i>: steps  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<i>desc</i>: number of steps you have walked today

example usage  http://127.0.0.1:8000/dinner_options?steps=5862
