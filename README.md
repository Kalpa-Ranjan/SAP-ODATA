



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676M3FGTI%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T001402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFOapf9eZSk8sORCUoQ%2FA6Y%2F9s0CRITf0rUf0medqmp1AiA6Ey75k1%2BFY3TFlKnNHVEoYv%2B88%2BKZ9DbQ0XeBsPknlCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMNuVQZCslP33f7CTDKtwDlGbWbstLQILfy72gT%2FMaHONfBPycp1Qd7RIFFuuWnsKwm8Y5422%2FRKvkEIPDr0Pu%2BFo322Bc7PlBQ%2FbIMfTcgT%2FZ9WsK%2Btqi%2FwaF7uFZ2pL4GVQpybs16woVoTuxpsK%2FcGlLLIwgOd2Os3kQps46sNLCXa3Yj7kZJxmhWeqFctsJFAJRZih0HKU6mKTgYcKNMNQMW%2BV1UToetVELlp75DdH5SkeHEc1T%2FZNXkHrfgNxIK8%2FJbV5kaxLxdihqKxj3TGn3bFTQsZaafOe4mVlc6hhXeWNKy4J585iXDioSXwDVIrw8L4Ux71OMMbtP5RT864aExSGsXYNVY5Uh3eOXGa%2B1k4urBv64WRkVNUUGl6DqH9laqRc%2F9wi0byEr8G%2FYWgfIU3MqCGh3lPo7flga1pSZmXJ3%2BKrUkOev3oRIF%2BqAQL5%2FgAlkksHcsQ0ht3EfmKPG%2BrAq6eaPmBfshA02UFE6KwsMZ6xD2KmM1emt2OCsySHI%2FCSKvlnRjym0nTBlHmJJNixq%2FVSPxHPTSuxVmc%2FDJnBXNwSpa9iWnhgYwDXM1RYqN8joV4qFmJiVOO78fpuqq4dVyNrKLiZK48BrFJCQWYztAFMhvipHuNyYuYcupEKbhAejUflWm5ww%2BOON2AY6pgEHKnpjQmW2h%2FXfcfCqyihtviuR4uO2oNl%2F3a2SoHBGCJvQJk0uJhudczFt9wC5eFL4pwbtKYKK3U3vlAqS1DdqWhOIcpmUjTA%2FKOjGuq7Nc0uo3tmzQd6ZFQ6%2BR1Ls0p%2BRXBvASL7vyxz5n%2Fh9vpeZ6pfc0bNSXBjZsLRR7G1LffE8hSV5ik9foaD%2FZX9GyxpX2sgyHGCn%2FSRQK2If%2BKU4bgTi5ymH&X-Amz-Signature=d86915728161b3ccd7c5f5cf35d7c0fb82f4f1f5ba52bb51e1046438ac53fb0d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676M3FGTI%2F20261123%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261123T001402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFOapf9eZSk8sORCUoQ%2FA6Y%2F9s0CRITf0rUf0medqmp1AiA6Ey75k1%2BFY3TFlKnNHVEoYv%2B88%2BKZ9DbQ0XeBsPknlCr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMNuVQZCslP33f7CTDKtwDlGbWbstLQILfy72gT%2FMaHONfBPycp1Qd7RIFFuuWnsKwm8Y5422%2FRKvkEIPDr0Pu%2BFo322Bc7PlBQ%2FbIMfTcgT%2FZ9WsK%2Btqi%2FwaF7uFZ2pL4GVQpybs16woVoTuxpsK%2FcGlLLIwgOd2Os3kQps46sNLCXa3Yj7kZJxmhWeqFctsJFAJRZih0HKU6mKTgYcKNMNQMW%2BV1UToetVELlp75DdH5SkeHEc1T%2FZNXkHrfgNxIK8%2FJbV5kaxLxdihqKxj3TGn3bFTQsZaafOe4mVlc6hhXeWNKy4J585iXDioSXwDVIrw8L4Ux71OMMbtP5RT864aExSGsXYNVY5Uh3eOXGa%2B1k4urBv64WRkVNUUGl6DqH9laqRc%2F9wi0byEr8G%2FYWgfIU3MqCGh3lPo7flga1pSZmXJ3%2BKrUkOev3oRIF%2BqAQL5%2FgAlkksHcsQ0ht3EfmKPG%2BrAq6eaPmBfshA02UFE6KwsMZ6xD2KmM1emt2OCsySHI%2FCSKvlnRjym0nTBlHmJJNixq%2FVSPxHPTSuxVmc%2FDJnBXNwSpa9iWnhgYwDXM1RYqN8joV4qFmJiVOO78fpuqq4dVyNrKLiZK48BrFJCQWYztAFMhvipHuNyYuYcupEKbhAejUflWm5ww%2BOON2AY6pgEHKnpjQmW2h%2FXfcfCqyihtviuR4uO2oNl%2F3a2SoHBGCJvQJk0uJhudczFt9wC5eFL4pwbtKYKK3U3vlAqS1DdqWhOIcpmUjTA%2FKOjGuq7Nc0uo3tmzQd6ZFQ6%2BR1Ls0p%2BRXBvASL7vyxz5n%2Fh9vpeZ6pfc0bNSXBjZsLRR7G1LffE8hSV5ik9foaD%2FZX9GyxpX2sgyHGCn%2FSRQK2If%2BKU4bgTi5ymH&X-Amz-Signature=401b6cd2c07facd333717a9b7cebb6ae80234e23be0aba27dc18e5cb53976a39&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







