



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVZDPBJJ%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T143816Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDILlZEHdq%2FS9TsvCwb9NHnlMQWu3H4AHiD%2FO%2F42QRApQIgT4kM4c3p96got0xPVOTvD9K3eDWolQcgdghNDjy0jlMqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN433uSSQ%2FTMYu9pMSrcA4oC3XxPx6FSUotRLSHOKuj680neorXxvIhj6TK3FI8ppLnmrIej0pN9WyU7bLtyQ7qLpuUQD2rNsb5DSJb7MQ8lxREEcu62mftWmt1kCDNrrGDbv5u%2FyqPPlbritpk7iaQ2Ctd4gL%2By5b%2BYKKmUX6bhzAYcWhEv3dmPjNWJlUDOcLUtnRwiM0hEGkH2FqbIMkqELsyNrKJHLed61ehNYscS2wevEFPJpJis2%2FG6OHLC%2FhuAP6XZpxd1QyyhJv6JcxlWyzZk23yXHzdGQevbuZp4s5NNxGgt7aZ8pJoyP21XV0%2F2DSVqmbaGXY7gLmSgVK2olgoNUoiMVZsMpIXK%2Be9xLIdwO%2FVdma%2FChPi1io%2BWQLEgfG8UDl0j6DKTwtcDnay9vOcGhn7QEcg%2FiLQ9W1fqMBnQBQvcqssebuAl9D7CPIpiLUZnI4eOC6yf%2B9CSbvqVQMOjjHFuqYC59bdoIIHzyuNqxDwRLsebtozpCUYIP7lDOQkiHsbDwNFmD%2BIoGxW6w4x44MUR%2BbuJW%2BqW4wtU4mqZj1byuUOw74wY%2BKEwAvEmn6dllDbG3hm1cbPgq2J7j8vsE5W1Z7drWxEGIhBj5P7WAjhqEmgbWS%2FHaq1HJ5F5aap6hgUO%2BcWDMKW4oNEGOqUBept%2Bag5vrzj3HQgW1pBUBWUlVzg1lXYGZqXgscrdKMQIiHuxnIxNcMszkEFrfRUKlFBfkWvzzFjOX1nnvm6cJFQv0a1Ezssg9qMoeqeYql7FbnmfXSsEK%2FoRdvOQO5qCeETCbi%2FDp869fxben0VfvLlq0o8NgC6L4B%2FItAMN%2FACA0QzP3wcl2mWyVBA%2BGWF1C5b5rLWOHwWkXaEtUp254%2FASCCsj&X-Amz-Signature=933ef0aaa9d460a9d65092ddcf6c9b9dc9e30d05cede2deefedf78b0cf5d5806&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVZDPBJJ%2F20260609%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260609T143817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIQDILlZEHdq%2FS9TsvCwb9NHnlMQWu3H4AHiD%2FO%2F42QRApQIgT4kM4c3p96got0xPVOTvD9K3eDWolQcgdghNDjy0jlMqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN433uSSQ%2FTMYu9pMSrcA4oC3XxPx6FSUotRLSHOKuj680neorXxvIhj6TK3FI8ppLnmrIej0pN9WyU7bLtyQ7qLpuUQD2rNsb5DSJb7MQ8lxREEcu62mftWmt1kCDNrrGDbv5u%2FyqPPlbritpk7iaQ2Ctd4gL%2By5b%2BYKKmUX6bhzAYcWhEv3dmPjNWJlUDOcLUtnRwiM0hEGkH2FqbIMkqELsyNrKJHLed61ehNYscS2wevEFPJpJis2%2FG6OHLC%2FhuAP6XZpxd1QyyhJv6JcxlWyzZk23yXHzdGQevbuZp4s5NNxGgt7aZ8pJoyP21XV0%2F2DSVqmbaGXY7gLmSgVK2olgoNUoiMVZsMpIXK%2Be9xLIdwO%2FVdma%2FChPi1io%2BWQLEgfG8UDl0j6DKTwtcDnay9vOcGhn7QEcg%2FiLQ9W1fqMBnQBQvcqssebuAl9D7CPIpiLUZnI4eOC6yf%2B9CSbvqVQMOjjHFuqYC59bdoIIHzyuNqxDwRLsebtozpCUYIP7lDOQkiHsbDwNFmD%2BIoGxW6w4x44MUR%2BbuJW%2BqW4wtU4mqZj1byuUOw74wY%2BKEwAvEmn6dllDbG3hm1cbPgq2J7j8vsE5W1Z7drWxEGIhBj5P7WAjhqEmgbWS%2FHaq1HJ5F5aap6hgUO%2BcWDMKW4oNEGOqUBept%2Bag5vrzj3HQgW1pBUBWUlVzg1lXYGZqXgscrdKMQIiHuxnIxNcMszkEFrfRUKlFBfkWvzzFjOX1nnvm6cJFQv0a1Ezssg9qMoeqeYql7FbnmfXSsEK%2FoRdvOQO5qCeETCbi%2FDp869fxben0VfvLlq0o8NgC6L4B%2FItAMN%2FACA0QzP3wcl2mWyVBA%2BGWF1C5b5rLWOHwWkXaEtUp254%2FASCCsj&X-Amz-Signature=48187a7ca9c09f746a3a4267833f64ea73a6fc54f8d79875bcb50589b591363a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







