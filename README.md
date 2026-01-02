



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URMOVREW%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T062708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIAnfsF6bExWCz2Bu3StbUnE6a12Ifc%2BSBNPCcJmt7Qf1AiBwge9JuRZM18uFANxmdWAFkxqjEMizzuIDq4TPTrAkTSqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv5T4O9uFyQrha%2F74KtwDhBSQfe09aQ3Tj%2FqXoVGewypapV7AW0LGTuBmsX6m0ytIMrYVEDBU0D%2BYxN2L0RCs4RqUDM9q3PnDejYrDJLOUSkDOcOnlhMmB8m5kz8z4%2F8DdHBbiWtXWC%2FzxMpdxbIbOo7jykFmiAYtgyT6cWuDwvAbtHrLQvh4r9RQIqc%2BFw4s52dw0SWN67yn1OXxzJq2gTBcPor%2FfrbnzYKI%2Fj0nTScF%2BIWp%2FJ3Um7HXrawC47a%2FoquyPnWQXZSzeKr3FBfMIlJzxA5A2b3FOLusiXVnkcZh6H7YE3qkOqtwcKHWPHrdO1P4F%2BFFBKSJT%2BtyMDC5hr0yWGWADVAqAQIr3vKpGWyHtKqYJsyeazARpkN9tWrVNRX2ualrBuIMF9kDYBn%2BXm739qY9H5pdxBhtZhwrEXi%2BChVD9lIZWnYc68aOCtDzy3fh%2FtgCgD%2Ba8CV4nJ%2Fn2ISbr%2FNSWYhGldLfPlQQpE42dCY1PvkhNJXDv18GTxG5ZKGI%2BGnd1Mta79ffdBO9C1PeiKvevIjd5U96cco3PkyRhux%2FxwnEjxBKCxQ%2FG8Nz1L7lkec94T74we1B6KuneKmfG7%2BvDlhEiBwNFb2A9FeXv5TGdpCkZpVP7rIYw4QtlWunfxamgpjpPb4wwu3cygY6pgGUvyBFK%2F0yZBetIl5xe8OINUtUj9dC4YTJM9tHFXhJntNhv4vUvBoiXlOi6bG6YffHM6s3q0UPm7VEw2Y7T1SYiGypAuatFkYPEMFnGn7V5GeGGZAcsSpQ5soNvZ3zO0jcZJCPBnMfHT1beVptFGB5WYs10M7PdPMtM7TLdQt2kg2TnCvWOXfod3OmquJRw4QGZ5E1z1rKEz146buekvHxgey5qvpH&X-Amz-Signature=981b3c8d8d94242ff7931541ba753787c1a81d48df1b3791f5fa4c94b9b1423c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URMOVREW%2F20260102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260102T062708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIAnfsF6bExWCz2Bu3StbUnE6a12Ifc%2BSBNPCcJmt7Qf1AiBwge9JuRZM18uFANxmdWAFkxqjEMizzuIDq4TPTrAkTSqIBAj0%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMv5T4O9uFyQrha%2F74KtwDhBSQfe09aQ3Tj%2FqXoVGewypapV7AW0LGTuBmsX6m0ytIMrYVEDBU0D%2BYxN2L0RCs4RqUDM9q3PnDejYrDJLOUSkDOcOnlhMmB8m5kz8z4%2F8DdHBbiWtXWC%2FzxMpdxbIbOo7jykFmiAYtgyT6cWuDwvAbtHrLQvh4r9RQIqc%2BFw4s52dw0SWN67yn1OXxzJq2gTBcPor%2FfrbnzYKI%2Fj0nTScF%2BIWp%2FJ3Um7HXrawC47a%2FoquyPnWQXZSzeKr3FBfMIlJzxA5A2b3FOLusiXVnkcZh6H7YE3qkOqtwcKHWPHrdO1P4F%2BFFBKSJT%2BtyMDC5hr0yWGWADVAqAQIr3vKpGWyHtKqYJsyeazARpkN9tWrVNRX2ualrBuIMF9kDYBn%2BXm739qY9H5pdxBhtZhwrEXi%2BChVD9lIZWnYc68aOCtDzy3fh%2FtgCgD%2Ba8CV4nJ%2Fn2ISbr%2FNSWYhGldLfPlQQpE42dCY1PvkhNJXDv18GTxG5ZKGI%2BGnd1Mta79ffdBO9C1PeiKvevIjd5U96cco3PkyRhux%2FxwnEjxBKCxQ%2FG8Nz1L7lkec94T74we1B6KuneKmfG7%2BvDlhEiBwNFb2A9FeXv5TGdpCkZpVP7rIYw4QtlWunfxamgpjpPb4wwu3cygY6pgGUvyBFK%2F0yZBetIl5xe8OINUtUj9dC4YTJM9tHFXhJntNhv4vUvBoiXlOi6bG6YffHM6s3q0UPm7VEw2Y7T1SYiGypAuatFkYPEMFnGn7V5GeGGZAcsSpQ5soNvZ3zO0jcZJCPBnMfHT1beVptFGB5WYs10M7PdPMtM7TLdQt2kg2TnCvWOXfod3OmquJRw4QGZ5E1z1rKEz146buekvHxgey5qvpH&X-Amz-Signature=fdc389efab4e79f214cc682fe61621176ba3a608b0d766fd80c9119791f0476b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







