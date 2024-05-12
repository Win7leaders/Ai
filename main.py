import openllm
client=openllm.client.HttpClient('http://localhost:3000')
response=client.query('explain Blockchain')
print (response)