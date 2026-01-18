



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYCQBMO7%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T182142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9pR1IXunkHcEOTiPW86My096qsj338sD4EG6QIaaRNAiEArjyQIQckj5SXYCU%2BTs114QjJzmf2lqB43SSY4CodCqAqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD873oGv3%2BuJKdBpOCrcA49UWJARvp%2FQJR1AdoahehMSAtDCpoU0UzAmvSLFDdk%2FNsaLis5vY0PHacbu7nHewEJ91F4xhIqNXllqTdzljigGDp60wHEFG6SvrrFwwLEOyZKl7PYxpnW%2FkE6oai4UF2BvjQiAB59clB%2B8rXFcCxgF4zE%2BXTUydn%2BDQ9uytq06xutckDA4UIdO8h32P%2Fmc84TuAMC1LztPHlwVI%2Fc4TIQJAKVMRuvYJj83eOgzKL%2FuczKapGqaANqOuvAAZuKj%2BAar6dADuRxAn6N4lLE%2FOe7QG7WnYaHmrWusXBOj5l%2BaZE%2BrPP5DGHXPu%2By9ZeHRYo41GpPb3m2oxD00%2FVv6viRFP6HY%2BEX79xoTSrBHm%2FjrhoVgWok5P2J4UAy1w5V2T6F%2BZsgQtI6sv8ch9yIshA2Au1RmLFhFwswKEDzdUGwH9lQJTsLiHzGFvBR%2B3pJdGWxH5clG5Cmp%2FKUougCMuAAgOKK2%2BYA0PxDkazKJjtjHyg7s0CNIt%2Bhg4ix6Jr%2BVOWCtpBbBQahbLm5qRKO%2FUDyn18SetheoxYP7ZmGZ90fB0U5TL39bIR5c2pF%2BGBSya2SCvUWW0zpqh7Gq1opnl%2BQY9Nz5EwD3Kl%2Bmmr1Rh6Br7GDCGQQkjyvoRNKYMIvss8sGOqUBUSoAl%2BzXdIVyJJtEQFtL9N%2FVD8OXhZV6wNHlmkzHSpBN3MGIz6oOWrIwjgt0pcg9LiNBb5mJK8yHc3TA%2Bhmrf9of87wD4W4hPBJPJT5KNmqAk8BTD2QG7IAROmLwLTjzsp48icqtdyYZsAsnZNAMkEsq9%2F0UyXj6yOxRgrxKD4pBkBAvWhgFjwZhfveeSxUWBZ3VUZE92e2vkPV3dsUXhUKa%2B1Y1&X-Amz-Signature=ca367664cb45a2a2de9f671c79c31f4ee1882a9f3cef349c1d713147077afe02&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYCQBMO7%2F20260118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260118T182142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB9pR1IXunkHcEOTiPW86My096qsj338sD4EG6QIaaRNAiEArjyQIQckj5SXYCU%2BTs114QjJzmf2lqB43SSY4CodCqAqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD873oGv3%2BuJKdBpOCrcA49UWJARvp%2FQJR1AdoahehMSAtDCpoU0UzAmvSLFDdk%2FNsaLis5vY0PHacbu7nHewEJ91F4xhIqNXllqTdzljigGDp60wHEFG6SvrrFwwLEOyZKl7PYxpnW%2FkE6oai4UF2BvjQiAB59clB%2B8rXFcCxgF4zE%2BXTUydn%2BDQ9uytq06xutckDA4UIdO8h32P%2Fmc84TuAMC1LztPHlwVI%2Fc4TIQJAKVMRuvYJj83eOgzKL%2FuczKapGqaANqOuvAAZuKj%2BAar6dADuRxAn6N4lLE%2FOe7QG7WnYaHmrWusXBOj5l%2BaZE%2BrPP5DGHXPu%2By9ZeHRYo41GpPb3m2oxD00%2FVv6viRFP6HY%2BEX79xoTSrBHm%2FjrhoVgWok5P2J4UAy1w5V2T6F%2BZsgQtI6sv8ch9yIshA2Au1RmLFhFwswKEDzdUGwH9lQJTsLiHzGFvBR%2B3pJdGWxH5clG5Cmp%2FKUougCMuAAgOKK2%2BYA0PxDkazKJjtjHyg7s0CNIt%2Bhg4ix6Jr%2BVOWCtpBbBQahbLm5qRKO%2FUDyn18SetheoxYP7ZmGZ90fB0U5TL39bIR5c2pF%2BGBSya2SCvUWW0zpqh7Gq1opnl%2BQY9Nz5EwD3Kl%2Bmmr1Rh6Br7GDCGQQkjyvoRNKYMIvss8sGOqUBUSoAl%2BzXdIVyJJtEQFtL9N%2FVD8OXhZV6wNHlmkzHSpBN3MGIz6oOWrIwjgt0pcg9LiNBb5mJK8yHc3TA%2Bhmrf9of87wD4W4hPBJPJT5KNmqAk8BTD2QG7IAROmLwLTjzsp48icqtdyYZsAsnZNAMkEsq9%2F0UyXj6yOxRgrxKD4pBkBAvWhgFjwZhfveeSxUWBZ3VUZE92e2vkPV3dsUXhUKa%2B1Y1&X-Amz-Signature=e4b6d645e08ab47e9f794fe14dad2a946034189f880e3602aa84f458b5e9ae32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







