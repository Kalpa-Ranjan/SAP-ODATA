



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRLZAE4Z%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T001434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDD4xzxTsQIL%2Fe54%2B63jv%2FaJPJcth0w2Ii2vT0UTabIKAiAs9cbumEwAXEuEtPABOcD4LG4WOGpGFtQGcDAO0nX%2Bnyr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIM2irhZX59qJLcMc%2BpKtwDnR10v68GP9vwbPu59ZjeB8NtfbCodGceWQ9uQuK5chDsh6xKlJWVeD3gN6YuoA%2B97vMPq1Z2bS0XrilsqX9ybklTizQbriuO%2F4%2BCrfT%2FS%2FfEo418%2B0Ln2y88uU7wk3ZrspX%2F4QvWBkmMiN3TUKne4pm9%2BCUuje6ONiaT6EKiFW6Ma38ad8aNgeZ9bo4ChzWa7a1UHD6okomtjmydMltuQIg%2FsFTIwLTuwtCDtGDqWkj93pwgAYAMCY51K%2BGiYs4qR%2B5KamDtf7xeLSaRh%2BM22J1hB%2Flrc2J1yTvOq7leLEadqQXz9Cov2t6rVoC32hOT9ns33Pu1cBrox%2B%2BE1YumVe2YnqEVj44OgRNnwMCm1BuLNsd04vSwfmpUUoVBKaR40O4BqH4ba5rv0cyWm648EOSaKbYDBXPk0k6elz2CBrEDwnCWBrLWIcDi7rh%2F6MFbRjzs%2BcykIX5W56WrRTrlGsYa%2Bz2aVhfs5fjpUso4WKTXRXzDSlfMZickoDyGHfElyWg7dltEolkvyzWORvNuD401Pj7pNNX2LKcGBbjESycYNkoMADi%2Ff33T8rC%2BNsSEHkt1i77WqXhK5i4KcSJih01BNxIxOYx2FZ5J3ghjzUJPVqJ%2FUZ9MGa15Cjkw9o6f1wY6pgFpwXF4islHJBdQedBy6NrVmLX7d3KoWTtZW2npZiFnvMXrdclOPiWgUArVR39Yqx%2BfGqnP7B5Jk7Dzd4%2Bpu3cOcca%2BoqBUqglPNmEvxrGeuq0QvDo4nIxwpleJF4Ifa4lt3kTKDcca1A0M2guYKRrX7xdbqoiiWnPdjzhj%2Fw2tfZoO3%2BHTaG3TZF8p0Nl1rCSBab2fuzL1AdX4P7E759a771xpK2bB&X-Amz-Signature=0e249580c3c991f92a32ed8e515fac66ebe1c60c23da1daa4120e11909ed35bb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WRLZAE4Z%2F20261102%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261102T001434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDD4xzxTsQIL%2Fe54%2B63jv%2FaJPJcth0w2Ii2vT0UTabIKAiAs9cbumEwAXEuEtPABOcD4LG4WOGpGFtQGcDAO0nX%2Bnyr%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIM2irhZX59qJLcMc%2BpKtwDnR10v68GP9vwbPu59ZjeB8NtfbCodGceWQ9uQuK5chDsh6xKlJWVeD3gN6YuoA%2B97vMPq1Z2bS0XrilsqX9ybklTizQbriuO%2F4%2BCrfT%2FS%2FfEo418%2B0Ln2y88uU7wk3ZrspX%2F4QvWBkmMiN3TUKne4pm9%2BCUuje6ONiaT6EKiFW6Ma38ad8aNgeZ9bo4ChzWa7a1UHD6okomtjmydMltuQIg%2FsFTIwLTuwtCDtGDqWkj93pwgAYAMCY51K%2BGiYs4qR%2B5KamDtf7xeLSaRh%2BM22J1hB%2Flrc2J1yTvOq7leLEadqQXz9Cov2t6rVoC32hOT9ns33Pu1cBrox%2B%2BE1YumVe2YnqEVj44OgRNnwMCm1BuLNsd04vSwfmpUUoVBKaR40O4BqH4ba5rv0cyWm648EOSaKbYDBXPk0k6elz2CBrEDwnCWBrLWIcDi7rh%2F6MFbRjzs%2BcykIX5W56WrRTrlGsYa%2Bz2aVhfs5fjpUso4WKTXRXzDSlfMZickoDyGHfElyWg7dltEolkvyzWORvNuD401Pj7pNNX2LKcGBbjESycYNkoMADi%2Ff33T8rC%2BNsSEHkt1i77WqXhK5i4KcSJih01BNxIxOYx2FZ5J3ghjzUJPVqJ%2FUZ9MGa15Cjkw9o6f1wY6pgFpwXF4islHJBdQedBy6NrVmLX7d3KoWTtZW2npZiFnvMXrdclOPiWgUArVR39Yqx%2BfGqnP7B5Jk7Dzd4%2Bpu3cOcca%2BoqBUqglPNmEvxrGeuq0QvDo4nIxwpleJF4Ifa4lt3kTKDcca1A0M2guYKRrX7xdbqoiiWnPdjzhj%2Fw2tfZoO3%2BHTaG3TZF8p0Nl1rCSBab2fuzL1AdX4P7E759a771xpK2bB&X-Amz-Signature=14f5a285ab46585c28de82601c4aa30b33805354713d5137f046b213f66a4fda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







