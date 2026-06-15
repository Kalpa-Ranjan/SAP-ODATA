



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3BHRDIL%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T115338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDXzErXSbIb%2F5SR3HBi%2F9G38%2FhBuy9KlObo7bVQCFBG8AiEA7%2FegzbIXKbzfsDbQscqob8jP6naFHkLm5F86PCV%2BYeEq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDNkf%2Bie72OoLyOHeIyrcA4DPFZ3vjpOVMsvx%2F3C6niF6RcDbXpkYmETHW0lPRqL%2B%2B84a7674w%2FNbUs7VuKiwWScfpZWoygpllaoMJznY38dN4IoDecJjppI8GkqHFmNa3hMZAUb3brKf620roRPT9Yhp9P89WPnkFQ%2Br1C5HYh%2FiwOO%2Fd%2Bb%2BQHY9tWK1AfxhgU7j3LWoAdWAqI%2BKCqewubXFOvNlyJQK25wkC%2FJUhz4mxACMH2%2FWbnaOIbkV%2BQdudgrAMsd%2BPD%2B8gnszZFwFtgNyyZcXLiUmkXPxNrJeZRzK1fAxDSo5mi%2F1pY12fQh2OT0q0qtMt2osoMYoul7P2GSSZWl29JTVE8tu7EIyWleu4jDFPqnDn6rT7EsYC0eFagayyWyXhS9rp%2FKQOB0NLLFV8GOVwpWgq%2FEP4CkpOpnOZj%2BUklpMDrIqXAXcGIdRP1LZgU6eIk0z3FZHxFxx1%2Bj01aaUrGQDGgmlY7YRv3nYUusCBNs115a3LaqsQpz%2FNm7eTkcCOKuvo2mNpDLWdKbgauC1%2F%2BY%2BbMm5xpJxRQxGe0h2iyuMFgK6n4zbfiOQfOYIGD7JIkiUv8vmAK9fS%2FS8fRYnOFzfDYNXxvchxlOqPQW8pP%2FMDYkWC7ix0ZIBtI6MBOLjeNevo3d4ML28v9EGOqUBi3C5anBWjUYscORrjT0jHvcnLJUSU0twd4ofOz%2By%2Fpg3r5MzXTYq17mO36jMr7V5mgeYL3MTEhWyrOj0trox1CXQftkK0BSK0f%2FK7L24%2BJKGS4gKKxVxb7PlQJpNTTOXnPZkX7awhbClDXQZZYstwDtGinLSShF%2BuAQ%2Bb1XFIkufjfTU1KNUXkvhZc3nzudG8caF6Q83RArvNR7FGRYBUHRfRa6J&X-Amz-Signature=9c31b9c98e1de542d40f1fe173517b93316baf2de88a13c547658233a1667715&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V3BHRDIL%2F20260615%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260615T115338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDXzErXSbIb%2F5SR3HBi%2F9G38%2FhBuy9KlObo7bVQCFBG8AiEA7%2FegzbIXKbzfsDbQscqob8jP6naFHkLm5F86PCV%2BYeEq%2FwMIXBAAGgw2Mzc0MjMxODM4MDUiDNkf%2Bie72OoLyOHeIyrcA4DPFZ3vjpOVMsvx%2F3C6niF6RcDbXpkYmETHW0lPRqL%2B%2B84a7674w%2FNbUs7VuKiwWScfpZWoygpllaoMJznY38dN4IoDecJjppI8GkqHFmNa3hMZAUb3brKf620roRPT9Yhp9P89WPnkFQ%2Br1C5HYh%2FiwOO%2Fd%2Bb%2BQHY9tWK1AfxhgU7j3LWoAdWAqI%2BKCqewubXFOvNlyJQK25wkC%2FJUhz4mxACMH2%2FWbnaOIbkV%2BQdudgrAMsd%2BPD%2B8gnszZFwFtgNyyZcXLiUmkXPxNrJeZRzK1fAxDSo5mi%2F1pY12fQh2OT0q0qtMt2osoMYoul7P2GSSZWl29JTVE8tu7EIyWleu4jDFPqnDn6rT7EsYC0eFagayyWyXhS9rp%2FKQOB0NLLFV8GOVwpWgq%2FEP4CkpOpnOZj%2BUklpMDrIqXAXcGIdRP1LZgU6eIk0z3FZHxFxx1%2Bj01aaUrGQDGgmlY7YRv3nYUusCBNs115a3LaqsQpz%2FNm7eTkcCOKuvo2mNpDLWdKbgauC1%2F%2BY%2BbMm5xpJxRQxGe0h2iyuMFgK6n4zbfiOQfOYIGD7JIkiUv8vmAK9fS%2FS8fRYnOFzfDYNXxvchxlOqPQW8pP%2FMDYkWC7ix0ZIBtI6MBOLjeNevo3d4ML28v9EGOqUBi3C5anBWjUYscORrjT0jHvcnLJUSU0twd4ofOz%2By%2Fpg3r5MzXTYq17mO36jMr7V5mgeYL3MTEhWyrOj0trox1CXQftkK0BSK0f%2FK7L24%2BJKGS4gKKxVxb7PlQJpNTTOXnPZkX7awhbClDXQZZYstwDtGinLSShF%2BuAQ%2Bb1XFIkufjfTU1KNUXkvhZc3nzudG8caF6Q83RArvNR7FGRYBUHRfRa6J&X-Amz-Signature=39d5e190ad48d92a9e33236243c487169e5fe8e3e6c715be69cd923ad4d9c8ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







