



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U26MJKJQ%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T190120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEyi8XrpPQHnTOOvPbM%2FP7zDWp5LJLnOLzRNQ3KIeyq%2FAiEAyqlGO2aW0OPGNht0139Oob1YEAQAcztB9W8KqDO8qGoqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDChjI7X%2F81gnMN7O9ircAxA%2B4WyQy2XZbeAtM4ap62NirzenmhFnt0XHwImfUY8IhwaY0W30ZF7%2FfmTm3FPIUSdLfHMfu9N8w5VB3Jyi2OQcb0XBZeRJolk30a89okzzfmOm7Zv1SIXPWyNO9UcFv2A23yKHnRfsE8mPOAzWZucEjx7sVte%2FAb41dE9dCBj95jmVzm5FpoVh47g7d83a4ajQUczegWfq1zOFcTy5Qg9z926Xw0Kc6rrO30CBAZU91h67%2Bjq6otjp5TpXAlL7xZel%2Fr9QY1ayWMfV9K8i%2B8s6SL%2BEixE7v%2BVQAye7yiqCJBzxfiI44x86nVlpeN2OIWIgOaEtNWjanninRUcHKLGzbbgpKTEnIHNEJDAFdn8VpH7aX8gNsBZGsnCZ7ak8Fr%2BaOHIHtUBUKdGR29uw53xzCTnF0OTz%2BOAUYLYCfAU13a3D5lO3cK8o6xbxMppXWob5BqiB4KLr%2FUo6zsM%2Fz09Cqi5fj1nHub0V9K2W98iELWbCN9Z3j6GZImtMEf4HZB0fh6rGZYSexVBfzXtdUIuOovQSh0zEpRUXe40kmprgauyodmb6vUprHbXbDBcCAgigQNS%2BE0BOb4rGJE4xbVwo%2FYQlx10gaRvJ6Ikw494dbNPtPC9AMomwsiaqMO%2BRqNAGOqUBimT7HWpZh%2BhAlSRPviCV%2ByH0VH3TTnEwjAvS7XKoOJ8m8fsb82%2FTFuW8RmK9G3p6tgr2TI0TvyAMEC0ZXkfEYk437z1H1%2BXQwxAeH5yNmSn7qjWkH3BTatsU%2FcKXfCbonqSOMxL4yqd6G71hkikz%2Fy4HqYbIwoS0igCMaxWpnRPwEmUYD1XnfrLaDva0NTxzS4Z%2Fzc6HALPTLqHDes7ID%2Ffe%2BvfM&X-Amz-Signature=bd12428b3ae43fe13e3fdad99b99eb2475a1e7f962e349e9f4544e64db4715a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U26MJKJQ%2F20260517%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260517T190120Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEyi8XrpPQHnTOOvPbM%2FP7zDWp5LJLnOLzRNQ3KIeyq%2FAiEAyqlGO2aW0OPGNht0139Oob1YEAQAcztB9W8KqDO8qGoqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDChjI7X%2F81gnMN7O9ircAxA%2B4WyQy2XZbeAtM4ap62NirzenmhFnt0XHwImfUY8IhwaY0W30ZF7%2FfmTm3FPIUSdLfHMfu9N8w5VB3Jyi2OQcb0XBZeRJolk30a89okzzfmOm7Zv1SIXPWyNO9UcFv2A23yKHnRfsE8mPOAzWZucEjx7sVte%2FAb41dE9dCBj95jmVzm5FpoVh47g7d83a4ajQUczegWfq1zOFcTy5Qg9z926Xw0Kc6rrO30CBAZU91h67%2Bjq6otjp5TpXAlL7xZel%2Fr9QY1ayWMfV9K8i%2B8s6SL%2BEixE7v%2BVQAye7yiqCJBzxfiI44x86nVlpeN2OIWIgOaEtNWjanninRUcHKLGzbbgpKTEnIHNEJDAFdn8VpH7aX8gNsBZGsnCZ7ak8Fr%2BaOHIHtUBUKdGR29uw53xzCTnF0OTz%2BOAUYLYCfAU13a3D5lO3cK8o6xbxMppXWob5BqiB4KLr%2FUo6zsM%2Fz09Cqi5fj1nHub0V9K2W98iELWbCN9Z3j6GZImtMEf4HZB0fh6rGZYSexVBfzXtdUIuOovQSh0zEpRUXe40kmprgauyodmb6vUprHbXbDBcCAgigQNS%2BE0BOb4rGJE4xbVwo%2FYQlx10gaRvJ6Ikw494dbNPtPC9AMomwsiaqMO%2BRqNAGOqUBimT7HWpZh%2BhAlSRPviCV%2ByH0VH3TTnEwjAvS7XKoOJ8m8fsb82%2FTFuW8RmK9G3p6tgr2TI0TvyAMEC0ZXkfEYk437z1H1%2BXQwxAeH5yNmSn7qjWkH3BTatsU%2FcKXfCbonqSOMxL4yqd6G71hkikz%2Fy4HqYbIwoS0igCMaxWpnRPwEmUYD1XnfrLaDva0NTxzS4Z%2Fzc6HALPTLqHDes7ID%2Ffe%2BvfM&X-Amz-Signature=07e89f9e74440208c7391e9b6c17fd43c9587d11bea50307439adabe45d79759&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







