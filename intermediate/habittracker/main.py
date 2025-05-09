import requests
USERNAME = "anirudh456"
TOKEN = "anirudhmulky7"
pixela_endpoint = "https://pixe.la/v1/users"

params = {
    "token": TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}

response = requests.post(url=pixela_endpoint,json=params)
print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id": "graph23",
    "name": "Meditation",
    "unit":"Min",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
response1 = requests.post(url=graph_endpoint,json=graph_params, headers=headers)
print(response1)