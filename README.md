



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMJMG3DQ%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T180553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGt4BRLxvfSr0Hku%2BznV9xoRTmJgOpNmHhz%2FLcSYG2iVAiBxKgPjVo%2B8hpr%2BtOhrxDq5dhbyHci6ZYNxaag1sxO0vCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMorjs8xi1TVaK22leKtwDbbCzr%2FTmZM2D9fEx01CJwrTqrmuv1g%2BpTKhWLB6bfLgo4eSUJBL%2FFlUskOXiTVqVkx6XWceyYRFo9z9pJQrP%2FvitHZ9lnS1jgw9DGN3jmV%2BFfJR4YriWfWyBFcDECFhUqMpvD9hV7xFz%2BpfyC3lvVO3fLdM5ESwowH5kv2fTgLuDpBvqADfIJTjMdkV54aYeiCR6N8BaJRdQzGvbvqRB2Zpdjph%2BW1cvPH%2B3hCbG7CfgxhM%2FkvRiL9SZuTqDmBHBNF4ofi7P4TkFMk4dSyk%2BUQpd9EWfyuV2swXdlQCLDxs0Ks97%2F7aHhKwPYFx%2FqbaBlGdjlqmDEKLiwkM4pTcWGpeLhjd%2B4EG424hCoeOaMEWKRVJn%2BHrjZmUmprlwLmNqgDt5SvriW9pBtM5CwieQ85isNMQly1VdwN188fVIp7TK%2BSUzmBEImSM9EGUeWvIGGj22DtTPrlNB2wEFd8YiDKDNMsXrubyWfpdfE4iZ1d5jRR0Om%2F63WFZOoKzbXpDu828hJY8U2BxryJR7NXrcAE9KKmdVCg1wQ1zlOnlTD2TVhQLBtIz9xmjQmCdgTyGWZhi5kmasu7SXCgMQZALoSCq5eT2YIERJiHL9iCNJdNRet2%2BnsOUl%2FohnvoIw%2B%2F2i1wY6pgHf2IXII5OXfOAzO686ypDD7JLl0GQR7ChuOZ3dzk0kAVm1s9qGrCDXO0BP56CcRnAQDEGszQIIhMAN%2BWaejxSVEft9IiBkPEIuCfG%2FhC79Lx%2FNRJK%2FH3fxD5hLrabr1HlMNAKXQdaWdYZQwUFx50IJAVwCrBitcykvmAx8JITgLZ4T%2BqBa6a31pOfU3nEqlYZwyu9YOdBzjVA3kuKZ9B6gx2sVHS%2Bv&X-Amz-Signature=9ec2ed485579fa90bdd4c27380e0d14b71105d4ff5a9bbc8f3bd698bd9f5d66c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMJMG3DQ%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T180553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGt4BRLxvfSr0Hku%2BznV9xoRTmJgOpNmHhz%2FLcSYG2iVAiBxKgPjVo%2B8hpr%2BtOhrxDq5dhbyHci6ZYNxaag1sxO0vCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMorjs8xi1TVaK22leKtwDbbCzr%2FTmZM2D9fEx01CJwrTqrmuv1g%2BpTKhWLB6bfLgo4eSUJBL%2FFlUskOXiTVqVkx6XWceyYRFo9z9pJQrP%2FvitHZ9lnS1jgw9DGN3jmV%2BFfJR4YriWfWyBFcDECFhUqMpvD9hV7xFz%2BpfyC3lvVO3fLdM5ESwowH5kv2fTgLuDpBvqADfIJTjMdkV54aYeiCR6N8BaJRdQzGvbvqRB2Zpdjph%2BW1cvPH%2B3hCbG7CfgxhM%2FkvRiL9SZuTqDmBHBNF4ofi7P4TkFMk4dSyk%2BUQpd9EWfyuV2swXdlQCLDxs0Ks97%2F7aHhKwPYFx%2FqbaBlGdjlqmDEKLiwkM4pTcWGpeLhjd%2B4EG424hCoeOaMEWKRVJn%2BHrjZmUmprlwLmNqgDt5SvriW9pBtM5CwieQ85isNMQly1VdwN188fVIp7TK%2BSUzmBEImSM9EGUeWvIGGj22DtTPrlNB2wEFd8YiDKDNMsXrubyWfpdfE4iZ1d5jRR0Om%2F63WFZOoKzbXpDu828hJY8U2BxryJR7NXrcAE9KKmdVCg1wQ1zlOnlTD2TVhQLBtIz9xmjQmCdgTyGWZhi5kmasu7SXCgMQZALoSCq5eT2YIERJiHL9iCNJdNRet2%2BnsOUl%2FohnvoIw%2B%2F2i1wY6pgHf2IXII5OXfOAzO686ypDD7JLl0GQR7ChuOZ3dzk0kAVm1s9qGrCDXO0BP56CcRnAQDEGszQIIhMAN%2BWaejxSVEft9IiBkPEIuCfG%2FhC79Lx%2FNRJK%2FH3fxD5hLrabr1HlMNAKXQdaWdYZQwUFx50IJAVwCrBitcykvmAx8JITgLZ4T%2BqBa6a31pOfU3nEqlYZwyu9YOdBzjVA3kuKZ9B6gx2sVHS%2Bv&X-Amz-Signature=5394e132bd0fea2b48ded919532593433e85ebe785bbbed171820ba2527c2261&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







