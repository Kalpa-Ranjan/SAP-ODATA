



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LIYOESA%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T002006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQD2TFi5aWSFQrLrJZKBRrDcHOpcixnc8WPQJ%2BEwMROrEgIgduCL%2BvJEcDtxcn%2B4sB31u7%2ByNmnq%2Bk80tEaZvpOyNK0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDAO8E43uEQnvBGo0TyrcA2uA2TwODIPpGItKzVGDU4xmVjTnreKbNt3Luvq61TGqnMZqOVZD7parFH4XjM2fURzJgScbsrYlRGHFA4fE3lLgvl9cVquvixDpGa0nm3l3PPHafqVpdMTiQ48qvw%2BpdwkMNYqM7V6hpp5BUsUe2%2B0vhWDyVpH38PSR4vaCoceqhL9YeQoBUAOvxBwTXaqSsnqeuEV2uZheltZud%2F4SsO6BZTGCJw%2Fzap9ms5V9%2FQQD1GgFyWHO9cqCOu92TPpTYEw7fq6zh%2F3986WKWf83bnyYHR%2FtLG7EytXQOCyd9L%2BxIJCd8NYt%2FW5LNijAAXdythjPXyRXXkBqQiiNBw1rWtYZOOIVTkG%2FB%2FfVD%2BvHniWkIbZou2mh%2F7fw2gcw85ak1aqDQ%2FJrP0pOS1TFenB4Phciq1Hp95GKPlKq2MGhkFwSECOnuDSFRYvaxC9QF%2Fkw%2BDAsOcHXJoDJYaASTEDN%2BYv1xIVRdFy8GX9BaYXSkV2nRbhPmABDWLA3It6sWoHCyEX7Mf%2BkeoVwqcnqGhwnu9J7Apf7sLRx3LwgidV%2Bx%2FQHQWF4%2Brht97f%2FUSZei7wZPk4XDPz3uHARh2beFbBHEJGPsPWvAwmtD0GT91mPBrUSdrv51hnaLsX1d7pzMPWdrNUGOqUBFiFMMwSMuZbTle%2Bs%2FEP9fO4By08XW01lBDp2UVDJQlN5d0d2ZOJ4fyJNQBxRWgOetyglFzfQWW1q97Wm%2B%2BS9uLewChawCHfI%2BqNZWCh9i1eVQIc1QReI9licbVdcSSyImabIQDkGCtQu01Dr9bz5JfOCOvE4yHd8b9KlHjLkUtaeKheCuyqkVpdUGg7A8SfZQP%2Fre18P1UhZzfVbhqhTqAuGK1vC&X-Amz-Signature=841ce9125c945ec871fa3f1ccd4bf32b27ccb85cf548eb74f60769680ffa0597&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666LIYOESA%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T002006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJHMEUCIQD2TFi5aWSFQrLrJZKBRrDcHOpcixnc8WPQJ%2BEwMROrEgIgduCL%2BvJEcDtxcn%2B4sB31u7%2ByNmnq%2Bk80tEaZvpOyNK0q%2FwMIHxAAGgw2Mzc0MjMxODM4MDUiDAO8E43uEQnvBGo0TyrcA2uA2TwODIPpGItKzVGDU4xmVjTnreKbNt3Luvq61TGqnMZqOVZD7parFH4XjM2fURzJgScbsrYlRGHFA4fE3lLgvl9cVquvixDpGa0nm3l3PPHafqVpdMTiQ48qvw%2BpdwkMNYqM7V6hpp5BUsUe2%2B0vhWDyVpH38PSR4vaCoceqhL9YeQoBUAOvxBwTXaqSsnqeuEV2uZheltZud%2F4SsO6BZTGCJw%2Fzap9ms5V9%2FQQD1GgFyWHO9cqCOu92TPpTYEw7fq6zh%2F3986WKWf83bnyYHR%2FtLG7EytXQOCyd9L%2BxIJCd8NYt%2FW5LNijAAXdythjPXyRXXkBqQiiNBw1rWtYZOOIVTkG%2FB%2FfVD%2BvHniWkIbZou2mh%2F7fw2gcw85ak1aqDQ%2FJrP0pOS1TFenB4Phciq1Hp95GKPlKq2MGhkFwSECOnuDSFRYvaxC9QF%2Fkw%2BDAsOcHXJoDJYaASTEDN%2BYv1xIVRdFy8GX9BaYXSkV2nRbhPmABDWLA3It6sWoHCyEX7Mf%2BkeoVwqcnqGhwnu9J7Apf7sLRx3LwgidV%2Bx%2FQHQWF4%2Brht97f%2FUSZei7wZPk4XDPz3uHARh2beFbBHEJGPsPWvAwmtD0GT91mPBrUSdrv51hnaLsX1d7pzMPWdrNUGOqUBFiFMMwSMuZbTle%2Bs%2FEP9fO4By08XW01lBDp2UVDJQlN5d0d2ZOJ4fyJNQBxRWgOetyglFzfQWW1q97Wm%2B%2BS9uLewChawCHfI%2BqNZWCh9i1eVQIc1QReI9licbVdcSSyImabIQDkGCtQu01Dr9bz5JfOCOvE4yHd8b9KlHjLkUtaeKheCuyqkVpdUGg7A8SfZQP%2Fre18P1UhZzfVbhqhTqAuGK1vC&X-Amz-Signature=7cd522a7dbd47fd10cdf04dadef261531c5e23d717414c5d0775bce94126a142&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







