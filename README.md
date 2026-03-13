



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O7C2UIX%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T183416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG3J6j7NNcFkx7yQRWLakEb%2ByeAcWgw8BSbBgqK2oTS7AiBTBEypk1GMBzuYYt76Q6APGIQ46hnQRC6dzjja%2FvQHOyqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML9abXU7951tONmEnKtwD2ehgkZHvmFV7JxRuSGrEYNDdLqF3VwlcAP%2BRUEOJi04UdU1Gk7DIMulc37sbayZ21SnfahmESDnrDdzus4dG0Z5gjuWGTPNG80CCm%2F%2FKgBKPU7l%2Fb19aGVrXe%2F7yP4j2ZQgTFqihDTqnc0%2FBYmhjDk1Tgb8r1YHIeOu9TYY0ZYAJr8l10AaejPblztOMRPc89AdBFQd61sOAZG6%2BxK%2Boxx9J5coDwjwcUO7%2BRPH3rmZt2PSumUsyxANJigkUO0OEOl%2FtnNpUWiXHbPVPkVRmG9khZxH9QO6srIwymsJ%2FjMHX1STXO5LEVmGNScMqzTII4N6hYd3I%2BiVhHb8QKABflqKt5vlIylwo4dGGSuQRwUMY1VT3SgasGRr18RdIMHdyWoP7%2BWnsGhRUa6OkEuzJWY2mCkLdieQRK9iLyuQ1mmfGtdSB%2FSZAkUhrExe0v%2BRv%2FiNoGOAe8XfNRu8GVAtPVjQWBTOZA5QKvxSV08ZO7hl2VVNt1Fb6XWdG5udRfLVhAED6vsBMXinY93U%2BPYvPkiblqnMtBGIRxUbB5B4XN7mcrX003mhkpuWg%2BzxXlBYTgyxLR0%2B9CN9aqUpxENcg%2Bx1nPHvIpNxax9L9RWJ8U5LZ12a8xVSaBNWLF5kwi43RzQY6pgHwJO%2F62FN1htmJEts%2B4qDV9AXVx%2FeIv9lcyH%2BzHqxWZu7iy9bhPB4nKaGQINUns%2BNU%2B0xt%2FM3y3%2FilfqzhnJf9cenIFW9UkxrYrI5JCGMR3%2F06TDeTGmdyaPIWXB2LhqrnKQFJtQ52nSmA1wp1e0LOlJopWhuCImk60d3TqbKP8%2BVhnnKz2Pu2Ytn0z2vqzNOL9JkDiFZaynQsLoRzuSRV2cRrZ1eL&X-Amz-Signature=f204068bbe6fbac5612a66edc3ff5e7947a05f38d1e2e19ea5117f516b0ae399&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666O7C2UIX%2F20260313%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260313T183416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG3J6j7NNcFkx7yQRWLakEb%2ByeAcWgw8BSbBgqK2oTS7AiBTBEypk1GMBzuYYt76Q6APGIQ46hnQRC6dzjja%2FvQHOyqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML9abXU7951tONmEnKtwD2ehgkZHvmFV7JxRuSGrEYNDdLqF3VwlcAP%2BRUEOJi04UdU1Gk7DIMulc37sbayZ21SnfahmESDnrDdzus4dG0Z5gjuWGTPNG80CCm%2F%2FKgBKPU7l%2Fb19aGVrXe%2F7yP4j2ZQgTFqihDTqnc0%2FBYmhjDk1Tgb8r1YHIeOu9TYY0ZYAJr8l10AaejPblztOMRPc89AdBFQd61sOAZG6%2BxK%2Boxx9J5coDwjwcUO7%2BRPH3rmZt2PSumUsyxANJigkUO0OEOl%2FtnNpUWiXHbPVPkVRmG9khZxH9QO6srIwymsJ%2FjMHX1STXO5LEVmGNScMqzTII4N6hYd3I%2BiVhHb8QKABflqKt5vlIylwo4dGGSuQRwUMY1VT3SgasGRr18RdIMHdyWoP7%2BWnsGhRUa6OkEuzJWY2mCkLdieQRK9iLyuQ1mmfGtdSB%2FSZAkUhrExe0v%2BRv%2FiNoGOAe8XfNRu8GVAtPVjQWBTOZA5QKvxSV08ZO7hl2VVNt1Fb6XWdG5udRfLVhAED6vsBMXinY93U%2BPYvPkiblqnMtBGIRxUbB5B4XN7mcrX003mhkpuWg%2BzxXlBYTgyxLR0%2B9CN9aqUpxENcg%2Bx1nPHvIpNxax9L9RWJ8U5LZ12a8xVSaBNWLF5kwi43RzQY6pgHwJO%2F62FN1htmJEts%2B4qDV9AXVx%2FeIv9lcyH%2BzHqxWZu7iy9bhPB4nKaGQINUns%2BNU%2B0xt%2FM3y3%2FilfqzhnJf9cenIFW9UkxrYrI5JCGMR3%2F06TDeTGmdyaPIWXB2LhqrnKQFJtQ52nSmA1wp1e0LOlJopWhuCImk60d3TqbKP8%2BVhnnKz2Pu2Ytn0z2vqzNOL9JkDiFZaynQsLoRzuSRV2cRrZ1eL&X-Amz-Signature=a3126a57f917bcf42047f5b04688e744f51efafb73637ab44075989792669e2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







