# Server-side code

This directory contains the server-side code for the REST API.

## Setup and Running

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the server by executing `python app.py`.

## REST API Endpoints

### POST /api/data

This endpoint is used to send data to the server for processing.

**Request Body**

The request body should be a JSON object with the necessary data fields.

Example:

{
"data": "Sample data"
}

**Response**

If the request is successful, the server will respond with a JSON object containing a success message.

Example response:

{
"message": "Data processed successfully"
}