



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLXQ24YH%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T060804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCICz1pVK0if5sjNUy13iUuBU%2BzVbW5KXC2bleM5%2FESebOAiBB7kJTSmCepaINrEy2C9LqeMgBOjHR%2FqaWKS2D2TGdaCqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWVa7Orn87bEytx%2BgKtwDbhB0zx4T6Lx8vcvxhWNkU7xtmFegjCcqgeQl1%2Bv3kOwpDYb43aQh5MOZnYD%2F6DNgiyded%2FMRNiHwSy37K5Xo%2F2iQa1QgzXUjDmKyY3DfaT%2FF1avkjtLLtEshqh1N90NHSBAKH1eFVFwJPCMs3xXFCv14wJTIUdQs0WESr7y0zpP5CTLlgUqV1UGKb0%2BdpyAngkUyH0v1WjW9YCD71%2FBRxyyaZzRWwgQSRkpPtdILmc%2Fz0KyP21y1nxy0ZmGDGdOIEswnj6xXlAtEusNGotjNlx83hzKb9M6mt2RO6jjza3L5lpZxO46RtAeLXBJcVIXEeih40S1KLNjiZHq5vxmlRRBKdZVBflLBJD%2FREfyli9bwCFzY0KPpFi8aKUDqrFgpcgg4QrA3JJT4Udfyg5HyAauckA19v18HpWwrSYb%2BoKSRbppaH9AUs4uonsdDbRXMCD%2FmR9i7FG3KX8%2FvVzEDlC8a%2BdFDsKY3HX1Jix8AWbfU%2FyRXY6HGvDtzCB4CG4fHBJY0nM9iPYkdVmI9hYq%2FgBj%2FZgsbZWsn52Tv1M5AzMJRdVbdzFsmtrNgQhpuBHKzjh86rGjOvhFblekR6STTnYxDhEBHekrkmiNH09sgvm%2F79gtrg%2FSuJeBL8nkwvPv01wY6pgGWbTESSAKbd1GwBUxqLoGGfx5h2KNsdfH5xmBxQgIRPa0rCpZlh7uN0uhrW1q573wZhVkwXMMKeyfk9MVxPJ5nqt1N5%2BBmFOpFhKs009IbR57qLHL9xqeZ%2Fk6ZkrB0NfBpRFUve4nOZRrPjB4ZD351I02BFR9pOLXNrNGQj656OYBj%2BvbeOzQDXcHXJbXsb7E4HSKSvT0NpCp4HU%2BhkVEKK6gWuoWc&X-Amz-Signature=1417c418d852fb27a3b39c88b40f98a9eca503bad531e4db07bd9d4728388ec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLXQ24YH%2F20261118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261118T060804Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCICz1pVK0if5sjNUy13iUuBU%2BzVbW5KXC2bleM5%2FESebOAiBB7kJTSmCepaINrEy2C9LqeMgBOjHR%2FqaWKS2D2TGdaCqIBAj2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWVa7Orn87bEytx%2BgKtwDbhB0zx4T6Lx8vcvxhWNkU7xtmFegjCcqgeQl1%2Bv3kOwpDYb43aQh5MOZnYD%2F6DNgiyded%2FMRNiHwSy37K5Xo%2F2iQa1QgzXUjDmKyY3DfaT%2FF1avkjtLLtEshqh1N90NHSBAKH1eFVFwJPCMs3xXFCv14wJTIUdQs0WESr7y0zpP5CTLlgUqV1UGKb0%2BdpyAngkUyH0v1WjW9YCD71%2FBRxyyaZzRWwgQSRkpPtdILmc%2Fz0KyP21y1nxy0ZmGDGdOIEswnj6xXlAtEusNGotjNlx83hzKb9M6mt2RO6jjza3L5lpZxO46RtAeLXBJcVIXEeih40S1KLNjiZHq5vxmlRRBKdZVBflLBJD%2FREfyli9bwCFzY0KPpFi8aKUDqrFgpcgg4QrA3JJT4Udfyg5HyAauckA19v18HpWwrSYb%2BoKSRbppaH9AUs4uonsdDbRXMCD%2FmR9i7FG3KX8%2FvVzEDlC8a%2BdFDsKY3HX1Jix8AWbfU%2FyRXY6HGvDtzCB4CG4fHBJY0nM9iPYkdVmI9hYq%2FgBj%2FZgsbZWsn52Tv1M5AzMJRdVbdzFsmtrNgQhpuBHKzjh86rGjOvhFblekR6STTnYxDhEBHekrkmiNH09sgvm%2F79gtrg%2FSuJeBL8nkwvPv01wY6pgGWbTESSAKbd1GwBUxqLoGGfx5h2KNsdfH5xmBxQgIRPa0rCpZlh7uN0uhrW1q573wZhVkwXMMKeyfk9MVxPJ5nqt1N5%2BBmFOpFhKs009IbR57qLHL9xqeZ%2Fk6ZkrB0NfBpRFUve4nOZRrPjB4ZD351I02BFR9pOLXNrNGQj656OYBj%2BvbeOzQDXcHXJbXsb7E4HSKSvT0NpCp4HU%2BhkVEKK6gWuoWc&X-Amz-Signature=f88a1deb40d0ef73addefee84a90d87215fcd61c1d61317a351a79f7412785b6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







