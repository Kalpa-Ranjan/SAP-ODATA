



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI4U7S4X%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T182414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIAXkTP%2B7jQoer1EqoNI1f3Ru1ES3iVd3zXiHOa8%2BK978AiAwATZfi2kG0qHMFf%2BvosEAToAFiUgHpjwiGPLLaYy2tir%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMSWmzjgdrc7pJ3IdiKtwDls4%2FBvc0SAFTfm4hN5XDQu%2Bx4P6gPXeFd3Ey%2Bh3J9IVMS5PPCYXsaCvWlPN2QJZjGLgHnGEU02TnCJA6P7iOR62YK322C5aYdQZdtQabtryZpifV%2BodgNZpoOH3cWMDgPCfpqyseTfDi%2F0W8WWbKhtN99i80OCRcSkn9WblAIrxWardmboopSZ59EdC%2F8XYPi5PoGzp3BDDHTTCTSccgA%2F%2FpJ4Xwr79l540liKI1JBsD0%2Fe3sUcvCbkrQ0w0HkINLngTvm0dcuLP2bHWlTkjNXqDGFBbM8V7Ff4kPhPRoJ3Z9F%2BRITFF047Y1ZWQMkSeEGGTvpsGJvzvSLVK%2FOm3Hn8eDIeAEkcUHr6hvG5VuCIU%2FJWq3J7Uu6DU7ZokWLoFCXDT5ofDfWfAew1sOfhMzdDIkRKQcfpf0J57Le2hr%2FlzKxnyiV4MZ%2FKy%2BXyThRolU36ctT2P%2Fqq3Ftz6CID0AHxRGllZkFVTOm%2FXaqElOrJG2oC7jrQDOOW3GhfO9DgkPcOFcxoc%2BHyZewhCfw7uoLX0ytYAKL9Vyj6LVyaCjLczax5L2eVFGx5ZvxKiBGNzopGEBmLgwFr7j62TbF9k8hMqjavBPlGWa33NYYfC91BsMSm%2BVQHtq2gkhkEwsrmrygY6pgFHOr1LHZ%2BhoPMTkQ5X8JeMaLQVvr8KVtil%2Bh7dX6y0oqxTlW5yaf9MepbMbamgm2PJm0oGXOWuaKoaIDc72BNsiHdjwDfO0Qp5cyIIr%2B8IVZKKlqCL1TN82YhKIdk0KnwCF82vSDOj%2BlxLgbJ4YV9i9zzlO35OwL9nLYBZzufo51Ske63Jqpr1CInlFe%2BjzChTppDdxidVW0kdhdsvTKGkv%2BgiaVz%2B&X-Amz-Signature=1ae7b54f6a3c2dcf7e8e5723f7abd011d1b06ac8456d580ff4076a4a58ba25fb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI4U7S4X%2F20251223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251223T182414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEoaCXVzLXdlc3QtMiJGMEQCIAXkTP%2B7jQoer1EqoNI1f3Ru1ES3iVd3zXiHOa8%2BK978AiAwATZfi2kG0qHMFf%2BvosEAToAFiUgHpjwiGPLLaYy2tir%2FAwgTEAAaDDYzNzQyMzE4MzgwNSIMSWmzjgdrc7pJ3IdiKtwDls4%2FBvc0SAFTfm4hN5XDQu%2Bx4P6gPXeFd3Ey%2Bh3J9IVMS5PPCYXsaCvWlPN2QJZjGLgHnGEU02TnCJA6P7iOR62YK322C5aYdQZdtQabtryZpifV%2BodgNZpoOH3cWMDgPCfpqyseTfDi%2F0W8WWbKhtN99i80OCRcSkn9WblAIrxWardmboopSZ59EdC%2F8XYPi5PoGzp3BDDHTTCTSccgA%2F%2FpJ4Xwr79l540liKI1JBsD0%2Fe3sUcvCbkrQ0w0HkINLngTvm0dcuLP2bHWlTkjNXqDGFBbM8V7Ff4kPhPRoJ3Z9F%2BRITFF047Y1ZWQMkSeEGGTvpsGJvzvSLVK%2FOm3Hn8eDIeAEkcUHr6hvG5VuCIU%2FJWq3J7Uu6DU7ZokWLoFCXDT5ofDfWfAew1sOfhMzdDIkRKQcfpf0J57Le2hr%2FlzKxnyiV4MZ%2FKy%2BXyThRolU36ctT2P%2Fqq3Ftz6CID0AHxRGllZkFVTOm%2FXaqElOrJG2oC7jrQDOOW3GhfO9DgkPcOFcxoc%2BHyZewhCfw7uoLX0ytYAKL9Vyj6LVyaCjLczax5L2eVFGx5ZvxKiBGNzopGEBmLgwFr7j62TbF9k8hMqjavBPlGWa33NYYfC91BsMSm%2BVQHtq2gkhkEwsrmrygY6pgFHOr1LHZ%2BhoPMTkQ5X8JeMaLQVvr8KVtil%2Bh7dX6y0oqxTlW5yaf9MepbMbamgm2PJm0oGXOWuaKoaIDc72BNsiHdjwDfO0Qp5cyIIr%2B8IVZKKlqCL1TN82YhKIdk0KnwCF82vSDOj%2BlxLgbJ4YV9i9zzlO35OwL9nLYBZzufo51Ske63Jqpr1CInlFe%2BjzChTppDdxidVW0kdhdsvTKGkv%2BgiaVz%2B&X-Amz-Signature=0fe891399989d3ea8c0666568f79bc6d81aa0e1a80e4fbd60bf61f34300d2f0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







