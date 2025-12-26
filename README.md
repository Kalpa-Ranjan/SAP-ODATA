



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVHYPT2G%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T123247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgrzlesCwLfhZysSIHAwp1BIS1NznKR5WlUoy%2FTfMRCAiEApT5a3zRfuZscJjWdeGqP8OcurB1MfELdHY6fqrEhsRUq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDITSKW9rksOewng8WSrcAw5Lu50gn8%2BiJWMBEdY3Oy42QEtoB8B2ljUrx7AZaIjxUtyj7IB5jOnDhQSe3PQL0y3Pp5zYFKcZMAuk0vcGi6TXoenNaKYjPxCIvzmqf6zDDjEKMWKZegzMYXWFuL8eoP%2BlLGggNWoiE03LwrAQrg5cbhJwpGP3D5AbF%2BJw9%2Bfo3OTZRxvWdOAgHgGbyun14FGs28SKt7Sj%2BHXhqZ%2BT1F%2Fs%2BirmQ2i5b9T3fbDm8wFwG4X9w%2FR7Xwaxv0lsUtibN%2BFkWJi7zUMeUNqghMCT30HyZwctfyzbpS8CKifpmZk1NMK7U%2BWiEOEeY6wf3nsxRR2tWC1r47J2ilF2Or4IbkwtyWEi97YyXThrk36p5yOlufgm0pCLpKjyVZjr8nYxz1wOoJs%2Fl4I5qxqGBQ8EnnmniaZMXgyEvdF52vfFx3xGBSMB449XOX4lLbctbE5xxrqbJKWiMoBX2CYLCt2BXGG2o%2FZ2tYYzt6KEzciDbXnRBx9nWUqXQkvjK25VHB113HSrJxr%2FlU%2FBy0leiVB2SZ0S1O5t1hlgDah3U%2FQRyCGnoggR%2BsK2zCq8DW84P5gIpWbLCKThstjTU5tE9ma0FvNt3KPCCsodH66%2FjZ7ez9IJlgiJv6A9miHrMzQUMOvnuMoGOqUB0szi%2FMAIJ72p8CwvfNpZaX0rIYRPCbtykAbqJMO8btDMho1hxUgHPt%2B7F5Y0i4GBVF%2B6p6EgksZpRLlYroRFvN2VvZnNyhZxAUXfljFJsFHSLzUK74fKUShoVNwSjNShmEfCqlOI3wpw%2BfvTRBWsHPboVfMPg3HrET6LHAPdnAovauxmEOv7OHqZnSZJ7uZmN2LiXM%2B0ejswVSrjxRT5xEfzuaZW&X-Amz-Signature=29eb4f15dbfb9867700ec2069c454ed91d077d2d6f687d0b9819075a92a46201&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TVHYPT2G%2F20251226%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251226T123248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGgrzlesCwLfhZysSIHAwp1BIS1NznKR5WlUoy%2FTfMRCAiEApT5a3zRfuZscJjWdeGqP8OcurB1MfELdHY6fqrEhsRUq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDITSKW9rksOewng8WSrcAw5Lu50gn8%2BiJWMBEdY3Oy42QEtoB8B2ljUrx7AZaIjxUtyj7IB5jOnDhQSe3PQL0y3Pp5zYFKcZMAuk0vcGi6TXoenNaKYjPxCIvzmqf6zDDjEKMWKZegzMYXWFuL8eoP%2BlLGggNWoiE03LwrAQrg5cbhJwpGP3D5AbF%2BJw9%2Bfo3OTZRxvWdOAgHgGbyun14FGs28SKt7Sj%2BHXhqZ%2BT1F%2Fs%2BirmQ2i5b9T3fbDm8wFwG4X9w%2FR7Xwaxv0lsUtibN%2BFkWJi7zUMeUNqghMCT30HyZwctfyzbpS8CKifpmZk1NMK7U%2BWiEOEeY6wf3nsxRR2tWC1r47J2ilF2Or4IbkwtyWEi97YyXThrk36p5yOlufgm0pCLpKjyVZjr8nYxz1wOoJs%2Fl4I5qxqGBQ8EnnmniaZMXgyEvdF52vfFx3xGBSMB449XOX4lLbctbE5xxrqbJKWiMoBX2CYLCt2BXGG2o%2FZ2tYYzt6KEzciDbXnRBx9nWUqXQkvjK25VHB113HSrJxr%2FlU%2FBy0leiVB2SZ0S1O5t1hlgDah3U%2FQRyCGnoggR%2BsK2zCq8DW84P5gIpWbLCKThstjTU5tE9ma0FvNt3KPCCsodH66%2FjZ7ez9IJlgiJv6A9miHrMzQUMOvnuMoGOqUB0szi%2FMAIJ72p8CwvfNpZaX0rIYRPCbtykAbqJMO8btDMho1hxUgHPt%2B7F5Y0i4GBVF%2B6p6EgksZpRLlYroRFvN2VvZnNyhZxAUXfljFJsFHSLzUK74fKUShoVNwSjNShmEfCqlOI3wpw%2BfvTRBWsHPboVfMPg3HrET6LHAPdnAovauxmEOv7OHqZnSZJ7uZmN2LiXM%2B0ejswVSrjxRT5xEfzuaZW&X-Amz-Signature=c487a66b4bf748c8e14a5d76cd21bc88aa18d386d0415148efdfba0bc05a1853&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







