



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIHRQPLI%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T123135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWCVS8MbGgmiYERNrb5bc0nmbRA%2FGgUKSUAzaYipsXbAiAGjp3N75b8rrjJGcAOS%2F3KQAK3goDjvhacWSNPjq%2F0iyr%2FAwhlEAAaDDYzNzQyMzE4MzgwNSIMPGR3z6JGfYAJ5vP6KtwDaehjKORcKECZz6rudG%2FLtj0VzkubDrQUDZjJKvser5TFTp0fJuhkJkeQ%2FnrXzS3NqBqBRHOlMXYUVvt0uhFdDs1SMZ3i%2BPBnzOqEKcZJGWoctN%2B1gQBpOJbOg7dYJL56iQoVv9Mom8eqPe%2FczvMonwzyWzNVKFNGN%2FSpiDIJTND78sMTU1OlZ4jXO9JQ3O%2B%2BTK6BkHA3IIlJT6WRn34pLbHdKhY1Oc7xzIfTWkjIdbXQMePBDEpVJi8iK%2FghxQmKl0PZE1Giu6WcynuOT81DkvngPKMhN6D4F4bGv%2B8OSQA3AsYtysCtZryLAIfs%2FIKDVwDbszLU552ro10UzfcrYkVgFECrJ%2F3iaHTTBxeG%2BzAyTbN3GT9ttfCUylmVEX%2BUzkh%2FH9OvxGnoXgWFt8kfD682Lowf%2BNGu%2BltCG3KnYkk0ptECRMLqFmLi%2BLsXoRwdtBR%2BPILJ12ytkakC3bCBoF0qnZ02I2KjFZ%2FfSHZGUQzfjmoZAYTI%2BblxNa1ECJwYfYt6T2yRe1jTycGIaDmbOWz%2B1Z1CoYyesmKHy91J4PcrW%2FKB3vlRHZrMdFlX6ryOnpJiXjyKJuTI3vZWVCX94qdFZ2MOnqDNFFRyKzo7EZlPk5BTqIYLcwo498QwgLPcyAY6pgGL1iqA%2FUWEidmqEnTpKDdZkXRlopTH4e22Ah2Jr3TqTym3xbhEB3IL8SyZZZGJum%2FLk8wxK3B4G7ttOdNWKYLqxAz9J2OWLnKG3QklJH9w65obEmjG1nDbl2qCLinZtkF%2BJy1wzAn9itSks0%2BqJPu5GkabK8jsjr%2F40ra3KPXl2w7KOV0UpZCBICyk7hOZOGGpGGnV3j7xM7gE4SRfrY7JRlvxUEvn&X-Amz-Signature=06ce4b616d3b9cf257403ab5324a7652347fd823fae980479087c816163626f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIHRQPLI%2F20251114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251114T123135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAWCVS8MbGgmiYERNrb5bc0nmbRA%2FGgUKSUAzaYipsXbAiAGjp3N75b8rrjJGcAOS%2F3KQAK3goDjvhacWSNPjq%2F0iyr%2FAwhlEAAaDDYzNzQyMzE4MzgwNSIMPGR3z6JGfYAJ5vP6KtwDaehjKORcKECZz6rudG%2FLtj0VzkubDrQUDZjJKvser5TFTp0fJuhkJkeQ%2FnrXzS3NqBqBRHOlMXYUVvt0uhFdDs1SMZ3i%2BPBnzOqEKcZJGWoctN%2B1gQBpOJbOg7dYJL56iQoVv9Mom8eqPe%2FczvMonwzyWzNVKFNGN%2FSpiDIJTND78sMTU1OlZ4jXO9JQ3O%2B%2BTK6BkHA3IIlJT6WRn34pLbHdKhY1Oc7xzIfTWkjIdbXQMePBDEpVJi8iK%2FghxQmKl0PZE1Giu6WcynuOT81DkvngPKMhN6D4F4bGv%2B8OSQA3AsYtysCtZryLAIfs%2FIKDVwDbszLU552ro10UzfcrYkVgFECrJ%2F3iaHTTBxeG%2BzAyTbN3GT9ttfCUylmVEX%2BUzkh%2FH9OvxGnoXgWFt8kfD682Lowf%2BNGu%2BltCG3KnYkk0ptECRMLqFmLi%2BLsXoRwdtBR%2BPILJ12ytkakC3bCBoF0qnZ02I2KjFZ%2FfSHZGUQzfjmoZAYTI%2BblxNa1ECJwYfYt6T2yRe1jTycGIaDmbOWz%2B1Z1CoYyesmKHy91J4PcrW%2FKB3vlRHZrMdFlX6ryOnpJiXjyKJuTI3vZWVCX94qdFZ2MOnqDNFFRyKzo7EZlPk5BTqIYLcwo498QwgLPcyAY6pgGL1iqA%2FUWEidmqEnTpKDdZkXRlopTH4e22Ah2Jr3TqTym3xbhEB3IL8SyZZZGJum%2FLk8wxK3B4G7ttOdNWKYLqxAz9J2OWLnKG3QklJH9w65obEmjG1nDbl2qCLinZtkF%2BJy1wzAn9itSks0%2BqJPu5GkabK8jsjr%2F40ra3KPXl2w7KOV0UpZCBICyk7hOZOGGpGGnV3j7xM7gE4SRfrY7JRlvxUEvn&X-Amz-Signature=7b6274af2e84a3c31bcbf16b07f30cea13f370780cd6607f9694d2be030bfdb2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







