



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVQVPNF%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T120615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGT9w%2FwXkLeU9hv45eC5keVFdZ3ZP%2FSATnVvz2mMPf1QIhAMAwBsHSqWEZl2284UWnuh%2F9Sf3iooAb8H5yQ2rtsGTbKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FzZDKF0UwEDqfp1Qq3AOLyKgVD5Rw6kxLstCvNmHh8Q0ZDIkYQouXyQs0K%2FqBCipklRZFNNn8yD506fnJoiGDZiHTpQvMhkSLKx52RRtcPMRhLku7vh1iMq1g%2Bj%2BzPTPz342Nnrn1PLvGbG%2FQTslkUivxyx2PrAlslVVWOA537l2vvGdOA7ucU6es7mwOXMgsleJ9PUrNZz5k8lUIBxT8AWk4uPSebQuWeiMW4t0CUA89TWQWI7XbbxQPYaKMHx%2FXS4gYM4Vag4LSlyJUyFLO%2BQxGm%2Bqn96LuliHqgYBta%2FVqg41fXfPWNukaFyh43zuiHZyTb0l3iBm1mKRyHHQeg%2BZj7BtMmq9lNTnSxngPnYtAGw1hAvcL9tLL6mvZXKMhFdh1Eki3Pnsh7zK1urJmgxjtYpIjKpRhVjCz2VFFFL6ZWANAkgy%2FtdOs%2Ftt8Q7kwoRkX9XwCAWH5%2BPZgUtkpziyJqk8VKAjSt1ePO2%2FevMqBkgH%2BPj5OC7cRFon4rEUnbeo437VrOAJ9mP1T7McihInuh5n%2FYcVeXTmVh85idtr1Q27DSpJypw%2FWJGI4aj9ArMD0EMEv9ZgZWz5h97Ub9BpPAkIGQO4%2B0M129XPeXfAqlqF0djpZGssDtDA6kgBZvcil3VRzNy4LJjCQw%2BDXBjqkAcI2Fohbqy%2F%2BNKCZq3iPCe53qLnfQH6jr6l1Goxj%2Bpab7oRqxceYMvDt9zvcSdHGtgXKRAoDqkcSe7pPmUv5hJ0b1kF9yYyECA3JplsCQAyKcUNAJkKUUI07LeFw2RwCxBNPT3LqZmLCjKqSQnCzhLmeqCBot4Dp0goYWvfJLGDuIY3bNvEI8WGRfrMXl8Gc7Qm7GZm1eaC42jcJa27kAItrOOoM&X-Amz-Signature=c1af6f3407007d04060a3996f9f2a2469f27868a35886f0c4ecec279ca181639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPVQVPNF%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T120615Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDGT9w%2FwXkLeU9hv45eC5keVFdZ3ZP%2FSATnVvz2mMPf1QIhAMAwBsHSqWEZl2284UWnuh%2F9Sf3iooAb8H5yQ2rtsGTbKogECJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2FzZDKF0UwEDqfp1Qq3AOLyKgVD5Rw6kxLstCvNmHh8Q0ZDIkYQouXyQs0K%2FqBCipklRZFNNn8yD506fnJoiGDZiHTpQvMhkSLKx52RRtcPMRhLku7vh1iMq1g%2Bj%2BzPTPz342Nnrn1PLvGbG%2FQTslkUivxyx2PrAlslVVWOA537l2vvGdOA7ucU6es7mwOXMgsleJ9PUrNZz5k8lUIBxT8AWk4uPSebQuWeiMW4t0CUA89TWQWI7XbbxQPYaKMHx%2FXS4gYM4Vag4LSlyJUyFLO%2BQxGm%2Bqn96LuliHqgYBta%2FVqg41fXfPWNukaFyh43zuiHZyTb0l3iBm1mKRyHHQeg%2BZj7BtMmq9lNTnSxngPnYtAGw1hAvcL9tLL6mvZXKMhFdh1Eki3Pnsh7zK1urJmgxjtYpIjKpRhVjCz2VFFFL6ZWANAkgy%2FtdOs%2Ftt8Q7kwoRkX9XwCAWH5%2BPZgUtkpziyJqk8VKAjSt1ePO2%2FevMqBkgH%2BPj5OC7cRFon4rEUnbeo437VrOAJ9mP1T7McihInuh5n%2FYcVeXTmVh85idtr1Q27DSpJypw%2FWJGI4aj9ArMD0EMEv9ZgZWz5h97Ub9BpPAkIGQO4%2B0M129XPeXfAqlqF0djpZGssDtDA6kgBZvcil3VRzNy4LJjCQw%2BDXBjqkAcI2Fohbqy%2F%2BNKCZq3iPCe53qLnfQH6jr6l1Goxj%2Bpab7oRqxceYMvDt9zvcSdHGtgXKRAoDqkcSe7pPmUv5hJ0b1kF9yYyECA3JplsCQAyKcUNAJkKUUI07LeFw2RwCxBNPT3LqZmLCjKqSQnCzhLmeqCBot4Dp0goYWvfJLGDuIY3bNvEI8WGRfrMXl8Gc7Qm7GZm1eaC42jcJa27kAItrOOoM&X-Amz-Signature=06ca7ea592feacb5bc5b8481df6b4e162f77058b8e51b0a1efcd58c18add1261&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







