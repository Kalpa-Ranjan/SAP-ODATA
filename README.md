



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US5H7C3A%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T185628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4TPiz7OnRXeoy97bxGwHwLbBccQn3xnpiUj99T4LYaQIgAbkF%2BPdV23ds7cB%2BijalWHUr%2FxKRJtck0RuK6tVCmtcqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLR%2F5NLBXQ%2FTu0DBCrcA8BI0WrhDvPFet3bjHeYYmb3ay%2F8mvFufH3RIyR1cWIYy7sqkE0I5b9mBiZl5iDJUlMCrD6NWIYgw1HODW%2BZHfIlc1sPNaYPjKQGavTJKwlXnf6RORHjhXYrqMIjEaPoHao7en%2BHtyfWUMA1gkQ85%2BFj7y0H8d7TBy%2FOk7Qbf7e2WZm6pS6oeRvumRwe%2BXNB9U5FHY4QDyU7erkVc6%2FgFvp9sWKGkD%2FwN3%2B0uiWWWtjF5fbaj4b4IauX5ntZy6FnGflLRhmDufqXqcc%2F66tUVjcmMZLe2MSvBpIMedc%2BSf3fi7rwYiAGnxafvV4Z878uomKijJ4lAQyo%2BcCjAuZ6NFI0ZOU5uYe6fZg6kQxrNewfbhVPf9kkNPUm0VC15jtILJXG9fgvr2e7TP54KmEOXPeOuWDSoGhAfqtahw046ncgT0oj5%2FlyacobRkDvre0fRUoskMTIEHRUWlubMH%2F0D9Uu5UcORqq%2FGMv3T00lLi9zd%2BhtbTzdYkPpWsFpem7Rqq%2Bfj%2BDh6WoT5Fbr0shTfMY1k%2BDLzFnhCdpFJAjee6xNFf5UmXQCy2OOO5dQEpwEu8eHEXyhXFDUq04%2B%2Fh47v8fs3d2VRtzKE0RrakaofR%2BOgcR6Y4l922XtY%2BLDMOOFs8wGOqUBn5U8rHLGgUrQfSxFaKHgtniKJ2SWVkKG95NwYy1rvffTmKlB40%2FzrB%2FdJF%2FtkospebRGN7E%2FDwKN46rgKlr0N86pd7Q1TmLUdFKaqCaX09znTWKsWnOlc2Xnz8Za2LQWT6twefbXXCsbaXyqSIgZUMlks0UEBkHa9hFEdo5uGqzI1SqhxpFtK6j9SaAGGWGEIHYDFcUQHrmMXpwrCqdtNBXG9mM6&X-Amz-Signature=088b6b3338cc595b745a68358865565f7f3cea4a475a7c94e9202671ada2e3ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466US5H7C3A%2F20260211%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260211T185632Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD4TPiz7OnRXeoy97bxGwHwLbBccQn3xnpiUj99T4LYaQIgAbkF%2BPdV23ds7cB%2BijalWHUr%2FxKRJtck0RuK6tVCmtcqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGLR%2F5NLBXQ%2FTu0DBCrcA8BI0WrhDvPFet3bjHeYYmb3ay%2F8mvFufH3RIyR1cWIYy7sqkE0I5b9mBiZl5iDJUlMCrD6NWIYgw1HODW%2BZHfIlc1sPNaYPjKQGavTJKwlXnf6RORHjhXYrqMIjEaPoHao7en%2BHtyfWUMA1gkQ85%2BFj7y0H8d7TBy%2FOk7Qbf7e2WZm6pS6oeRvumRwe%2BXNB9U5FHY4QDyU7erkVc6%2FgFvp9sWKGkD%2FwN3%2B0uiWWWtjF5fbaj4b4IauX5ntZy6FnGflLRhmDufqXqcc%2F66tUVjcmMZLe2MSvBpIMedc%2BSf3fi7rwYiAGnxafvV4Z878uomKijJ4lAQyo%2BcCjAuZ6NFI0ZOU5uYe6fZg6kQxrNewfbhVPf9kkNPUm0VC15jtILJXG9fgvr2e7TP54KmEOXPeOuWDSoGhAfqtahw046ncgT0oj5%2FlyacobRkDvre0fRUoskMTIEHRUWlubMH%2F0D9Uu5UcORqq%2FGMv3T00lLi9zd%2BhtbTzdYkPpWsFpem7Rqq%2Bfj%2BDh6WoT5Fbr0shTfMY1k%2BDLzFnhCdpFJAjee6xNFf5UmXQCy2OOO5dQEpwEu8eHEXyhXFDUq04%2B%2Fh47v8fs3d2VRtzKE0RrakaofR%2BOgcR6Y4l922XtY%2BLDMOOFs8wGOqUBn5U8rHLGgUrQfSxFaKHgtniKJ2SWVkKG95NwYy1rvffTmKlB40%2FzrB%2FdJF%2FtkospebRGN7E%2FDwKN46rgKlr0N86pd7Q1TmLUdFKaqCaX09znTWKsWnOlc2Xnz8Za2LQWT6twefbXXCsbaXyqSIgZUMlks0UEBkHa9hFEdo5uGqzI1SqhxpFtK6j9SaAGGWGEIHYDFcUQHrmMXpwrCqdtNBXG9mM6&X-Amz-Signature=0d7acc2aa533d9ded10c35350afc63f3ddb1ee01fc253589b7f366e136945c7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







