



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W57CL2CO%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T061345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0BT6ZfsMARS2Vyf43uyMuxTXVnn7zWkrvQ7J%2BRH5bXAiAX%2BKhDnMN5AlSBIqLnwZws2xWu4dqMbAMHRxN1ZMZ2Ryr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMg83RYtQzhUWYY8%2ByKtwDXHguejazCQFsdV1gcAWCVzwJLsDgg4CE06eI%2F612F8Hrvv8nR3WMbQApfTiHciT1tMivTHXdILFeBasvjYh0tWzH%2Fz9qLOOHZMFXKtuZisW6Pr0CNjmdI%2Bizr4iCz9dSubBTVM1saTvA3NM2qkZFZKFVBPkI65ZkM564z6TwE1f9Q3JI4asRFaKRzpZMQij5iRv8ue25gdc0c7PQYMFwvxOKQ8xCvi92BRWDSY7byng0ULlIwYnisd5z9He%2FXxkw82kooNSyjRCdb%2Bt1x95wLnlMePXzfaC8yTdxH1Cu3S3QNVhRnWmE%2BO6x7lrJd9pH5su49wcBamKVCaFdjWdvMLT0l4n7UXHjxwq886BARk3rHNJbKQLc0stDEM2D%2BPsSv5QPLNGewbsTO8jf5anMMIFKOn6JGrvu75yli%2B2X3iQyulgUN23TbZio2EDBt%2BlR2prbpdmBs8F4bQjbxxl%2BfratzPxMWL%2B8rSSvWDGCaMcLli7KdSReeE%2F83SIgChAJrXFzdAQBpU%2BCVgXQS4NU%2Bl6L3mBKbtdM%2FRqLqf5xvqIm8AlpyaShHUxMIXDSjj8Qcn%2BOYW68qYCfjISMyy%2FzNi%2F0juSBMiM4Oz191CLE9lKKv8bM%2Fk8HzhYCwqAwt%2FCI1QY6pgGql5tYHsYnmDpBJbJtChfZdzkQisB0LqlQofV12r07y0slff4smZHkv7MPJ6Z4sESDFmiVF9vweyN4TirX3v8dQ9QpaIYvLbyyqESM1d7Uk7PGw8%2BFe4hOhKkkfXGnn%2FwjukCG8LTyDAiSAF9fBpPGcE3J9HD5vSqtVda7jAfgXRNOdLUl12Sfu1%2FbnPa3Bgojk%2FDG1mFxLBXW8VMh6q46l%2Bu%2FYS4y&X-Amz-Signature=66c129c6cd88a7a9f3dc6b7b95837c1abe88f8b5d39c3a77cdb02e7398328a50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W57CL2CO%2F20260910%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260910T061345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0BT6ZfsMARS2Vyf43uyMuxTXVnn7zWkrvQ7J%2BRH5bXAiAX%2BKhDnMN5AlSBIqLnwZws2xWu4dqMbAMHRxN1ZMZ2Ryr%2FAwh%2BEAAaDDYzNzQyMzE4MzgwNSIMg83RYtQzhUWYY8%2ByKtwDXHguejazCQFsdV1gcAWCVzwJLsDgg4CE06eI%2F612F8Hrvv8nR3WMbQApfTiHciT1tMivTHXdILFeBasvjYh0tWzH%2Fz9qLOOHZMFXKtuZisW6Pr0CNjmdI%2Bizr4iCz9dSubBTVM1saTvA3NM2qkZFZKFVBPkI65ZkM564z6TwE1f9Q3JI4asRFaKRzpZMQij5iRv8ue25gdc0c7PQYMFwvxOKQ8xCvi92BRWDSY7byng0ULlIwYnisd5z9He%2FXxkw82kooNSyjRCdb%2Bt1x95wLnlMePXzfaC8yTdxH1Cu3S3QNVhRnWmE%2BO6x7lrJd9pH5su49wcBamKVCaFdjWdvMLT0l4n7UXHjxwq886BARk3rHNJbKQLc0stDEM2D%2BPsSv5QPLNGewbsTO8jf5anMMIFKOn6JGrvu75yli%2B2X3iQyulgUN23TbZio2EDBt%2BlR2prbpdmBs8F4bQjbxxl%2BfratzPxMWL%2B8rSSvWDGCaMcLli7KdSReeE%2F83SIgChAJrXFzdAQBpU%2BCVgXQS4NU%2Bl6L3mBKbtdM%2FRqLqf5xvqIm8AlpyaShHUxMIXDSjj8Qcn%2BOYW68qYCfjISMyy%2FzNi%2F0juSBMiM4Oz191CLE9lKKv8bM%2Fk8HzhYCwqAwt%2FCI1QY6pgGql5tYHsYnmDpBJbJtChfZdzkQisB0LqlQofV12r07y0slff4smZHkv7MPJ6Z4sESDFmiVF9vweyN4TirX3v8dQ9QpaIYvLbyyqESM1d7Uk7PGw8%2BFe4hOhKkkfXGnn%2FwjukCG8LTyDAiSAF9fBpPGcE3J9HD5vSqtVda7jAfgXRNOdLUl12Sfu1%2FbnPa3Bgojk%2FDG1mFxLBXW8VMh6q46l%2Bu%2FYS4y&X-Amz-Signature=50df1d2111c4dcfde989d2bba8b9887b46fbccd4f6da9322f25c560eba8fb3c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







