# API Documentation
    Overview-->
        Welcome to the API documentation for TaskManager. This API provides functionality to manage tasks. It includes endpoints for user authentication, task creation, retrieval, update, and deletion.

        Authentication -->
            To access protected endpoints, you need to authenticate using Token-based authentication. Include the token in the Authorization header of your HTTP request.

# Endpoints -->
1. Login -->

    Endpoint: api/login/
    Method: POST
    Authentication: Not required
    Request Body:
        {
        "username": "your_username",
        "password": "your_password"
        }

    Response:
        Status: 200 OK
        Body:
            {
            "token": "YOUR_AUTH_TOKEN"
            }

2. Add Task -->

    Endpoint: api/addTask/
    Method: POST
    Authentication: Required
    Request Body:
        {
        "title": "Your Task Title",
        "description": "Your Task Description"
        }

    Response:
        Status: 201 Created
        Body: Details of the created task

3. Get Task -->

    Endpoint: api/getTask/<int:task_id>/
    Method: GET
    Authentication: Required
    Response:
        Status: 200 OK
        Body: Details of the requested task

4. Get All Tasks -->

    Endpoint: api/allTasks/
    Method: GET
    Authentication: Required
    Response:
        Status: 200 OK
        Body: List of all tasks

5. Delete Task -->

    Endpoint: api/deleteTask/<int:task_id>/
    Method: GET
    Authentication: Required
    Response:
        Status: 204 No Content

6. Update Task -->

    Endpoint: api/updateTask/<int:task_id>/
    Method: POST
    Authentication: Required
    Request Body:
        {
        "title": "Updated Task Title",
        "description": "Updated Task Description"
        }

    Response:
        Status: 200 OK
        Body: Details of the updated task


# Error Handling -->

    400 Bad Request:
        Invalid request format or missing required fields.
    401 Unauthorized:
        Token missing or invalid.
    403 Forbidden:
        User doesn't have permission to access the resource.
    404 Not Found:
        The requested resource (task) doesn't exist.
    500 Internal Server Error:
        An unexpected error occurred on the server.