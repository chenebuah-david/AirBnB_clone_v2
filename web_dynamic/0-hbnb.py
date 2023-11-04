#!/usr/bin/python3
"""
    The Flask application
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from uuid import uuid4
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(error):
    """
        This closes the database session after each request
    """
    storage.close()


@app.route('/0-hbnb', strict_slashes=False)
def hbnb():
    """
        The flask route at /hbnb
        This fills the hbnb homepage
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    st_ct = []

    # Sort cities inside each states
    for state in states:
        st_ct.append([state, sorted(state.cities, key=lambda k: k.name)])

    amenities = storage.all(Amenity).values()
    amenities = sorted(amenities, key=lambda k: k.name)

    places = storage.all(Place).values()
    places = sorted(places, key=lambda k: k.name)

    values = {"states": states, "amenities": amenities,
              "places": places, "cache_id": uuid4()}

    return render_template('0-hbnb.html', **values)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
