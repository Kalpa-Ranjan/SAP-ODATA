



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKVXULXM%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T135659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDieTzjW1La90xMLhoaR7mRldogcyLFLHqFBTM2jFIc3wIhAMzOM94K8ZVuT3I2mRv9LPz7fqL%2BSCUkeADrO6dotuFxKv8DCH8QABoMNjM3NDIzMTgzODA1Igz5RA29mL0iFL7213cq3AMrZgHLL8MWp2cmtf6wrK%2BMenqmduVpHILvP68boOMn6fPUKYhpIKnR9bXgp3i%2BLHs%2FpgynZPrRR8NT9vY5ZDdIp%2BOVyxrw9J%2FOwebsbx%2B%2FmqyFhJMupLXDv1c5GrqsKsrgCLKNxSSbdYXs8%2F8AX3Qwg%2B54xp0ix9QvSsMo7vuf0sIchjAFUvqQ3dlfJA6%2Fg6S8Pi8H3AWy2wqqvNrvohFr0MwR9NUb6Ritx6icmmjx80wr8n9JccV2kFX6QnFubx6lPnMcq%2FHY6VrWeuqxtenGcyFbO78F7kwy0jnkWdsSUEOK7YzCAXYShCuOz0omKPTf2x7QCQVG2DvlNVXDtxFxDjRHHtXmtHtEV17%2Fiu3vhMQZHBUVyenzVNMowhasC6Q4ROgkG7R%2BsJJ5reu2myzczWoIcrn56oKKWCKY0KDWMG1vDMiZf9f8S5GXlhzB29Ul0yPQ23snivubyc1RyGu8O5VTsmFxlXy2d7pMSh4oGIz7DZepgALpkcHO2uw%2BgWWswA0BW3Ej5v4ArjXAvV1%2BhmC0xwCxYdAyTp2IdOHRwlluaysX%2BR19jg3O5BrHJSVHsQJGR8OGglWpCIOcDTFTyfEIGBVh%2BR2ZZB%2B4S%2F6fMcWgkzpU%2FlR0GUfJaDCpgKjTBjqkAfl9nJN3XJ4n9YsC7lY4u2zepe%2BaI43bzd5dxpIkTmbWiJCDp7GPjUMw8KmspJwixIe96FwAdCn3fVUJ0ooEm57twI69F5zYpKrJSg64XrdEGOA2%2F0xr9zPnpFLVhy8mCppRifFPKdQqQWmlmrZREqT5rneXi1lMY29z%2FuBws%2BMQB0s7w4ziaXOvvmud61DcAHEhQWSEoxogLaPaRgQAO77rbKjL&X-Amz-Signature=ebcf7e267cd16d552199b340315a4c4a474a3c27767c826b307acdc867374c06&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QKVXULXM%2F20260729%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260729T135659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDieTzjW1La90xMLhoaR7mRldogcyLFLHqFBTM2jFIc3wIhAMzOM94K8ZVuT3I2mRv9LPz7fqL%2BSCUkeADrO6dotuFxKv8DCH8QABoMNjM3NDIzMTgzODA1Igz5RA29mL0iFL7213cq3AMrZgHLL8MWp2cmtf6wrK%2BMenqmduVpHILvP68boOMn6fPUKYhpIKnR9bXgp3i%2BLHs%2FpgynZPrRR8NT9vY5ZDdIp%2BOVyxrw9J%2FOwebsbx%2B%2FmqyFhJMupLXDv1c5GrqsKsrgCLKNxSSbdYXs8%2F8AX3Qwg%2B54xp0ix9QvSsMo7vuf0sIchjAFUvqQ3dlfJA6%2Fg6S8Pi8H3AWy2wqqvNrvohFr0MwR9NUb6Ritx6icmmjx80wr8n9JccV2kFX6QnFubx6lPnMcq%2FHY6VrWeuqxtenGcyFbO78F7kwy0jnkWdsSUEOK7YzCAXYShCuOz0omKPTf2x7QCQVG2DvlNVXDtxFxDjRHHtXmtHtEV17%2Fiu3vhMQZHBUVyenzVNMowhasC6Q4ROgkG7R%2BsJJ5reu2myzczWoIcrn56oKKWCKY0KDWMG1vDMiZf9f8S5GXlhzB29Ul0yPQ23snivubyc1RyGu8O5VTsmFxlXy2d7pMSh4oGIz7DZepgALpkcHO2uw%2BgWWswA0BW3Ej5v4ArjXAvV1%2BhmC0xwCxYdAyTp2IdOHRwlluaysX%2BR19jg3O5BrHJSVHsQJGR8OGglWpCIOcDTFTyfEIGBVh%2BR2ZZB%2B4S%2F6fMcWgkzpU%2FlR0GUfJaDCpgKjTBjqkAfl9nJN3XJ4n9YsC7lY4u2zepe%2BaI43bzd5dxpIkTmbWiJCDp7GPjUMw8KmspJwixIe96FwAdCn3fVUJ0ooEm57twI69F5zYpKrJSg64XrdEGOA2%2F0xr9zPnpFLVhy8mCppRifFPKdQqQWmlmrZREqT5rneXi1lMY29z%2FuBws%2BMQB0s7w4ziaXOvvmud61DcAHEhQWSEoxogLaPaRgQAO77rbKjL&X-Amz-Signature=8b4c90efaefa35ffc57d3743e83f392eb99ad2c41b95e440f9560f8ba4090c58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







