



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4W52TT7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T062333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEQQrZrRzPux3oLbOTpE1%2BXAtOvxWyqEe2xX7gE2f0XXAiEA3p8XPRVBf94G8ncOX8pMaDspqvKi6nTC0nsqvAPMMokq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDPFaBYgyghHpAmkDUircAzdrC8%2FZ0QmeUSoNgt1xRUkIeaHWMIc4PO%2BKCXLFDZiukJ4PS4cH%2BUN8xfPfscggc9kWSMysHWxCjDImRUvwCN1LstfKUpg9qJWoXzw5V7307OlrdsWprid3fy6waXZQ3%2FaIMGFrovi4eGODwvAzjMUqJpvG2N2fXb0VkJfEVwQ0DgzDAUm5ZBXT%2ByvaxLp9ACPaGMmVM8KVIy%2F5EABnhzeP726oMBjHxCFGgAWQbn4hJul6vh62iHIkScR7WRc9TnqlQ12YNzonQXvZ2lzA19Or3xE3vFsSQgTJlMnqm8gl93%2Fz4rHlhmtcIgmDimCYczHNO%2FuJwMv29zksYFkfRVC7dMvuQBejcCWlN5xHZfbUkGwtTAqRNkzPUhMrBV%2BmVny93I1fbGY%2FHeaXHnKrH7yeH2df4aDKg%2BAHjvJHxyoFZeANVKYB19%2BCXczvHy1VJH6KgbuVbDKb%2BouNtNvDSjzBsI1455l6kWizi4eeUu1ofWWVpqXwpXChfCYmXi631tuS8%2BAyoVG7TA84aDRo7kJw62STlzZQ1Tv87loU9bLFJEEP9VibVP7TtdSQY0y5FRtdeBKFSVEC%2Fuu%2FYM5VO7qMmF5EdDAtKWk%2FNOiQFKwPIFk%2BDeRrqG4MlRQ6MO3p88kGOqUBhjmUNh3FycymaA9SNrN2z63iqYe%2FHYx3gDXK%2BCeT%2BfbHCygKiVS7l6QFxdHAO6qBtMH9hZM3e1HeKQ6C0HAwejJACPG3HbPNPEH0%2FAkbsL1XcVgPuGMFAR9MZpnr43D967jjdc9scpyoAoZTy%2F14RUPYBS6sPa8E8IxT0liXz8f1PyNed9KYb0Ui0isVQmKRANrQrHjgqi9%2F3Z%2FwsNtadUF1Q6QJ&X-Amz-Signature=e9c3e5ee8a0a7fe5f76dfe6422ebe5599833808d418610a7355d15fd4e606373&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4W52TT7%2F20251213%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251213T062333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIEQQrZrRzPux3oLbOTpE1%2BXAtOvxWyqEe2xX7gE2f0XXAiEA3p8XPRVBf94G8ncOX8pMaDspqvKi6nTC0nsqvAPMMokq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDPFaBYgyghHpAmkDUircAzdrC8%2FZ0QmeUSoNgt1xRUkIeaHWMIc4PO%2BKCXLFDZiukJ4PS4cH%2BUN8xfPfscggc9kWSMysHWxCjDImRUvwCN1LstfKUpg9qJWoXzw5V7307OlrdsWprid3fy6waXZQ3%2FaIMGFrovi4eGODwvAzjMUqJpvG2N2fXb0VkJfEVwQ0DgzDAUm5ZBXT%2ByvaxLp9ACPaGMmVM8KVIy%2F5EABnhzeP726oMBjHxCFGgAWQbn4hJul6vh62iHIkScR7WRc9TnqlQ12YNzonQXvZ2lzA19Or3xE3vFsSQgTJlMnqm8gl93%2Fz4rHlhmtcIgmDimCYczHNO%2FuJwMv29zksYFkfRVC7dMvuQBejcCWlN5xHZfbUkGwtTAqRNkzPUhMrBV%2BmVny93I1fbGY%2FHeaXHnKrH7yeH2df4aDKg%2BAHjvJHxyoFZeANVKYB19%2BCXczvHy1VJH6KgbuVbDKb%2BouNtNvDSjzBsI1455l6kWizi4eeUu1ofWWVpqXwpXChfCYmXi631tuS8%2BAyoVG7TA84aDRo7kJw62STlzZQ1Tv87loU9bLFJEEP9VibVP7TtdSQY0y5FRtdeBKFSVEC%2Fuu%2FYM5VO7qMmF5EdDAtKWk%2FNOiQFKwPIFk%2BDeRrqG4MlRQ6MO3p88kGOqUBhjmUNh3FycymaA9SNrN2z63iqYe%2FHYx3gDXK%2BCeT%2BfbHCygKiVS7l6QFxdHAO6qBtMH9hZM3e1HeKQ6C0HAwejJACPG3HbPNPEH0%2FAkbsL1XcVgPuGMFAR9MZpnr43D967jjdc9scpyoAoZTy%2F14RUPYBS6sPa8E8IxT0liXz8f1PyNed9KYb0Ui0isVQmKRANrQrHjgqi9%2F3Z%2FwsNtadUF1Q6QJ&X-Amz-Signature=b805e8c84d9f386279ef53a8a6c0ba0723a94bbece3090cdc70bc6da0c489387&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







