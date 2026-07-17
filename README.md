



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633IEOWVR%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T185924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVMrlJ3uP6uo34ZafSDA%2F9DzwP62pizsrRKskd2q3xkQIhANQtqZgEMBGYeN8MbaLzaNGCjzO3Rfr8lIIcuwKJ%2FmPcKv8DCGMQABoMNjM3NDIzMTgzODA1IgzOvgH9C2GBG5jMD2Uq3AOrYu6aSL82gx9DFhxULULBn4J9EKrN62aHRTUHGnBRY48YVtxL9bKGIgozCjC43jHwxdZwhjlmV%2F1CLZJ6MTrZzZps6%2BCpfmsXtiDAu3ZA%2B8gigN2xbxwookEEWOqvYj31SksglstVQ9XWEV6kWSd50DugMbVZTA7ciL07CcWZaw5puAwrCn90tInPYx%2FtnLUr0gbVh5U5DWKHXUzID6mMWcV78r9%2Frk9MkxXyhPmHcpbNSho2mJuR9xdDPTEVK%2B8AMHY811tB71yMXiCjIN6y3cUGiFxszr9%2BStL2JF8bhZ1AEmqEI7VBJU7nb6pkyjr8RTKTAPoWBUdNbgzj0mCKUjTerXVnO0sT%2BywuxkUKvpVqQNkJSLuMOHtyV1v7B046C3Z2xcnGG1ujYc1ygaQIdsKbw0cKzcDbz2MlXUBrRWRXTFGtXDvJHwoyFm8rtq5jf8FPfDULjrfc2QMPgaObvNpCGPpgrGo%2FdYpQcaDCM8o9tLGAceevzW2ifUwWK5gfQ35qbfTYycHibWLiOgTgC%2FSd9XHOUSsM5SxQHMb5B3ePvaLQPF87awl1Cyzvo4we%2FAjnomBFhdBiuKkWCXr8cEBxzy6jrmTbsd%2FhGb3NRXNJteG7STQZ64McmTDJyunSBjqkAfeEuvdaDiXkVtrOw%2BX5Sovq11nADXaUiG1gRZlgGrXhU67lsIX%2FeVvjIEMwmvc0A4mb6f3YzCAI7rLgB%2BtVBPHX5rcyhvEvFDXCueliasftSKCgJmeav0L6wMp%2B82kKD0lMS8XI1Qh56B33CNU1QRg%2BndJIPUdbxYg8U%2BL%2FbU0vwrbSn36%2FEhvIAWeWAMa3s6Tn7W%2Fo0X25M4L0sAvkJ72p924N&X-Amz-Signature=3bd9dd8eb6d4c6f585a02a9371c7277bd5eeb0c18b08bde9ceac701ac72dd751&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633IEOWVR%2F20260717%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260717T185924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVMrlJ3uP6uo34ZafSDA%2F9DzwP62pizsrRKskd2q3xkQIhANQtqZgEMBGYeN8MbaLzaNGCjzO3Rfr8lIIcuwKJ%2FmPcKv8DCGMQABoMNjM3NDIzMTgzODA1IgzOvgH9C2GBG5jMD2Uq3AOrYu6aSL82gx9DFhxULULBn4J9EKrN62aHRTUHGnBRY48YVtxL9bKGIgozCjC43jHwxdZwhjlmV%2F1CLZJ6MTrZzZps6%2BCpfmsXtiDAu3ZA%2B8gigN2xbxwookEEWOqvYj31SksglstVQ9XWEV6kWSd50DugMbVZTA7ciL07CcWZaw5puAwrCn90tInPYx%2FtnLUr0gbVh5U5DWKHXUzID6mMWcV78r9%2Frk9MkxXyhPmHcpbNSho2mJuR9xdDPTEVK%2B8AMHY811tB71yMXiCjIN6y3cUGiFxszr9%2BStL2JF8bhZ1AEmqEI7VBJU7nb6pkyjr8RTKTAPoWBUdNbgzj0mCKUjTerXVnO0sT%2BywuxkUKvpVqQNkJSLuMOHtyV1v7B046C3Z2xcnGG1ujYc1ygaQIdsKbw0cKzcDbz2MlXUBrRWRXTFGtXDvJHwoyFm8rtq5jf8FPfDULjrfc2QMPgaObvNpCGPpgrGo%2FdYpQcaDCM8o9tLGAceevzW2ifUwWK5gfQ35qbfTYycHibWLiOgTgC%2FSd9XHOUSsM5SxQHMb5B3ePvaLQPF87awl1Cyzvo4we%2FAjnomBFhdBiuKkWCXr8cEBxzy6jrmTbsd%2FhGb3NRXNJteG7STQZ64McmTDJyunSBjqkAfeEuvdaDiXkVtrOw%2BX5Sovq11nADXaUiG1gRZlgGrXhU67lsIX%2FeVvjIEMwmvc0A4mb6f3YzCAI7rLgB%2BtVBPHX5rcyhvEvFDXCueliasftSKCgJmeav0L6wMp%2B82kKD0lMS8XI1Qh56B33CNU1QRg%2BndJIPUdbxYg8U%2BL%2FbU0vwrbSn36%2FEhvIAWeWAMa3s6Tn7W%2Fo0X25M4L0sAvkJ72p924N&X-Amz-Signature=0fe3809b268443c556e1483133a1e22ef312ec6a5f43a034dfb8dc061b2b119b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







