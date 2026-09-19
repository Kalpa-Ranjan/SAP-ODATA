



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU7NNB62%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T061157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB8p0V4JHlWeacNAiio2zGkKWNYiBryBI6wfqrjB8rS2AiAtzrxwt%2FvhTqvfchWsniHROgkZkldZBQqucneYcSa2Byr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMJCKyYXxS%2B%2BzDPeKOKtwDS3Tq79RQ9I7e1sf57%2BX92jkGWUMwY5n%2BFLq4R%2FqeQuonIH6Sb96eEW%2FwD7MFd96l3Ne105sA1%2BHXfHPABJGPNfgN3Tw%2F7M0Sg3%2B3mtivfifUFj1DKL1DbvXH%2BkIzFzAj08cQneT5IXE3KYDgvTSn590GsjjoOFrZegvq0FAJRF0lYEJpQHARkULX1RpH%2BI3%2FQvasimk6zu%2BxlG9iv6sPnL3I6i7nu9mbGDTxFdAPw6pRkh1p7%2B9bdBdhSNm80XjwSQxZdMx0C0c47FZaukMvuYaQsyBq2yBs6%2Bk3fblfsG%2F8odjakvYa6yJvY1%2B1vptlrNxK8hhK5cJPQIH%2Bt%2Bf7upWOd%2B9%2Ff34yGEDvUCJXfKP6%2BA3D70gdMQBOsD1NbYkl3nVcBT4Xl17QwAgPZ6Sfda3X%2BThl0yblQf3eaZJ01yO5QFwxa0OifYcEo3KuoNQq6rpVLRWiuvW3Bzw%2B%2BQ%2BoxhgAwOSMO%2BgevZXz%2FI3ym4KGfsEbX30ZJ8FzZRRnSb%2F7hhEOLOUpV26jZInUO7bAFKy2T8mxKD4juE%2FjiKR%2FM4BTZEVH4%2FW2M4%2BpdxQfRPb3UsvWN%2Fv0636vmmHLVAyg1NclKzK2IxUMeBfyXPYsro2meFI9JwMwMDb5h4Ywg8y31QY6pgGZMpWmZGpRO34Liw2ihgb42huhA6ZEt7VNbDCUn9OCDukxR0OrXVgUGofRLjebPOEMqueLcDG3WZKUNczGldCF1aJeqpqgJVomz4j%2BsEVhrp%2FIpQOdofMXuKrrP4TLQgq0I9bu3jCHhp1Dko77pl%2F7oz9hb5JCut%2FlzS7SMAzjGXufibhnw8iL9FrznieXl1AN9ILcKBqQwErwnskb97zA5QGJ%2BE8i&X-Amz-Signature=b6780ded5f8e1dd0c142662ca778a557c6ca67555fe538bf1971e655eb7a44a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UU7NNB62%2F20260919%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260919T061157Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB8p0V4JHlWeacNAiio2zGkKWNYiBryBI6wfqrjB8rS2AiAtzrxwt%2FvhTqvfchWsniHROgkZkldZBQqucneYcSa2Byr%2FAwhTEAAaDDYzNzQyMzE4MzgwNSIMJCKyYXxS%2B%2BzDPeKOKtwDS3Tq79RQ9I7e1sf57%2BX92jkGWUMwY5n%2BFLq4R%2FqeQuonIH6Sb96eEW%2FwD7MFd96l3Ne105sA1%2BHXfHPABJGPNfgN3Tw%2F7M0Sg3%2B3mtivfifUFj1DKL1DbvXH%2BkIzFzAj08cQneT5IXE3KYDgvTSn590GsjjoOFrZegvq0FAJRF0lYEJpQHARkULX1RpH%2BI3%2FQvasimk6zu%2BxlG9iv6sPnL3I6i7nu9mbGDTxFdAPw6pRkh1p7%2B9bdBdhSNm80XjwSQxZdMx0C0c47FZaukMvuYaQsyBq2yBs6%2Bk3fblfsG%2F8odjakvYa6yJvY1%2B1vptlrNxK8hhK5cJPQIH%2Bt%2Bf7upWOd%2B9%2Ff34yGEDvUCJXfKP6%2BA3D70gdMQBOsD1NbYkl3nVcBT4Xl17QwAgPZ6Sfda3X%2BThl0yblQf3eaZJ01yO5QFwxa0OifYcEo3KuoNQq6rpVLRWiuvW3Bzw%2B%2BQ%2BoxhgAwOSMO%2BgevZXz%2FI3ym4KGfsEbX30ZJ8FzZRRnSb%2F7hhEOLOUpV26jZInUO7bAFKy2T8mxKD4juE%2FjiKR%2FM4BTZEVH4%2FW2M4%2BpdxQfRPb3UsvWN%2Fv0636vmmHLVAyg1NclKzK2IxUMeBfyXPYsro2meFI9JwMwMDb5h4Ywg8y31QY6pgGZMpWmZGpRO34Liw2ihgb42huhA6ZEt7VNbDCUn9OCDukxR0OrXVgUGofRLjebPOEMqueLcDG3WZKUNczGldCF1aJeqpqgJVomz4j%2BsEVhrp%2FIpQOdofMXuKrrP4TLQgq0I9bu3jCHhp1Dko77pl%2F7oz9hb5JCut%2FlzS7SMAzjGXufibhnw8iL9FrznieXl1AN9ILcKBqQwErwnskb97zA5QGJ%2BE8i&X-Amz-Signature=2502a3bbeca8c2ade3354b92d01a7b0f731487a4d63b858e62b5649de5b40782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







