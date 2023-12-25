# Codename Scratch n Claw
## Getting Started
```
docker-compose up --build
```
## API documentation
### Model
Pet
- Owner
- Pet Species
- Pet Name
- Level
- Strength
- Defense
- Hit Points

Ability
- Ability Name
- Abiility Type

Ability Type
- Type Name

Species
- Species Name

## API URLs
| End Point  | Method  | URL  |
|---|---|---|
| Get a list of pets  | GET  | http://localhost:8000/api/pets/  |
| Get a specific pet  | GET  | http://localhost:8000/api/pets/:id  |
| Create a pet  | POST  | http://localhost:8000/api/pets/  |
| Delete a pet  | DELETE  | http://localhost:8000/api/pets/:id  |
| Update a pet  | DELETE  |  http://localhost:8000/api/pets/:id |

## CRUD Operations
To get a list of pets send a post request to the appropriate url with nothing in the body of the request. It should return:
```
[
    { 
        "owner": "Admin",
        "pet_name": "Professor Boh Boh",
        "pet_species": "Clownee",
        "level": 1,
        "strength": 1,
        "defense": 1,
        "hit_points": 1,
    },{ 
        "owner": "Admin",
        "pet_name": "Professor Boh Boh",
        "pet_species": "Clownee",
        "level": 1,
        "strength": 1,
        "defense": 1,
        "hit_points": 1,
    }
]
```

### Species
| End Point  | Method  | URL  |
|---|---|---|
| Get a list of species  | GET  | http://localhost:8000/api/species/
| Get a specific species  | GET  | http://localhost:8000/api/species/:id
| Create a species  | POST  | http://localhost:8000/api/species/
| Delete a species  | DELETE  | http://localhost:8000/api/species/:id
| Update a species  | PUT  |  http://localhost:8000/api/species/:id

### CRUD Operations
To get a list of pets send a post request to the appropriate url with nothing in the body of the request. It should return:
```
[
    { 

    }
]
```

### Accounts
| End Point  | Method  | URL  |
|---|---|---|
| Get a list of accounts  | GET  | http://localhost:8000/api/account/
| Get a specific account  | GET  | http://localhost:8000/api/account/:id
| Create a account  | POST  | http://localhost:8000/api/account/
| Delete a account  | DELETE  | http://localhost:8000/api/account/:id
| Update a account  | DELETE  |  http://localhost:8000/api/account/:id

### CRUD Operations
To get a list of pets send a post request to the appropriate url with nothing in the body of the request. It should return:
```
[
    { 

    }
]
```