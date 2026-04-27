



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJMQ24BD%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEGSoNblTUezu9yu0O8hX%2FgVssDekTTPzuZ0FT%2FnFZgeAiEA0wvTMLTU5BoLv0nvyykAFnZptOuCDM4Ve4hB5XbGHNIqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCI3ywgIV%2FV9X8aSQCrcAzCaStGGmcX7zeBifhmGZ4OGxJKL7i69WcDN3SzX9Nwkzb11D1YiRetMqYMtswiz3mKqsDc2Xxwu1Q2jNh1hruJWgac9dnNefzrs5IbOKDmkEMu%2Byxa%2FATLQe6Ay2%2F6MiuUdaUzeZLWzsZ%2F9xaEr%2FoSq2L8gSM1OVoEi%2FXy0mJYCgL9m8HrOA4fi%2BxZRly4kC0Don%2Frmkb41PzrxsXjJODZfOt4e5uYWQIXrRXXkcsyIHZqT%2BI5K2glOKAq9usokl3YQ5zpShxKN9zQVA1qaim6rEGFN5xLTUbs3twXoWUbMORpRwiQydyP3qBX7TjManeQAi8PwPbQoVXsQTAPQp%2BUKnVCAnoLHHCKS0n9gLoIu%2FIW4hcNP62FFB%2FtTYh8E6dKhVca28rqmEiksA8yEnWgSpMAcFgOz5y3MNU5Tl1vJYs1ds6417cDiWHxMKoGZ%2FKiLadV7C2g1H82i%2Fb52kmhGtklmKNPiHsW5gQL%2BnK%2BJZnI7uEBs0nXVb9oN8ndSZvt6zCu6i%2BulIRErSD5MX%2FPywsuWeSRUHTKHUcieQE6JVYa9BaXoRhDA86agEHdVIeQ2WaJpMqapbhP6XOUWpTt1Txk6wiSxICaeSOkJjJsSeyqc7ptp%2BPf0fE9MMIXovs8GOqUBNqjL%2FmW0VKbu3vnHtUEv0DGATGJFcEnTrgDQWzBmFzw%2Fgodboa0UFZJhltM4tkQFxU0MjjVTRJ5%2BVTlOv5dwkMIVYmLkYq%2F620z7brhHuWMfWsCsTT5SGP%2FUydgSn1xCxYX55gvAmQoy3tC0xpgReKU9dIxBvExbIylzQFBJ9BBg0aBLj97DHlGUxU8FI1vKfdqglN4jX%2BtMGfAI%2FQCxMWxlZ0oG&X-Amz-Signature=9ba29aaa3d9122be11eaa55cf61393280345acd54f961a52a91f9581d07506c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJMQ24BD%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIEGSoNblTUezu9yu0O8hX%2FgVssDekTTPzuZ0FT%2FnFZgeAiEA0wvTMLTU5BoLv0nvyykAFnZptOuCDM4Ve4hB5XbGHNIqiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCI3ywgIV%2FV9X8aSQCrcAzCaStGGmcX7zeBifhmGZ4OGxJKL7i69WcDN3SzX9Nwkzb11D1YiRetMqYMtswiz3mKqsDc2Xxwu1Q2jNh1hruJWgac9dnNefzrs5IbOKDmkEMu%2Byxa%2FATLQe6Ay2%2F6MiuUdaUzeZLWzsZ%2F9xaEr%2FoSq2L8gSM1OVoEi%2FXy0mJYCgL9m8HrOA4fi%2BxZRly4kC0Don%2Frmkb41PzrxsXjJODZfOt4e5uYWQIXrRXXkcsyIHZqT%2BI5K2glOKAq9usokl3YQ5zpShxKN9zQVA1qaim6rEGFN5xLTUbs3twXoWUbMORpRwiQydyP3qBX7TjManeQAi8PwPbQoVXsQTAPQp%2BUKnVCAnoLHHCKS0n9gLoIu%2FIW4hcNP62FFB%2FtTYh8E6dKhVca28rqmEiksA8yEnWgSpMAcFgOz5y3MNU5Tl1vJYs1ds6417cDiWHxMKoGZ%2FKiLadV7C2g1H82i%2Fb52kmhGtklmKNPiHsW5gQL%2BnK%2BJZnI7uEBs0nXVb9oN8ndSZvt6zCu6i%2BulIRErSD5MX%2FPywsuWeSRUHTKHUcieQE6JVYa9BaXoRhDA86agEHdVIeQ2WaJpMqapbhP6XOUWpTt1Txk6wiSxICaeSOkJjJsSeyqc7ptp%2BPf0fE9MMIXovs8GOqUBNqjL%2FmW0VKbu3vnHtUEv0DGATGJFcEnTrgDQWzBmFzw%2Fgodboa0UFZJhltM4tkQFxU0MjjVTRJ5%2BVTlOv5dwkMIVYmLkYq%2F620z7brhHuWMfWsCsTT5SGP%2FUydgSn1xCxYX55gvAmQoy3tC0xpgReKU9dIxBvExbIylzQFBJ9BBg0aBLj97DHlGUxU8FI1vKfdqglN4jX%2BtMGfAI%2FQCxMWxlZ0oG&X-Amz-Signature=323430ba290301ebf315942898f5ac9db1475d306d5bf893897c99ce5e9dcab5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







