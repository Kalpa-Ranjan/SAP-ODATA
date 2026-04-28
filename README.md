



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25MRC53%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T192628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDxMwopcsKN5pFZtMFu9l%2BrhqDHwTvRgdEH6JpYQKwJ6gIhAIvL0ghGGG6C2%2BCS6hhPdbJPnV7r9xQN3MoJfzkhyzxmKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvCzFkAYqQRokdvUkq3AN%2B99BRLwwme7bY45yHT3gkv1OzPjTJUEMlkcJCsubsVfJjqBiCT07pqHX1lfPBnUnT6SnOk%2FP%2FBGrwXvTwY07RJdoLl8B%2FG0g9NK0pefd0Rgs5ce9gwP2iI2vsCoPVHJ2Lz6TRAZXshr%2BxJYZWgMaKZJFl5M6wx2WW9m4fq8E06aKz0RGMPEU%2FR8cxr%2FL2xtfgjy1Y44LD4xErfIe09jp5mjTNL5yfym96XEU7ykmaNq2TP5%2FmW4TpJm%2B9zZ1Cif3kFwc5Xud%2Bnx1mXP2vF2ES40XE82SpDl%2FYqnxtbZpJQP9smeqZutwbSmPjZRkSdorUk8F2hviWf3oesHIzOG7b8Sjs5cY2SYIjFVQFd8L128343RTieuVpXqI9Cjn%2BxfmZc7kvHaMdAmJ4rna5yrb3ZuqxIAQc1MCs2YLSvf4Mum6jyYTKnY4E82tq1xopIGHkteRqzt66E%2BAK5arj3fIWUiIbcqDJR0w9nWDaODa0Mv366fr2T22f1fg%2FJ2E83NJjLCVZ%2FkDR%2BK21f9fckns6hk03aTSih5wRkoOcaTOfGymJ3nyP1Z%2FPsyDtfsgJVhHUioA47cYv5YoApGMlIt4teHCGVuSSM8ngDmUHzxL%2BpPR7RFRFcxBYgAQNcTD%2F4cPPBjqkAShSAakYqrue7A3rqQZgvvG6tt%2BoAFDeuolphEV0GXfRBB6jgK1WhsmaH3CMQ5I5S%2FA5GItPXrWwQpACC8DfwVT88U7HE5GIw7Bnj71DYHSs4er5y%2Bg%2FaLyUEj7IyIV%2F%2BGy%2FZXNyzVFP7RdVhn%2FI0vhD%2BmsPdrp55qFr3W2wGW48eO8kR8TMNkliLsffj%2BvGsPhr%2BHKXsWBPHPUIPXM%2F6qFYoSZY&X-Amz-Signature=3faca99780b3fa1145ffeb46173f9980a525b9ef599c374bd9c8ab34f5b6e9ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T25MRC53%2F20260428%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260428T192628Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJIMEYCIQDxMwopcsKN5pFZtMFu9l%2BrhqDHwTvRgdEH6JpYQKwJ6gIhAIvL0ghGGG6C2%2BCS6hhPdbJPnV7r9xQN3MoJfzkhyzxmKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyvCzFkAYqQRokdvUkq3AN%2B99BRLwwme7bY45yHT3gkv1OzPjTJUEMlkcJCsubsVfJjqBiCT07pqHX1lfPBnUnT6SnOk%2FP%2FBGrwXvTwY07RJdoLl8B%2FG0g9NK0pefd0Rgs5ce9gwP2iI2vsCoPVHJ2Lz6TRAZXshr%2BxJYZWgMaKZJFl5M6wx2WW9m4fq8E06aKz0RGMPEU%2FR8cxr%2FL2xtfgjy1Y44LD4xErfIe09jp5mjTNL5yfym96XEU7ykmaNq2TP5%2FmW4TpJm%2B9zZ1Cif3kFwc5Xud%2Bnx1mXP2vF2ES40XE82SpDl%2FYqnxtbZpJQP9smeqZutwbSmPjZRkSdorUk8F2hviWf3oesHIzOG7b8Sjs5cY2SYIjFVQFd8L128343RTieuVpXqI9Cjn%2BxfmZc7kvHaMdAmJ4rna5yrb3ZuqxIAQc1MCs2YLSvf4Mum6jyYTKnY4E82tq1xopIGHkteRqzt66E%2BAK5arj3fIWUiIbcqDJR0w9nWDaODa0Mv366fr2T22f1fg%2FJ2E83NJjLCVZ%2FkDR%2BK21f9fckns6hk03aTSih5wRkoOcaTOfGymJ3nyP1Z%2FPsyDtfsgJVhHUioA47cYv5YoApGMlIt4teHCGVuSSM8ngDmUHzxL%2BpPR7RFRFcxBYgAQNcTD%2F4cPPBjqkAShSAakYqrue7A3rqQZgvvG6tt%2BoAFDeuolphEV0GXfRBB6jgK1WhsmaH3CMQ5I5S%2FA5GItPXrWwQpACC8DfwVT88U7HE5GIw7Bnj71DYHSs4er5y%2Bg%2FaLyUEj7IyIV%2F%2BGy%2FZXNyzVFP7RdVhn%2FI0vhD%2BmsPdrp55qFr3W2wGW48eO8kR8TMNkliLsffj%2BvGsPhr%2BHKXsWBPHPUIPXM%2F6qFYoSZY&X-Amz-Signature=9dc07560499a6e768fd3c088805aa2b4761294a5f6c4236f96ea8a304ea2b14a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







