



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A6AHMGR%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T185016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIGZYk1vzSwP8QwVPNVBqSy9z3ggtYW%2BIDzKcqMwenStEAiBT0cmRHILfG%2FnXLtjLy%2BDJQd4tQ9ko%2BZWf4iTi0JjoFir%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMtzWyM9P1dqx9SBL9KtwDzfJgicl%2B%2Fh2pP1yqN%2FgpR5z7H00XA6uV%2FigCXJY1Y6M5h2JAOvM9ZR977wjydfEru79r6cTx4jA0ambz42%2BEm2UIWE4Bg17SxYLP6P%2FxwkFOCk1S24bskNeMdMNJRJ3IXKE1liVBbWThlISz%2BdX8e0YtAEqTWOGTLdr3Xr%2BryxVaSbkquMsmfRz5LynCCb7IJKyAdrkwSTtda3k44W9cDxxDzNmTua8yTKydZPs3P8%2B4X5vBvD%2BNjsDJDDy%2FV3JGC08WBD%2FOXF9JDGOhdqHmV5zSVihPaTvFUPY6c%2FIf%2BYBvQjiSf8XVXk3qGqazcwICTX4%2FxOy9TYJPaJ5ZkCcTyI3%2F6GoLvgFr96JfBo3ZyEv9%2F5n8fDYoDkX7tZk3AoG%2BpKtdzS6hbrfSUf0%2BUNM9LXUmfxLGrS1lq9f1GQxF%2BvN%2By6wpBuN3zRTPL1tOylaNAuzABYRy%2BczY3EcKZ4oS76yd6D4Z7d%2BpAs2q8arO%2B9Jky1jZAKV9GuLtUJ8joqi9xiQ2sYrCXD9twwNoasFbg2gXlLTrjvSwbILvbC4Ee2Mkwwxx40qszyQMQ7yjOU3EPpgZ1hOSlIybTwrvggtlSjYx9BDDZPA6eAaRQpWzxQqJMaKiM9qwSec67LUw%2BviIzAY6pgHCZs%2BvTCMdPaldcquXSZpnDQs7fljcvybGZejrK2V18secHP1dV63sSvsVMtKQSZHYjBDr16tqKBAJte2MYZ%2BznQCSTZFg0quuJiYpubhn9RPNYESW%2Bij8ASzYukS7RoDNPD6QigWBQLRO5Me2lmVdeC91To1qjd1pAnidGr38bMLRr3HVbJqtuIAlL4vM6BWwOVU8cRcnb%2BN6xoyKO6WMQztlNFn0&X-Amz-Signature=22f0a2be6d299c27b4e20e475a4e92dc896272428a67b1e4ba8792da4d96b339&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A6AHMGR%2F20260203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260203T185016Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDsaCXVzLXdlc3QtMiJGMEQCIGZYk1vzSwP8QwVPNVBqSy9z3ggtYW%2BIDzKcqMwenStEAiBT0cmRHILfG%2FnXLtjLy%2BDJQd4tQ9ko%2BZWf4iTi0JjoFir%2FAwgDEAAaDDYzNzQyMzE4MzgwNSIMtzWyM9P1dqx9SBL9KtwDzfJgicl%2B%2Fh2pP1yqN%2FgpR5z7H00XA6uV%2FigCXJY1Y6M5h2JAOvM9ZR977wjydfEru79r6cTx4jA0ambz42%2BEm2UIWE4Bg17SxYLP6P%2FxwkFOCk1S24bskNeMdMNJRJ3IXKE1liVBbWThlISz%2BdX8e0YtAEqTWOGTLdr3Xr%2BryxVaSbkquMsmfRz5LynCCb7IJKyAdrkwSTtda3k44W9cDxxDzNmTua8yTKydZPs3P8%2B4X5vBvD%2BNjsDJDDy%2FV3JGC08WBD%2FOXF9JDGOhdqHmV5zSVihPaTvFUPY6c%2FIf%2BYBvQjiSf8XVXk3qGqazcwICTX4%2FxOy9TYJPaJ5ZkCcTyI3%2F6GoLvgFr96JfBo3ZyEv9%2F5n8fDYoDkX7tZk3AoG%2BpKtdzS6hbrfSUf0%2BUNM9LXUmfxLGrS1lq9f1GQxF%2BvN%2By6wpBuN3zRTPL1tOylaNAuzABYRy%2BczY3EcKZ4oS76yd6D4Z7d%2BpAs2q8arO%2B9Jky1jZAKV9GuLtUJ8joqi9xiQ2sYrCXD9twwNoasFbg2gXlLTrjvSwbILvbC4Ee2Mkwwxx40qszyQMQ7yjOU3EPpgZ1hOSlIybTwrvggtlSjYx9BDDZPA6eAaRQpWzxQqJMaKiM9qwSec67LUw%2BviIzAY6pgHCZs%2BvTCMdPaldcquXSZpnDQs7fljcvybGZejrK2V18secHP1dV63sSvsVMtKQSZHYjBDr16tqKBAJte2MYZ%2BznQCSTZFg0quuJiYpubhn9RPNYESW%2Bij8ASzYukS7RoDNPD6QigWBQLRO5Me2lmVdeC91To1qjd1pAnidGr38bMLRr3HVbJqtuIAlL4vM6BWwOVU8cRcnb%2BN6xoyKO6WMQztlNFn0&X-Amz-Signature=999fa3aa6b3c0d54d50740163d17d8f7f1b4c830c5cff7d629baf6ac88a23f6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







