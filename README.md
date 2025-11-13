



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U4XNCCG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T062422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCIQC99UDwP1nZ0aSoBzVCgp8FHn2vA75dE4A85CdAt22cmQIgXW0F0fhXJEI114HsMCL%2FthFOxVCOy8B2A1ZTgSXjPaIq%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDFJBP%2FHNWNL6q4zzsircA2MKOtzsm9krqe6wRUto0qnThfJyjpc2pjneBlA%2BkVWoxKl7RyqVsSdnfftYqzGrUH1sJtOyifEIFGCcLuviUUGUSMIRX7Fwsx8trqJ%2FjpQeEWZTWhunG6rNqTHPrQnTdGBiFLBIUQGOX1M4CcFH8j4Jr3Cmy3iu4VpAVjHiX5FSi5sYFcEKeAiBf6fAK%2F6zARVvPaamvOZI%2FM5RDXtMz8KiSMVhj73d2lZ%2FW%2FJ7IP6AZsAaHZeYmyACBJD1Sn%2Bq1dE2faa9iscate5QSK5K8BfGtxDG3uuOvLgO6cYejSvgzGZfywvke4fOrHt9vOFs4ZY0OwF0DDKdEtAyrAq5Bhgrii6wjhIikaYLS5UGLkc8qTKJ3GF7dgTQCRNyn%2FeUwsFTDo6rfWQI7SQNlLCH1cDGyytwOyjLa%2B%2FrCs71nuAigDSs71%2BKYrNepI1nZqaIdN%2Bs3GqdFEgf8IGVBH%2Bbd%2B6F9tDGSXnBL9aE%2F5mq6pc0yNzUeDJ%2BB5cWzg2A%2FkZvdI104M38rMfnAAhc7CyQWyoue%2BxYDFnb47y31%2BHEl5OErnWK7Ij4QxrYJ68X0LUEcynFD7WiKlDc0Z2Wf%2B7dqerd8emImjbt10u%2BlfmD47QsySJLZuVbR%2Bo2jwEwMMDK1cgGOqUBBwLkMz2qICWYBdgQEfvs9dtifchR33fBfOmR2E36DySkyMIKmLWriwe32I%2Fx%2FgBYsAtVePGOjakOKarZEK%2FIWNIM5aUdXzCeV5neou%2FtRTEBPETeC7nqBryrRnCbCGjuD9ZG4oI5LAy5dRf6o5MoJNC4wuzsRM0l4t7oX22%2FVqtT5LdJ9OhmwsSMaj23Kgp%2FpwG2G%2BLzlE2TfNon9XYGw8Aq%2BdNK&X-Amz-Signature=2d0bdc753a2c993a9ab1cb7e3ade1fea890b9c14510e2e30d04f83dc6f24a6ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662U4XNCCG%2F20251113%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251113T062422Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH0aCXVzLXdlc3QtMiJHMEUCIQC99UDwP1nZ0aSoBzVCgp8FHn2vA75dE4A85CdAt22cmQIgXW0F0fhXJEI114HsMCL%2FthFOxVCOy8B2A1ZTgSXjPaIq%2FwMIRhAAGgw2Mzc0MjMxODM4MDUiDFJBP%2FHNWNL6q4zzsircA2MKOtzsm9krqe6wRUto0qnThfJyjpc2pjneBlA%2BkVWoxKl7RyqVsSdnfftYqzGrUH1sJtOyifEIFGCcLuviUUGUSMIRX7Fwsx8trqJ%2FjpQeEWZTWhunG6rNqTHPrQnTdGBiFLBIUQGOX1M4CcFH8j4Jr3Cmy3iu4VpAVjHiX5FSi5sYFcEKeAiBf6fAK%2F6zARVvPaamvOZI%2FM5RDXtMz8KiSMVhj73d2lZ%2FW%2FJ7IP6AZsAaHZeYmyACBJD1Sn%2Bq1dE2faa9iscate5QSK5K8BfGtxDG3uuOvLgO6cYejSvgzGZfywvke4fOrHt9vOFs4ZY0OwF0DDKdEtAyrAq5Bhgrii6wjhIikaYLS5UGLkc8qTKJ3GF7dgTQCRNyn%2FeUwsFTDo6rfWQI7SQNlLCH1cDGyytwOyjLa%2B%2FrCs71nuAigDSs71%2BKYrNepI1nZqaIdN%2Bs3GqdFEgf8IGVBH%2Bbd%2B6F9tDGSXnBL9aE%2F5mq6pc0yNzUeDJ%2BB5cWzg2A%2FkZvdI104M38rMfnAAhc7CyQWyoue%2BxYDFnb47y31%2BHEl5OErnWK7Ij4QxrYJ68X0LUEcynFD7WiKlDc0Z2Wf%2B7dqerd8emImjbt10u%2BlfmD47QsySJLZuVbR%2Bo2jwEwMMDK1cgGOqUBBwLkMz2qICWYBdgQEfvs9dtifchR33fBfOmR2E36DySkyMIKmLWriwe32I%2Fx%2FgBYsAtVePGOjakOKarZEK%2FIWNIM5aUdXzCeV5neou%2FtRTEBPETeC7nqBryrRnCbCGjuD9ZG4oI5LAy5dRf6o5MoJNC4wuzsRM0l4t7oX22%2FVqtT5LdJ9OhmwsSMaj23Kgp%2FpwG2G%2BLzlE2TfNon9XYGw8Aq%2BdNK&X-Amz-Signature=d41418cc305b6a8305c159a1902551beb3c18093ff2ff907acda131ed22bd988&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







