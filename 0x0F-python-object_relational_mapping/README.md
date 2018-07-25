#### Projects to introduce SQL Alchemy in Python

All non-model scripts take at minimum in order mysql username, mysql password, and database name. Any extra arguments come after those three.  

##### Using MYSQLDB
**0-select_states.py**: select states from database  
**1-filer_states.py**: select states starting with N  
**2-my_filter_states.py**: filter states with user input via argument to script  
**3-my_filter_states.py**: filter states inject safe  
**4-cities_by_states.py**: list all cities ordered by city id  
**5-filter_cities.py**: list all cities in a state sorted by city id  

##### Using SQLAlchemy
**model_state.py**: ORM model for a state using SQLAlchemy  
**7-model_state_fetch_all.py**: get all states  
**8-model_state_fetch_first.py**: get first state in table  
**9-model_state_filter_a.py**: get states with lowercase 'a' in their name  
**10-model_state_my_get.py**: get state with name pass as argument to script  
**11-model_state_insert.py**: insert "Louisiana" into the states table  
**12-model_state_insert.py**: change name of state with id=2 to New Mexico  
**13-model_state_delete_a.py**: delete all states with lowercase 'a' in their name  
**model_city.py**: ORM model for city  
**14-model_city_fetch_by_state**: List all cities along with their state's name  
