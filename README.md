



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDCAW5YR%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T012524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIFbl06gSwNG2%2FLwXc3W6fuFqpWthz9YvWanJnkdPzkzRAiEA8QxZ2U1vXqVP6BD3lTz4p4J9H%2BS9CrpsA6dMSMgnSPcqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVNA2ftZM8WmFFPhircAwR0z9BfZJJVsC5sU1kS3Vz1fZDXeZGiv6SVqvNxkSdJuWM5cJk37hUBlhyEJAHSFrfMoFAg7W8YLzgSPlg1axc3vOecXxdzdaMltHdzNeZqirW9RUt1pBjeXyi5LzP0zc63jG93tx2oYMVxPeFE0U9rZpn7DN2EerqXemjiHgSstq%2BTstQNTuJz1y99jShrQ%2Fr%2FRHqskAnAX6rNgCsHdXjyydCPUKTFw8icWoi8SKmVgTBCuUn5BCUr5RBE3aW%2BAilJNvpHOU1ns%2F49PvUMQkMdEOLKKz6n%2BUdhEwDGl0bF3m5yK6x2TRuwVlfEi5%2BnHfHRYYHWfqN4xE3KicdJtFzI8fDAGc2K%2BODNrzBDF1JKjt0keId7P87aInTtlVqTmqu7OqgaBrf%2B7EnsH7gKjvsQT%2BjTYnLPMGmkNRczDbR3jG%2F8XZMUWQs3924JNwix02IfgweMBIl6VpSEC2Q6cLwfia5meMPOwQJsaggF35Y99IRkb6K%2Bbq8jKqUy8dl2VN4KZZTyT6O4TyuWCE5mqc%2Bl6QM5PRuZPKZogrBksokyy7KACgDEaS1rISmmQLCeJL%2BKz4i%2FptA3868H%2B0KiHEVz0%2F3yknD74V%2FQpVbSNGOofAQOz5OfFAk27E8eMLfO89MGOqUBhkYQsmTvTSxd01eJ99hCpPxeSwT1nXd4Q25RbbFnN2teXDVU0qNBEs0cveWmp5tLjStQ9lc9LK6hV4%2FmmTyBYoM42G5aQ8aBKNsBa%2BMF%2BxdrMO7Dn5jV7sMb0CaBrgu7O4DRlYYkv5ZNtSnepG%2B7uxpr%2BmmIYm8Njl2OcQocTqKSOOMhexP8S3CLaVhnFL63WT%2BMOVv3cnVadpa40gEIze43%2BDAC&X-Amz-Signature=881604c575026412978604581aaca01b4cca4d08499fea1612683dc32b717dae&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SDCAW5YR%2F20260813%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260813T012524Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA4aCXVzLXdlc3QtMiJHMEUCIFbl06gSwNG2%2FLwXc3W6fuFqpWthz9YvWanJnkdPzkzRAiEA8QxZ2U1vXqVP6BD3lTz4p4J9H%2BS9CrpsA6dMSMgnSPcqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVNA2ftZM8WmFFPhircAwR0z9BfZJJVsC5sU1kS3Vz1fZDXeZGiv6SVqvNxkSdJuWM5cJk37hUBlhyEJAHSFrfMoFAg7W8YLzgSPlg1axc3vOecXxdzdaMltHdzNeZqirW9RUt1pBjeXyi5LzP0zc63jG93tx2oYMVxPeFE0U9rZpn7DN2EerqXemjiHgSstq%2BTstQNTuJz1y99jShrQ%2Fr%2FRHqskAnAX6rNgCsHdXjyydCPUKTFw8icWoi8SKmVgTBCuUn5BCUr5RBE3aW%2BAilJNvpHOU1ns%2F49PvUMQkMdEOLKKz6n%2BUdhEwDGl0bF3m5yK6x2TRuwVlfEi5%2BnHfHRYYHWfqN4xE3KicdJtFzI8fDAGc2K%2BODNrzBDF1JKjt0keId7P87aInTtlVqTmqu7OqgaBrf%2B7EnsH7gKjvsQT%2BjTYnLPMGmkNRczDbR3jG%2F8XZMUWQs3924JNwix02IfgweMBIl6VpSEC2Q6cLwfia5meMPOwQJsaggF35Y99IRkb6K%2Bbq8jKqUy8dl2VN4KZZTyT6O4TyuWCE5mqc%2Bl6QM5PRuZPKZogrBksokyy7KACgDEaS1rISmmQLCeJL%2BKz4i%2FptA3868H%2B0KiHEVz0%2F3yknD74V%2FQpVbSNGOofAQOz5OfFAk27E8eMLfO89MGOqUBhkYQsmTvTSxd01eJ99hCpPxeSwT1nXd4Q25RbbFnN2teXDVU0qNBEs0cveWmp5tLjStQ9lc9LK6hV4%2FmmTyBYoM42G5aQ8aBKNsBa%2BMF%2BxdrMO7Dn5jV7sMb0CaBrgu7O4DRlYYkv5ZNtSnepG%2B7uxpr%2BmmIYm8Njl2OcQocTqKSOOMhexP8S3CLaVhnFL63WT%2BMOVv3cnVadpa40gEIze43%2BDAC&X-Amz-Signature=8baab42afb6caef545189e5f52f01766a134de566a43109655dcbd8217969754&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







