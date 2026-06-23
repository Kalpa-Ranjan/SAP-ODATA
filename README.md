



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZTVI6SI%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T024535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDAlDR%2B6BxwnOGc1dTzoxCLtQc5yPWlYQbOqsQ7V2RU7QIgIAuPw8eIqm22xsRc4WnASdSNZUKm3ZTqV%2FVZR%2FhaFocq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDMeIGkLD17wmlGE5circA6WWSh2S4Zvm8kcwrOwr49fwpXZyrdBoN03DzTW6pfYpn%2FGCmnd23MV2U3n1sKdLjq9u1ep8%2BNmRJbkLkFIk6XpfdlFdpOJQvRLPmwo2xg7ty4B%2Bu8kjKcUYvDuUs8byRoPFNGRw5eGg4PhbvzysZIf5%2BFqAAbTU3TMtDZqFgDrll9rY0weJky8PHMZ%2BtOEyyczA704namndWtrp0yze07TSzsDhFisV9%2FNeN%2Fy9d6dWFc9t3lXuSkIEYWr0cgrgG3n0y%2Bw0%2Fd5c5u%2FKuDIzR8Cy4ewIQ6CMxtDIZF8DZO9%2FffsKE2M020kssJPKjEwlb17zLcFSewtBNKqPlBzTHhQxQ1aGjqPX2aSVbAcu%2BqgOCxiF1eUjT4eAocZIRKP5lLODc%2F99a%2BLEapl05ScwJeTecLKapsT0HXKv44FgE7%2BJr13KkFgULEvPWWsC0lzP%2FWLGgyb5khOh1iqOddwTK5hUYuvYjolwvR4YN82SBnpA3iZZipEqdYLuFKXCTKIBPQncRtjs5R0fXMHsESO4QFH443W38AKpPwOKKk0%2FOFlYo2Jmnk410b5S838fO3GGpNOg4hj449g5qLKvYtat0%2FqF1we2xyAoSd59z3JqK3Ir1yiGoEEhGbs9Ud9eMMbG59EGOqUBPkFn9Wuq7slnhiIBCFRREzuODghZtA%2FDjA%2FlQJVI0EHrh%2F2Hxh73V0RBu9K7e3v%2F%2Fz%2F3zWocPcVG%2B1zWZwIFajfMBdIirFrGR6%2FTU%2F%2FXqDmB79PRf2bgJeYdGa84eKCqeCag7Up4xmMYoohUdrKKqvlf5IEZGzgDC7l8GsxCMIFw%2Bh1pN9LooIpOY06f6mOfCPnCR4%2FOf%2Ftysi55noqtz2pyLFWS&X-Amz-Signature=6c8629c5b927d8ce3eabe852514fc31d3badf5cdfb84910ab6361778cfc8f59f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZTVI6SI%2F20260623%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260623T024535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJHMEUCIQDAlDR%2B6BxwnOGc1dTzoxCLtQc5yPWlYQbOqsQ7V2RU7QIgIAuPw8eIqm22xsRc4WnASdSNZUKm3ZTqV%2FVZR%2FhaFocq%2FwMIExAAGgw2Mzc0MjMxODM4MDUiDMeIGkLD17wmlGE5circA6WWSh2S4Zvm8kcwrOwr49fwpXZyrdBoN03DzTW6pfYpn%2FGCmnd23MV2U3n1sKdLjq9u1ep8%2BNmRJbkLkFIk6XpfdlFdpOJQvRLPmwo2xg7ty4B%2Bu8kjKcUYvDuUs8byRoPFNGRw5eGg4PhbvzysZIf5%2BFqAAbTU3TMtDZqFgDrll9rY0weJky8PHMZ%2BtOEyyczA704namndWtrp0yze07TSzsDhFisV9%2FNeN%2Fy9d6dWFc9t3lXuSkIEYWr0cgrgG3n0y%2Bw0%2Fd5c5u%2FKuDIzR8Cy4ewIQ6CMxtDIZF8DZO9%2FffsKE2M020kssJPKjEwlb17zLcFSewtBNKqPlBzTHhQxQ1aGjqPX2aSVbAcu%2BqgOCxiF1eUjT4eAocZIRKP5lLODc%2F99a%2BLEapl05ScwJeTecLKapsT0HXKv44FgE7%2BJr13KkFgULEvPWWsC0lzP%2FWLGgyb5khOh1iqOddwTK5hUYuvYjolwvR4YN82SBnpA3iZZipEqdYLuFKXCTKIBPQncRtjs5R0fXMHsESO4QFH443W38AKpPwOKKk0%2FOFlYo2Jmnk410b5S838fO3GGpNOg4hj449g5qLKvYtat0%2FqF1we2xyAoSd59z3JqK3Ir1yiGoEEhGbs9Ud9eMMbG59EGOqUBPkFn9Wuq7slnhiIBCFRREzuODghZtA%2FDjA%2FlQJVI0EHrh%2F2Hxh73V0RBu9K7e3v%2F%2Fz%2F3zWocPcVG%2B1zWZwIFajfMBdIirFrGR6%2FTU%2F%2FXqDmB79PRf2bgJeYdGa84eKCqeCag7Up4xmMYoohUdrKKqvlf5IEZGzgDC7l8GsxCMIFw%2Bh1pN9LooIpOY06f6mOfCPnCR4%2FOf%2Ftysi55noqtz2pyLFWS&X-Amz-Signature=f0cb3bcb12397d705add78e2fd871f9e595a98b3c65322b77bf2fd10e7e87983&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







