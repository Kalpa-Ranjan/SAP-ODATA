



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    1. RPC APIs:- Remote Procedure Calls
    1. WebSocket APIs:- Used JSON objects, two way communication
    1. REST API: - Most Popular
    

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

    1. The formatted resource is called a Representation in REST.
    1. Request should identify recourses by using URI
    1. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    1. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    1. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    1. Communication method in which the server completes every client request independently of all previous request.
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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTGF3GT2%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIDKd0aNmTC3jYLabVuSN44fNbkGWVj3MQKFFuNGlwEf%2FAiByP%2BkbNDHuXFO7wvfRUibEFLH7PhE0SK7ShKuH99JwJyqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGyH7XNUjRae0CF4AKtwDXRIouzLtiEp4FVyA38IFzVWtCvUqlKFtIkW%2BbIZk7gLCDFjNYkoxutugjcn3I5QoqVCmgh88%2FLfKwDtuXUSLWDq8P0Vm0YxPq6TEF18nLBHWSQc4ykMClHbM5wKJ6%2BqZfFUzNqfklyPJPDSaWnr5ABLwVUo3P%2Fnmx7yzvdBVd%2FklwWUSnNv4prLknR0Nd8mW6oMnJrR4y522eif2JBZYgraPkz5pxp39k6%2Fjlem1cdLwwDoH%2FnOB4ek4MMm%2BFu6gh3pqHVAFSQXEw%2Fr3wWN9CONsuvBgRZP1C78m%2FbJbKjQ9Q5nby02MtPeE%2BTI8LxnhiR9Hs99hA3aw5BFMPczdn6mEHqTNnwoy0JKV1f5lCeUFHGwLbL9O4MFFb4K3UVLcMSUguQ80RoEiE8SdH8ZUhBEwDdQeRvjZf9L6pB9gFFi148wTst5bTVkd1Fk1p8kP%2FTbBmX5FUhx%2F26pLrBMbuw9ts0eSqcXC8oiVHjpmkhyJKtobnHaWhnDigpgGxoovqgQ2nCuJ6KJOldw%2FuCrB8F%2FHdRJiSEKq0vyl6ZuV2RcfG8O%2FQnRMZ1CtchdVQAgzt5IFp7XEr24NhKBOJOcnemERJNIY2rn2BT7BBztza5qJm49i42hsNTw8pT8w%2FMWPyAY6pgFfbgvzXPpFb9%2BpttjNp%2BfZUn9co3oAQskR%2Bv%2Be8KEauHwK7QKTwZQQp5bLDdnrExuYgE789UNtFBmxArydyHteCHpoS30ejZOz3sKUSxP2oSYyCRuaGGcVHSKkEreVHtNVyyRSTG9AGMN0gCq%2B90L1QQ39h%2F%2B4l%2BXWehAw6nI6nyDblVtDrcz8%2FDFZVHmaGL5OXHbu80OCLu7wpMOQTvUxb5tjgRmg&X-Amz-Signature=e90e406a0394f038ce9dd5f7a0b6b57d0d956452326ceb635e15d91888096322&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTGF3GT2%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T225622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJGMEQCIDKd0aNmTC3jYLabVuSN44fNbkGWVj3MQKFFuNGlwEf%2FAiByP%2BkbNDHuXFO7wvfRUibEFLH7PhE0SK7ShKuH99JwJyqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGyH7XNUjRae0CF4AKtwDXRIouzLtiEp4FVyA38IFzVWtCvUqlKFtIkW%2BbIZk7gLCDFjNYkoxutugjcn3I5QoqVCmgh88%2FLfKwDtuXUSLWDq8P0Vm0YxPq6TEF18nLBHWSQc4ykMClHbM5wKJ6%2BqZfFUzNqfklyPJPDSaWnr5ABLwVUo3P%2Fnmx7yzvdBVd%2FklwWUSnNv4prLknR0Nd8mW6oMnJrR4y522eif2JBZYgraPkz5pxp39k6%2Fjlem1cdLwwDoH%2FnOB4ek4MMm%2BFu6gh3pqHVAFSQXEw%2Fr3wWN9CONsuvBgRZP1C78m%2FbJbKjQ9Q5nby02MtPeE%2BTI8LxnhiR9Hs99hA3aw5BFMPczdn6mEHqTNnwoy0JKV1f5lCeUFHGwLbL9O4MFFb4K3UVLcMSUguQ80RoEiE8SdH8ZUhBEwDdQeRvjZf9L6pB9gFFi148wTst5bTVkd1Fk1p8kP%2FTbBmX5FUhx%2F26pLrBMbuw9ts0eSqcXC8oiVHjpmkhyJKtobnHaWhnDigpgGxoovqgQ2nCuJ6KJOldw%2FuCrB8F%2FHdRJiSEKq0vyl6ZuV2RcfG8O%2FQnRMZ1CtchdVQAgzt5IFp7XEr24NhKBOJOcnemERJNIY2rn2BT7BBztza5qJm49i42hsNTw8pT8w%2FMWPyAY6pgFfbgvzXPpFb9%2BpttjNp%2BfZUn9co3oAQskR%2Bv%2Be8KEauHwK7QKTwZQQp5bLDdnrExuYgE789UNtFBmxArydyHteCHpoS30ejZOz3sKUSxP2oSYyCRuaGGcVHSKkEreVHtNVyyRSTG9AGMN0gCq%2B90L1QQ39h%2F%2B4l%2BXWehAw6nI6nyDblVtDrcz8%2FDFZVHmaGL5OXHbu80OCLu7wpMOQTvUxb5tjgRmg&X-Amz-Signature=a31f3f8501addbc7114c17f07b68188a3d56d6fa80e876bbea4c26bf208b53b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  1. Atom publishing Protocol
  1. RSS ( Really Simple Syndication) 


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





Test Github-Notion synch



