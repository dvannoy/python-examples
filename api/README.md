## API Provided

| HTTP Method | URL                                                                    | Optional Parameters          | Action                                          |
|-------------|------------------------------------------------------------------------|--------------------------------------------------------------------------------|-----|
| GET         | http://127.0.0.1:5000/vehicle_stops/v0.1                               | page=[int]                   | Get list of vehicle stops.                      |

## Setup
Dependencies: Python and the sqlite and flask packages.

You need sqlite command line utility if you want to install
the database from scratch. Alternatively you can use the provided sqlite db. To initialize from scratch,
 run the following at the command line: ```sqlite3 vehicle_stops.db < create_db.sql```

Run python basic_web_api.py to start the API