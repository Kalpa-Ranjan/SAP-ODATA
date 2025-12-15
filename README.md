



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMGF7V2J%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T182533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBZgATIkLklhRM9NqsIoeBX4iHj1784Qx2L0p8ZOSo4gIgei600R9Q4Dpwvrmwkw7A4rPil6IaSOCTwhsYnpTY4vgq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDHOi5xO0GrfLew2LIircA%2F7M2C4NIpZV5jTcAN%2B9mhg7V16bc8IAlhc2o5G3V7C%2FYKgcXAX6NS6kJKRvPQSeZE7DBoX1JJOqenPJFTAv5gbHpYZysMaBw8lKg%2BArnZ3H4BZp4OfQASBdAORpBVFzc%2FOf9H2E04O9epPwIKtFcZBPaDok6oSj7oq4q5WlQPary1qPH1RbuCbZIAXEmsGNl3%2BZJgSegZo7LuTYp5PNcW94iCPmsimc4mRbIeowdRl0b4zAvkjVLFjuRw7tTxyQlJi4jtCfToMgGS7sUsQLeMPGXPPRK%2BS0DfHV1uBw6cTeSoD7F1ceg6GoZ%2F419w7Wq0%2Bd2xCKg5O8J%2BD22NkpbWnz4fZiRwK1ZYO9ZKxM3bbXEDcquc631KHOvjV%2BvDSsUIPROdPqKF11MB%2B99n1dtoH5yYlebSg2gv43HgYOkvXuv7HBJU05YzRa5tD8Kd1m8A4%2FQEX7gZI1L6KifVuYt8opx2vi37MOYLVPf2ojz%2BXUOE1Xp3XUcm%2FZ0nCPuEmgEIfCGfq7cUfu7DUbohi4rUIAaUKjS3viG2bJhJoukPd9NQDY98%2FwKBz7apKugKPbt6Ezxh5vBQY0mzAy2u3kgOKOG%2FdC%2Fw7Lv6hW0mEMv0qLb1GCQTf4Hy6DhrSwMK2VgcoGOqUBvuaVDjkzp0Vi06x5xfCIUNNAHMo%2BClT3jtEezft%2B3m0NRBLS%2FP3kJ7VeSnqFOLuv556jakzcDCvck8dO8J8SaRe96HeG3rPLjoZaYJWSgs7KaLcfkehmAv9DMQz3A4Up1G4xtLswgfNjHsxVDP18v%2BtCsnTNWJow2P46pnbLEE%2FcBIKiBtoLlWdHN1%2FLINg4ly8OXHZ1IPjfQBmQRqp7DnlanOY7&X-Amz-Signature=4944fcbe8bcba7ca5f8506fa29ba508a5fa7e8beeae0354289e983d8bae6abb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMGF7V2J%2F20251215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251215T182533Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBZgATIkLklhRM9NqsIoeBX4iHj1784Qx2L0p8ZOSo4gIgei600R9Q4Dpwvrmwkw7A4rPil6IaSOCTwhsYnpTY4vgq%2FwMIUxAAGgw2Mzc0MjMxODM4MDUiDHOi5xO0GrfLew2LIircA%2F7M2C4NIpZV5jTcAN%2B9mhg7V16bc8IAlhc2o5G3V7C%2FYKgcXAX6NS6kJKRvPQSeZE7DBoX1JJOqenPJFTAv5gbHpYZysMaBw8lKg%2BArnZ3H4BZp4OfQASBdAORpBVFzc%2FOf9H2E04O9epPwIKtFcZBPaDok6oSj7oq4q5WlQPary1qPH1RbuCbZIAXEmsGNl3%2BZJgSegZo7LuTYp5PNcW94iCPmsimc4mRbIeowdRl0b4zAvkjVLFjuRw7tTxyQlJi4jtCfToMgGS7sUsQLeMPGXPPRK%2BS0DfHV1uBw6cTeSoD7F1ceg6GoZ%2F419w7Wq0%2Bd2xCKg5O8J%2BD22NkpbWnz4fZiRwK1ZYO9ZKxM3bbXEDcquc631KHOvjV%2BvDSsUIPROdPqKF11MB%2B99n1dtoH5yYlebSg2gv43HgYOkvXuv7HBJU05YzRa5tD8Kd1m8A4%2FQEX7gZI1L6KifVuYt8opx2vi37MOYLVPf2ojz%2BXUOE1Xp3XUcm%2FZ0nCPuEmgEIfCGfq7cUfu7DUbohi4rUIAaUKjS3viG2bJhJoukPd9NQDY98%2FwKBz7apKugKPbt6Ezxh5vBQY0mzAy2u3kgOKOG%2FdC%2Fw7Lv6hW0mEMv0qLb1GCQTf4Hy6DhrSwMK2VgcoGOqUBvuaVDjkzp0Vi06x5xfCIUNNAHMo%2BClT3jtEezft%2B3m0NRBLS%2FP3kJ7VeSnqFOLuv556jakzcDCvck8dO8J8SaRe96HeG3rPLjoZaYJWSgs7KaLcfkehmAv9DMQz3A4Up1G4xtLswgfNjHsxVDP18v%2BtCsnTNWJow2P46pnbLEE%2FcBIKiBtoLlWdHN1%2FLINg4ly8OXHZ1IPjfQBmQRqp7DnlanOY7&X-Amz-Signature=6cbb64e851a1fa4029ec14497ee9551a26a0da6b227f14feb037e07634bc926b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







