



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTWY5OMF%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T192147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDiPsA1U8suGlRFKgM7XYqZm%2F3weIoQZHT8mMcVJB%2Fn8wIhAMf1YL9zs2tHKiWtKRUfrZbF6BAW9ICNiSrOp1hosBj8Kv8DCCwQABoMNjM3NDIzMTgzODA1IgxGDhBgF7Whctb715Qq3AMkuACgnsOMvX09Ed9xdSXj3ktDVmgomWHU9CN%2BnD1XGBoB4sYAJVfq3WyCu784QgmxGlu8StLMzV1OwbzikV02%2FdA3CK%2BownKKY0Jnmi9ShudTDIashtVlfLyVnWN7crZxBXR%2BgNhcmOfPeqNeUXYKuK5KI3qEhAatvPYd0QDkCE0sriY7y64VcrwmYSK9kYaGLAm3RpkxN9IQ07hbzHe3oDpxXNlm3rAkPyVzoxoFDjyBF%2FBGBmO5AIaGPtKFqKKaUB1d7m2SPT2QxvOiAp14rbod9ybT2heM0IQF%2BY5THL23ty5n%2Bvf9ihtKfz44P0NECzD7hBtgVuy0JHhqbmYv9glTvy1cz5%2FsYQLMs99SgSTNKsfexY672H0E2LnSxgyU0%2BFl9TMxMj1XRZOz%2FznIB24ag7SSsXzlLQThHH%2F%2FWijZ2ohTmyfl0Dnz%2BqFxfjk46GIkv3NOR%2FYWBY%2F9LzIUzgWA3naX4DdqNEpci%2F4OgfJEM5JF6acFUP08aezyN51t3xO%2BNnFdRFxkewsYBirZAWbK66OwlQ5B416GuHWLUeb7MS7CLD04Q8TZwYBKK2rV53qtG5A3LX9UOTTGtxCR8oxPHdJLAL6bYxSm80Ii%2By6hHkM%2B1oMbC63rcjCOgc7TBjqkAV22m%2BWawzOUE%2FFGcB%2BRfFXmEO0srzaDonY36LTN1L7yr5KaNpI0SPwvceGuUckf8def4uFgY8iE5Z4oc%2BsPks7FdVoTyKJSGXSotWNQoaEq2oNL%2FU9yjYMxtOZL5AtF5LF1JKlxME%2Bg%2FPZ%2Bfpsa8euvWNJhLl6lJH0mNEjJZ05xb%2B84v1EArKlXKyihrGXh4M2LXq8NFMdI19sNBUXTyM777Qdh&X-Amz-Signature=72690de46059032ea34fe79210146ea8c66ccddb17e214c4798f1e87eac9c224&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTWY5OMF%2F20260805%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260805T192147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGMaCXVzLXdlc3QtMiJIMEYCIQDiPsA1U8suGlRFKgM7XYqZm%2F3weIoQZHT8mMcVJB%2Fn8wIhAMf1YL9zs2tHKiWtKRUfrZbF6BAW9ICNiSrOp1hosBj8Kv8DCCwQABoMNjM3NDIzMTgzODA1IgxGDhBgF7Whctb715Qq3AMkuACgnsOMvX09Ed9xdSXj3ktDVmgomWHU9CN%2BnD1XGBoB4sYAJVfq3WyCu784QgmxGlu8StLMzV1OwbzikV02%2FdA3CK%2BownKKY0Jnmi9ShudTDIashtVlfLyVnWN7crZxBXR%2BgNhcmOfPeqNeUXYKuK5KI3qEhAatvPYd0QDkCE0sriY7y64VcrwmYSK9kYaGLAm3RpkxN9IQ07hbzHe3oDpxXNlm3rAkPyVzoxoFDjyBF%2FBGBmO5AIaGPtKFqKKaUB1d7m2SPT2QxvOiAp14rbod9ybT2heM0IQF%2BY5THL23ty5n%2Bvf9ihtKfz44P0NECzD7hBtgVuy0JHhqbmYv9glTvy1cz5%2FsYQLMs99SgSTNKsfexY672H0E2LnSxgyU0%2BFl9TMxMj1XRZOz%2FznIB24ag7SSsXzlLQThHH%2F%2FWijZ2ohTmyfl0Dnz%2BqFxfjk46GIkv3NOR%2FYWBY%2F9LzIUzgWA3naX4DdqNEpci%2F4OgfJEM5JF6acFUP08aezyN51t3xO%2BNnFdRFxkewsYBirZAWbK66OwlQ5B416GuHWLUeb7MS7CLD04Q8TZwYBKK2rV53qtG5A3LX9UOTTGtxCR8oxPHdJLAL6bYxSm80Ii%2By6hHkM%2B1oMbC63rcjCOgc7TBjqkAV22m%2BWawzOUE%2FFGcB%2BRfFXmEO0srzaDonY36LTN1L7yr5KaNpI0SPwvceGuUckf8def4uFgY8iE5Z4oc%2BsPks7FdVoTyKJSGXSotWNQoaEq2oNL%2FU9yjYMxtOZL5AtF5LF1JKlxME%2Bg%2FPZ%2Bfpsa8euvWNJhLl6lJH0mNEjJZ05xb%2B84v1EArKlXKyihrGXh4M2LXq8NFMdI19sNBUXTyM777Qdh&X-Amz-Signature=315cd5b9c2691679fac3207afaed35ea7442d125924050786eeea27b9f5ec7c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







