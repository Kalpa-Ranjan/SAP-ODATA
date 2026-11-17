



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFENLRFE%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T001241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAdBvn%2FR0bj3NWCJIyC%2BVVTI3nJx6JYbXWa4uBA8K0dHAiEAwl6wOKc3lsHRZ08%2FFsNp6p2AXs5l5aflP5AuVw2WtpgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQQtVRRCs7cv%2F4IIyrcA2eCTctRlPvDEdgUWFliOmBHGGqBfuQg7MQjARQUciTzxTFulH7bng4Dk5Wrl1Dl0PVINzEP4bdtIVVFJ83iNHnqdWRnEi6c%2BQiUN9JM1qhecuFKB%2B%2FbCwdIyXtoVK3LPbGQVHXRn0Ok%2FZhkRMOMnktODKoi8FImVdh%2B49V1dfC%2B8aiQYuAJfLYqEYsSnU%2BN8hAdeM6WFLDW0oW5Ixl1Q9oITMlVw1O%2FOz%2FndiJBG5b6Ugbfk%2Fvb2IKqVh%2Fwe1UJK2zydgBGNrp710jH9eVRhVlLe6bcy%2FVC%2FjhnG5y57IhEZa4ashEuu1nhk3U5P1%2BE4zaUQ7%2FZVcRMCgt58YZXKYiTdthJL7WjA0628FwgbrpZK97iw87PhMFrfKAzJwKjDuS9W7iu5%2Bxh6KWzwKTDnX7IvCV%2BIAfEfT6%2BbK7SfhlV8Ktn5FFF3zjIcUAUdkfOjHeOvxfPuiiopt5nu1P2%2Br9t0yqFEqEV3KmnN8tYZEvQ0cTh%2F3elQUgnQjQivMCPkeECBOEHOSGoAtaxc9iUsoUk%2B3QmwIlR9eBalAXRAn9dyK4xL5d1cGm%2FkLy2BWm2vtJ7ShHHTFpKMzOxUSjAEe4Ca8Fbyesm1otaTzOxRJncDq9wkIuUNtSBJzRDMICL7tcGOqUBJBjmUbThbb6oupookRtVpKCP5xrYrm%2FR2h57oB46TQqamlp6arO2Wul%2F7JC8fBplF%2BiLjuFQpUZ3%2FjIbJSZyY6NYsoT3VsOAued03ogk940fNUy6VUx7t0Tq0LSvNsa9JCCwI2vvKd%2BwZqX2I9%2FR5YuCRDSakOeM6j%2B0L3C8vGNKiXROpicYXr1MzcKMcVeiyaVy6dT0KnnW2KlvDgbsRDoZLHT9&X-Amz-Signature=72ef93c007155a80dd63de5d7da7948ff89c58957c730626be3f041f724cd4a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFENLRFE%2F20261117%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261117T001241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA8aCXVzLXdlc3QtMiJHMEUCIAdBvn%2FR0bj3NWCJIyC%2BVVTI3nJx6JYbXWa4uBA8K0dHAiEAwl6wOKc3lsHRZ08%2FFsNp6p2AXs5l5aflP5AuVw2WtpgqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPQQtVRRCs7cv%2F4IIyrcA2eCTctRlPvDEdgUWFliOmBHGGqBfuQg7MQjARQUciTzxTFulH7bng4Dk5Wrl1Dl0PVINzEP4bdtIVVFJ83iNHnqdWRnEi6c%2BQiUN9JM1qhecuFKB%2B%2FbCwdIyXtoVK3LPbGQVHXRn0Ok%2FZhkRMOMnktODKoi8FImVdh%2B49V1dfC%2B8aiQYuAJfLYqEYsSnU%2BN8hAdeM6WFLDW0oW5Ixl1Q9oITMlVw1O%2FOz%2FndiJBG5b6Ugbfk%2Fvb2IKqVh%2Fwe1UJK2zydgBGNrp710jH9eVRhVlLe6bcy%2FVC%2FjhnG5y57IhEZa4ashEuu1nhk3U5P1%2BE4zaUQ7%2FZVcRMCgt58YZXKYiTdthJL7WjA0628FwgbrpZK97iw87PhMFrfKAzJwKjDuS9W7iu5%2Bxh6KWzwKTDnX7IvCV%2BIAfEfT6%2BbK7SfhlV8Ktn5FFF3zjIcUAUdkfOjHeOvxfPuiiopt5nu1P2%2Br9t0yqFEqEV3KmnN8tYZEvQ0cTh%2F3elQUgnQjQivMCPkeECBOEHOSGoAtaxc9iUsoUk%2B3QmwIlR9eBalAXRAn9dyK4xL5d1cGm%2FkLy2BWm2vtJ7ShHHTFpKMzOxUSjAEe4Ca8Fbyesm1otaTzOxRJncDq9wkIuUNtSBJzRDMICL7tcGOqUBJBjmUbThbb6oupookRtVpKCP5xrYrm%2FR2h57oB46TQqamlp6arO2Wul%2F7JC8fBplF%2BiLjuFQpUZ3%2FjIbJSZyY6NYsoT3VsOAued03ogk940fNUy6VUx7t0Tq0LSvNsa9JCCwI2vvKd%2BwZqX2I9%2FR5YuCRDSakOeM6j%2B0L3C8vGNKiXROpicYXr1MzcKMcVeiyaVy6dT0KnnW2KlvDgbsRDoZLHT9&X-Amz-Signature=fc1b016e16e686259999c5b82d0863acaaaf65ffa04d6060e235011c6e804298&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







