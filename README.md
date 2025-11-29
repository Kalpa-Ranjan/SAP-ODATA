



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UECFF5NB%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T182051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCfg2qfaK6Wjp%2BrDY0%2FzhAvRPXaz9Q9KxIrtmc6CieOXAIhAP9XePlWrl4WoWtVkNLD%2FvMnALgIx5Z3pWw4wIXxDin7KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrOrikCDyMsOJMQpUq3AOKdZz%2BVXEiOWHANiKooSULxUE2fv3h96Xehappm%2F8KbnmIFsux4O3RQIzQha3F7IMa%2FUCLB8MszhBBXEsiy7aSSudmBxh8IQvsBvbzRoOFF6ib5WUkr0zmY6bQ1RI5LZj0Pk0bTNHNrn2yvG8yzTk%2FUuJ619aXku1mnHVCK7J6loXzD8vQqHfrWw7%2FS60%2FJJBpYygBGylsQalrYS7RHPbROxE%2BDw%2BaknFnKMf7j%2BzqRmDhsUB6QiKw4DhKfi1dbAurvXhSjygJAivNB7BdmeHyMym%2FpMHvg0rBUGgsilLRYQzjb%2BLmJYtkpZwAFvJ1dNQbxBsfxkmH1dpWRk8%2FLgWV13BnIkoPBKNdryqZ9Z6MxMlBWzAmB7g9B6L1TX2BrqqKh9VKtmO0HO6U%2FUrDHizNTVFBR93ngPCx8MUUaj0wsCt8RPXK0fjuCiQ9TxPQJxx7Mo64cINXRGqMT5%2B%2F8SfSS5Y8ubZadQvgDMTYfeP2s2xPeWsN%2FkiOJ%2B6anjIu1mSfM7uayAjSQaRwyVIDI9uXxBGLm89jUAj3ewyglaIyGUP6PzPOm25lLOzs5%2FQF3DgfINoV9bzB4iEOkfGA3GSCi5%2FyVUSUp1pAAA9AH9C%2B276w75pOjnO1MhDY2DD0rKzJBjqkAQVGgtXZ%2BRX%2FyPruNhVQ0P%2FyBxDf1e7Iow0bD3tn1VvTvC8vAd24TYaRMZ591injUdiG%2F8CTqA8UW5SpPz3XEjcMjcimkCapo2eJD7AStpKKhpbpSsdyO81yd9UUdti%2BiwEvN9uERjuD6JW%2BqAtG4J9El9iEVa%2F7zjeZm2ikLK%2FGgRYTpp89nYITjN82o0BBzYPME0jdH3tnukIUIXa%2FAWuHC2bb&X-Amz-Signature=b669554b16b6207d8dc1546e13eeca776fd73a51c5f3bc3fcba3c6cd40341c44&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UECFF5NB%2F20251129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251129T182051Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAgaCXVzLXdlc3QtMiJIMEYCIQCfg2qfaK6Wjp%2BrDY0%2FzhAvRPXaz9Q9KxIrtmc6CieOXAIhAP9XePlWrl4WoWtVkNLD%2FvMnALgIx5Z3pWw4wIXxDin7KogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrOrikCDyMsOJMQpUq3AOKdZz%2BVXEiOWHANiKooSULxUE2fv3h96Xehappm%2F8KbnmIFsux4O3RQIzQha3F7IMa%2FUCLB8MszhBBXEsiy7aSSudmBxh8IQvsBvbzRoOFF6ib5WUkr0zmY6bQ1RI5LZj0Pk0bTNHNrn2yvG8yzTk%2FUuJ619aXku1mnHVCK7J6loXzD8vQqHfrWw7%2FS60%2FJJBpYygBGylsQalrYS7RHPbROxE%2BDw%2BaknFnKMf7j%2BzqRmDhsUB6QiKw4DhKfi1dbAurvXhSjygJAivNB7BdmeHyMym%2FpMHvg0rBUGgsilLRYQzjb%2BLmJYtkpZwAFvJ1dNQbxBsfxkmH1dpWRk8%2FLgWV13BnIkoPBKNdryqZ9Z6MxMlBWzAmB7g9B6L1TX2BrqqKh9VKtmO0HO6U%2FUrDHizNTVFBR93ngPCx8MUUaj0wsCt8RPXK0fjuCiQ9TxPQJxx7Mo64cINXRGqMT5%2B%2F8SfSS5Y8ubZadQvgDMTYfeP2s2xPeWsN%2FkiOJ%2B6anjIu1mSfM7uayAjSQaRwyVIDI9uXxBGLm89jUAj3ewyglaIyGUP6PzPOm25lLOzs5%2FQF3DgfINoV9bzB4iEOkfGA3GSCi5%2FyVUSUp1pAAA9AH9C%2B276w75pOjnO1MhDY2DD0rKzJBjqkAQVGgtXZ%2BRX%2FyPruNhVQ0P%2FyBxDf1e7Iow0bD3tn1VvTvC8vAd24TYaRMZ591injUdiG%2F8CTqA8UW5SpPz3XEjcMjcimkCapo2eJD7AStpKKhpbpSsdyO81yd9UUdti%2BiwEvN9uERjuD6JW%2BqAtG4J9El9iEVa%2F7zjeZm2ikLK%2FGgRYTpp89nYITjN82o0BBzYPME0jdH3tnukIUIXa%2FAWuHC2bb&X-Amz-Signature=f98b13ff0c010148d2ed8d986eb1bad6d8ed725db7778ab18f1df30eb2155417&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







