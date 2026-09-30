



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VS5OV6N%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T002318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrJmS4Xqd%2BaBe7URTY6mMUjFox1aD2YZEZuQ8%2BPImUjAiA6uSbhn%2BCP6CNGiBU8HVK8Uk3DoPKqNZvlMjpNkT0FuCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMWrtdGsz3vBo5jF2tKtwDHb594GTs%2F5WekWKw2Dp8UdUCVJaYU4So%2FnSTuz2LcNiCLKeRoInpannbK222iXryPUk1vgLPkGPlkFn5Aspx%2BDXNxjbQN3%2BCsaoi%2BwrUYQP4Z6VkXwcPFQ5pkqv%2FiJf4GkQx7s6kkcO3Otw47Z2YG6vMw4uOQSLLYnVGgv7%2B%2Fjn0BYsUrfGfqKMvsB8BwDjUdLRjJwfizyRrhand549oJp3ZswMHjGwfMaOGugBOPxEClEeMR5bWhwBumYmjdZfJ9oNjrAfBSNSdoBKR4akdxKYR9gvkTqf%2FG3Wpey9g7CL93r1ykdiogVuuHp6Dz2wfbZdUMREq%2BDZ%2FRpY8dISuTv5YBWRY3WUL01FyprZCKOtGk1vIw7juZDlbpud0VCW1vQgAqDz32R%2BY71%2F2S5W5K67OWEBZSDRMNKx50ubZA%2BM056kGqUuRg7xaQBOIhNdgG1GHLVLpQMDb5kZe1gthpHY7sPVQ39%2BCwUnOIe8kmNqyI0JUht59OP%2F44QJJvHVKZQKf90cvMfZvUee%2B%2FkDhPgC4xelJB4T1UFffkIHj8fBwQG5%2BRTc70gyn9EE9e9I8bthLXs3YsMYFH6Xj2OmbcCF977kok2leBUmVzM2TGaaGA2xtAcmKz%2BVjrnUws7Lw1QY6pgFL%2FxinFakh0vmvt6n%2B%2BoY%2FE3bB0nZ9CYzIgHEgmvV3HNSeUzgnE80OwSyVzbS8fJJk0npFZlP0284NagM2rLP3lpv15lWFdlZRH5m2H%2BiFVjd1geXWaywlCmgoNLbM5MtEQuxPTGQLDqx74oEQG%2BUYGQWH%2F6HxUVOaLXWoskhrprW1WvEF8RLf8w6jVPkia6PPQpOG5JJVPM%2F1eByKh8tfo6enBVXw&X-Amz-Signature=c0f78115a77bab233822f35b75dbd0c93a11cbeabbcbfe1488d14487b0da97c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VS5OV6N%2F20260930%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260930T002318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrJmS4Xqd%2BaBe7URTY6mMUjFox1aD2YZEZuQ8%2BPImUjAiA6uSbhn%2BCP6CNGiBU8HVK8Uk3DoPKqNZvlMjpNkT0FuCr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMWrtdGsz3vBo5jF2tKtwDHb594GTs%2F5WekWKw2Dp8UdUCVJaYU4So%2FnSTuz2LcNiCLKeRoInpannbK222iXryPUk1vgLPkGPlkFn5Aspx%2BDXNxjbQN3%2BCsaoi%2BwrUYQP4Z6VkXwcPFQ5pkqv%2FiJf4GkQx7s6kkcO3Otw47Z2YG6vMw4uOQSLLYnVGgv7%2B%2Fjn0BYsUrfGfqKMvsB8BwDjUdLRjJwfizyRrhand549oJp3ZswMHjGwfMaOGugBOPxEClEeMR5bWhwBumYmjdZfJ9oNjrAfBSNSdoBKR4akdxKYR9gvkTqf%2FG3Wpey9g7CL93r1ykdiogVuuHp6Dz2wfbZdUMREq%2BDZ%2FRpY8dISuTv5YBWRY3WUL01FyprZCKOtGk1vIw7juZDlbpud0VCW1vQgAqDz32R%2BY71%2F2S5W5K67OWEBZSDRMNKx50ubZA%2BM056kGqUuRg7xaQBOIhNdgG1GHLVLpQMDb5kZe1gthpHY7sPVQ39%2BCwUnOIe8kmNqyI0JUht59OP%2F44QJJvHVKZQKf90cvMfZvUee%2B%2FkDhPgC4xelJB4T1UFffkIHj8fBwQG5%2BRTc70gyn9EE9e9I8bthLXs3YsMYFH6Xj2OmbcCF977kok2leBUmVzM2TGaaGA2xtAcmKz%2BVjrnUws7Lw1QY6pgFL%2FxinFakh0vmvt6n%2B%2BoY%2FE3bB0nZ9CYzIgHEgmvV3HNSeUzgnE80OwSyVzbS8fJJk0npFZlP0284NagM2rLP3lpv15lWFdlZRH5m2H%2BiFVjd1geXWaywlCmgoNLbM5MtEQuxPTGQLDqx74oEQG%2BUYGQWH%2F6HxUVOaLXWoskhrprW1WvEF8RLf8w6jVPkia6PPQpOG5JJVPM%2F1eByKh8tfo6enBVXw&X-Amz-Signature=5445098189d756e263b42ec63470cdcc6b47b21749253978309d5734f2356582&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







