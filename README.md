



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY4OPBTQ%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T182238Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI2fYerfgaj71nopU28wj1PkBRZPe%2FzouqE1ayI2fsqwIhAPyHckzv49cP9NPK1ENx8rKB610b%2BRtObUL5wC8xvDwCKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4vsdUwZcpfZXme8cq3AMUggZ0VnqDpd1f7CirDcmIaVXx66r1qgslUyHb0KVFcDjvO4L5A4WAVgCvmM%2FS9%2BGassUgvpa5sq3ou%2BIce2VIMLN51xrqoZE4XHBVSXh2%2FkIlTPn2VBCkZRlECpwBIEJiBg2ZCwHbIT2iSj5Ow0hfLkmrVPH7aeKwtGaytYdYpC1HoLEiSs%2BUp%2FAPVpCxHU2dFoeB4I2wA3mGwyMG6QiBAH4NicekNmpikVP4X%2FS9lCVcl4e1j3Z2kNIkhxyjHVDNxwiQCVtiHGO7gL%2FQpmf1zC5qZUjx7ujS30egA75bWposIsje2h9vaLozpSttsjA3j6Neh0yzqlZbyfOWSGAIcKwR2rELN7ZR8vCvCFmFf%2BQODz0oqU1pNC%2BQrzTF4QAnuvI1g6oxAU9qAl3fZSG%2Fk1wIrlVMfVXUTMclnVnF0A4J5W3sVh7%2F6DfLVQ82XsTWo5Mn1nQW%2FOgR2HBqEEOp7yRkqBAyxcSbCZAOU026ubfDS8NBshbykdIRlXODGcMQh3emVPf1PO1P21fyxNeXftm9kqUFC4a9%2FoMzZbaw54CKIQJK%2FBCu85iqBGd2zPQyO2BPk6PdnjB7TojZTZckBN9Txd%2Bz1h7G1S8wW4wTahjeqSOzpAVuYV%2B8wzCw3YnLBjqkAcxILEpugndMTHraIpgSPluyMLMAl%2FYXYdqmH%2FV5pq6rNrhaXLmAqx9giR8JzhBCQrR1oE0ZiJxDhEK7%2BprR8tFdRnUxfZygHGsi6cUjPGZVZ9e50i1mRuk4rgVaA77mkJMhJGMkPap24jH6u3E98buq2vKJqasvW1ttgOdr%2BnQdMsTZ%2FZWw2v5ug06UXGq6u1qcPveUSf1MqVYXESccc0ym4f%2BE&X-Amz-Signature=6199ae9ef317bf3a737d10a3c452085142fbcaafe590c6038008dba210910bf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RY4OPBTQ%2F20260110%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260110T182239Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDI2fYerfgaj71nopU28wj1PkBRZPe%2FzouqE1ayI2fsqwIhAPyHckzv49cP9NPK1ENx8rKB610b%2BRtObUL5wC8xvDwCKogECMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy4vsdUwZcpfZXme8cq3AMUggZ0VnqDpd1f7CirDcmIaVXx66r1qgslUyHb0KVFcDjvO4L5A4WAVgCvmM%2FS9%2BGassUgvpa5sq3ou%2BIce2VIMLN51xrqoZE4XHBVSXh2%2FkIlTPn2VBCkZRlECpwBIEJiBg2ZCwHbIT2iSj5Ow0hfLkmrVPH7aeKwtGaytYdYpC1HoLEiSs%2BUp%2FAPVpCxHU2dFoeB4I2wA3mGwyMG6QiBAH4NicekNmpikVP4X%2FS9lCVcl4e1j3Z2kNIkhxyjHVDNxwiQCVtiHGO7gL%2FQpmf1zC5qZUjx7ujS30egA75bWposIsje2h9vaLozpSttsjA3j6Neh0yzqlZbyfOWSGAIcKwR2rELN7ZR8vCvCFmFf%2BQODz0oqU1pNC%2BQrzTF4QAnuvI1g6oxAU9qAl3fZSG%2Fk1wIrlVMfVXUTMclnVnF0A4J5W3sVh7%2F6DfLVQ82XsTWo5Mn1nQW%2FOgR2HBqEEOp7yRkqBAyxcSbCZAOU026ubfDS8NBshbykdIRlXODGcMQh3emVPf1PO1P21fyxNeXftm9kqUFC4a9%2FoMzZbaw54CKIQJK%2FBCu85iqBGd2zPQyO2BPk6PdnjB7TojZTZckBN9Txd%2Bz1h7G1S8wW4wTahjeqSOzpAVuYV%2B8wzCw3YnLBjqkAcxILEpugndMTHraIpgSPluyMLMAl%2FYXYdqmH%2FV5pq6rNrhaXLmAqx9giR8JzhBCQrR1oE0ZiJxDhEK7%2BprR8tFdRnUxfZygHGsi6cUjPGZVZ9e50i1mRuk4rgVaA77mkJMhJGMkPap24jH6u3E98buq2vKJqasvW1ttgOdr%2BnQdMsTZ%2FZWw2v5ug06UXGq6u1qcPveUSf1MqVYXESccc0ym4f%2BE&X-Amz-Signature=ba982552afbdd856ac0783f17449f2dc17bc795c1ecb997caaabf7016dd39be3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







