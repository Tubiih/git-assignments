from os import getenv
from datetime import datetime
print(f'hello {getenv("USERNAME")}')

user = getenv('user')  
weekday = datetime.now().strfime('%A')
print('Hello {user}, happy {weekday}!')