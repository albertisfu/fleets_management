
# Fleet Management




## Deployment

To deploy this project first go to .docker directory

```bash
  cd .docker
```

Then run docker compose
```bash
sudo docker-compose up
```
Wait until django container is deployed

Open http://localhost:8000/ in your browser

Before login create a superuser, in a new terminal run:
```bash
docker-compose exec django sh
```
Inside run:

```bash
python manage.py createsuperuser
```
Create your user as required.

Go back to http://localhost:8000/ and login.

You'll be redirect to the dashboard without vehicles.

To create and manage vehicles you could use the API REST as follow:


## API Reference

#### Get Auth Token

```http
  POST /api/get_auth_token
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `username` | `string` | **Required**. Your username |
| `password` | `string` | **Required**. Your password |

Return
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `token` | `string` | Your Token|


#### Create Vehicle

```http
  POST /api/vehicles
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Header` | **Required**. Token xxxxxxxxx |
| `vehicle_id` | `int` | **Required**. Vehicle ID |

Return
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | id|
| `vehicle_id` | `int` | Vehicle ID|

#### GET Vehicles

```http
  POST /api/vehicles
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `Authorization` | `Header` | **Required**. Token xxxxxxxxx |

Return
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | id|
| `vehicle_id` | `int` | Vehicle ID|
| `current_location` | `string` | |
| `last_trip_distance` | `decimal` | |
| `total_distance` | `decimal` | |
| `fuel_efficency` | `decimal` | |
| `fuel_total_efficency` | `decimal` | |



#### Get Vehicle

```http
  GET /api/vehicles/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization` | `Header` | **Required**. Token xxxxxxxxx |

Return
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | id|
| `vehicle_id` | `int` | Vehicle ID|



#### Update Vehicle

```http
  PUT /api/vehicles/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization` | `Header` | **Required**. Token xxxxxxxxx |
| `vehicle_id`      | `string` | **Required**. Vehicle ID |

Return
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `id` | `int` | id|
| `vehicle_id` | `int` | Vehicle ID|


#### Delete Vehicle

```http
  DELETE /api/vehicles/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization` | `Header` | **Required**. Token xxxxxxxxx |


#### Send Instruction to Vehicle

```http
  PUT /api/send_instruction/${id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `Authorization` | `Header` | **Required**. Token xxxxxxxxx |
| `current_location`      | `string` | **Required**. City to Travel: 'city_a', 'city_b', 'city_c' |

You can find a json postman file of this API: Fleets.postman_collection.json


After add data, then you can return to Dashboard: http://localhost:8000/

You would see a vehicle marker over the map and you can click to see more details.
Also you can click over the buttón "Ver" on a vehicle to see travel history and more details.

Example: http://localhost:8000/detail_vehicle/1/

