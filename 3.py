import requests

url_1 = "https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken"
url_2 = "https://api.blockcypher.com/v1/eth/main"

#измерение скорости ответа 1
response = requests.get(url_1)
time_1 = response.elapsed.total_seconds()
print(f"time_1: {time_1}")

response_1 = response.json()
print(f"result: {response_1['result']} -> {eval(response_1['result'])}")

#измерение скорости ответа 2
response = requests.get(url_2)
time_2 = response.elapsed.total_seconds()
print(f"time_2: {time_2}")

response_2 = response.json()
print(f"height: {response_2['height']}")

if time_1 > time_2:
    print("https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=YourApiKeyToken - быстрее")
elif time_1 == time_2:
    print("РАВНЫ")
else:
    print("https://api.blockcypher.com/v1/eth/main - быстрее")

#реобразование hex -> int
response_1 = eval(response_1["result"])

if response_1 > response_2["height"]:
    print("result больше")
elif response_1 == response_2["height"]:
    print("height = result")
else:
    print("height больше")
