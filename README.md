



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FQNJVI4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T124729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCJ7GV3hTwxP%2F8aYB8n0bUTVtaM2W8xpCDhCtZaB6R3PgIhALLu70QQqxModSX2TdRBj5qFDkiYs%2BWumbMzdKc44PcaKv8DCD0QABoMNjM3NDIzMTgzODA1IgyLZkxa8VWHBqm6Kekq3AN1UQD2YBk8nw3tJ8k2MpuYBvr88nBzBLds5leBk0lFK8a2muu273g5yB7Y1dvF%2FdnRjDmweUgixIjSGxK6cI61YFwVO4MGf6geBPme5uLySv44iiJIF7Ei7NoTPLyCUKZkQpK43bL3N6%2BrKz%2FLwUE6UP%2Btw4B0%2FqMpG%2BLGWgwO%2Fuc3ciYEoPcTZdXYdQ5UzS5iItFkXlt33eu2cuZa26iY1fViVDNKrBZUJQSs1xwUmuiRKJX9gUvIUOUamb0zWu1Tx7kz%2F4%2F%2BoKTNocER1%2F%2BIDxI2mbN2I4n8pP3hkkj5fEMzN2Uv3x3GtXW2gAy0Met9jstmLm6ckbemVBhXsS8efeMbMFOkJiqUWpEAhJeCkAfoBi0%2FOKdzsXVjRnzUuNQ4SzG%2Fxps%2FhkwzeSrYOzHJ4eXEQOu5qn2YVqhRdLvnzMmWsyKRbDpB7sCCJ2BA29xg0AGmRzrvxROJ04fxZ3DXI%2FiNS9aXfGLv1tJAwEokuUHDoU0vBuycJKB%2B6CfDSuih4oSxKtCWPHyKuctEOV0%2Bz29gCahBoKHAUVFryL0dW2u9%2FYoxmlWcwjEIRR1UOP3pTZK2vOHNxhUfvwDN5N1JOukVjV%2BJPuZ%2BSlQ98C578ZwuhFhzKVDYB4ZjPjD0jobNBjqkAS2nZO7V1Eyfn7XuAypwY97GVvS7fzz6XoIifBQN9sMg75nDCjcmvqImclIRx1J1MGzb%2BBt3urRRoPtHhD8RSoZrTOi98dQ%2FdO0WSuD%2Flo%2FYz2W8WHoyy9OJTofqp7wpICASykTrPa0nGcewQgdeIi6%2BbLq44KDYk0XwswyefdOmNmyy3bvC483bTGEu6BjEGke1mHwN24eC1OcOcE54YmbOpcdH&X-Amz-Signature=d0354814a7e3f3de65a1d605819d65a56ac2d9dc73c9b18ca14b027f9ff941f1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FQNJVI4%2F20260227%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260227T124729Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCJ7GV3hTwxP%2F8aYB8n0bUTVtaM2W8xpCDhCtZaB6R3PgIhALLu70QQqxModSX2TdRBj5qFDkiYs%2BWumbMzdKc44PcaKv8DCD0QABoMNjM3NDIzMTgzODA1IgyLZkxa8VWHBqm6Kekq3AN1UQD2YBk8nw3tJ8k2MpuYBvr88nBzBLds5leBk0lFK8a2muu273g5yB7Y1dvF%2FdnRjDmweUgixIjSGxK6cI61YFwVO4MGf6geBPme5uLySv44iiJIF7Ei7NoTPLyCUKZkQpK43bL3N6%2BrKz%2FLwUE6UP%2Btw4B0%2FqMpG%2BLGWgwO%2Fuc3ciYEoPcTZdXYdQ5UzS5iItFkXlt33eu2cuZa26iY1fViVDNKrBZUJQSs1xwUmuiRKJX9gUvIUOUamb0zWu1Tx7kz%2F4%2F%2BoKTNocER1%2F%2BIDxI2mbN2I4n8pP3hkkj5fEMzN2Uv3x3GtXW2gAy0Met9jstmLm6ckbemVBhXsS8efeMbMFOkJiqUWpEAhJeCkAfoBi0%2FOKdzsXVjRnzUuNQ4SzG%2Fxps%2FhkwzeSrYOzHJ4eXEQOu5qn2YVqhRdLvnzMmWsyKRbDpB7sCCJ2BA29xg0AGmRzrvxROJ04fxZ3DXI%2FiNS9aXfGLv1tJAwEokuUHDoU0vBuycJKB%2B6CfDSuih4oSxKtCWPHyKuctEOV0%2Bz29gCahBoKHAUVFryL0dW2u9%2FYoxmlWcwjEIRR1UOP3pTZK2vOHNxhUfvwDN5N1JOukVjV%2BJPuZ%2BSlQ98C578ZwuhFhzKVDYB4ZjPjD0jobNBjqkAS2nZO7V1Eyfn7XuAypwY97GVvS7fzz6XoIifBQN9sMg75nDCjcmvqImclIRx1J1MGzb%2BBt3urRRoPtHhD8RSoZrTOi98dQ%2FdO0WSuD%2Flo%2FYz2W8WHoyy9OJTofqp7wpICASykTrPa0nGcewQgdeIi6%2BbLq44KDYk0XwswyefdOmNmyy3bvC483bTGEu6BjEGke1mHwN24eC1OcOcE54YmbOpcdH&X-Amz-Signature=6145b1228a940c73cd6a6bbe69b4ede64171c92dd25204f6d98696ed06bc9229&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







