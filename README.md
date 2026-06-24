



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOCITJLQ%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T193923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIBTY1uR5CZ5aKVTbJAnCzGwA33YlApxREldHooiCJOULAiEA9sC3ozcH8LwySW%2F5LGnbN9pHpBQG0t9Gb4j%2FbkwnN1oq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDEOIlSIvFB30e5XfCircAzxCTBeTQbT7G3DzhUDf31MjshAaoHffuXP2TYJelK6BWuBJ%2BI68lomuhuuJckJ%2FtnWo%2BW1H3lFF5UTE6OOW1Su8xIJbCTJwGyUDCR2Vf6FS9wl0JLhYJ5cQhFHuh2a9Lkp%2FFkOoIjju1BaBCpLIbbg9C4ApEikl72HsFOuGyEtdgPZeIeIim76HbdshqMsofzzNprhvkBaxDweOr%2BcR9CUFk0D%2FjP5qhehLBqwsmhOXxT1szFoQRfGEg8%2FaXcKJGY4avMbnDTSJiVMX3mGZ7k30UmgjQqnUpd9Mc3WO8YmBP1EiGzsNX7wNItQdEBj6XBym%2BqbqwL0RC0qxNiwtiqPxWtzKnoBDEuBNUg8%2FST8YTfGf9573VZCz%2BcR7XUsrjkeDb9QaB1XemlwvSw1bV7DmB6Pz1%2F0gdPbTjiKK2Fsa1CGu7S6fAN4v40%2FD3RDYvCZ4LqWG8lg9n6mRthhjSqFFY2zHe23WV4EwsbygpUDA4QiZltdA2RY8HfOHq%2FtxedWh%2FVCmqaumQLBJ9eJxhUGknHz2MOwk6Hfn8Vy5LSxvIq8etEc2qCOoOMBK9yybqmHJO%2B%2Ftmhw6hgBIUXPlXgFWFRg2icDfhX8Uk%2BmnX3NvZrEBb7lSb5rPzsjcMI%2BW8NEGOqUBIZk8Fk%2FEJUwkMk5E99pb8u9sidepapYYxbS6jMrnkyoVm%2Fu0Zt%2F7daXF5qimA56MqLuODbMCC1ByocbO5VEZq%2BmbVAMeUVjFdWoioYIUMgbRz0kM6X85bvlOgc5bAFaFI8NIvoRRtFNfif0ztcEoe5xjmmtoDTj%2FhrZ%2FHwAGXhRn7Ckdhw%2Fpc%2FUQwsBHGAHKfS32hOLDPpnH2TLRC6DO9uTFYzcQ&X-Amz-Signature=c90091cd256cbe7839d8574e2248a24dd361968bf62b4e76e5e5aca6bf932920&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOCITJLQ%2F20260624%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260624T193923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJHMEUCIBTY1uR5CZ5aKVTbJAnCzGwA33YlApxREldHooiCJOULAiEA9sC3ozcH8LwySW%2F5LGnbN9pHpBQG0t9Gb4j%2FbkwnN1oq%2FwMIOhAAGgw2Mzc0MjMxODM4MDUiDEOIlSIvFB30e5XfCircAzxCTBeTQbT7G3DzhUDf31MjshAaoHffuXP2TYJelK6BWuBJ%2BI68lomuhuuJckJ%2FtnWo%2BW1H3lFF5UTE6OOW1Su8xIJbCTJwGyUDCR2Vf6FS9wl0JLhYJ5cQhFHuh2a9Lkp%2FFkOoIjju1BaBCpLIbbg9C4ApEikl72HsFOuGyEtdgPZeIeIim76HbdshqMsofzzNprhvkBaxDweOr%2BcR9CUFk0D%2FjP5qhehLBqwsmhOXxT1szFoQRfGEg8%2FaXcKJGY4avMbnDTSJiVMX3mGZ7k30UmgjQqnUpd9Mc3WO8YmBP1EiGzsNX7wNItQdEBj6XBym%2BqbqwL0RC0qxNiwtiqPxWtzKnoBDEuBNUg8%2FST8YTfGf9573VZCz%2BcR7XUsrjkeDb9QaB1XemlwvSw1bV7DmB6Pz1%2F0gdPbTjiKK2Fsa1CGu7S6fAN4v40%2FD3RDYvCZ4LqWG8lg9n6mRthhjSqFFY2zHe23WV4EwsbygpUDA4QiZltdA2RY8HfOHq%2FtxedWh%2FVCmqaumQLBJ9eJxhUGknHz2MOwk6Hfn8Vy5LSxvIq8etEc2qCOoOMBK9yybqmHJO%2B%2Ftmhw6hgBIUXPlXgFWFRg2icDfhX8Uk%2BmnX3NvZrEBb7lSb5rPzsjcMI%2BW8NEGOqUBIZk8Fk%2FEJUwkMk5E99pb8u9sidepapYYxbS6jMrnkyoVm%2Fu0Zt%2F7daXF5qimA56MqLuODbMCC1ByocbO5VEZq%2BmbVAMeUVjFdWoioYIUMgbRz0kM6X85bvlOgc5bAFaFI8NIvoRRtFNfif0ztcEoe5xjmmtoDTj%2FhrZ%2FHwAGXhRn7Ckdhw%2Fpc%2FUQwsBHGAHKfS32hOLDPpnH2TLRC6DO9uTFYzcQ&X-Amz-Signature=1e5712263d746be1ce43af874d17f94adcbb208e8a023e046e9fe4cadc44bae3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







