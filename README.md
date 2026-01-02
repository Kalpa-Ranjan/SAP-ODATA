



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSG47ZHN%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T123254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJGMEQCIBf%2BA2mULnjj7fq7bhL3mzDR%2F8yLsJTfdKzE1BVf3r3WAiAhvYPTcri%2BrFQxNOxS0v2OEM3Ezx0DHygKmmb8ka%2FKzCqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyIN%2FJhWNur9y8LqKtwDdlz%2B91MT1xlN7%2Baksts%2BURSq6kmjznAH0MIf1%2BAjyoVrp%2FWDtxosRFwlWPvJlmnMfNi3dNMrmiLifjkZmDRw%2BPi2%2FQuJMWf3iWwXTXh25i7UZ634xzLYZpvjvgEA%2B3%2FwW3%2FFL%2FNSSY9fOLj9qQr2puCPXyDIkCtxihv%2FFYPpvlQPI7wfgKtgiZnnTBpB9%2B1nDgPkR8iJqRKPMVrDH4gIPdzJR57JP1QffhevhlYM0xOtdWGwuVwjrsXC%2BW3yhoG1KJjyzsstgfcamhYtQc%2BFzwfzR6k8H3kvGWeElJcs%2BNROgJUdnT1LGvFrXYqB6SmzEJ6Nxp7lSIpQpLXyTHs30Gqfe9pA8gKyw84j76xd%2BBk5MJbbMqg3YtUYziA8D62nd2ho9CdynRGSbc%2FPEDLOziNAKiqBAcemHSoFJuWiOM0zlV%2BEygjatBAEiFyOO%2BClg6d8hgWV%2Bj4T68JZCjgtztfKcivCqL29xgM8Kqc1o%2BH1A%2BRKD0grw9oy3BsgwjPamR%2BMFZIVwzs8DRsdzk43uAE%2BT6FJAugh%2BfwNE1cJdmVgnjI6gwiIkrTplZGW%2FbPYG015r3kMeJAmJwuuTpa6rvD8I%2FjK5%2F%2F%2FimitXoaZFt91FBjBcPpN3EPS9QMww%2B%2FeygY6pgEN9VUSt1LXrjBPUiSZwGWwKLjmF4QP%2BpkB0bxFeblw%2B1uP9yY258kX7IQMUc8Mpg2GYG26ljBjzgD%2BZPmIO6DHjIuD1Sxt0rBC5u4i3cfOH4K1WSmjEgexxPW%2BMJ21Xjwx7%2FIj6xKTU4iGIENvri5nD8fIlAyL%2BxcJ1y%2BDycaMy0OI74xrls5y2BS7FzCpO2T1Cl0Fxfr2NrHmbzenFjo689qBtQ0D&X-Amz-Signature=362efd13c4316439637bc5c78fd6bced0cff35fe94e18c82d3cf9c7c1d8387d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSG47ZHN%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T123254Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDUaCXVzLXdlc3QtMiJGMEQCIBf%2BA2mULnjj7fq7bhL3mzDR%2F8yLsJTfdKzE1BVf3r3WAiAhvYPTcri%2BrFQxNOxS0v2OEM3Ezx0DHygKmmb8ka%2FKzCqIBAj9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsyIN%2FJhWNur9y8LqKtwDdlz%2B91MT1xlN7%2Baksts%2BURSq6kmjznAH0MIf1%2BAjyoVrp%2FWDtxosRFwlWPvJlmnMfNi3dNMrmiLifjkZmDRw%2BPi2%2FQuJMWf3iWwXTXh25i7UZ634xzLYZpvjvgEA%2B3%2FwW3%2FFL%2FNSSY9fOLj9qQr2puCPXyDIkCtxihv%2FFYPpvlQPI7wfgKtgiZnnTBpB9%2B1nDgPkR8iJqRKPMVrDH4gIPdzJR57JP1QffhevhlYM0xOtdWGwuVwjrsXC%2BW3yhoG1KJjyzsstgfcamhYtQc%2BFzwfzR6k8H3kvGWeElJcs%2BNROgJUdnT1LGvFrXYqB6SmzEJ6Nxp7lSIpQpLXyTHs30Gqfe9pA8gKyw84j76xd%2BBk5MJbbMqg3YtUYziA8D62nd2ho9CdynRGSbc%2FPEDLOziNAKiqBAcemHSoFJuWiOM0zlV%2BEygjatBAEiFyOO%2BClg6d8hgWV%2Bj4T68JZCjgtztfKcivCqL29xgM8Kqc1o%2BH1A%2BRKD0grw9oy3BsgwjPamR%2BMFZIVwzs8DRsdzk43uAE%2BT6FJAugh%2BfwNE1cJdmVgnjI6gwiIkrTplZGW%2FbPYG015r3kMeJAmJwuuTpa6rvD8I%2FjK5%2F%2F%2FimitXoaZFt91FBjBcPpN3EPS9QMww%2B%2FeygY6pgEN9VUSt1LXrjBPUiSZwGWwKLjmF4QP%2BpkB0bxFeblw%2B1uP9yY258kX7IQMUc8Mpg2GYG26ljBjzgD%2BZPmIO6DHjIuD1Sxt0rBC5u4i3cfOH4K1WSmjEgexxPW%2BMJ21Xjwx7%2FIj6xKTU4iGIENvri5nD8fIlAyL%2BxcJ1y%2BDycaMy0OI74xrls5y2BS7FzCpO2T1Cl0Fxfr2NrHmbzenFjo689qBtQ0D&X-Amz-Signature=dc7633ca663c563578e1d26e6d6116ce32c2ff0e542a3cd0ed0e50a294e6e680&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







