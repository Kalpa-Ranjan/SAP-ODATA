



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EINUOZ%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T125819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9k%2BKnEjZwOitHZ2gIT9Si88BBJ2p1xZBkt8x0xBpPLAiEA3dcuezxZ1DFsfmnScUL5FNto1E7YWa1fsfX5Vp9e4u8qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzcnx%2BrXDb%2BQWTX9ircA2950tjLQUUvWivf6J%2FQDPlN7H%2F0Qyjmv2HSmBvosH1QWSLka6zoPTReCjeRNuu%2FcrrR8bhEk39r3T8xKOULcqS8MiEt1rpkp59J6Tzfo4KunTW5NwEeGviXl4lgYRVSINPRNNMf4v4kw1bxYXz%2BjHEbbjxS6QHRzeQnrQqGYd3AK1lIXfcQEycdAn8Vwi6HdMCeruR6p42mENM%2BaEI263taeNdnUqdP%2FJdFWVI%2FxQBew%2B8vC9nals0C%2Feh8CeeplfJ8bSe1EfBhQAn0KPZYcpSCu1VAzNVLkLzexgSeDtP%2Fy%2BTJ0RGtuR4wmImThjofIWP87%2BfylhIphtxvHmzw2SIwQokUPGkVbnH7PwRBfpxKaHLQJgsqaFEFSCYV58ihwoRFvASX3hrzio6WytKtZrSJQNU4ARBPsThRLyyyawIdZNUcLXh0Y1lSFyvIx421j5yBXTr61BaLy7PiXkdqvjEtvBbXAV7%2BZlB1msWVQ8W3qtj89jVHdmSiVIAJ9gDP5xNZOs1aIOBFN4%2BVc7z98d%2Bty9uzLnDUCBde2OSyyQMx08VZQfVvA%2BCmaOj%2FO4RDgTyF2MiiDqkwDQA%2ByKgCPgHERvmpuadysTdxaXfCrG2oc%2BhmMjkgN2bF0kZ%2FMOGyp8wGOqUBtbu3hYAVae6EGhQPrCCA%2Fh3EtyXDrchGbGDNU%2F53DinJU93QitmRz8wagGRKUxu641MMUiZb%2BWSR9bNjtucEznMlra5APD66J5VDcvH4z338dnwXMWbZHmhHxyvb%2F1q3JMIN7MdZ2x5D%2FKsnYioNz64BAEX73k6D8vxBtsMrcoAdY5i8GUlRbjOynWJuMLCkw2S6yTFWCgZTEv6eIa%2FFBB6f6O%2BM&X-Amz-Signature=1383861dde46a0676e377a5958f4c242d287ba0329a380f38743a0655e98aefb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3EINUOZ%2F20260209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260209T125819Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG9k%2BKnEjZwOitHZ2gIT9Si88BBJ2p1xZBkt8x0xBpPLAiEA3dcuezxZ1DFsfmnScUL5FNto1E7YWa1fsfX5Vp9e4u8qiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGzcnx%2BrXDb%2BQWTX9ircA2950tjLQUUvWivf6J%2FQDPlN7H%2F0Qyjmv2HSmBvosH1QWSLka6zoPTReCjeRNuu%2FcrrR8bhEk39r3T8xKOULcqS8MiEt1rpkp59J6Tzfo4KunTW5NwEeGviXl4lgYRVSINPRNNMf4v4kw1bxYXz%2BjHEbbjxS6QHRzeQnrQqGYd3AK1lIXfcQEycdAn8Vwi6HdMCeruR6p42mENM%2BaEI263taeNdnUqdP%2FJdFWVI%2FxQBew%2B8vC9nals0C%2Feh8CeeplfJ8bSe1EfBhQAn0KPZYcpSCu1VAzNVLkLzexgSeDtP%2Fy%2BTJ0RGtuR4wmImThjofIWP87%2BfylhIphtxvHmzw2SIwQokUPGkVbnH7PwRBfpxKaHLQJgsqaFEFSCYV58ihwoRFvASX3hrzio6WytKtZrSJQNU4ARBPsThRLyyyawIdZNUcLXh0Y1lSFyvIx421j5yBXTr61BaLy7PiXkdqvjEtvBbXAV7%2BZlB1msWVQ8W3qtj89jVHdmSiVIAJ9gDP5xNZOs1aIOBFN4%2BVc7z98d%2Bty9uzLnDUCBde2OSyyQMx08VZQfVvA%2BCmaOj%2FO4RDgTyF2MiiDqkwDQA%2ByKgCPgHERvmpuadysTdxaXfCrG2oc%2BhmMjkgN2bF0kZ%2FMOGyp8wGOqUBtbu3hYAVae6EGhQPrCCA%2Fh3EtyXDrchGbGDNU%2F53DinJU93QitmRz8wagGRKUxu641MMUiZb%2BWSR9bNjtucEznMlra5APD66J5VDcvH4z338dnwXMWbZHmhHxyvb%2F1q3JMIN7MdZ2x5D%2FKsnYioNz64BAEX73k6D8vxBtsMrcoAdY5i8GUlRbjOynWJuMLCkw2S6yTFWCgZTEv6eIa%2FFBB6f6O%2BM&X-Amz-Signature=a8df0b881a42e6090b248d3bcf2cf871c5c3c681f4a4fd60eda0f4bd753f2f8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







