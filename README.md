



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU6YTMWI%2F20251031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251031T123132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIGFga1jG2gtOykQflXCCWdOvunUcOzFIxns0W5wz2Re2AiEAyPLIMli5%2Fwxc5A6DJ2dzKAG3%2BDl5bovkPmmK9de5TAYq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDGeKH6piXGUJcmnefCrcA1fzLlpFbMEqAutgMylYEkBFMhR6rJli9cd7EqnIgppWQBuf7N1m1MZQC7Ngbk9C5s3ieSr4EEjoumaWGiRdsrASGPIsO3uFNqMR5TEVCBV7PjWVifputPkeCwSS%2Bv3oEnSjHrEx7rfKc%2FsBn5ubHF2xk44AIn%2By376RKgbgjUYPSoaa6dDnCaxOHPF7xqcHaqN1iTo9N8iMwa8YV%2BGW%2BcbtgCIDNFQW2aboa4MmnOny%2FVfOP55jcL4ZElc9gJiATaVsIJQyf2DUO1q%2BLesXU000vkecOTV8IIWILekT62T75Woie2fzaFfOK1rv7kPDTE%2ByaAFJ7XPs2rxmdhH9t1P42fvwF4G336ESf7K3laltTEAGK696CduGOmKNeQihi0qt6WeLpk4REyJBWVm%2FSYmlcFrTl1E7KvoUfZscpra5PdWzKdFyrNDScoFgHaX%2FHTypm3SO9a1Lh5MsMxP82i6kuSwJ%2B9UEg49G9j9QjYvWgNyA%2FK70ch%2Bi1a%2FrzKS%2BNPjhx6T3ShtDn%2FUpyQc6fsZwXs6O3gOqNQElBXn4BJTDzGpcDWCI7tTYbs2lucIehjlDIyHfGUS8luKKL1LjK6O87EqUtfz4vvoDtHSe9SoCwKcY5uYLTFyMcq48MMvRksgGOqUB0L5CmvlfQJXb7AEzMFTRHJkZtO1GtZMHbcuZ%2BHJgMKlXoYH%2FTdUcZfRzENtpt%2Bg9ezjK5TMBvcWy193K%2BkKjKfRAqDCKFEi6wEFr%2FTe2Oo83SHaBQMVzEr8%2FbhUM5x4tAKUleB%2FWZ%2Fn6KgvVMxcmUHT3q3Lid1xGpI%2FaTcY4Fvz99sDRmsUd%2BuF6XRl7p%2FUU%2BSQRqd475xMzUr3%2Fm%2Fe6y6k7ndjX&X-Amz-Signature=18e78ff1314d9d5a1c1442aef8a7e76df9475ba936b3876a7b03e3d259de99a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YU6YTMWI%2F20251031%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251031T123132Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJHMEUCIGFga1jG2gtOykQflXCCWdOvunUcOzFIxns0W5wz2Re2AiEAyPLIMli5%2Fwxc5A6DJ2dzKAG3%2BDl5bovkPmmK9de5TAYq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDGeKH6piXGUJcmnefCrcA1fzLlpFbMEqAutgMylYEkBFMhR6rJli9cd7EqnIgppWQBuf7N1m1MZQC7Ngbk9C5s3ieSr4EEjoumaWGiRdsrASGPIsO3uFNqMR5TEVCBV7PjWVifputPkeCwSS%2Bv3oEnSjHrEx7rfKc%2FsBn5ubHF2xk44AIn%2By376RKgbgjUYPSoaa6dDnCaxOHPF7xqcHaqN1iTo9N8iMwa8YV%2BGW%2BcbtgCIDNFQW2aboa4MmnOny%2FVfOP55jcL4ZElc9gJiATaVsIJQyf2DUO1q%2BLesXU000vkecOTV8IIWILekT62T75Woie2fzaFfOK1rv7kPDTE%2ByaAFJ7XPs2rxmdhH9t1P42fvwF4G336ESf7K3laltTEAGK696CduGOmKNeQihi0qt6WeLpk4REyJBWVm%2FSYmlcFrTl1E7KvoUfZscpra5PdWzKdFyrNDScoFgHaX%2FHTypm3SO9a1Lh5MsMxP82i6kuSwJ%2B9UEg49G9j9QjYvWgNyA%2FK70ch%2Bi1a%2FrzKS%2BNPjhx6T3ShtDn%2FUpyQc6fsZwXs6O3gOqNQElBXn4BJTDzGpcDWCI7tTYbs2lucIehjlDIyHfGUS8luKKL1LjK6O87EqUtfz4vvoDtHSe9SoCwKcY5uYLTFyMcq48MMvRksgGOqUB0L5CmvlfQJXb7AEzMFTRHJkZtO1GtZMHbcuZ%2BHJgMKlXoYH%2FTdUcZfRzENtpt%2Bg9ezjK5TMBvcWy193K%2BkKjKfRAqDCKFEi6wEFr%2FTe2Oo83SHaBQMVzEr8%2FbhUM5x4tAKUleB%2FWZ%2Fn6KgvVMxcmUHT3q3Lid1xGpI%2FaTcY4Fvz99sDRmsUd%2BuF6XRl7p%2FUU%2BSQRqd475xMzUr3%2Fm%2Fe6y6k7ndjX&X-Amz-Signature=ed900b41bdf109f6061b327da2b539d9b9c0c160997264dab1914afbefa5c8b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







