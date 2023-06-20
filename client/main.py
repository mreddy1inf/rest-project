import requests

def send_data(data):
    url = 'http://localhost:5000/api/data'
    payload = {'data': data}
    response = requests.post(url, json=payload)
    return response.json()

def main():
    user_input = input("Enter the data to send to the server: ")
    response = send_data(user_input)
    print("Server response:", response)

if __name__ == '__main__':
    main()