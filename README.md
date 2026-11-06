



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIFNPNII%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T001307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIH3e%2BwgoHPccbA%2BumUk4WNJCmbT0sxd37%2F%2FbNSYHa7s5AiEA8ygI%2FTO%2Fr7%2BTAhab%2BOofMlMkGXtsG3GXAxYGBg1BsTsqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRKgidB6RB7KADu8yrcA0oV3U6oFbvuOFUklTNUUcmlvZRMN1xD49mGAdYqgwJ2EQB7S7M3orwsWYTMhcwhuqU2YS6iSU6GAhVB5LVBm69h0rO7ifjTdZJ5Jvj3d8Bu3LcJLFWd7QCU3K%2B8BXOsj7K3WhJ1%2FHPyMblw32yvPeKvAV%2BtZvpIPAMtOzC5AEXNu6ut%2FLBWHeF46iUHRN1SO44jVCLpluM%2BQ1HKtRLxiWuFraCV7VFNhxl7r8kWGI7LJCIEMRvHQveB0SaQvLa0Dej6orHCPSQaC5DTLJXY2IQMsoeFHDDBleU9O%2B5X3xV84JS4XVWkjvXk%2Ff2cQcNLo%2FTx%2F2n1dqDVP1zLS%2FQSWVZqUcws%2F8Ryy5LDWg3y6qjKskH897bkdpeE7qyue0oyfmAH6jYAzPg8u58l2XbfmlNJKOcJ%2FcABHPwmTEfwCCnr3i82fon69i5wrbNiTMHPj1gX6vPLOCsar%2BY0PZ0b5nr4np879KnWucjHq54NDlvLA05q%2BdBLdgxzTRYNT0VF0Qd%2FWnbSL%2BwfocGUVSIZch2ILHIEzBF3vgaP4Q%2F1p11I2C2zHeZX9Uk7WljBYWa8WU7RU9gG%2Fh8mKe9h5357dnHOJfEC0kxTStVtM6fu6nf1dNyatJXzxY%2BdvQQPMP3Bs9cGOqUBRUecX4zUMxvgljtu%2BNCYBSS%2BkuSFWIMMYbyCI7jopYuSdqFU5rfkNHBSD3iDRKIaxG7JlD5C0t4TF8fKcXbJsDHOy6H7SruJcxKjFeAZtR3VSGj8nXD7f6btMpruDxbirOyuXiRNABALOipJrINqCfMZoaqapHSHv13WAUl4M3UPO1wYHmi%2FyPnRHqagzYgh44FrzUNkbfma0Oz5v%2BI9yo%2F0amLB&X-Amz-Signature=dd367427f9619af27c774c807eb9dda732309c31b523a696b9417a75b63feca5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIFNPNII%2F20261106%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261106T001307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIH3e%2BwgoHPccbA%2BumUk4WNJCmbT0sxd37%2F%2FbNSYHa7s5AiEA8ygI%2FTO%2Fr7%2BTAhab%2BOofMlMkGXtsG3GXAxYGBg1BsTsqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLRKgidB6RB7KADu8yrcA0oV3U6oFbvuOFUklTNUUcmlvZRMN1xD49mGAdYqgwJ2EQB7S7M3orwsWYTMhcwhuqU2YS6iSU6GAhVB5LVBm69h0rO7ifjTdZJ5Jvj3d8Bu3LcJLFWd7QCU3K%2B8BXOsj7K3WhJ1%2FHPyMblw32yvPeKvAV%2BtZvpIPAMtOzC5AEXNu6ut%2FLBWHeF46iUHRN1SO44jVCLpluM%2BQ1HKtRLxiWuFraCV7VFNhxl7r8kWGI7LJCIEMRvHQveB0SaQvLa0Dej6orHCPSQaC5DTLJXY2IQMsoeFHDDBleU9O%2B5X3xV84JS4XVWkjvXk%2Ff2cQcNLo%2FTx%2F2n1dqDVP1zLS%2FQSWVZqUcws%2F8Ryy5LDWg3y6qjKskH897bkdpeE7qyue0oyfmAH6jYAzPg8u58l2XbfmlNJKOcJ%2FcABHPwmTEfwCCnr3i82fon69i5wrbNiTMHPj1gX6vPLOCsar%2BY0PZ0b5nr4np879KnWucjHq54NDlvLA05q%2BdBLdgxzTRYNT0VF0Qd%2FWnbSL%2BwfocGUVSIZch2ILHIEzBF3vgaP4Q%2F1p11I2C2zHeZX9Uk7WljBYWa8WU7RU9gG%2Fh8mKe9h5357dnHOJfEC0kxTStVtM6fu6nf1dNyatJXzxY%2BdvQQPMP3Bs9cGOqUBRUecX4zUMxvgljtu%2BNCYBSS%2BkuSFWIMMYbyCI7jopYuSdqFU5rfkNHBSD3iDRKIaxG7JlD5C0t4TF8fKcXbJsDHOy6H7SruJcxKjFeAZtR3VSGj8nXD7f6btMpruDxbirOyuXiRNABALOipJrINqCfMZoaqapHSHv13WAUl4M3UPO1wYHmi%2FyPnRHqagzYgh44FrzUNkbfma0Oz5v%2BI9yo%2F0amLB&X-Amz-Signature=0fb354891e99ba6cf4666d1c18ba6a0ce923f2963806be3026541b821642d65e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







