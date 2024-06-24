## Installation

To install the required dependencies for this project, you can use the following command:
```bash
pip install -r requirements.txt
```
To run the project, you can use the following command:
```bash
uvicorn main:app --reload
```
 
## Encoded values for developers
### Function 01: team_selection

Encoded values for 'Team 1', 'Team 2', 'Winner', and 'toss':
```javascript
  'Afghanistan': 0
  'Australia': 1
  'Bangladesh': 2 
  'Canada': 3
  'England': 4
  'India': 5
  'Ireland': 6 
  'Kenya': 7
  'Netherlands': 8 
  'New Zealand': 9 
  'Oman': 10
  'Pakistan': 11 
  'Scotland': 12 
  'South Africa': 13 
  'Sri Lanka': 14
  'U.A.E.': 15
  'United Arab Emirates': 16 
  'West Indies': 17
  'Zimbabwe': 18
  'no result': 19 
  'tied': 20 
```
Encoded values for 'ground':
```javascript
  'Abu Dhabi': 0
  'Adelaide': 1
  'Ahmedabad': 2
  'Auckland': 3
  'Bengaluru': 4
  'Birmingham': 5
  'Bloemfontein': 6
  'Brisbane': 7
  'Bristol': 8
  'Bulawayo': 9
  'Cape Town': 10
  'Cardiff': 11
  'Centurion': 12
  'Chester-le-Street': 13
  'Christchurch': 14
  'Colombo (RPS)': 15
  'Colombo (SSC)': 16
  'Cuttack': 17
  'Dambulla': 18
  'Delhi': 19
  'Dharamsala': 20
  'Dubai (DSC)': 21
  'Dublin': 22
  'Dublin (Malahide)': 23
  'Dunedin': 24
  'Durban': 25
  'East London': 26
  'Eden Gardens': 27
  'Edinburgh': 28
  'Fatullah': 29
  'Galle': 30
  'Gqeberha': 31
  'Guwahati': 32
  'Hambantota': 33
  'Hamilton': 34
  'Harare': 35
  'Hobart': 36
  'Hyderabad': 37
  'Johannesburg': 38
  'Karachi': 39
  'Kimberley': 40
  'Kingston': 41
  'Lahore': 42
  'Leeds': 43
  "Lord's": 44
  'Lucknow': 45
  'Manchester': 46
  'Melbourne': 47
  'Mirpur': 48
  'Mohali': 49
  'Mount Maunganui': 50
  'Nagpur': 51
  'Nelson': 52
  'North Sound': 53
  'Nottingham': 54
  'Paarl': 55
  'Pallekele': 56
  'Perth': 57
  'Port of Spain': 58
  'Pune': 59
  'Rajkot': 60
  'Ranchi': 61
  'Sharjah': 62
  'Sydney': 63
  'The Oval': 64
  'Thiruvananthapuram': 65
  'Visakhapatnam': 66
  'Wankhede': 67
  'Wellington': 68
  ```
Encoded values for 'toss_decision':
```javascript
  'bat': 0,
  'field': 1
```
Encoded values for 'weather' :
```javascript
'Sunny' : 1
'Partly Cloudy' : 2
'Cloudy' : 3
'Light Drizzle' : 4
'Rain' : 5
```
Encoded values for 'player_values':
```javascript
  'Top order Batter': 1
  'Wicketkeeper Batter': 2
  'Opening Batter': 3
  'Middle order Batter': 4
  'Batter': 5
  'Wicketkeeper': 6
  'Allrounder': 7
  'Batting Allrounder': 8
  'Bowling Allrounder': 9
  'Bowler': 10
```
### Function 02: nutrition_plan
Encoded values for 'blood_group':
```javascript
	'O+' : 1
	'A+' : 2
	'B+' : 3
	'AB+' : 4
	'O-' : 5
	'A-' : 6
	'B-' : 7
	'AB-' : 8
```
Encoded values for 'injury_type':
```javascript
'Head' : 1
'Hand and fingers' : 2	
'Knee' : 3
'Lumbar' : 4	
'soft tissue' : 5	
'none' : 6
```


### API Endpoints
#### 1. /team_selection
This endpoint is used to predict the winning team based on the input features. The input features are 'Team 1', 'Team 2', 'Ground', 'Toss Winner', 'Toss Decision', 'Winner', and 'Country'. The output is the predicted team composition and player strike rates. 

This is a GET request to the URL:[http://127.0.0.1:8000/team_composition/](http://127.0.0.1:8000/team_composition/)

**Parameters:**

* `team1`
* `team2` 
* `winner` 
* `ground` 
* `margin_wickets` 
* `margin_runs`
* `weather`
* `toss`
* `toss_decision`

![postman screenshot](/Screenshot%2001.png )

#### 2. /nutrition_plan
This endpoint is used to predict the nutrition plan based on the input features. The input features are 'Height (cm)', 'Weight (kg)', 'blood_group', 'injury type'.

This is a GET request to the URL:[http://127.0.0.1:8000/nutrition_plan/](http://127.0.0.1:8000/nutrition_plan/)

**Parameters:**

* `player_value`
* `weight_in_kg`
* `height_in_cm`
* `blood_group`
* `injury_type`

![postman screenshot](/Screenshot%2002.png )

#### 3. /predictPosture
This endpoint is used to predict the posture of the player based on the input features. The input video. The output is the predicted posture of the player whether correct or wrong.

This is a POST request to the URL:[http://127.0.0.1:8000/predictPosture](http://127.0.0.1:8000/predictPosture)

"# TeamsPro" 
