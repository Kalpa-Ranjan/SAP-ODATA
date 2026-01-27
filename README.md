



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJCNMJML%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T062830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5%2BK0Qi6VZ%2BPrfbvbR%2BI%2Fa%2Fg86MANPAiHEL941MWcm8QIhAOotzgzvqjrVw6WPWuEosR5x1MKhohV%2FHX%2Fb5T81OomSKv8DCE8QABoMNjM3NDIzMTgzODA1IgzloGi6aS%2BmtrpzAFgq3AOMyUSVVY3k%2Bbohdri%2FGYCBqaveqB1eHmgVr6XeXAr7ByQekOyyoBy%2F8KvmnPYPLTGy85TO9pet8L9t0OWjDo%2Bjg2oBRURTLAryJzu%2FrCngv2LA3xXo5%2F5nchsL1Dg4TLtKmH%2B4jBCWTofyFzt9RGQ2kMYNJDn%2BxJrZB%2BScoOgyLHSvAmJlrxAL7NpbBVrpbFYjyTAGJCi6wv70HZoQihhw1N5%2Fcw1MEfXW6vZoZNHgia7yrihQ2uK8m5Vq2qRkEdkQe%2BFLmIUNx3NAgqnen5gwdQ9HR9m1blvw8XYqJLNVVRIFtQap7nhlneOJFM5EAj3m1z5Tmj2k8ThJF%2Bcuqbie%2ByAgv6%2BkOAn1trNITaxwo%2BO%2B6bulZTBrZQ4a4YojIG6SNUTlRWoMMUXLECf9l0%2FaEYJFfiiikbgBaAiLqvky%2BweVbLv6RFeeiLMAhpkiOoKR9wMcxSxPpMeYSh1Wq9Q%2BMYLWBDJEmEMM4Ef50c7OoRiOgHbR8d3c3POmDRokyHJoZ3DhDBJp5aoAR9srTRb79%2FrtmmswnRc5UvK6ZAhO7rFpNHejgfwJBsvrpsypXOpwiiUe%2FZmLR1VQPhaQAHt%2FtUDHALmtFD1A3%2FeGEGM4T%2BXdlq%2FjPmG%2Bz9SBpjC6m%2BHLBjqkAXLQMaPzCJykOCZTzQWvCoH%2BMUNaXK4ytzMyujQkeM%2F%2FQZwPb8rIcEOjPexSagJi%2FtxDFb%2BCMEifJ1ee2uzNMDV2jHmJ%2BbsK6vIq8WM3t26spuAfG4YK2MvAxG5JCCoQK1FxHmBKsIZnjOVqEEDaJ0c09FGVGU%2BD%2FqbYptmeSserTDu%2B0VvJEe3uGmpv6WLyAxLs7aB9ZTC6gdppZbSy1DookYQv&X-Amz-Signature=41ee7d22bfb9e68c35410809b0db2bc7a99ca1fbb949056836b5da0d6e8a754d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJCNMJML%2F20260127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260127T062830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC5%2BK0Qi6VZ%2BPrfbvbR%2BI%2Fa%2Fg86MANPAiHEL941MWcm8QIhAOotzgzvqjrVw6WPWuEosR5x1MKhohV%2FHX%2Fb5T81OomSKv8DCE8QABoMNjM3NDIzMTgzODA1IgzloGi6aS%2BmtrpzAFgq3AOMyUSVVY3k%2Bbohdri%2FGYCBqaveqB1eHmgVr6XeXAr7ByQekOyyoBy%2F8KvmnPYPLTGy85TO9pet8L9t0OWjDo%2Bjg2oBRURTLAryJzu%2FrCngv2LA3xXo5%2F5nchsL1Dg4TLtKmH%2B4jBCWTofyFzt9RGQ2kMYNJDn%2BxJrZB%2BScoOgyLHSvAmJlrxAL7NpbBVrpbFYjyTAGJCi6wv70HZoQihhw1N5%2Fcw1MEfXW6vZoZNHgia7yrihQ2uK8m5Vq2qRkEdkQe%2BFLmIUNx3NAgqnen5gwdQ9HR9m1blvw8XYqJLNVVRIFtQap7nhlneOJFM5EAj3m1z5Tmj2k8ThJF%2Bcuqbie%2ByAgv6%2BkOAn1trNITaxwo%2BO%2B6bulZTBrZQ4a4YojIG6SNUTlRWoMMUXLECf9l0%2FaEYJFfiiikbgBaAiLqvky%2BweVbLv6RFeeiLMAhpkiOoKR9wMcxSxPpMeYSh1Wq9Q%2BMYLWBDJEmEMM4Ef50c7OoRiOgHbR8d3c3POmDRokyHJoZ3DhDBJp5aoAR9srTRb79%2FrtmmswnRc5UvK6ZAhO7rFpNHejgfwJBsvrpsypXOpwiiUe%2FZmLR1VQPhaQAHt%2FtUDHALmtFD1A3%2FeGEGM4T%2BXdlq%2FjPmG%2Bz9SBpjC6m%2BHLBjqkAXLQMaPzCJykOCZTzQWvCoH%2BMUNaXK4ytzMyujQkeM%2F%2FQZwPb8rIcEOjPexSagJi%2FtxDFb%2BCMEifJ1ee2uzNMDV2jHmJ%2BbsK6vIq8WM3t26spuAfG4YK2MvAxG5JCCoQK1FxHmBKsIZnjOVqEEDaJ0c09FGVGU%2BD%2FqbYptmeSserTDu%2B0VvJEe3uGmpv6WLyAxLs7aB9ZTC6gdppZbSy1DookYQv&X-Amz-Signature=9649a6f1b19f656bfd05005364f2316164caeb867bbe46e0331a2cf99470f54e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







