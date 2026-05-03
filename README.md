



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7ML3RTI%2F20260503%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260503T125824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwnCrBwHi%2FEB8A1GlwFXniLsx75djkGt1uhGJ17zmDCgIgPU%2BgFBRGV1axw8IgCwKE2hpCpTbXWksnWxa4%2FtbIN4sq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLqIee2NQl1AfqQ%2FtyrcA4V%2FcZA%2F4TuDxNeI5MJOT4xbrujAm6HR16v0IqxPeq9ASmJJ7%2BrZddbkerk%2FRI6TKESXTyz74DQg61Rt2hP8QZEe593TjNE6gY4EO8EijawwhwRjmLnT2S2qWwUvviKl98kdb8RxTtuFSES3SMUSfMGgQblCdGsj0Fuqt1z0jWQWGquRzKeEdAe1XX%2FSBEYfuenpkziAUPXwp7CjUhIhal8ejKmH3P9GWW%2FVTvuRg5%2Fxqc8%2B9ljDJkVOPtfFLnB5ANPb5SqB%2FCjT9qqQ2UDIo8myVabL4C4WZZnfmPNTf9mtSIIAW%2FSKdb4w2SrZli4SzXU7hzW9c2vFcxq9P07Wf%2FkRQsetq9mjyfakryFgxDDkU%2FKKK2PR5OJCoatz62ntYVdqg%2B%2FIIgFEqOVARiudjKWvZ7wP%2Fyti7NDUtjE0uL%2FKpWK6FoTYlr7n%2F%2FrErKwEyfU9MjgX9HsGbGe%2Ba5bE3BDq7uggZ2a%2FxEI4wHFd%2Frfh8AeU%2B9CvFjsDe29U8TRKGQ%2BeH7wEA5e%2Bge8ec4UA9L3ACRCs9BekATfijI8zzQWJNGPqh9tSi4IXwsBONhP91d64jZbPUoe8Y%2BLOxIZArXWuhPhjz6oRdKa6am87%2Fu01YTZrgfBJ5LsfJN7vMPzz3M8GOqUBp4Wd4qW4hAE0cXYkCIikVgKi%2BQ7qBlp%2FRo2FbJSqTTovP4BbOnS6juMbTgYtBoM%2FKOccQQbk3fcedpDgERQnbZSFXd7366TQTI7Z6BOj522QbmeBUA%2F5faHFYUUjJc5fEC6EK%2BqFLBVRkJeuwl520Hg9FHi55JmFywkIc3JVAmkqeAbkkkrdElYvKVG1D06q1LfMLLTKiRBDqXBqLlLVBmT2vHzY&X-Amz-Signature=b12285063a2aae16cf28a29c3145c162def4eeb3a8bea8bf88853eca4b5a9567&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q7ML3RTI%2F20260503%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260503T125824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwnCrBwHi%2FEB8A1GlwFXniLsx75djkGt1uhGJ17zmDCgIgPU%2BgFBRGV1axw8IgCwKE2hpCpTbXWksnWxa4%2FtbIN4sq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDLqIee2NQl1AfqQ%2FtyrcA4V%2FcZA%2F4TuDxNeI5MJOT4xbrujAm6HR16v0IqxPeq9ASmJJ7%2BrZddbkerk%2FRI6TKESXTyz74DQg61Rt2hP8QZEe593TjNE6gY4EO8EijawwhwRjmLnT2S2qWwUvviKl98kdb8RxTtuFSES3SMUSfMGgQblCdGsj0Fuqt1z0jWQWGquRzKeEdAe1XX%2FSBEYfuenpkziAUPXwp7CjUhIhal8ejKmH3P9GWW%2FVTvuRg5%2Fxqc8%2B9ljDJkVOPtfFLnB5ANPb5SqB%2FCjT9qqQ2UDIo8myVabL4C4WZZnfmPNTf9mtSIIAW%2FSKdb4w2SrZli4SzXU7hzW9c2vFcxq9P07Wf%2FkRQsetq9mjyfakryFgxDDkU%2FKKK2PR5OJCoatz62ntYVdqg%2B%2FIIgFEqOVARiudjKWvZ7wP%2Fyti7NDUtjE0uL%2FKpWK6FoTYlr7n%2F%2FrErKwEyfU9MjgX9HsGbGe%2Ba5bE3BDq7uggZ2a%2FxEI4wHFd%2Frfh8AeU%2B9CvFjsDe29U8TRKGQ%2BeH7wEA5e%2Bge8ec4UA9L3ACRCs9BekATfijI8zzQWJNGPqh9tSi4IXwsBONhP91d64jZbPUoe8Y%2BLOxIZArXWuhPhjz6oRdKa6am87%2Fu01YTZrgfBJ5LsfJN7vMPzz3M8GOqUBp4Wd4qW4hAE0cXYkCIikVgKi%2BQ7qBlp%2FRo2FbJSqTTovP4BbOnS6juMbTgYtBoM%2FKOccQQbk3fcedpDgERQnbZSFXd7366TQTI7Z6BOj522QbmeBUA%2F5faHFYUUjJc5fEC6EK%2BqFLBVRkJeuwl520Hg9FHi55JmFywkIc3JVAmkqeAbkkkrdElYvKVG1D06q1LfMLLTKiRBDqXBqLlLVBmT2vHzY&X-Amz-Signature=cc62a9f9cf9f637b4026abef48e79cc9bba48a2ff5957e220902cc08ff299f7e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







