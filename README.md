



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JI54PHM%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T164543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCl%2FAZVpVqgmqd2vT3kSWy2Qy5LA4o9EOLnZCo29nZbDgIgOgZgWHN8u409qT5wCZIswK7ulglhsf0KrJkPNNkXS%2B4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDOBkb%2Fo9ANc2BqaRMircA%2BKq3edXsZ6WzhCzjfUF0kGD8%2B%2BN3%2FXygFc8KZfgaADl79mNTu%2Bbs9KX6%2BMGCj%2FyF0wdi2SCqqozNhXgmib6OlTc9ZI5aWWoqfArn0uNZOWwt5k5i4eW4yLLb6OzJ92%2BMuO9CFV8ryKk4OcNHacmy2FvUVCPEAxignFzjti%2BSwf3P8LHsmoZ6JdEsLQjfk3xUdT0HvWT%2B7I4t%2BnONaTuVyh%2B0VjZzgzgWY%2B2GO3FkYn8guTJdr68CgjUAmbADjzN2bJAveCKtd%2B5HDd4EydhejQ26vkNLdvwY7y5DhhT8qQETgZvJLvwFMuDXJ%2B5utYBXpzAbOO6CO%2BVZUaGHXsTaFwzPDd0uUdMov2Z7fjfIV95TlRL6JSWOmZB%2FIdgEPqiLNDco1p98bwvuP9lZf%2B4JYIEsiUCWhuLB0r7rpDpDSsJs8%2FRgz6oFsEDjPmif%2BdmQFjbP%2Bm7ZBK92HiyDx57d%2Bk0laJxwQ4HFaVC0oOyl7ORTRGhUYnMefKcvcz39CThmEzLpO5AwWzpHkN2kL2VZYHdJzLFf52R0Jjmo5NOYDGKkGVy4QaGNl0uw4WsyxzFeARu75lvQgmWjvQgUkt7pB2O7AtvAjP6GapiDC%2BkR%2Bnf3Cctd9ndbLyEH191MJi45dEGOqUBV7VWsMznQoOD4hI323nkE7lSr8Em0Mj5ZzNBSCkKjpEiTd%2FUseCUe78%2BX%2B%2FHt%2FUG2H8LjkJ8GLktWVf1m9axtLHk5jY5uvDgx2bxbmAndoUBPMC8xzaVmJyVgcYr3YkNDxf9yrv2OjIsHQZQzvSbKj59b2H%2BpEOkz5cS4n2RBofW6TBKL8%2BZtMG1vEDMHyoBnjv2wYy0iVj8WwZxv8A5ptZ5uAqH&X-Amz-Signature=300977fd9386a86872f7388d4896e0cca4f56536aa785f20aec168f31b7f6202&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664JI54PHM%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T164543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIQCl%2FAZVpVqgmqd2vT3kSWy2Qy5LA4o9EOLnZCo29nZbDgIgOgZgWHN8u409qT5wCZIswK7ulglhsf0KrJkPNNkXS%2B4q%2FwMICRAAGgw2Mzc0MjMxODM4MDUiDOBkb%2Fo9ANc2BqaRMircA%2BKq3edXsZ6WzhCzjfUF0kGD8%2B%2BN3%2FXygFc8KZfgaADl79mNTu%2Bbs9KX6%2BMGCj%2FyF0wdi2SCqqozNhXgmib6OlTc9ZI5aWWoqfArn0uNZOWwt5k5i4eW4yLLb6OzJ92%2BMuO9CFV8ryKk4OcNHacmy2FvUVCPEAxignFzjti%2BSwf3P8LHsmoZ6JdEsLQjfk3xUdT0HvWT%2B7I4t%2BnONaTuVyh%2B0VjZzgzgWY%2B2GO3FkYn8guTJdr68CgjUAmbADjzN2bJAveCKtd%2B5HDd4EydhejQ26vkNLdvwY7y5DhhT8qQETgZvJLvwFMuDXJ%2B5utYBXpzAbOO6CO%2BVZUaGHXsTaFwzPDd0uUdMov2Z7fjfIV95TlRL6JSWOmZB%2FIdgEPqiLNDco1p98bwvuP9lZf%2B4JYIEsiUCWhuLB0r7rpDpDSsJs8%2FRgz6oFsEDjPmif%2BdmQFjbP%2Bm7ZBK92HiyDx57d%2Bk0laJxwQ4HFaVC0oOyl7ORTRGhUYnMefKcvcz39CThmEzLpO5AwWzpHkN2kL2VZYHdJzLFf52R0Jjmo5NOYDGKkGVy4QaGNl0uw4WsyxzFeARu75lvQgmWjvQgUkt7pB2O7AtvAjP6GapiDC%2BkR%2Bnf3Cctd9ndbLyEH191MJi45dEGOqUBV7VWsMznQoOD4hI323nkE7lSr8Em0Mj5ZzNBSCkKjpEiTd%2FUseCUe78%2BX%2B%2FHt%2FUG2H8LjkJ8GLktWVf1m9axtLHk5jY5uvDgx2bxbmAndoUBPMC8xzaVmJyVgcYr3YkNDxf9yrv2OjIsHQZQzvSbKj59b2H%2BpEOkz5cS4n2RBofW6TBKL8%2BZtMG1vEDMHyoBnjv2wYy0iVj8WwZxv8A5ptZ5uAqH&X-Amz-Signature=b8857605bbf22e62aef5133a56b0a1a430317e7adfced8b904e3dabcdf01f2a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







