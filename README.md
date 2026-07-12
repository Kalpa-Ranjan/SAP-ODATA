



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CL2NRI4%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T080743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICPQJqvqnL8%2FhlnfEdEWgNCcSq0JDNd%2B5vKAL3k%2BNsztAiBvR0XFm3arxLapjbVSCBFnZBfqyyJOWCkIEG9pHXam3SqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoh0dcPERVAa2k%2BD7KtwDrq6eXc2NSJYRPCQyvYNzkkSddYAK938zTXwPkFZSDjD5PxP9xRZqbL3bdIQiotXzwee3pGgOUw6paOf5vArWVAECnpOw3Ytq0LJEX3sa6e070taBKv8ARt7fl8mQzsA%2FNR1NNYewr6uNjgJ4Tq4RB07MUwHHaqdVmeMet%2Bo4n%2B%2BndsmGGoMa87%2F%2B9XSZTa68nRmNnZsSMivhN6i1ZT0zV3XD9jTNiuxqYZs0oQe7cS9S44vLpsJTAmZ9FCg4ljp656p%2FJJNmkdyRQCjMWVGnQTduq3XlzwlaQohOCHtvkA3Vtvpj4f0fQztu8b2b2cIg8gJQkz4nnfvD3P9tDTSHGxi7IV5G7ShNu51niojMykpKsCPoIN%2B0ksIkr%2FPtq0ROqoo%2FTCqSs0tvBMYpLj7fK0tUjfTsLJnlqDs06VeqLGbhhFVU4fSXydON5M47nYVJMT1qei7dsv3nXDdM1l%2FLubG6nF%2FqSHuaqioJ7PB1Lz%2B7k50kWZJaGAEdksX2Klb7GrKS20p0ZGGEm5NvbpId42nqgKS7aqmW8vzzymCvoP2hu2O1C269St0cE2mPIZEOQZY0%2F8YWCtL5ZfW6fcErRoT8MbvYEB5bNG4tzQBBhhH9qD8Mws0NWAQX3WIwwIrN0gY6pgEvaUC1RAJZRbhfHWyvWJUOnBXql33UlIXafXD97sVbPqzzSsClqUqIbr0K8AepW%2B6CjlO2ukWFnvkB8aIK8egMKAtVQgCqZlArag6Ydf5VoSWFaTvequZY6Ewo8Gl939KDmlVIFdLXPMOLwRMem%2F0ykNp%2BCJXiOUjCl4V5vPH%2ByhxVdmMF0%2FWOsgxjPGkTW36vLD7fb5GkV8HOKrdoVQ8xuH1WxOmJ&X-Amz-Signature=981789588d1b0f4959fe49d2c1c51bdda501b17a62264686a7adfa706fb72a03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CL2NRI4%2F20260712%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260712T080743Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCICPQJqvqnL8%2FhlnfEdEWgNCcSq0JDNd%2B5vKAL3k%2BNsztAiBvR0XFm3arxLapjbVSCBFnZBfqyyJOWCkIEG9pHXam3SqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMoh0dcPERVAa2k%2BD7KtwDrq6eXc2NSJYRPCQyvYNzkkSddYAK938zTXwPkFZSDjD5PxP9xRZqbL3bdIQiotXzwee3pGgOUw6paOf5vArWVAECnpOw3Ytq0LJEX3sa6e070taBKv8ARt7fl8mQzsA%2FNR1NNYewr6uNjgJ4Tq4RB07MUwHHaqdVmeMet%2Bo4n%2B%2BndsmGGoMa87%2F%2B9XSZTa68nRmNnZsSMivhN6i1ZT0zV3XD9jTNiuxqYZs0oQe7cS9S44vLpsJTAmZ9FCg4ljp656p%2FJJNmkdyRQCjMWVGnQTduq3XlzwlaQohOCHtvkA3Vtvpj4f0fQztu8b2b2cIg8gJQkz4nnfvD3P9tDTSHGxi7IV5G7ShNu51niojMykpKsCPoIN%2B0ksIkr%2FPtq0ROqoo%2FTCqSs0tvBMYpLj7fK0tUjfTsLJnlqDs06VeqLGbhhFVU4fSXydON5M47nYVJMT1qei7dsv3nXDdM1l%2FLubG6nF%2FqSHuaqioJ7PB1Lz%2B7k50kWZJaGAEdksX2Klb7GrKS20p0ZGGEm5NvbpId42nqgKS7aqmW8vzzymCvoP2hu2O1C269St0cE2mPIZEOQZY0%2F8YWCtL5ZfW6fcErRoT8MbvYEB5bNG4tzQBBhhH9qD8Mws0NWAQX3WIwwIrN0gY6pgEvaUC1RAJZRbhfHWyvWJUOnBXql33UlIXafXD97sVbPqzzSsClqUqIbr0K8AepW%2B6CjlO2ukWFnvkB8aIK8egMKAtVQgCqZlArag6Ydf5VoSWFaTvequZY6Ewo8Gl939KDmlVIFdLXPMOLwRMem%2F0ykNp%2BCJXiOUjCl4V5vPH%2ByhxVdmMF0%2FWOsgxjPGkTW36vLD7fb5GkV8HOKrdoVQ8xuH1WxOmJ&X-Amz-Signature=e0a40ea69754fd26eddd32cf519f50e93415645714b789ec28679bf21b7d5349&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







