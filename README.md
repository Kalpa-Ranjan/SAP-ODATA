



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDKQVNJ%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T022340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDxE9Oo%2BBpnofkFbcvkUUGoV6wia6mjrGvP6GL%2BW%2BbQAiAUUreVM6XuWFlaqmbG2ELfGk3DRMYp78zNiK5RS6EVViqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMykvjQ1aBq9UwxHlnKtwDFvORlDarENR1xnY64xgNZ3mrth9hXSWimbzu7Vs8Au%2BJ1Ob4qfVXvrp%2FgfHcMvYlJ0Zg47U5oWcx8hiSrvnvdaGqOFKBZpt%2B5Ru3DBUQoFB8DCi%2FBh2LFVSsTRGZ8gJToMCbqyBgGPgRWP3yb%2FVijPuop4p6ZUIkMvDwZtugVATvxVtjZDCOZ4zHt%2FVVj%2Fd%2FL%2BKHsU2qN8ZNX6gd%2F3EhGRR%2Bm68OOeiBdMTptX5%2B8vMAfWCxoLVP6Thg9DkumKOvdrTGl1WC4%2FldWdBOvjyTJLxTYeguyo281gHFnpkvLjlaEQyfUeZ0Fgt3N0pBFXKS4VmoJGZkUwWhc011VkF25%2FgqlCbxaIxTAx%2BxIh2MdoliMX41aMJqDREZR%2FMm3kFVDU09VL3YP7BxVHLPUGT%2FYqNpLzEbpHiZVEpWRK8%2BiBZnXrOLOlvYxIyfq534UMEdiHQ4VOM%2Fl%2FzuPpXpBJUCnyCVXr2hptMnrkUXWyBq2JYZVGt16zCLuRgdDLLH2PuAv4PT92B6P2LtLIqBfx2Rx7SzCgsNz7mhZd5HaiaEdu029vPifWSeW5ylH20sDI3HP%2FHT5wLS51owIR1rOWMwJDvu4uUo%2BdENWcl8G5XRWc9rG5QoN7Fh3GKBclYw44q7zwY6pgEiHg%2FFK8irBZqe2A0Z1qTJHy9X2pA0hTCUaZi4NmMflPGAGKQ52xvqXFKI%2F8MzF1e%2FFLMp2cOyvIo6psEuFax1beqUWNzJ66jurN%2F97v9ZoWnhPmc0yVBlFw0hrAS9cmutrxxvlF0YipEg6axQsIM1OAPG8WChe%2BImxMUIRIRDHY3DXjGpvQab74ajIG9dKtaqCvx0aTaGFI3OSbLGIDIh3cey%2F%2B0D&X-Amz-Signature=f0a7e0c67c70205ce179eed2bae79cabf3e2117489abeec05523d163ec47fbdb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJDKQVNJ%2F20260427%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260427T022340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDxE9Oo%2BBpnofkFbcvkUUGoV6wia6mjrGvP6GL%2BW%2BbQAiAUUreVM6XuWFlaqmbG2ELfGk3DRMYp78zNiK5RS6EVViqIBAi7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMykvjQ1aBq9UwxHlnKtwDFvORlDarENR1xnY64xgNZ3mrth9hXSWimbzu7Vs8Au%2BJ1Ob4qfVXvrp%2FgfHcMvYlJ0Zg47U5oWcx8hiSrvnvdaGqOFKBZpt%2B5Ru3DBUQoFB8DCi%2FBh2LFVSsTRGZ8gJToMCbqyBgGPgRWP3yb%2FVijPuop4p6ZUIkMvDwZtugVATvxVtjZDCOZ4zHt%2FVVj%2Fd%2FL%2BKHsU2qN8ZNX6gd%2F3EhGRR%2Bm68OOeiBdMTptX5%2B8vMAfWCxoLVP6Thg9DkumKOvdrTGl1WC4%2FldWdBOvjyTJLxTYeguyo281gHFnpkvLjlaEQyfUeZ0Fgt3N0pBFXKS4VmoJGZkUwWhc011VkF25%2FgqlCbxaIxTAx%2BxIh2MdoliMX41aMJqDREZR%2FMm3kFVDU09VL3YP7BxVHLPUGT%2FYqNpLzEbpHiZVEpWRK8%2BiBZnXrOLOlvYxIyfq534UMEdiHQ4VOM%2Fl%2FzuPpXpBJUCnyCVXr2hptMnrkUXWyBq2JYZVGt16zCLuRgdDLLH2PuAv4PT92B6P2LtLIqBfx2Rx7SzCgsNz7mhZd5HaiaEdu029vPifWSeW5ylH20sDI3HP%2FHT5wLS51owIR1rOWMwJDvu4uUo%2BdENWcl8G5XRWc9rG5QoN7Fh3GKBclYw44q7zwY6pgEiHg%2FFK8irBZqe2A0Z1qTJHy9X2pA0hTCUaZi4NmMflPGAGKQ52xvqXFKI%2F8MzF1e%2FFLMp2cOyvIo6psEuFax1beqUWNzJ66jurN%2F97v9ZoWnhPmc0yVBlFw0hrAS9cmutrxxvlF0YipEg6axQsIM1OAPG8WChe%2BImxMUIRIRDHY3DXjGpvQab74ajIG9dKtaqCvx0aTaGFI3OSbLGIDIh3cey%2F%2B0D&X-Amz-Signature=966601ea9c00fbed60cffe0c95b461a20dab5dd2d32073ce805e3045186df7aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







