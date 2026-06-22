



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6TA73G2%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T034022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJHMEUCIQCzd3WbHNnPuDS%2FB16zvYVCK2GZckXA1PeJd32LZOm%2F0AIgVvNV%2BSYP8N1epOVd1KoAZy%2BJUHxAQzbh1EKooaQV4NwqiAQI%2Ff%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4y4%2FY1IcnGQklGiircAyE8x5md5TxrSsS87OpV6GVRFrHrG0H1UIJxztF6MTYrs4ZpL%2FajNqOwZY872prHDnhYVn3VmDDgKU6KEgM0V4hLFWZsLVDTJC49fzVICvImXqEgzfk5NwgTq0KtupqWDYYaeV8vmYRlWhNz7XOaJwltBvn22%2FcuN41AnEWMXLM4JFgHatl7ngIzotc9mK0awdes7l%2FeSSGZCELN2Q%2FR3ZjHedx5TpvB%2FTshJUsKHL%2FhAGZKMer2lL1GwklTWSxmm1MDKMwzfI%2Bmv%2BOleWBOX6A7Wr8kE6MiUC54md8GRa4VvofDIIMmCXQN3VqJaB30KOsq%2FzrGNP82WrOgRHTLCuiT9%2B%2B9qTv0yat27pv2qGltw1LrQebwvHKfwvP8neceb6yDVOglHw2d6Jo3cqdPsC1D0XKDj%2B7hbFms4LduF1MW%2FDUjloPzyWQhatryCkY1BqtGO5c6OBKndegKxHMaWMiGe22LGscmkoxq3qF9xZy19R4FJNPDC352UVh2AnrLx4nbUmUGACu9%2BDyutqpVvXN14GFJdVOdG8a7xFm9hCNJ2IsO5iFx1uJesl%2BEW5BRa%2F8%2F9ffm9wpHJnwOnwqupzJFRGyKh%2FPvqYbrO%2B%2BKyqpyCyJfCLaaLKa%2BVVmOMMfX4tEGOqUBh795VLgI7Sn3yvnOeN42%2FT%2F51MMQ2lJhzCPHjm2G9orlUTN9ZoKC0zg9DbA%2BOk6GJuU2BhwzvMPE3eP7%2FfXeMa5BVBwV34WYUBhKbAyl98w5rZZLFuL2cWPBNFan0eUHtgnivSJEopAlgEhxl8QKMNd3nw%2BopgOAEX1z3Lr3vwafO6Ock9dmucjnDg4YNjl8BMY%2FGuWaFYhtknod4kSsszGdQiYA&X-Amz-Signature=c96073dcde5f69598bdf7c1894b94d05e80ca5dc5e42bd1fa871818f0c9a5388&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S6TA73G2%2F20260622%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260622T034022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDQaCXVzLXdlc3QtMiJHMEUCIQCzd3WbHNnPuDS%2FB16zvYVCK2GZckXA1PeJd32LZOm%2F0AIgVvNV%2BSYP8N1epOVd1KoAZy%2BJUHxAQzbh1EKooaQV4NwqiAQI%2Ff%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL4y4%2FY1IcnGQklGiircAyE8x5md5TxrSsS87OpV6GVRFrHrG0H1UIJxztF6MTYrs4ZpL%2FajNqOwZY872prHDnhYVn3VmDDgKU6KEgM0V4hLFWZsLVDTJC49fzVICvImXqEgzfk5NwgTq0KtupqWDYYaeV8vmYRlWhNz7XOaJwltBvn22%2FcuN41AnEWMXLM4JFgHatl7ngIzotc9mK0awdes7l%2FeSSGZCELN2Q%2FR3ZjHedx5TpvB%2FTshJUsKHL%2FhAGZKMer2lL1GwklTWSxmm1MDKMwzfI%2Bmv%2BOleWBOX6A7Wr8kE6MiUC54md8GRa4VvofDIIMmCXQN3VqJaB30KOsq%2FzrGNP82WrOgRHTLCuiT9%2B%2B9qTv0yat27pv2qGltw1LrQebwvHKfwvP8neceb6yDVOglHw2d6Jo3cqdPsC1D0XKDj%2B7hbFms4LduF1MW%2FDUjloPzyWQhatryCkY1BqtGO5c6OBKndegKxHMaWMiGe22LGscmkoxq3qF9xZy19R4FJNPDC352UVh2AnrLx4nbUmUGACu9%2BDyutqpVvXN14GFJdVOdG8a7xFm9hCNJ2IsO5iFx1uJesl%2BEW5BRa%2F8%2F9ffm9wpHJnwOnwqupzJFRGyKh%2FPvqYbrO%2B%2BKyqpyCyJfCLaaLKa%2BVVmOMMfX4tEGOqUBh795VLgI7Sn3yvnOeN42%2FT%2F51MMQ2lJhzCPHjm2G9orlUTN9ZoKC0zg9DbA%2BOk6GJuU2BhwzvMPE3eP7%2FfXeMa5BVBwV34WYUBhKbAyl98w5rZZLFuL2cWPBNFan0eUHtgnivSJEopAlgEhxl8QKMNd3nw%2BopgOAEX1z3Lr3vwafO6Ock9dmucjnDg4YNjl8BMY%2FGuWaFYhtknod4kSsszGdQiYA&X-Amz-Signature=bfbd78da8db826603dbaf7c76101861f6b2994539f53a8601df9a3cc8f52674c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







