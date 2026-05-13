



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXV6EJWQ%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T142117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDPJxbV754J6UllUqwYIhN5uG6EsLhpBFeQ98q%2FbPj7mgIhAMDIcHtuq%2BKgIS5R4ZyTViWKlO4xXTWMvq6wZSE9wdLcKv8DCEcQABoMNjM3NDIzMTgzODA1IgxS%2BQK8cSP6ueVRAY8q3AN%2BseLYBgOLRhatK%2BR9qoG%2FQSTO4qiIqThmJus%2BAROLVwe58NksN3m5kyE8ACqLXjekAJQFmcEI5v5golt90uyURkfjKHSzum2iIu2g4GsES%2BrrwTNNm2BsuXBldYoWZwHSZV1Zii2jvUvMd%2Fxa4cMopkfZyvZLWSxY0P3XaRohVHE1s3%2BKuEqrFLvzYLyYcqhOrdYiQ94JSzvvjJqbvvmpzrKE4wZTrigxBkAkp7UQxY0gKf4AQUiKBp7aqiE4Q8ko1Q0qCgkrAWNYrXftbqpWOHKF4O%2FGUoH3NPQ34KhpVCPz6kAIfUJMHNFXmsBdfRmm%2BJ3SeQVPbmdgqgUW%2BkQYJfYV%2FwhcNI%2FXL%2B78TZqyJ%2Bv3NMeh4%2FjjlSGkB5VHwG3JZkJoMjEKQP2ISnvaAhx3W50tcnrf6zD7kyO5Z9e7nbgjKRekNXrQ145UNkMT0zhr8dVWetsSC57r43XiV%2ByQWMuXDMclV02zcBssqYRYsSvrIKVTxRCVX23wPPjmedNAYf0P7E2%2Bs4bkR2N%2FpdNdFLEKR0%2Fh9U6d1CooQdwqSKCYEsGx9OOAlJS445Wis3dtQXRNRESexYM2rhB%2F5ngSIA9bSTrZQLgrPgp6wZ%2BqrAj2XlTZq%2BcPeUewKDCI%2BZHQBjqkAXEVXKEK0u9I2XuwS%2F%2FA1pCrQ6BPOpx66TTqI9j6nms3NPUB8vnYVrPWJUb4hBUPrgq8mMr31XyzqKGuKvon6EJHFOJx442MASz3MsKVmjL0MwtLfTHXnRopavh%2FFQfCLTLrMg0CDqxByWy2yaxomOoSie5xOZVRBZXEXectESqPWHiA0vaPsD8Kdu9AB7QOI6%2FDIWsInPJFJqS0mi813iKKQj%2Fy&X-Amz-Signature=950d4530ef12da8b2924d27793541265a0b494040870e109abef38b3dfcb31cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXV6EJWQ%2F20260513%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260513T142117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJIMEYCIQDPJxbV754J6UllUqwYIhN5uG6EsLhpBFeQ98q%2FbPj7mgIhAMDIcHtuq%2BKgIS5R4ZyTViWKlO4xXTWMvq6wZSE9wdLcKv8DCEcQABoMNjM3NDIzMTgzODA1IgxS%2BQK8cSP6ueVRAY8q3AN%2BseLYBgOLRhatK%2BR9qoG%2FQSTO4qiIqThmJus%2BAROLVwe58NksN3m5kyE8ACqLXjekAJQFmcEI5v5golt90uyURkfjKHSzum2iIu2g4GsES%2BrrwTNNm2BsuXBldYoWZwHSZV1Zii2jvUvMd%2Fxa4cMopkfZyvZLWSxY0P3XaRohVHE1s3%2BKuEqrFLvzYLyYcqhOrdYiQ94JSzvvjJqbvvmpzrKE4wZTrigxBkAkp7UQxY0gKf4AQUiKBp7aqiE4Q8ko1Q0qCgkrAWNYrXftbqpWOHKF4O%2FGUoH3NPQ34KhpVCPz6kAIfUJMHNFXmsBdfRmm%2BJ3SeQVPbmdgqgUW%2BkQYJfYV%2FwhcNI%2FXL%2B78TZqyJ%2Bv3NMeh4%2FjjlSGkB5VHwG3JZkJoMjEKQP2ISnvaAhx3W50tcnrf6zD7kyO5Z9e7nbgjKRekNXrQ145UNkMT0zhr8dVWetsSC57r43XiV%2ByQWMuXDMclV02zcBssqYRYsSvrIKVTxRCVX23wPPjmedNAYf0P7E2%2Bs4bkR2N%2FpdNdFLEKR0%2Fh9U6d1CooQdwqSKCYEsGx9OOAlJS445Wis3dtQXRNRESexYM2rhB%2F5ngSIA9bSTrZQLgrPgp6wZ%2BqrAj2XlTZq%2BcPeUewKDCI%2BZHQBjqkAXEVXKEK0u9I2XuwS%2F%2FA1pCrQ6BPOpx66TTqI9j6nms3NPUB8vnYVrPWJUb4hBUPrgq8mMr31XyzqKGuKvon6EJHFOJx442MASz3MsKVmjL0MwtLfTHXnRopavh%2FFQfCLTLrMg0CDqxByWy2yaxomOoSie5xOZVRBZXEXectESqPWHiA0vaPsD8Kdu9AB7QOI6%2FDIWsInPJFJqS0mi813iKKQj%2Fy&X-Amz-Signature=3570966abee96481046cc8222c2cf1da8d58ad37bfb621e783ecdc1f6b0dd493&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







