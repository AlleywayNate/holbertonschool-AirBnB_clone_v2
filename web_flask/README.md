This is a README for 0x03. AirBnB clone - Web framework

This project builds on our previous v2 AirBnB clone creating a web framework
in Flask.

There are 12 mandatory tasks in this project as follows
Task 0 - Hello Flask!
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Application must use option strict_slashes=False in route definition

Task 1 - HBNB
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Route /hbnb : display "HBNB"
   - Application must use option strict_slashes=False in route definition

Task 2 - C is fun
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Route /hbnb : display "HBNB"
   - Route /c/<text> : Display "C" followed by the value of the text variable
        - Replace '_' with ' '
   - Application must use option strict_slashes=False in route definition

Task 3 - Python is cool!
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Route /hbnb : display "HBNB"
   - Route /c/<text> : Display "C" followed by the value of the text variable
        - Replace '_' with ' '
   - Route /python/(<text>) : Display "Python" followed by the value of text
        - Replace '_' with ' '
   - Application must use option strict_slashes=False in route definition

Task 4 - Is it a number?
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Route /hbnb : display "HBNB"
   - Route /c/<text> : Display "C" followed by the value of the text variable
        - Replace '_' with ' '
   - Route /python/(<text>) : Display "Python" followed by the value of text
        - Replace '_' with ' '
   - Route /number/<n> : display "'n' is a number" only if 'n' is an integer
   - Application must use option strict_slashes=False in route definition

Task 5 - Number template
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Route /hbnb : display "HBNB"
   - Route /c/<text> : Display "C" followed by the value of the text variable
        - Replace '_' with ' '
   - Route /python/(<text>) : Display "Python" followed by the value of text
        - Replace '_' with ' '
   - Route /number/<n> : display "'n' is a number" only if 'n' is an integer
   - Route /number_template/<n> : display a HTML page only if 'n' is an INT
        - H1 tag: "Number; 'n'" inside the tag BODY
   - Application must use option strict_slashes=False in route definition

Task 6 - Odd or even
 - Write a script that starts a Flask web application
   - Application must be listening on 0.0.0.0.:5000
   - Route / : display "Hello HBNB!"
   - Route /hbnb : display "HBNB"
   - Route /c/<text> : Display "C" followed by the value of the text variable
        - Replace '_' with ' '
   - Route /python/(<text>) : Display "Python" followed by the value of text
        - Replace '_' with ' '
   - Route /number/<n> : display "'n' is a number" only if 'n' is an integer
   - Route /number_template/<n> : display a HTML page only if 'n' is an INT
        - H1 tag: "Number: 'n'" inside the tag BODY
   - Route /number_odd_or_even/<n> : display a HTML page only if 'n'
     is an integer
        - H1 tag: "Number: 'n' is even|odd" inside the tag BODY
   - Application must use option strict_slashes=False in route definition

Task 7 - Improve engines
 - Update FileStorage: (models/engine/file_storage.py)
    - Add a public method def close(self): call reload() method for
      deserializing the JSON file to objects
 - Update DBStorage: (models/engine/db_storage.py)
    - Add a public method def close(Self): call remove() method on the private
      session attribute (self.__session) or close() on the class Session
 - Update State: (models/state.py)
    - If storage engine is not DBStorage, add a public getter method cities to
      return the list of City objects from storage linked to the current State

Task 8 - List of states
 - Write a script that starts a Flask web application
    - Application myust be listening on 0.0.0.0:5000
 - Must use storage for fetching data from the storage engine (FileStorage
   or DBStorage) => from models import storage and storage.all(...)
 - After each request, remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call this method storage.close()
 - Routes
    - /states_list: display a HTML page(inside the tag BODY)
        - H1 tag: "States"
        - UL tag: with the list of all State objects present in DBStorage
          sorted by name (A-Z)
            - LI tag: description of one State: <state.id>: <B><state.name></B>
 - Must use the option strict_slashes=False in route definition

Task 9 - Cities by States
 - Write a script that starts a Flask web application
    - Application myust be listening on 0.0.0.0:5000
 - Must use storage for fetching data from the storage engine (FileStorage
   or DBStorage) => from models import storage and storage.all(...)
 - To load all cities of a State:
    - If storage engine is DBStorage, must use cities relationship
    - Otherwise, use the public getter method cities
 - After each request, remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call this method storage.close()
 - Routes
    - /cities_by_states: display a HTML page(inside the tag BODY)
        - H1 tag: "States"
        - UL tag: with the list of all State objects present in DBStorage
          sorted by name (A-Z)
            - LI tag: description of one State: <state.id>: <B><state.name></B>
              + UL tag: with the list of City objects sorted by namm (A-Z)
                - LI tag: description of one City: <city.id> : <B><city.name>
                  </B>
 - Must use the option strict_slashes=False in route definition

Task 10 - States and State
 - Write a script that starts a Flask web application
     - Application myust be listening on 0.0.0.0:5000
 - Must use storage for fetching data from the storage engine (FileStorage
   or DBStorage) => from models import storage and storage.all(...)
 - To load all cities of a State:
    - If storage engine is DBStorage, must use cities relationship
    - Otherwise, use the public getter method cities
 - After each request, remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call this method storage.close()
 - Routes
    - /states: display a HTML page(inside the tag BODY)
        - H1 tag: "States"
        - UL tag: with the list of all State objects present in DBStorage
          sorted by name (A-Z)
            - LI tag: description of one State: <state.id>: <B><state.name></B>
    - /states/<id>: display a HTML page(inside the tag BODY)
        - if a State object is found with this id:
            - H1 tag: State
            - H3 tag: Cities
            - UL tag: with the list of City objects linked to the State sorted
              by name (A-Z)
                -LI tag: description of one City: <city.id>: <B><city.name></B>
        - Otherwise:
            - H1 tag:"Not found!" 
 - Must use the option strict_slashes=False in route definition

Task 11 - HBNB filters
 - Write a script that starts a Flask web application
     - Application myust be listening on 0.0.0.0:5000
 - Must use storage for fetching data from the storage engine (FileStorage
   or DBStorage) => from models import storage and storage.all(...)
 - To load all cities of a State:
    - If storage engine is DBStorage, must use cities relationship
    - Otherwise, use the public getter method cities
 - After each request, remove the current SQLAlchemy Session:
    - Declare a method to handle @app.teardown_appcontext
    - Call this method storage.close()
 - Routes:
    - /hbnb_filters: display a HTML page like 6-index.html, whit was done
      during 0x01. AirBnB clone - Web static
        - Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css
          from web_statix/styles/ to the folder web_flask/static/styles
        - Copy files icon.png and logo.png from web_static/images to the folder
          web_flask/static/images
        - Update .popover class in 6-filters.css to allow scrolling in the
          popover and a max height of 300 pixels.
        - Use 6-index.html content as source code for the template
          10-hbnb_filters.html
            - Replace the content of the H4 tag under each filter titls (H3
              States and H3 Amenities) by &nbsp;
        - State, City, Amenity objects must be loaded from DBStorage and
          sorted by name (A-Z)
    - Must use option strict_slashes=False