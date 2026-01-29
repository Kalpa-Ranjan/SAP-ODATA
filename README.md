



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XOCOPYP%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T124532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE44G%2BqiiHpieteoKxD6uXxJ3b4Y5EeglZT0L%2Bc1lzwlAiEAqvL2q%2BQF9nrH9HeoEQHFmgX3UucweZz%2FnjDLPFhdizkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHtobwIn6ay%2F%2FJLjzircA8GXLVSyvRAZUAmFQLTeSnG9ahS4CuxhOtU9IJxEwc7VvkzWpiuLTLCpt2mhF5%2Fsuy6ok1Y342ZCkeBPsAN1zBhCr1m40MBtk8mEODgURJ8oDfcmsnoO8QqK%2Ff4%2Frn%2FV8PMABj2rPUiyNOPi9teUBv2XvHhcVehYyky77myZ9pUeGlDdtycsti0aof7inprpCDtyTe5GmkGQMjxa1l9uIKfaPfBl2%2Bt8dVu%2FK8BAN%2FOo2fom6aQ7S87w4rDbHh1nnZnt67aDuGorQSSHH%2BivsL%2BGPv94c00qFIzW2SrLt7o%2BsIz%2FhsuR6%2BPKP%2Fl0hr4Jzjdf0LTGTCEVH1zc18%2FMNiQKR4EwDtked7zOF0lyPJBxcwHnsj2YhtcHZ0j%2F1hIyoFr28HA9E10m5CYJ9CeuiaMqtUaBvSoMGOwrMjkNCmL4hyoQCQCKh1LvL8JYLgUc3OV4bTPbZXw%2BxT6o3AAQuGfXBWZlfEoSf5f%2B5QC%2FFH6M8WIB8M8cNUdnc2MQZkFhyH%2BgSXHOomtVpXkhomW%2FSWwqWqDuQGQw7vkPfn05pK9FrC8VJjpzrbDqrEL%2FEleG8J3UxUs0tpNHbkVJyZOiIYw%2FcDaWRirnx1kk0dhiQ%2BYgYONpakpSXCqOUyixMJeU7csGOqUBMsfvkWRaK7o2%2BlHomf%2BCgSIoMORo%2Fu2IPSZ9af9CLzCph7K0l%2Bs%2Fjui%2F%2BvtsptiboNu09LI8qYPPtioA5Qtphpr7id9Z1OqOpVY1rcsNqCPbrb7cZrzH4vnqo93SS75DaLfuuFhM%2FKiYIwC28GQNCsEsNhkHHSk0NDRyZader%2F1tZHi%2B6QOr%2F7iXyXZ4RHe2y58KVb28%2FZG20nKTe2rfNtjWB%2Fay&X-Amz-Signature=a5b26612d9bedbcd0925df0dbbbd29ff08911bf65d901651280f317388f65018&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XOCOPYP%2F20260129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260129T124532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE44G%2BqiiHpieteoKxD6uXxJ3b4Y5EeglZT0L%2Bc1lzwlAiEAqvL2q%2BQF9nrH9HeoEQHFmgX3UucweZz%2FnjDLPFhdizkqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHtobwIn6ay%2F%2FJLjzircA8GXLVSyvRAZUAmFQLTeSnG9ahS4CuxhOtU9IJxEwc7VvkzWpiuLTLCpt2mhF5%2Fsuy6ok1Y342ZCkeBPsAN1zBhCr1m40MBtk8mEODgURJ8oDfcmsnoO8QqK%2Ff4%2Frn%2FV8PMABj2rPUiyNOPi9teUBv2XvHhcVehYyky77myZ9pUeGlDdtycsti0aof7inprpCDtyTe5GmkGQMjxa1l9uIKfaPfBl2%2Bt8dVu%2FK8BAN%2FOo2fom6aQ7S87w4rDbHh1nnZnt67aDuGorQSSHH%2BivsL%2BGPv94c00qFIzW2SrLt7o%2BsIz%2FhsuR6%2BPKP%2Fl0hr4Jzjdf0LTGTCEVH1zc18%2FMNiQKR4EwDtked7zOF0lyPJBxcwHnsj2YhtcHZ0j%2F1hIyoFr28HA9E10m5CYJ9CeuiaMqtUaBvSoMGOwrMjkNCmL4hyoQCQCKh1LvL8JYLgUc3OV4bTPbZXw%2BxT6o3AAQuGfXBWZlfEoSf5f%2B5QC%2FFH6M8WIB8M8cNUdnc2MQZkFhyH%2BgSXHOomtVpXkhomW%2FSWwqWqDuQGQw7vkPfn05pK9FrC8VJjpzrbDqrEL%2FEleG8J3UxUs0tpNHbkVJyZOiIYw%2FcDaWRirnx1kk0dhiQ%2BYgYONpakpSXCqOUyixMJeU7csGOqUBMsfvkWRaK7o2%2BlHomf%2BCgSIoMORo%2Fu2IPSZ9af9CLzCph7K0l%2Bs%2Fjui%2F%2BvtsptiboNu09LI8qYPPtioA5Qtphpr7id9Z1OqOpVY1rcsNqCPbrb7cZrzH4vnqo93SS75DaLfuuFhM%2FKiYIwC28GQNCsEsNhkHHSk0NDRyZader%2F1tZHi%2B6QOr%2F7iXyXZ4RHe2y58KVb28%2FZG20nKTe2rfNtjWB%2Fay&X-Amz-Signature=1f96b92cfe8c53d4fcf950a31db6bea6bfcb85e9f1cabcb21820a36073f46fe3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







