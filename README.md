



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO3QXPXS%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T182340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJHMEUCIFi%2BnPyAdRuvRqa1LrX0lprfNI%2BDufMy5YN8G%2FPvuiEuAiEA0jp1YW%2ByVNp2MFYTFSsCH4UdnA3j5%2F9LcDOZ9vM94fEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNcbJkkWgTKoMH0yQyrcA9pHmjoQfxAtoBzetnghrQ9TRrJynEjR18scNLqr2UtaFcLX0avNQEZSBIyZXWtmgoBiTXRfy3op86NjcExJtDttstCmgY5U2DQ1gBmxvDaWcpQZcuuee%2FNALT4gNeEcN80aozkRskg13JPYNOfUz4oZES5knAZGcnYDSl%2BA1gFoSsPT9uT1lwXGYZxkOJXYFzAQu9s3%2Bdxm9OzheUf0su92QPdCS75sB7e3VjNVOMnmAC28tdFK7eiktkiTm0Uqm7M2xSzX4ShLDB%2BsLpGvc3ssK0dgLU36ozbGjCDJewc5wDYTkmLPPaaGIBHbUstkxhI%2BaXWAZA4QxqgUIr9AQb2fqsNl%2FCRtyF%2BsUatR5BNjUmM%2B%2BSH66G6mAkmfNWuf4yqp9yjRECx48CB5LkA5Z%2B7wlQs8OzVzMqloDdZMLgVx%2FsuHheS%2BgHQIH4cQ06FTV8O60b2ItioUHOGaqvB%2Fj80k79irKLQsnALav9rzUOhL2ENlEc1PbACmwwQFknKfDGRrDGwo6Hsm%2FoDAy6xVElr7lXSsH6DnuoK8hHbgOoU%2FbvV2codpZc3CBpQ5wQikfS8nW4asRDoDX3VfeZD1%2FcTX4SDV7iu8RM43%2FRnaoGnzqaeoxUjpAAYdPqyDMPPfr8oGOqUB36twFGk81dv%2FIFrazbIclb4NIcLZwMwaUILKwKXDGyRxMr49aigJOQEuNvX%2FnHfUQ1wuLKc2RsAD8BNRkuEsGfcHKHRHQNxiHYMrSavM%2BTl34yFSEWmVSVuhjOv3iu6pK3TY7FmgMo%2BqhR7xaVlR1DGiTb85Rp2%2B0nvXf140%2F2pwKsDlMGFzOwqKW5Dws4ia%2FYIpA%2FJKi1Gnu3%2FCtp7PDU3wVUPq&X-Amz-Signature=6282ac085b81b758d2b48326580dead4936a82910ef06708fbf7ba94cbbf259d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UO3QXPXS%2F20251224%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251224T182340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXVzLXdlc3QtMiJHMEUCIFi%2BnPyAdRuvRqa1LrX0lprfNI%2BDufMy5YN8G%2FPvuiEuAiEA0jp1YW%2ByVNp2MFYTFSsCH4UdnA3j5%2F9LcDOZ9vM94fEq%2FwMIJxAAGgw2Mzc0MjMxODM4MDUiDNcbJkkWgTKoMH0yQyrcA9pHmjoQfxAtoBzetnghrQ9TRrJynEjR18scNLqr2UtaFcLX0avNQEZSBIyZXWtmgoBiTXRfy3op86NjcExJtDttstCmgY5U2DQ1gBmxvDaWcpQZcuuee%2FNALT4gNeEcN80aozkRskg13JPYNOfUz4oZES5knAZGcnYDSl%2BA1gFoSsPT9uT1lwXGYZxkOJXYFzAQu9s3%2Bdxm9OzheUf0su92QPdCS75sB7e3VjNVOMnmAC28tdFK7eiktkiTm0Uqm7M2xSzX4ShLDB%2BsLpGvc3ssK0dgLU36ozbGjCDJewc5wDYTkmLPPaaGIBHbUstkxhI%2BaXWAZA4QxqgUIr9AQb2fqsNl%2FCRtyF%2BsUatR5BNjUmM%2B%2BSH66G6mAkmfNWuf4yqp9yjRECx48CB5LkA5Z%2B7wlQs8OzVzMqloDdZMLgVx%2FsuHheS%2BgHQIH4cQ06FTV8O60b2ItioUHOGaqvB%2Fj80k79irKLQsnALav9rzUOhL2ENlEc1PbACmwwQFknKfDGRrDGwo6Hsm%2FoDAy6xVElr7lXSsH6DnuoK8hHbgOoU%2FbvV2codpZc3CBpQ5wQikfS8nW4asRDoDX3VfeZD1%2FcTX4SDV7iu8RM43%2FRnaoGnzqaeoxUjpAAYdPqyDMPPfr8oGOqUB36twFGk81dv%2FIFrazbIclb4NIcLZwMwaUILKwKXDGyRxMr49aigJOQEuNvX%2FnHfUQ1wuLKc2RsAD8BNRkuEsGfcHKHRHQNxiHYMrSavM%2BTl34yFSEWmVSVuhjOv3iu6pK3TY7FmgMo%2BqhR7xaVlR1DGiTb85Rp2%2B0nvXf140%2F2pwKsDlMGFzOwqKW5Dws4ia%2FYIpA%2FJKi1Gnu3%2FCtp7PDU3wVUPq&X-Amz-Signature=e7ff2bb27585b0b0aee6e919ed2daa8d9cd858ed319fdf311ea054bd2a7d6638&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







