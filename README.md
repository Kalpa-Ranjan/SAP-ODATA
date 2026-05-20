



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PRP3KWT%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T145034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQCe%2BYNlSUdsU6OqhZ5hSDeOVr5T%2BAJQ04fFTWLGcFv50AIhANIBh%2BiXm53IoMADnmCpPOFtJvInsVdRIdYVl1rVhj7RKogECPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwf6YZdqWI0LBW3zyYq3ANekPNh8g%2Fpg0ro4STol%2BgESYNNbMGpCfBtlDK1qIEDA69EseRh6wjdtVVrtJxAtYn5dlvcupPL1K3%2FoMSfjxCy7WPxGrJ2UVEjq6mGPFQul8rvVnhc4fbzpF9X0B1WvE97rshE4pB7c4v0%2BUE8AYz6sw7mKy8FeGXq0C2DOZN0FOFlPXXu3pq%2FcXa3FbdUQPZUewNJltzUSeRLax9NFyBE9Epq4XkKYzxaP9LlqA5JYbLY2HkUdssUlwM8xPDDUtKFQ1ZQRPBgEuYUtcdiQv%2B8ZoFfFO0N2XrYB%2BJx0pswDch3I%2B%2BHtloxNo9nWI234O0V5uf2V%2F%2FdTDjcEXolA1z7JjxXgoXJgZiMpo1nXDyJDgeWTPbp6FS78ZehCZTWhtXkS%2BXgopfo%2BHrFf4FNa%2ByFMoxBarNnBS02yEYpbWt17XsHCbS6n0%2Bl%2Fuo2htPOHyKPArPhYHgnAcxAUy6Wo0xT9FgHBIXOgU5ucysvRC0%2BAJfXvvWMjmyOucYqg06TUvsBnFcJbl4cWi2C6EF5Rp2VndUxHSXTaCMMtp7al0R8GD7o%2B7uSi0blVYVTkIA4Dt6XC%2B%2BChBaYeNGcVgtzIhu5JMCCAuetdCbx2YigCjbcJvyPqWmgZUIMUPztKTDEkrfQBjqkAVnoPLvqJIhLSTuoLps6TIDl5zERokez2HIDFMmIrJ0Z1CLCQ9wdFUHHpSAS3f4TxXzHKmVYvfLaKoT9DN7x1ObAC5B5Fov4ipo2gFeCu4TwMiUyxIBoz4IXSuHL7AdrRWwsB7R9GY3Ddb0OneN5gLhs55oXaJM8fHuMVCKG5W95%2Bf3sEZwhbhy0DCArwNm017TpMI72L6cxjJkDpJ7vi7oNecz3&X-Amz-Signature=df61114c157215773df1cb2aef2f8924230b37ebb277bde1edcf9301343c5286&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PRP3KWT%2F20260520%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260520T145034Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECcaCXVzLXdlc3QtMiJIMEYCIQCe%2BYNlSUdsU6OqhZ5hSDeOVr5T%2BAJQ04fFTWLGcFv50AIhANIBh%2BiXm53IoMADnmCpPOFtJvInsVdRIdYVl1rVhj7RKogECPD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwf6YZdqWI0LBW3zyYq3ANekPNh8g%2Fpg0ro4STol%2BgESYNNbMGpCfBtlDK1qIEDA69EseRh6wjdtVVrtJxAtYn5dlvcupPL1K3%2FoMSfjxCy7WPxGrJ2UVEjq6mGPFQul8rvVnhc4fbzpF9X0B1WvE97rshE4pB7c4v0%2BUE8AYz6sw7mKy8FeGXq0C2DOZN0FOFlPXXu3pq%2FcXa3FbdUQPZUewNJltzUSeRLax9NFyBE9Epq4XkKYzxaP9LlqA5JYbLY2HkUdssUlwM8xPDDUtKFQ1ZQRPBgEuYUtcdiQv%2B8ZoFfFO0N2XrYB%2BJx0pswDch3I%2B%2BHtloxNo9nWI234O0V5uf2V%2F%2FdTDjcEXolA1z7JjxXgoXJgZiMpo1nXDyJDgeWTPbp6FS78ZehCZTWhtXkS%2BXgopfo%2BHrFf4FNa%2ByFMoxBarNnBS02yEYpbWt17XsHCbS6n0%2Bl%2Fuo2htPOHyKPArPhYHgnAcxAUy6Wo0xT9FgHBIXOgU5ucysvRC0%2BAJfXvvWMjmyOucYqg06TUvsBnFcJbl4cWi2C6EF5Rp2VndUxHSXTaCMMtp7al0R8GD7o%2B7uSi0blVYVTkIA4Dt6XC%2B%2BChBaYeNGcVgtzIhu5JMCCAuetdCbx2YigCjbcJvyPqWmgZUIMUPztKTDEkrfQBjqkAVnoPLvqJIhLSTuoLps6TIDl5zERokez2HIDFMmIrJ0Z1CLCQ9wdFUHHpSAS3f4TxXzHKmVYvfLaKoT9DN7x1ObAC5B5Fov4ipo2gFeCu4TwMiUyxIBoz4IXSuHL7AdrRWwsB7R9GY3Ddb0OneN5gLhs55oXaJM8fHuMVCKG5W95%2Bf3sEZwhbhy0DCArwNm017TpMI72L6cxjJkDpJ7vi7oNecz3&X-Amz-Signature=89791a034fe6f4a17d8ee2860fa05f3ed82b9c7222506439559f485617f5e843&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







