



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJVDUK2%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T145608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtXUv9jvnncr0Hq81AZhmEURHJzeVjEhG8fTQzDbd4%2BgIhAMXaHT0DZ%2FOLO7HbSkflxS2iAz8KABfaPH6UhqjKXdPvKv8DCHsQABoMNjM3NDIzMTgzODA1IgwqJizX77NCn%2FUOnA4q3ANArkevBugJZ4zWABFgFDpzMLo%2B4AizakUfga73o%2F7cSp4oQNb%2F95zk6mrQgdm%2FVLbqb7vAJM3SbQ5eFSJdyGzPd1RZppfwLQn8tjFX9MGMoVUhsaNR8Q7TNVjO2ibyv0jfyY7%2FY7kUgDMBmBKDNt%2Bgq86VlGmf%2FYQZExmUovrcWiAYTrhlVFC6I25UKoBx6P9FRMNbH7S9YCYGS4z9jb5K8KotKK6jN1IV2mgYkcLgeqHm%2FeuY8hcH62JbbBAA4Xt4X3ZLHYIp6m6XuiVCy74ZN9Qjmgd7923bpfihDlalWmdlsxbnB5g8pz%2BsDJOifS115N76jYIv0XBytT6rfcy0rhyO14iMK6Zd%2BGNdo1tKaesHdwPzo6cYrcYCFeKisD692INwOb55i%2BLQ75eUpxwGzhDztjamCKe%2Bf3yf7bIOOfx3yD4BxmU%2BViADEV99nMtJyqbDvXnFtsSZ1FacJ6az7ZaRtF6gv3HUcD3TWX%2FgiDC5ykVkiH7CKY5sQiHnUxRV8PYpkM3IV3PgEdFRWpBbwtMIDjcZA%2BrdA72IhF7fOpr2G4dva9ycut3dORNpjdpdAT3LXrBtQUr2jk5wtL0zIbD6Tfo2h7YxaNd13cau2pnWFG%2BGbTsN%2FfXFEjDR19XQBjqkAXx1r%2By1o6dcMClbzSyd4CevrCIOvERCz3NyEQk%2FqaUkA371xYsJI9Do9CRhBuOPNzWGw2kkaYbzZYoOnVO14TDEJW6v34vIHzdxqCcyIY7yIYtjZLOux4Na2R4aNyAYXZQo6M7f6NSGds26RKuQzW5HZW%2F5x8%2Fa3x7m5u0PqXRVXebo86h1fWAhkLj5frBjP9e9r4DC3aygNNjxdr0ostN88j54&X-Amz-Signature=7bf2ba7c19d3870115181b8631ae715e55bd01613a28abc5c3d7694fa51f7635&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSJVDUK2%2F20260526%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260526T145608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtXUv9jvnncr0Hq81AZhmEURHJzeVjEhG8fTQzDbd4%2BgIhAMXaHT0DZ%2FOLO7HbSkflxS2iAz8KABfaPH6UhqjKXdPvKv8DCHsQABoMNjM3NDIzMTgzODA1IgwqJizX77NCn%2FUOnA4q3ANArkevBugJZ4zWABFgFDpzMLo%2B4AizakUfga73o%2F7cSp4oQNb%2F95zk6mrQgdm%2FVLbqb7vAJM3SbQ5eFSJdyGzPd1RZppfwLQn8tjFX9MGMoVUhsaNR8Q7TNVjO2ibyv0jfyY7%2FY7kUgDMBmBKDNt%2Bgq86VlGmf%2FYQZExmUovrcWiAYTrhlVFC6I25UKoBx6P9FRMNbH7S9YCYGS4z9jb5K8KotKK6jN1IV2mgYkcLgeqHm%2FeuY8hcH62JbbBAA4Xt4X3ZLHYIp6m6XuiVCy74ZN9Qjmgd7923bpfihDlalWmdlsxbnB5g8pz%2BsDJOifS115N76jYIv0XBytT6rfcy0rhyO14iMK6Zd%2BGNdo1tKaesHdwPzo6cYrcYCFeKisD692INwOb55i%2BLQ75eUpxwGzhDztjamCKe%2Bf3yf7bIOOfx3yD4BxmU%2BViADEV99nMtJyqbDvXnFtsSZ1FacJ6az7ZaRtF6gv3HUcD3TWX%2FgiDC5ykVkiH7CKY5sQiHnUxRV8PYpkM3IV3PgEdFRWpBbwtMIDjcZA%2BrdA72IhF7fOpr2G4dva9ycut3dORNpjdpdAT3LXrBtQUr2jk5wtL0zIbD6Tfo2h7YxaNd13cau2pnWFG%2BGbTsN%2FfXFEjDR19XQBjqkAXx1r%2By1o6dcMClbzSyd4CevrCIOvERCz3NyEQk%2FqaUkA371xYsJI9Do9CRhBuOPNzWGw2kkaYbzZYoOnVO14TDEJW6v34vIHzdxqCcyIY7yIYtjZLOux4Na2R4aNyAYXZQo6M7f6NSGds26RKuQzW5HZW%2F5x8%2Fa3x7m5u0PqXRVXebo86h1fWAhkLj5frBjP9e9r4DC3aygNNjxdr0ostN88j54&X-Amz-Signature=39bcc027f97ef52d42411ce380b81dd30d4b5e6979c2f84400028c68965b8c26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







