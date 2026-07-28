



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FIA4QPS%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T191500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPpkcsoSxE7UIctBlS6xmxzHPSb20LFeJJSBwzqB00NAIhAIIoDk6HKiA4fk8r3TDZzb%2BTQf50W4yXihHwFU8oGKBVKv8DCGwQABoMNjM3NDIzMTgzODA1IgwVjWAU0d2GeqpaYS8q3AOuZOhbaiJclCeJC6WLza%2BuRjPnE10VnHbl3jh4QdUQoxvzf250UzF5KY%2B7o%2BA%2FIAJl3hSB1%2B1IDHUKkLX%2FqBBkw76VfYJDPrI%2BxY5fZkzpei8vQSQlk68vQWYISf7CTzxFObQu5Jib7%2FpT8iH8Fvmqnn0WYjdMpsvPLgMUKJ6QY%2Bz3uoH4tfr%2BUNEMGdUbGJx69ZLjpCCUVCGNpEWyDH0OG0lISzHz118rK%2FZRB9PhIhUCVpmX%2BBISRbi3w3dbn1ch7%2FHw3kv9767D%2Fo2bdZaGG%2BAoACmdZ9pXyz6Q2LJYTOFDDKC%2FSL9pAlRmBbXtx6qqew9jP9p4i%2BSpvfXilzup2MLCSj%2BoB7f65OPJHlfzbBwTsynlFVNKkuQ7unFnQ8EGY5tEy4wNPGfMsxzbycflBU%2BPj8Sv%2FVwVXw1BgtOu%2BWVHUYwojtc8ocXhOSWzX2XwKAegPh6qx3DyXuY1PVMVRVxGmMpgOKYFkqAAxhTcJJaczTe3%2F%2BDw9hbK3sDng0KfgyRC%2F049zkE3h%2FjVl7uqybKN%2FnekEr8yCJS0%2BFVquCoAlrTGIUcr4%2F3N9Q%2B7ki6tlDLm%2BkD5OiELFiVNq1wgL2Yde7ghFMCsWeWeA8kr8OMXzWm02T7d5AfNnzCI9qPTBjqkAV3YZUb3Uv8iPO0ZZQafT4amhow0VqX%2FNknc6Z6L%2BNh9FIYcgKhZiDgFtsMMZvH5OQAvWrJep%2FiEHy0mxZhjeDQIU10HagOERv2kQHqT5nzm%2BVELv2n2NlDxCRMLILpOC9KGpXupisgmehR9dX2ZOQNfLfdxrRi98GN4jqS9XNEaN%2FKDGJnBrV5GA9ZY%2FvMGAWMku4Xq623PnJb1YVA0Ydc7HtaR&X-Amz-Signature=51ae8d71c768a266cb2fcf7e222319855eea681a9fe7838f0a7e3beb731afb86&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FIA4QPS%2F20260728%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260728T191500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPpkcsoSxE7UIctBlS6xmxzHPSb20LFeJJSBwzqB00NAIhAIIoDk6HKiA4fk8r3TDZzb%2BTQf50W4yXihHwFU8oGKBVKv8DCGwQABoMNjM3NDIzMTgzODA1IgwVjWAU0d2GeqpaYS8q3AOuZOhbaiJclCeJC6WLza%2BuRjPnE10VnHbl3jh4QdUQoxvzf250UzF5KY%2B7o%2BA%2FIAJl3hSB1%2B1IDHUKkLX%2FqBBkw76VfYJDPrI%2BxY5fZkzpei8vQSQlk68vQWYISf7CTzxFObQu5Jib7%2FpT8iH8Fvmqnn0WYjdMpsvPLgMUKJ6QY%2Bz3uoH4tfr%2BUNEMGdUbGJx69ZLjpCCUVCGNpEWyDH0OG0lISzHz118rK%2FZRB9PhIhUCVpmX%2BBISRbi3w3dbn1ch7%2FHw3kv9767D%2Fo2bdZaGG%2BAoACmdZ9pXyz6Q2LJYTOFDDKC%2FSL9pAlRmBbXtx6qqew9jP9p4i%2BSpvfXilzup2MLCSj%2BoB7f65OPJHlfzbBwTsynlFVNKkuQ7unFnQ8EGY5tEy4wNPGfMsxzbycflBU%2BPj8Sv%2FVwVXw1BgtOu%2BWVHUYwojtc8ocXhOSWzX2XwKAegPh6qx3DyXuY1PVMVRVxGmMpgOKYFkqAAxhTcJJaczTe3%2F%2BDw9hbK3sDng0KfgyRC%2F049zkE3h%2FjVl7uqybKN%2FnekEr8yCJS0%2BFVquCoAlrTGIUcr4%2F3N9Q%2B7ki6tlDLm%2BkD5OiELFiVNq1wgL2Yde7ghFMCsWeWeA8kr8OMXzWm02T7d5AfNnzCI9qPTBjqkAV3YZUb3Uv8iPO0ZZQafT4amhow0VqX%2FNknc6Z6L%2BNh9FIYcgKhZiDgFtsMMZvH5OQAvWrJep%2FiEHy0mxZhjeDQIU10HagOERv2kQHqT5nzm%2BVELv2n2NlDxCRMLILpOC9KGpXupisgmehR9dX2ZOQNfLfdxrRi98GN4jqS9XNEaN%2FKDGJnBrV5GA9ZY%2FvMGAWMku4Xq623PnJb1YVA0Ydc7HtaR&X-Amz-Signature=e61fa903680a570f401ada5a88d4db5632b7c3d46ff137eea79e8b1e04505724&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







