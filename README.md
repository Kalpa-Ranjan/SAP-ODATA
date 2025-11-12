



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H7VEJGG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T011229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIAhCdAUvGpMV%2F1Tj4fKH5TpVLICIpPqDTlNNImJ%2BpVG6AiAIFfd%2BaRuY3cmqa9W%2FNxtnLAGb2nISft7ULrhun%2Fttoyr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMPIaUQQE%2BRxpHC0TSKtwDdOrCEDuwJbM1ko0FT%2BA909akZlIpht%2Bgj%2BFxGFLxRmGPHi1uXbYWI3KHf3S9%2FISHGbdTlctxWiA7iHTM0ShDAhQRF5EPy%2B38bTeE7D6Vhp0WQ3fHDUH3XJO9c5LvRJ8EKfR9E9srgFpZmy3iYjXwIbv59kyJcHkTFXzJ3ua1gMty%2BK11UkLXKwtPUoA%2FWLJJgMcnpolho12O3hNqlcKJiFMx8gVr47M6dePG1WEKURQQeXGYCcC5oLpNTkI%2FfWxB1tz7mDht9po9PYYTTdx0ZSbsszf%2FCttcvI2lZhKNPpyz%2BLNWyk2ZwbMfp0EXJKVDOS%2BMrgUUgJuaEoKUUyww8iyGiV2Q110pk1DimFDQP%2Bw%2Bf45EivMeqTUI7IRvmQID29gWHJiscgbRhEFUW0ApACZtxyhdP6JLg%2FWugt9X4R8Aqbf3f5YqRrW7ZGTrb3LyJcm1Blp9qpBCl3lc3jLwBURJrifgysp5fzqjNA1mMtIZcv%2Be3aMSoKrqYVdK3PE%2Bbh9QvWv14ly8u%2FUk4vNB5h8cf9JtYydpUDKqwzE7VcNCUG5KicEuYFihNHyPo9pNMTpdjhJoZhBdL3sgDRwy2LErCSB1a6mj7TAJ8Od72VYO5kumlC9W2fZssf0wkqDPyAY6pgFzggrWuQDkSkhHh5X%2Ff035oJun1R5une34qR9YZLMd3pVF4GER6QCqi6h0zKmUOBdFYQ2ubtKdDCOLb59%2FU3JB3zPhgDjjnHTNMMeCaCMWprOtzOwK2gF2fchtI%2BAE9XjxZsmC%2FVcDN1f49gZ15mjDphbcsMXaxHNiVfXCQMjNeero%2FyaxA5SCsaHkv99Blu8NdJybfX3%2B%2FzvCUHu1PfkOOrEdCX4U&X-Amz-Signature=f42e231a07e5f3b88e08740a86daa00e11e0830fb4b1067077d66e8540af0741&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H7VEJGG%2F20251112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251112T011229Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJGMEQCIAhCdAUvGpMV%2F1Tj4fKH5TpVLICIpPqDTlNNImJ%2BpVG6AiAIFfd%2BaRuY3cmqa9W%2FNxtnLAGb2nISft7ULrhun%2Fttoyr%2FAwgpEAAaDDYzNzQyMzE4MzgwNSIMPIaUQQE%2BRxpHC0TSKtwDdOrCEDuwJbM1ko0FT%2BA909akZlIpht%2Bgj%2BFxGFLxRmGPHi1uXbYWI3KHf3S9%2FISHGbdTlctxWiA7iHTM0ShDAhQRF5EPy%2B38bTeE7D6Vhp0WQ3fHDUH3XJO9c5LvRJ8EKfR9E9srgFpZmy3iYjXwIbv59kyJcHkTFXzJ3ua1gMty%2BK11UkLXKwtPUoA%2FWLJJgMcnpolho12O3hNqlcKJiFMx8gVr47M6dePG1WEKURQQeXGYCcC5oLpNTkI%2FfWxB1tz7mDht9po9PYYTTdx0ZSbsszf%2FCttcvI2lZhKNPpyz%2BLNWyk2ZwbMfp0EXJKVDOS%2BMrgUUgJuaEoKUUyww8iyGiV2Q110pk1DimFDQP%2Bw%2Bf45EivMeqTUI7IRvmQID29gWHJiscgbRhEFUW0ApACZtxyhdP6JLg%2FWugt9X4R8Aqbf3f5YqRrW7ZGTrb3LyJcm1Blp9qpBCl3lc3jLwBURJrifgysp5fzqjNA1mMtIZcv%2Be3aMSoKrqYVdK3PE%2Bbh9QvWv14ly8u%2FUk4vNB5h8cf9JtYydpUDKqwzE7VcNCUG5KicEuYFihNHyPo9pNMTpdjhJoZhBdL3sgDRwy2LErCSB1a6mj7TAJ8Od72VYO5kumlC9W2fZssf0wkqDPyAY6pgFzggrWuQDkSkhHh5X%2Ff035oJun1R5une34qR9YZLMd3pVF4GER6QCqi6h0zKmUOBdFYQ2ubtKdDCOLb59%2FU3JB3zPhgDjjnHTNMMeCaCMWprOtzOwK2gF2fchtI%2BAE9XjxZsmC%2FVcDN1f49gZ15mjDphbcsMXaxHNiVfXCQMjNeero%2FyaxA5SCsaHkv99Blu8NdJybfX3%2B%2FzvCUHu1PfkOOrEdCX4U&X-Amz-Signature=9ca88f9a70f80ac36ed44d6121ad7dff2b1632897939cabcdf3d37468bc5c8a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







