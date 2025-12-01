



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BVGR5FH%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T062637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIBV8OKUpM5flpgY3cKXgnaBn%2FOFRv%2FJ2pgZrKCnov4SJAiEA8ncPGveZRQ6vTCdf1EyRTDw9I9TW4TjSd3JZrhLFSswqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaRq%2Bn%2F1Xxpp%2FuYHircAxUgv%2FqcQy2CgPwXLiI76FSS5J4S9sDg80yBKNqbPMQgNS0MD0JUr6cA7wK7B7zCS2JNQhrGlBNUAujSVRRaJa%2BVY6srBZgIzd0HrapTmpgmN3GGN0RIrmvjleQ4Fd8v3jgeVHbR2Xe4poXPa5%2Fi8WyW6%2F7b6T8MhQZKxQ3vMGPuMLe%2FiPCRdT%2FdprELXT09duTpvqf%2FB4Wvypk%2B7RpCUbEDtIANerc5nuolByhGRqYDzz8HThtlfa%2FyLxNsY4aga%2FgCNVxSrhPVrYh4LaM3eX1xu0sE8PpIcTyub9ISBIg%2FYpSUmbh1%2BOSWkZf1IKQJICoDF5O73DBAO4nCYFdwFEuWTxEpWEE9%2BgpRscjfkpRixGANkNcMJUE4NTEL%2FbogWX%2F4N%2FFqiJwGLGGW3D3LyHTfdVCinY4FiQKOTvJ3TPb9mcZoqZHev624EcQW8%2F5sAVtRaRxwZgZN3IeUmQRAOvfVHt396ctRfhIXTiiRd0Y8FULk%2FXa2k6eOHoI9gouodcHLbw8jCTmR6EzDTgBQUa10L9qIWZ9e5OCsp0jDB3RTz0oiQYKst0WeGQgW3x2NAJl625LjpTaX86sxc3ncASg2QSl9Z%2BG19jiyl%2FRDLFfLha9FIHN8%2BXk%2BW6IdMPiktMkGOqUBqrPbWFDSR69z8JAKw%2B7g%2B0zC2Q4g4v4yyu1tGM2r4qOHHIsSsbfhKq%2BRhEdr2X2vmDVnvQvYlxdI5hyHEZTKWDd5oB41z0wCNCI5G%2FSlpK0lB0Pie84r8hEtzPRH%2BGs0DCuNaaFlO1o2327%2FLq4RtsBtWw35AS9ryGIbXOpRav%2Bf4S9re34143WO%2FBlsysb1400I4qaKS72TmVP2faI3GA%2F7yzbj&X-Amz-Signature=3ced4326713ced6169a7331209f6e2ac7ce1195ed9785daa3e36cf694342f5c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BVGR5FH%2F20251201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251201T062637Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECwaCXVzLXdlc3QtMiJHMEUCIBV8OKUpM5flpgY3cKXgnaBn%2FOFRv%2FJ2pgZrKCnov4SJAiEA8ncPGveZRQ6vTCdf1EyRTDw9I9TW4TjSd3JZrhLFSswqiAQI9f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMaRq%2Bn%2F1Xxpp%2FuYHircAxUgv%2FqcQy2CgPwXLiI76FSS5J4S9sDg80yBKNqbPMQgNS0MD0JUr6cA7wK7B7zCS2JNQhrGlBNUAujSVRRaJa%2BVY6srBZgIzd0HrapTmpgmN3GGN0RIrmvjleQ4Fd8v3jgeVHbR2Xe4poXPa5%2Fi8WyW6%2F7b6T8MhQZKxQ3vMGPuMLe%2FiPCRdT%2FdprELXT09duTpvqf%2FB4Wvypk%2B7RpCUbEDtIANerc5nuolByhGRqYDzz8HThtlfa%2FyLxNsY4aga%2FgCNVxSrhPVrYh4LaM3eX1xu0sE8PpIcTyub9ISBIg%2FYpSUmbh1%2BOSWkZf1IKQJICoDF5O73DBAO4nCYFdwFEuWTxEpWEE9%2BgpRscjfkpRixGANkNcMJUE4NTEL%2FbogWX%2F4N%2FFqiJwGLGGW3D3LyHTfdVCinY4FiQKOTvJ3TPb9mcZoqZHev624EcQW8%2F5sAVtRaRxwZgZN3IeUmQRAOvfVHt396ctRfhIXTiiRd0Y8FULk%2FXa2k6eOHoI9gouodcHLbw8jCTmR6EzDTgBQUa10L9qIWZ9e5OCsp0jDB3RTz0oiQYKst0WeGQgW3x2NAJl625LjpTaX86sxc3ncASg2QSl9Z%2BG19jiyl%2FRDLFfLha9FIHN8%2BXk%2BW6IdMPiktMkGOqUBqrPbWFDSR69z8JAKw%2B7g%2B0zC2Q4g4v4yyu1tGM2r4qOHHIsSsbfhKq%2BRhEdr2X2vmDVnvQvYlxdI5hyHEZTKWDd5oB41z0wCNCI5G%2FSlpK0lB0Pie84r8hEtzPRH%2BGs0DCuNaaFlO1o2327%2FLq4RtsBtWw35AS9ryGIbXOpRav%2Bf4S9re34143WO%2FBlsysb1400I4qaKS72TmVP2faI3GA%2F7yzbj&X-Amz-Signature=0a095b00abce34a08c21ce7c8b5e42dedcdb1c553b16c13d98618ebf3040b4ae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







