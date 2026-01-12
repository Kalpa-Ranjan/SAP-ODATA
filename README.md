



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPM3OU5%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T062945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCICf1edQE%2BIpfcO1F4cex0612n2APl7TmhT6sPzlbh7gYAiAdNYz%2FQn79cG7cm3TEOkxD4gYpuSWGZlmvcEPhMrkHuiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1UL7zYxodzQtVkBfKtwD1qWaX0V94zDFyWAurPQJoik0iX8BYz3iFD4hirqQa%2FJN8WMZqcCk1RoTrfDMx7DzvlH19X5TAF8BNxV6THjZofokQlGjvy9E1A4h%2FrzrSjYE1BoUhfSM3z1iy32j6jqiPYH0iAB4zFSElB04kQmkZ73XSa0lBM6ztxzlF857A81DFCJJJTBKBjxO406niEV%2BW9m%2FGwYvv%2FZNnHZKKdUV91c83N8A9vV7myjLVOyMkNgM3H4BHfWIJBB9pfaP%2FEYn20SE%2FbdZ5zviCjpiQnyoGXelVUz8KEHI92n%2Bzn1f%2B6AWNqOHb0O89Y9%2Bv0VfvBs%2FNnWzmpTGYYeQGq0lVJ74tis3o2s8EhS%2FBSKskctNFhD0E6qqsf%2F0FS870RSTvDlABLjF6kSWjch07voWJbPzglqP76r0FCDxFedK9%2BoLRRFMgPTtYmOBMvsOw9QXiqGsizWRuZbwKu1VaoW2fshk3exonJGCkuiG3jG%2BzwbuOnYFKOUVm5uuUVbv03F76FyXPUZEFmOmVzbb8WeWlPPtjFXaX0s%2FSoaDNYS%2F2Cf5gFA%2Bo1zkH%2Bg5K2PXZBnB4K0LrqqNsbAfRugISTxd54R49k2eDsPb0Bo%2FSA4R5GrLwuuiSq5dXcA3gQbMry8wx6aSywY6pgHpnbnRpGpecCtHkL7SxeR1x%2FjIldFV0ozpHdmxTuGDoEGAaSvLYID4ElTh1NUImR0Zgi6Sn0grV8ij45%2Bostgxp9LdjhS2tR7fCjbuJ0LXJMs2WcEJzCzI7O1O7UjQPFnMQaBQBNt7gLydPntJcllNjvk8ykZLYfz7LaBG7ZYxGki9LRG5yq%2BUfXGmiY%2Fnz6qMsBaPb0nl11TveWaavMYyhnW2GsC7&X-Amz-Signature=ecd74e652524f256f646dd5b0ebcdaf1928d17e1f0a8c6ccf1c47df62af34ffa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DPM3OU5%2F20260112%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260112T062945Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJGMEQCICf1edQE%2BIpfcO1F4cex0612n2APl7TmhT6sPzlbh7gYAiAdNYz%2FQn79cG7cm3TEOkxD4gYpuSWGZlmvcEPhMrkHuiqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1UL7zYxodzQtVkBfKtwD1qWaX0V94zDFyWAurPQJoik0iX8BYz3iFD4hirqQa%2FJN8WMZqcCk1RoTrfDMx7DzvlH19X5TAF8BNxV6THjZofokQlGjvy9E1A4h%2FrzrSjYE1BoUhfSM3z1iy32j6jqiPYH0iAB4zFSElB04kQmkZ73XSa0lBM6ztxzlF857A81DFCJJJTBKBjxO406niEV%2BW9m%2FGwYvv%2FZNnHZKKdUV91c83N8A9vV7myjLVOyMkNgM3H4BHfWIJBB9pfaP%2FEYn20SE%2FbdZ5zviCjpiQnyoGXelVUz8KEHI92n%2Bzn1f%2B6AWNqOHb0O89Y9%2Bv0VfvBs%2FNnWzmpTGYYeQGq0lVJ74tis3o2s8EhS%2FBSKskctNFhD0E6qqsf%2F0FS870RSTvDlABLjF6kSWjch07voWJbPzglqP76r0FCDxFedK9%2BoLRRFMgPTtYmOBMvsOw9QXiqGsizWRuZbwKu1VaoW2fshk3exonJGCkuiG3jG%2BzwbuOnYFKOUVm5uuUVbv03F76FyXPUZEFmOmVzbb8WeWlPPtjFXaX0s%2FSoaDNYS%2F2Cf5gFA%2Bo1zkH%2Bg5K2PXZBnB4K0LrqqNsbAfRugISTxd54R49k2eDsPb0Bo%2FSA4R5GrLwuuiSq5dXcA3gQbMry8wx6aSywY6pgHpnbnRpGpecCtHkL7SxeR1x%2FjIldFV0ozpHdmxTuGDoEGAaSvLYID4ElTh1NUImR0Zgi6Sn0grV8ij45%2Bostgxp9LdjhS2tR7fCjbuJ0LXJMs2WcEJzCzI7O1O7UjQPFnMQaBQBNt7gLydPntJcllNjvk8ykZLYfz7LaBG7ZYxGki9LRG5yq%2BUfXGmiY%2Fnz6qMsBaPb0nl11TveWaavMYyhnW2GsC7&X-Amz-Signature=a237a366858b914358b15ce36b24f5428059ccf1b443ea34905b8ec63f49e6bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







