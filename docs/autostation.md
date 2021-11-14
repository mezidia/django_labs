# Autostation app

## How to start

First of all launch the script and see the opened window by the command in terminal:

```bash
python app.py
```

You will see window like this:

![](images/Start.png)

Here you can see all available routes, cars and routes in the list boxes:

![](images/Start.png)

You can do different operations here:

- insert data;
- update data;
- delete data;
- get data;

## Routes

### Insert

To insert a route you need to fill the **name of the route**, **places from** and **to**, **price** of the route and
**car identifier** like this and press button "insert" in the section "Work with routes":

![](images/InsertRoutes.png)

### Update

To update a route you need to fill the **name of the route** and all other fields - changed or not, but every field,
like this and then press button "update" in the section "Work with routes":

![](images/UpdateRoutes.png)

### Delete

To delete a route you need to fill the **name of the route** like this and then press button "delete" in the section
"Work with routes":

![](images/DeleteRoutes.png)

### Get

To get a route you need to fill the **name of the route** like this and then press button "get" in the section
"Work with routes":

![](images/GetRoutes.png)

## Cars

### Insert

To insert a car you need to fill the **name of the car** like this and press button "insert" in the section
"Work with cars":

![](images/InsertCars.png)

### Update

You can't to update the place in our app.

### Delete

To delete a car you need to fill the **id of the car** like this and then press button "delete" in the section
"Work with cars":

![](images/DeleteCars.png)

### Get

To get a car you need to fill the **id of the car** like this and then press button "get" in the section
"Work with cars":

![](images/GetCars.png)

## Places

### Insert

To insert a place you need to fill the **name of the place** like this and press button "insert" in the section
"Work with places":

![](images/InsertPlaces.png)

### Update

You can't to update the place in our app.

### Delete

To delete a place you need to fill the **name of the place** like this and then press button "delete" in the section
"Work with places":

![](images/DeletePlaces.png)

### Get

To get a car you need to fill the **name of the place** like this and then press button "get" in the section
"Work with places":

![](images/GetPlaces.png)

## Export

### To SQLite

To export Database to SQLite click this button

![](images/ExportSQLite.png)

### To PostgreSQl

To export Database to PostgreSQL click this button

![](images/ExportPostgreSQL.png)

## Code of the app

The full length of the app is near **500 lines**, so it is better to watch the code at
[GitHub](https://github.com/mezidia/medivac/blob/main/app.py). You won't get lost, because there are many comments.
