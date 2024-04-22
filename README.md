# TodoList Django Backend 

## Set up

First, clone this repository:
```
git clone https://github.com/Ru28/Todolist-Django-Backend.git
```

Install dependencies:
```
pip install -r requirements.txt
```

Apply migrations to your database
```
python manage.py migrate
```
To run the development server:
```
python manage.py runserver
```


![Screenshot (56)](https://github.com/Ru28/Todolist-Django-Backend/assets/54779977/bd82010c-b57e-4fe4-8fd9-30e29a936bd2)

![Screenshot (57)](https://github.com/Ru28/Todolist-Django-Backend/assets/54779977/9bf7e34a-2a9f-43e8-952a-4aebfc23f3ab)
![Screenshot (58)](https://github.com/Ru28/Todolist-Django-Backend/assets/54779977/426bc125-083e-4951-a44c-3230a1a441d2)

## GET Req {{URL}}/todos

### response
```json
[
    {
        "id": 3,
        "task": "Learn a React",
        "completed": false
    },
    {
        "id": 4,
        "task": "pray to god",
        "completed": false
    },
    {
        "id": 5,
        "task": "Learn JavaScript",
        "completed": false
    },
    {
        "id": 6,
        "task": "Learn Dev",
        "completed": false
    },
    {
        "id": 7,
        "task": "learn DSA",
        "completed": false
    },
    {
        "id": 8,
        "task": "play cricket",
        "completed": false
    },
    {
        "id": 10,
        "task": "go to gym",
        "completed": false
    }
]
```

## Patch Req {{url}}/<int:todo_id>

in Request Payload
```
{
  task: "Learn a React and Django"
}
```
response
```json
{
  "id": 3,
  "task": "Learn a React and Django",
  "completed": false
}
```

## Post {{url}}/todos
in Request payload
```
{
  id: 11
  status: "Active"
  task: "Watch IPL"
}
```

respnse
```josn
{
   "id:: 11,
   "task": "Watch IPL",
   "completed": false
}
```

## Delete {{url}}/<int:todo_id>

  


