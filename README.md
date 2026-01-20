



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677O3FH66%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T182909Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbLha8%2BycrpQL88GNpoV7hWf5OsnusBWFGcjwT3o%2BWIwIgX%2FoRT9Au4VjkdfUTsC1hZ19e1pSVoCrjEMbnezS%2B4sMqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrPUpoWu5O%2BJgY%2BsyrcA1mqh4eWFLkN6LN8SRAnFeecE0xRHKnT3lgcb6XG%2FljuFdJDv1NfP%2F4uKJDhrmlzO%2BMFbdwSycr8Cbhnwytzg%2BwjCpfsZLeu4UZdZMUTpqrqz5Vs4fiLRe7aFRMiSlzPkjQ5rArbeNND3b%2BsTWeYb3eqF22JpkvLftZETgSObWAz1LzsBxyCekqtVIHRDgU%2FOwbndMekEHKPPp3MOQd7rkN2MS56zU99VA0hiD%2FV8KMrEdsIOfVn5MbTAwz4M9vCT0uOrzbdUZCGm6AUbSD8gI6VbWP0gEmTL5vGgHjkvghfoEzeGPz9c%2BZ1%2B2iNUvVgdsY6cH%2BRaAqkclicusmjs5NdYynkd5p7Um%2B0z%2BU3J8CmBoLScl%2BXg%2BLvvqD4kUOBTPlb%2BBQAm3%2BUEJHRo1pI2YkILr4NAu9vD8uoNBfbCWG9CPX%2Bmni9sbkaBLWgoVP01KzbB%2FBo7HcfiVnt9Jy3588yLDqZCnvHq%2B0NBg4jw7on%2Fd%2FOv4Sx8oC0NalliVf%2F5VWdQqetUZH4GnIm7QjohBEO2tJQhkzO33Y3fcIoIQhfQKyeiRik235dqkazno9bFpINm4thlrYQlhpE8jEx2S2IVOEPorMomZA0ow2d9g2mvHZ9Gee3gLTL0W%2FNMKHyvssGOqUBHOCJ%2FzMVPrqx0xAPxXHeWOlccueThGVuspLA8gujeEqNCicIzpdxfe96s%2Bt%2BOM7iUAsGmIQ3fjZzY43uNHckWQ0pmdYyhX24fr9cZ8HX7ENQ2ogOwjMMS%2Bh3ZoR6ANgHn9HvHhHQXVJE%2BV7kv0oQH7C0ND7GbXcFsGWEd5m48PWJEx12c1gD8YSA6xb9wnHFcSIC8d82moVwd%2BlaObYB0ME1aL01&X-Amz-Signature=5f26d26e84255484d1634ec46b935a9b763fe6eae28d563facd4a9152db77e0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677O3FH66%2F20260120%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260120T182910Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDbLha8%2BycrpQL88GNpoV7hWf5OsnusBWFGcjwT3o%2BWIwIgX%2FoRT9Au4VjkdfUTsC1hZ19e1pSVoCrjEMbnezS%2B4sMqiAQIsv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPrPUpoWu5O%2BJgY%2BsyrcA1mqh4eWFLkN6LN8SRAnFeecE0xRHKnT3lgcb6XG%2FljuFdJDv1NfP%2F4uKJDhrmlzO%2BMFbdwSycr8Cbhnwytzg%2BwjCpfsZLeu4UZdZMUTpqrqz5Vs4fiLRe7aFRMiSlzPkjQ5rArbeNND3b%2BsTWeYb3eqF22JpkvLftZETgSObWAz1LzsBxyCekqtVIHRDgU%2FOwbndMekEHKPPp3MOQd7rkN2MS56zU99VA0hiD%2FV8KMrEdsIOfVn5MbTAwz4M9vCT0uOrzbdUZCGm6AUbSD8gI6VbWP0gEmTL5vGgHjkvghfoEzeGPz9c%2BZ1%2B2iNUvVgdsY6cH%2BRaAqkclicusmjs5NdYynkd5p7Um%2B0z%2BU3J8CmBoLScl%2BXg%2BLvvqD4kUOBTPlb%2BBQAm3%2BUEJHRo1pI2YkILr4NAu9vD8uoNBfbCWG9CPX%2Bmni9sbkaBLWgoVP01KzbB%2FBo7HcfiVnt9Jy3588yLDqZCnvHq%2B0NBg4jw7on%2Fd%2FOv4Sx8oC0NalliVf%2F5VWdQqetUZH4GnIm7QjohBEO2tJQhkzO33Y3fcIoIQhfQKyeiRik235dqkazno9bFpINm4thlrYQlhpE8jEx2S2IVOEPorMomZA0ow2d9g2mvHZ9Gee3gLTL0W%2FNMKHyvssGOqUBHOCJ%2FzMVPrqx0xAPxXHeWOlccueThGVuspLA8gujeEqNCicIzpdxfe96s%2Bt%2BOM7iUAsGmIQ3fjZzY43uNHckWQ0pmdYyhX24fr9cZ8HX7ENQ2ogOwjMMS%2Bh3ZoR6ANgHn9HvHhHQXVJE%2BV7kv0oQH7C0ND7GbXcFsGWEd5m48PWJEx12c1gD8YSA6xb9wnHFcSIC8d82moVwd%2BlaObYB0ME1aL01&X-Amz-Signature=6630f5467a0542ea0c783d98058252f528b3df7cfb2a82e655a99255423a05dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







