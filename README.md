



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB73ONOD%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T005635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIHLZRZYIHUuVHyLv1SvzFTfpHdaBsaeJJXACuqNqyK9fAiB6CLz67qbz4C%2BWymf%2F1Ij8Jz2VV6box3%2FQZBdUxCeOtyr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIM7MkTXG7SA87%2BiGqjKtwDxsKBSC2kteaBW4XKiXN%2BClpKMOUsHWvSsrGmS%2FDqgYnNc3Olg89XWeYmP%2B23dZv4B9aSgGa8Ea%2BdDyPNwAOV%2Fh%2Fiqr7oZDz02oaiw0gcssjj1cO9c4yxdKjK47YnGi2jFhkjLzMlF4OYEScw52YO%2BCdbytw%2FpsnzMg0jJdlNF%2F4qiPEjVl%2FyBm6XEgc79ixv6zbUcplFBI8qRYhjB6XFJafdOgquh2sv8iJWquCf3ZCivpx8xkasBz%2BRoph9jhbpN98FowXB9tkiyfFDZYAaHOwZiaqcAbC0b09RtOE90cT2dDlDPuR47gMSzC57%2BgEirUjgBDJYGZkNOI1EjaitxQR%2FSjhKbb8azmRoj8w13YIIppSzs25nQFOvnKkMkDoh4%2BmSOq6KrBkIAZcoucM2H8fDcKuUpczn8LfcVohlcuDQNNhRL2S9rAGWmTFRR2LOYBecnT3fnZA3WEHDE1Rtz1LedN5quS%2Fn5pExLyJvZJtI%2Bhab5j8l6Ar0H3WA6dDfog1nBK8Mbd5rrQnYCXkjMh4C2djemDbQXjKHag65VT7Y%2FjbMJmlg16bsXxVVQqsQ6GNuEJMad4emwrAxiHUVaiVL9k4xPuF8Y5Ot38JbsqwogsYUe6XrXdzOWvEw4q2J1AY6pgF9E%2BjQ3b9JfrA24OVJ6shS3ShpKkjQ%2B9DQ7Nn4ZLk840VgaXybUtla1dhPO2x9q7DPNU4XJ1Tsb%2BlLw88x2VU6O0lM5fdZjG8n%2BOwslcZQRrDw5nGDFUeWchkSw1851aKf6FKD1%2BWj4VmcUeiadMG4mV4gRmtb1lDkcFb6FcraxJrKh2lPO19KQOzvvrv3oYgq%2BNERmP2tZ5Pkx8LvhUF5eRPF0o3U&X-Amz-Signature=d1355319c3dcccfade5394b1111c03022082c3e36e1dc7aab2c4113f47e566ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TB73ONOD%2F20260817%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260817T005635Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJGMEQCIHLZRZYIHUuVHyLv1SvzFTfpHdaBsaeJJXACuqNqyK9fAiB6CLz67qbz4C%2BWymf%2F1Ij8Jz2VV6box3%2FQZBdUxCeOtyr%2FAwg6EAAaDDYzNzQyMzE4MzgwNSIM7MkTXG7SA87%2BiGqjKtwDxsKBSC2kteaBW4XKiXN%2BClpKMOUsHWvSsrGmS%2FDqgYnNc3Olg89XWeYmP%2B23dZv4B9aSgGa8Ea%2BdDyPNwAOV%2Fh%2Fiqr7oZDz02oaiw0gcssjj1cO9c4yxdKjK47YnGi2jFhkjLzMlF4OYEScw52YO%2BCdbytw%2FpsnzMg0jJdlNF%2F4qiPEjVl%2FyBm6XEgc79ixv6zbUcplFBI8qRYhjB6XFJafdOgquh2sv8iJWquCf3ZCivpx8xkasBz%2BRoph9jhbpN98FowXB9tkiyfFDZYAaHOwZiaqcAbC0b09RtOE90cT2dDlDPuR47gMSzC57%2BgEirUjgBDJYGZkNOI1EjaitxQR%2FSjhKbb8azmRoj8w13YIIppSzs25nQFOvnKkMkDoh4%2BmSOq6KrBkIAZcoucM2H8fDcKuUpczn8LfcVohlcuDQNNhRL2S9rAGWmTFRR2LOYBecnT3fnZA3WEHDE1Rtz1LedN5quS%2Fn5pExLyJvZJtI%2Bhab5j8l6Ar0H3WA6dDfog1nBK8Mbd5rrQnYCXkjMh4C2djemDbQXjKHag65VT7Y%2FjbMJmlg16bsXxVVQqsQ6GNuEJMad4emwrAxiHUVaiVL9k4xPuF8Y5Ot38JbsqwogsYUe6XrXdzOWvEw4q2J1AY6pgF9E%2BjQ3b9JfrA24OVJ6shS3ShpKkjQ%2B9DQ7Nn4ZLk840VgaXybUtla1dhPO2x9q7DPNU4XJ1Tsb%2BlLw88x2VU6O0lM5fdZjG8n%2BOwslcZQRrDw5nGDFUeWchkSw1851aKf6FKD1%2BWj4VmcUeiadMG4mV4gRmtb1lDkcFb6FcraxJrKh2lPO19KQOzvvrv3oYgq%2BNERmP2tZ5Pkx8LvhUF5eRPF0o3U&X-Amz-Signature=1226798def16017760be0d7bade81cb4c48f527f220b35b56717aa32f1c12910&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







