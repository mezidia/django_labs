# MongoDB

## Overview

MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License (SSPL).

## Usage

We used [pymongo library](https://github.com/mezidia/medivac/blob/main/database.py) to make a work with
database easier. Constructor of the class has a path to database as a variable.

There are several main methods:

- [insert route](https://github.com/mezidia/medivac/blob/main/app.py#L13-L45)
- [insert car](https://github.com/mezidia/medivac/blob/main/app.py#L48-L65)
- [insert place](https://github.com/mezidia/medivac/blob/main/app.py#L68-L85)
- [delete route](https://github.com/mezidia/medivac/blob/main/app.py#L88-L104)
- [delete car](https://github.com/mezidia/medivac/blob/main/app.py#L107-L123)
- [delete place](https://github.com/mezidia/medivac/blob/main/app.py#L126-L142)
- [update route](https://github.com/mezidia/medivac/blob/main/app.py#L145-L174)
- [update car](https://github.com/mezidia/medivac/blob/main/app.py#L177-L182)
- [update place](https://github.com/mezidia/medivac/blob/main/app.py#L185-L190)
- [get route](https://github.com/mezidia/medivac/blob/main/app.py#L193-L215)
- [get car](https://github.com/mezidia/medivac/blob/main/app.py#L218-L236)
- [get place](https://github.com/mezidia/medivac/blob/main/app.py#L239-L257)

All these methods has docstrings, so you can read what they do and which parameters takes.

## Example

There is [file with implementation](https://github.com/mezidia/medivac/blob/main/app.py),
but you can also view the code below:

```python
routes_client = Client(os.getenv('DB_PASS', 'password'), 'medivac', 'routes')
cars_client = Client(os.getenv('DB_PASS', 'password'), 'medivac', 'cars')
places_client = Client(os.getenv('DB_PASS', 'password'), 'medivac', 'places')


def insert_route():
    """
    Function for inserting data into 'routes' table
    :return: MessageBox call
    """
    route_name = entries['route_name'].get()
    place_from = entries['place_from'].get()
    place_to = entries['place_to'].get()
    price = entries['price'].get()
    car = entries['car_name'].get()

    if all(entries.values()):
        route = {
            'name': route_name,
            'place_from': place_from,
            'place_to': place_to,
            'price': price,
            'car': car
        }
        result = routes_client.insert(route)
        pprint.pprint(result)
        if result:
            entries['route_name'].delete(0, 'end')
            entries['place_from'].delete(0, 'end')
            entries['place_to'].delete(0, 'end')
            entries['price'].delete(0, 'end')
            entries['car_name'].delete(0, 'end')
            show()
            message_box.showinfo('Insert Status', 'Inserted successfully')
        else:
            message_box.showerror('Insert Status', 'An error occurred while inserting')
    else:
        message_box.showerror('Insert Status', 'All fields are required')
```
