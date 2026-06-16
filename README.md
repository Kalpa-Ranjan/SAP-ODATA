



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UZ242AK%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T110152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBXWUfnJZ9pPO0ItqVCUWIn3GlTvcxU2t4ZWpPi4CMCgIgDihxeYkfp0nZRRvR7gkYexkE1BikR%2F%2FTvDo59NlTPDwq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDLox1HE40J9FD5JlkircA1ZHzbzCTpdAXsgxCXoypTVXBGIbiAd1G4fk2AM%2Bwypu3rS8nAmh%2BJgiVHcyqNrGdQuK4mlRHOxuZrkbK24SPgSYi2kHg9lTgrofqFcxLTq7ptE8roFVWPBaF5Fz7SFUdQ0NnvGIk%2BiAAR9iboiuuIgnZeSJqY%2FR7gjJLZON37EshKCUCGIHGZj3qSsQqCh2WR5XdA8nw9NDq1p%2FCQu8fFfU0u00IbTdvdugQCYJ%2B1Cgu5MnHF7PGuefy0OVjbvolwqYE4XUdWR40OGS%2FCSP%2FtvQVV2u74FGiz5%2FsMbnxj28ncxuZJgHsLcVcawii2yuZxm3M6MzMCxf3d82ZG%2BJDmQDSRiPgnK1bwVWUm5clgE4VqvnkDjueRAYSAJoGO271SV9LXIaYd6fNX7K0qcugxP1AuspoP%2BOV73hqwgKJ54tqiGJ9JyQV6Yav4YL5SzaSFFqCN%2Bc4R1nQzDkr0Yth9CYzbs4ZwXrn9Q%2Fq3ITpW9qb%2FR3elMti2M8G1UNe2AqCjhXIwbIxam1ZnMIKy4%2BOyt8dS9S103b4Pr6sHa3gxFabZlaVaeVS79TyjIjQFUEH7VLWeOzzFe4hOwkw3sE2gAaGhEF0ife3ie8wgyiOHscaQvHDUPWHNePuB1kMOnbw9EGOqUBNf6fmniL7e1QpBSjeN8nRDE%2BPRizajcwcB4BX2WzhRrdM%2F0vKy1h66ixep2BlfxEccYY5gVNK92F9udp10fN9xgzeK4cNn40SRYRVBxNRORJAn%2BWIzqG2YMpHXCbClAlv6935b00fKp1cH3SZ89OcW2wc8RON4e3IFWZEyM7FmFgQXfjwLZeSUtFhIIsrdWRiMEqmCkTNrQzR5wFAFuEi5M5MD4z&X-Amz-Signature=5a8726909268daa30c9b705a07083d86b513512a54d19085260559e47d930d43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UZ242AK%2F20260616%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260616T110153Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBXWUfnJZ9pPO0ItqVCUWIn3GlTvcxU2t4ZWpPi4CMCgIgDihxeYkfp0nZRRvR7gkYexkE1BikR%2F%2FTvDo59NlTPDwq%2FwMIcBAAGgw2Mzc0MjMxODM4MDUiDLox1HE40J9FD5JlkircA1ZHzbzCTpdAXsgxCXoypTVXBGIbiAd1G4fk2AM%2Bwypu3rS8nAmh%2BJgiVHcyqNrGdQuK4mlRHOxuZrkbK24SPgSYi2kHg9lTgrofqFcxLTq7ptE8roFVWPBaF5Fz7SFUdQ0NnvGIk%2BiAAR9iboiuuIgnZeSJqY%2FR7gjJLZON37EshKCUCGIHGZj3qSsQqCh2WR5XdA8nw9NDq1p%2FCQu8fFfU0u00IbTdvdugQCYJ%2B1Cgu5MnHF7PGuefy0OVjbvolwqYE4XUdWR40OGS%2FCSP%2FtvQVV2u74FGiz5%2FsMbnxj28ncxuZJgHsLcVcawii2yuZxm3M6MzMCxf3d82ZG%2BJDmQDSRiPgnK1bwVWUm5clgE4VqvnkDjueRAYSAJoGO271SV9LXIaYd6fNX7K0qcugxP1AuspoP%2BOV73hqwgKJ54tqiGJ9JyQV6Yav4YL5SzaSFFqCN%2Bc4R1nQzDkr0Yth9CYzbs4ZwXrn9Q%2Fq3ITpW9qb%2FR3elMti2M8G1UNe2AqCjhXIwbIxam1ZnMIKy4%2BOyt8dS9S103b4Pr6sHa3gxFabZlaVaeVS79TyjIjQFUEH7VLWeOzzFe4hOwkw3sE2gAaGhEF0ife3ie8wgyiOHscaQvHDUPWHNePuB1kMOnbw9EGOqUBNf6fmniL7e1QpBSjeN8nRDE%2BPRizajcwcB4BX2WzhRrdM%2F0vKy1h66ixep2BlfxEccYY5gVNK92F9udp10fN9xgzeK4cNn40SRYRVBxNRORJAn%2BWIzqG2YMpHXCbClAlv6935b00fKp1cH3SZ89OcW2wc8RON4e3IFWZEyM7FmFgQXfjwLZeSUtFhIIsrdWRiMEqmCkTNrQzR5wFAFuEi5M5MD4z&X-Amz-Signature=0ebe64b07e9fe7a3a8668a930b017da908aafdd2ce42f9348de3ef3f51add1ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







