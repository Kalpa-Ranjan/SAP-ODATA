



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZI53SXT%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T011053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyBl2XZmwda2g%2F%2B%2BITRiXmtFWfMiuVhGlI4zqufiv8pQIhANscYkFyNzOWOi65JpS2vwCYsdNC%2Bc7GNUT31gPmcQyYKv8DCGkQABoMNjM3NDIzMTgzODA1IgyO0wrlxWittOxsv04q3AMaxuDj%2BB0qLn9x6xxf8YK%2BkMRxQN%2BnRi77QK2j9htbVhr0qCNDzq4L%2Bs%2BJ3stX0%2BdPzzQWA%2BTISJ69OP6%2BssH8y1N%2BksIjqB8scC2UdO78TY8x6uFqTuBtEG4G1tFI2qIgGVhivCx5f2RudzOKY98qEkJBJpF36MdQVb6Q4ROE9GVARtOXVIU%2FVlObmouasLkM0AYnr6AEQT8pv2oWih2u6zCnNI%2BkYT2jw0dDvCN0aMOG33d5qntZiRKGv1NSwbs1fWR%2F0wtDBtJ0BdGk275s%2FBU7vNDMAs3jPZQTG%2BAvjeDuA2IWKmjoliD8h%2BAW3xWH91l%2FmF1MnLovoFIl03RLwU5e1PVKOVB6%2FfCYWELuSvnpFGg6E%2Bnf%2FFNWHVwZZlLXS6JF%2B7fhPgO%2F8%2BotRbuUQ9t%2Bn3HTaBUXOncZVjG54%2B9OeOpoOlpiLqtRdl64gtQaWvUABCzLmn3RalilE4iuA8%2FsOtnRRzrJyjjvgoSKfJgRgaOYkfb9gE8cNW8u7Nx5Y6yVJ%2F7h2JeKgMAacty%2BxtSdLF%2BXvIkUR3kV%2BIQzI9VDVM%2FooXlFpwysckexLfY%2FuJQIoT1OnQo8SoTs%2FKLvYe8di1PUubKe3%2BZ6Z8Lpo7dOdb%2BoiW3AQBm%2FpzDP6M3JBjqkAQNI3igjtIIxBagu54%2BXlyBXtUlyjNVyzlJ9eh0R6%2FcB1dP5CEctDOz7tmPeSwNvySiqEEIK14ixDS%2Bi5q%2FvVfF2pDUc%2BZCC388cwH%2BSfdyWvO2sD57aFD6axsoqz5cOxo6oupm7DiEsRkQ8lZNAJ1z5c%2F2Rk4LedP6amjlXzSZjnyW1FzsW8ARJXUjjYqey%2FEzYAts3V32A9yYQeE49mOZrElwm&X-Amz-Signature=4bfad9ccf1c088a1cb346626428ba4729404a5d4995353bceb1680a0d5080df1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ZI53SXT%2F20251206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251206T011053Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyBl2XZmwda2g%2F%2B%2BITRiXmtFWfMiuVhGlI4zqufiv8pQIhANscYkFyNzOWOi65JpS2vwCYsdNC%2Bc7GNUT31gPmcQyYKv8DCGkQABoMNjM3NDIzMTgzODA1IgyO0wrlxWittOxsv04q3AMaxuDj%2BB0qLn9x6xxf8YK%2BkMRxQN%2BnRi77QK2j9htbVhr0qCNDzq4L%2Bs%2BJ3stX0%2BdPzzQWA%2BTISJ69OP6%2BssH8y1N%2BksIjqB8scC2UdO78TY8x6uFqTuBtEG4G1tFI2qIgGVhivCx5f2RudzOKY98qEkJBJpF36MdQVb6Q4ROE9GVARtOXVIU%2FVlObmouasLkM0AYnr6AEQT8pv2oWih2u6zCnNI%2BkYT2jw0dDvCN0aMOG33d5qntZiRKGv1NSwbs1fWR%2F0wtDBtJ0BdGk275s%2FBU7vNDMAs3jPZQTG%2BAvjeDuA2IWKmjoliD8h%2BAW3xWH91l%2FmF1MnLovoFIl03RLwU5e1PVKOVB6%2FfCYWELuSvnpFGg6E%2Bnf%2FFNWHVwZZlLXS6JF%2B7fhPgO%2F8%2BotRbuUQ9t%2Bn3HTaBUXOncZVjG54%2B9OeOpoOlpiLqtRdl64gtQaWvUABCzLmn3RalilE4iuA8%2FsOtnRRzrJyjjvgoSKfJgRgaOYkfb9gE8cNW8u7Nx5Y6yVJ%2F7h2JeKgMAacty%2BxtSdLF%2BXvIkUR3kV%2BIQzI9VDVM%2FooXlFpwysckexLfY%2FuJQIoT1OnQo8SoTs%2FKLvYe8di1PUubKe3%2BZ6Z8Lpo7dOdb%2BoiW3AQBm%2FpzDP6M3JBjqkAQNI3igjtIIxBagu54%2BXlyBXtUlyjNVyzlJ9eh0R6%2FcB1dP5CEctDOz7tmPeSwNvySiqEEIK14ixDS%2Bi5q%2FvVfF2pDUc%2BZCC388cwH%2BSfdyWvO2sD57aFD6axsoqz5cOxo6oupm7DiEsRkQ8lZNAJ1z5c%2F2Rk4LedP6amjlXzSZjnyW1FzsW8ARJXUjjYqey%2FEzYAts3V32A9yYQeE49mOZrElwm&X-Amz-Signature=4f7fd2146087f8708bc65d41f9d83dd0dbdfba3ab572065e344558a72670b957&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







