



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA64EA37%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T185519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwV3oMTnaZBt%2B1UzgQatS3kZhf1w%2BGeMDsJUCDwqOfvwIhANSXNydu%2B8uBYQvap14DA3R627EswjCcdz0KcklzejKrKv8DCHwQABoMNjM3NDIzMTgzODA1IgzOObKNXXq22iSLvBoq3ANpFnDp0j01eZruL%2F2uc40n18vTpi%2FAip8JJIVDLpebc%2B67Gv42UoHSgLPcAV8aaMEFbI7bw9GGS%2FQ1JP1jYxmMZORWPqZw9CIy77SYINDeX4W8qXJSPuCLPmO%2BwA%2BUAGNIctFO5RAYSdwY5wydfi%2B0XkXOVrL05jP8hBkPfns3gke4OdnUg1rYA105fn8%2BmRGpGuP0X4AAziA0WsdQ%2FsdFqMRmjM4lmWp2yT48%2FVipOF1XZCJvGeU26FAfuqwJS9WtENv4Bgj12K9JKPdX5aBok%2FfSmeMl%2FMTCy2BofD7f%2Byi623X2tph%2BJkD0idgCMhCjoDJtTHnsIW3dNjDg%2FPZJre9pLM5xF%2B4zitf7pYieG0BFG74r4t1xFk%2FoYXUu0H%2FnPnEVBFFTSPfkLbFkTBD334myVVqvLRPzoQ6sW%2BRUjeZN6IrFcogYLQ2Z4OWjC3bcu5vWl%2FfQz7O%2BMuuSx%2FNyQ8%2Fno23B5yTb9TlIVDRkxQ2E6QC7CntHJ3dPYuI0PAiCICoFhJQwpIeFQiti%2FafA0d%2BGE%2FYxXSqU1wCBBtorxs7XP8fJGCaH0eACTY22gdAY%2B%2FtUebCEaI%2BVPttzAMD6JULzTtFrWzbhqbNPUPQAZui4zoJnOukERBj%2FWDCVke%2FSBjqkASPkTaclL161Ps0OOvHIkGJ%2BdHVTO2CKODybYq4GrtH6c%2BFgpv8Mw1jwa0Fh5uaNw%2FaQVMXAtgZvWUDXgTiuQamMMaJ5RGbCytx%2BshMcxFwbSUwiPfjr5%2FRVQvUXHMyV4xeet89nEktkIbz2rzwzisqJ9uuKKKiUPi4jLlIZMR%2BvV29EYsI1RJ7DIzvZKsna4qkRVE2IBYY%2Fo33zIC6NefKZN%2Fw0&X-Amz-Signature=c7f5b0fe6dd12e16f280d82bb28cd397337098c52c14b8bf2bd73a7aa0a392c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XA64EA37%2F20260718%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260718T185519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwV3oMTnaZBt%2B1UzgQatS3kZhf1w%2BGeMDsJUCDwqOfvwIhANSXNydu%2B8uBYQvap14DA3R627EswjCcdz0KcklzejKrKv8DCHwQABoMNjM3NDIzMTgzODA1IgzOObKNXXq22iSLvBoq3ANpFnDp0j01eZruL%2F2uc40n18vTpi%2FAip8JJIVDLpebc%2B67Gv42UoHSgLPcAV8aaMEFbI7bw9GGS%2FQ1JP1jYxmMZORWPqZw9CIy77SYINDeX4W8qXJSPuCLPmO%2BwA%2BUAGNIctFO5RAYSdwY5wydfi%2B0XkXOVrL05jP8hBkPfns3gke4OdnUg1rYA105fn8%2BmRGpGuP0X4AAziA0WsdQ%2FsdFqMRmjM4lmWp2yT48%2FVipOF1XZCJvGeU26FAfuqwJS9WtENv4Bgj12K9JKPdX5aBok%2FfSmeMl%2FMTCy2BofD7f%2Byi623X2tph%2BJkD0idgCMhCjoDJtTHnsIW3dNjDg%2FPZJre9pLM5xF%2B4zitf7pYieG0BFG74r4t1xFk%2FoYXUu0H%2FnPnEVBFFTSPfkLbFkTBD334myVVqvLRPzoQ6sW%2BRUjeZN6IrFcogYLQ2Z4OWjC3bcu5vWl%2FfQz7O%2BMuuSx%2FNyQ8%2Fno23B5yTb9TlIVDRkxQ2E6QC7CntHJ3dPYuI0PAiCICoFhJQwpIeFQiti%2FafA0d%2BGE%2FYxXSqU1wCBBtorxs7XP8fJGCaH0eACTY22gdAY%2B%2FtUebCEaI%2BVPttzAMD6JULzTtFrWzbhqbNPUPQAZui4zoJnOukERBj%2FWDCVke%2FSBjqkASPkTaclL161Ps0OOvHIkGJ%2BdHVTO2CKODybYq4GrtH6c%2BFgpv8Mw1jwa0Fh5uaNw%2FaQVMXAtgZvWUDXgTiuQamMMaJ5RGbCytx%2BshMcxFwbSUwiPfjr5%2FRVQvUXHMyV4xeet89nEktkIbz2rzwzisqJ9uuKKKiUPi4jLlIZMR%2BvV29EYsI1RJ7DIzvZKsna4qkRVE2IBYY%2Fo33zIC6NefKZN%2Fw0&X-Amz-Signature=2dcca7929a583c17bdb59134ace726ab2da7056375ab72ad9068f25e7137343a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







