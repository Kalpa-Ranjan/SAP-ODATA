



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPHHMDRE%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T023410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQD6HwaWCxTVYRxFiORQA9ER%2FetSgcOqZE%2Fxinz8pLvPIAIgIuTecIXHUqq6yhJ98c2a3BtXx9plnZDviq6FdgKkpNkq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDK2jDiVol7wC5DrZ8CrcAx5mgq6kgChpfaCjHHj2%2BE2gCUS7porN0pBleKS9ws9%2FSMfm1TWsqZc81pc7NKx2HpPyKO2acpW1M88DkGtvKMnWH8RlIYHyvMU8dLAGQjSWgKdhbHxt0oj215RT9m7sqX7X5hmH%2BvVWBzf%2FQcLHc2rbbghzG0Z7WMPsZynfEDUdXAZOOPPFl0W3omLOhC9tzel75awYh3M9XGZiIbrTGwB%2BFBZgaMSF6pKdiHtFwdqRyD1ugaTJtVY%2BU8ONlwib1Feesre3PB7yHZMmpACmaG6rW%2FiuKsdm6KWPycSNOasb8KdYXVMEd7gLVmbFfzREfJvkDstxeeRmvh7J7XfvAD1ZpAB2RtRSC6SFQvos0il%2BCR6HPYrBGtagXacZq2U8UbmJbA9emRDy3CeH6upP6ow8wZzkeALSC69rpuRFZKW5eBb7vJCeW8IPLp8QdfzuUyi8jKU3kozvMpzGO%2BCB6MOCi60hTBH4%2FasecghU%2BowI3d2OMIICXoc8VWWmoYLon84qkZUw8bbRF8iiXKoy7WRpdo76HiSsu6YP%2FHfdCqBewjyj5BB3NeMcm8KRrnmy5ARiRNqtr0SYKmoN%2FbQy4DaktlrhBPtqGwZJcQetmY7sROtq6p%2BtA%2Bo%2Bp6PbMK7B7dQGOqUBG9pfIJIkehji9W%2BtvEfDImnYng%2FIOuomNhjajlg7y%2BTldpbo84iwpDF2wUSWW23lSttHDkMLInZZ4sjix2afYArAzQi9kHgCEtc%2BueP8cIopnLJnUUxy35JM8q3RwtkXy8JQ4HdmMRi11jzmTBQM%2BnHE1wIkrl2jw8t0HqGi0n4IFrJIFVWRx8PCMf4dnKNWcSsxjVU4xKJ2k5yEGaB5P1ebqVe7&X-Amz-Signature=a7566d4047b2909f5c02ce14c85f74a87f3eb0b24cc135fdaf4922e697ed3902&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZPHHMDRE%2F20260905%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260905T023410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDkaCXVzLXdlc3QtMiJHMEUCIQD6HwaWCxTVYRxFiORQA9ER%2FetSgcOqZE%2Fxinz8pLvPIAIgIuTecIXHUqq6yhJ98c2a3BtXx9plnZDviq6FdgKkpNkq%2FwMIARAAGgw2Mzc0MjMxODM4MDUiDK2jDiVol7wC5DrZ8CrcAx5mgq6kgChpfaCjHHj2%2BE2gCUS7porN0pBleKS9ws9%2FSMfm1TWsqZc81pc7NKx2HpPyKO2acpW1M88DkGtvKMnWH8RlIYHyvMU8dLAGQjSWgKdhbHxt0oj215RT9m7sqX7X5hmH%2BvVWBzf%2FQcLHc2rbbghzG0Z7WMPsZynfEDUdXAZOOPPFl0W3omLOhC9tzel75awYh3M9XGZiIbrTGwB%2BFBZgaMSF6pKdiHtFwdqRyD1ugaTJtVY%2BU8ONlwib1Feesre3PB7yHZMmpACmaG6rW%2FiuKsdm6KWPycSNOasb8KdYXVMEd7gLVmbFfzREfJvkDstxeeRmvh7J7XfvAD1ZpAB2RtRSC6SFQvos0il%2BCR6HPYrBGtagXacZq2U8UbmJbA9emRDy3CeH6upP6ow8wZzkeALSC69rpuRFZKW5eBb7vJCeW8IPLp8QdfzuUyi8jKU3kozvMpzGO%2BCB6MOCi60hTBH4%2FasecghU%2BowI3d2OMIICXoc8VWWmoYLon84qkZUw8bbRF8iiXKoy7WRpdo76HiSsu6YP%2FHfdCqBewjyj5BB3NeMcm8KRrnmy5ARiRNqtr0SYKmoN%2FbQy4DaktlrhBPtqGwZJcQetmY7sROtq6p%2BtA%2Bo%2Bp6PbMK7B7dQGOqUBG9pfIJIkehji9W%2BtvEfDImnYng%2FIOuomNhjajlg7y%2BTldpbo84iwpDF2wUSWW23lSttHDkMLInZZ4sjix2afYArAzQi9kHgCEtc%2BueP8cIopnLJnUUxy35JM8q3RwtkXy8JQ4HdmMRi11jzmTBQM%2BnHE1wIkrl2jw8t0HqGi0n4IFrJIFVWRx8PCMf4dnKNWcSsxjVU4xKJ2k5yEGaB5P1ebqVe7&X-Amz-Signature=547c9cefb4251ffa77bcbd70a103102a84b8004ebc6fd9025901c3e045dca623&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







