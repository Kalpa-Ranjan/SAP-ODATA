



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667N5FH3KQ%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T121305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIH6lGarf1wQ327gXKJxU1yMGRSC000KhUPnNM%2BD9U4FWAiAB%2BbydP6vM%2BNh7AAbRrpDR9M5QYucDMABy1JQcHZBxSCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMohHf%2FdgMdPF%2BKuO%2FKtwD%2BuPqLYIxEz4PR13HB9vEHvRkjJic%2B1BIopIR%2Fk648Ccuz0%2B%2FLOsfdCY%2FXeB7KOVCuipE6BifCXyqO4XVh24e6hAv4a%2FmYS7km9yrn78jRsNMvcJwzvq3U81XCUS4AwfSTsdnuhhVCwbzScdCA%2FRp2BSXvdtcenUdyiRv4yrCfA81I67ULOmPavjFatjSHgv9rjw1RsbR9BLXFDhdiC9ljYmrNQQhWrQyJB08YBJfz8dgdbBGKfkceziBu%2B5WNZZDW2QaRqX9U35LJoZ5XNLPk2GLwu%2B%2Fn%2BVwrzjuWZ4EZcrW6ESVTWEMRsS7iVfMTKFStKxpvHN%2F7VAMpxeCxo9f7FAL6hSHrEcWKfd1r7O6Uxk3y8IINLzM5nVwaZeJdRXObch2D5KjKDbi1a9bXZExxF6cM2M9SxPcEhtgZl85qvzlPAKd2gFyVgM0060EpQgliShsIWljmWBrfVXaDcn5Ble2g8TaD2aM5%2F4F9tzk%2BJEq%2FtsKTZ5sN6WCpC%2BY010jxtkyD3uwjNvMRE%2F5J6SrjXXl2ITmowyJnlbnbUUZCrJQFyVsyIs5qQEQ%2FUaRfm73ipxdLZSCGH4at3vxtsUPXF9uZ19SWqlDcgg2DozmlDjnGKI0SiCDvJiqBfww%2Bd%2BN1gY6pgE0gVuMK%2FuHOu%2FmJq1rD4RA34handWWEMDcQZ%2F7lVpHLS9U0L1vfhG%2Bt76e2bty5rvpdP6it4CJsbiq5Qhb50okkYV%2F7EVGnB3Tbn%2FoNbm94WB%2BD2TRLg5KNb6Koe5Co7%2Fl3aRtjnznHrXDcVyzfx0AWQODiqeatAKIwZFlLUq50r4TzBzcRtl23ikIA1ePuBjJWZ5jP6Xio2OfpbWvN%2F%2BSGujOsLEj&X-Amz-Signature=7b63b39615dd4527bc362bdd8af684033f8c51b854aa976b740a5d8b12f13bec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667N5FH3KQ%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T121305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIH6lGarf1wQ327gXKJxU1yMGRSC000KhUPnNM%2BD9U4FWAiAB%2BbydP6vM%2BNh7AAbRrpDR9M5QYucDMABy1JQcHZBxSCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMohHf%2FdgMdPF%2BKuO%2FKtwD%2BuPqLYIxEz4PR13HB9vEHvRkjJic%2B1BIopIR%2Fk648Ccuz0%2B%2FLOsfdCY%2FXeB7KOVCuipE6BifCXyqO4XVh24e6hAv4a%2FmYS7km9yrn78jRsNMvcJwzvq3U81XCUS4AwfSTsdnuhhVCwbzScdCA%2FRp2BSXvdtcenUdyiRv4yrCfA81I67ULOmPavjFatjSHgv9rjw1RsbR9BLXFDhdiC9ljYmrNQQhWrQyJB08YBJfz8dgdbBGKfkceziBu%2B5WNZZDW2QaRqX9U35LJoZ5XNLPk2GLwu%2B%2Fn%2BVwrzjuWZ4EZcrW6ESVTWEMRsS7iVfMTKFStKxpvHN%2F7VAMpxeCxo9f7FAL6hSHrEcWKfd1r7O6Uxk3y8IINLzM5nVwaZeJdRXObch2D5KjKDbi1a9bXZExxF6cM2M9SxPcEhtgZl85qvzlPAKd2gFyVgM0060EpQgliShsIWljmWBrfVXaDcn5Ble2g8TaD2aM5%2F4F9tzk%2BJEq%2FtsKTZ5sN6WCpC%2BY010jxtkyD3uwjNvMRE%2F5J6SrjXXl2ITmowyJnlbnbUUZCrJQFyVsyIs5qQEQ%2FUaRfm73ipxdLZSCGH4at3vxtsUPXF9uZ19SWqlDcgg2DozmlDjnGKI0SiCDvJiqBfww%2Bd%2BN1gY6pgE0gVuMK%2FuHOu%2FmJq1rD4RA34handWWEMDcQZ%2F7lVpHLS9U0L1vfhG%2Bt76e2bty5rvpdP6it4CJsbiq5Qhb50okkYV%2F7EVGnB3Tbn%2FoNbm94WB%2BD2TRLg5KNb6Koe5Co7%2Fl3aRtjnznHrXDcVyzfx0AWQODiqeatAKIwZFlLUq50r4TzBzcRtl23ikIA1ePuBjJWZ5jP6Xio2OfpbWvN%2F%2BSGujOsLEj&X-Amz-Signature=91c78976997868e62f1a1ae59fd35cf23be8a0415759ceb9fd32f527b4e514ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







