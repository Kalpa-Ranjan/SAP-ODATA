



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5BPI3J%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T124237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgZiMLRJo24%2FuIhQiQCrIEio2W3EwdAg9n%2F299MRxdawIgC%2B3O4fRNhl70%2Fy%2Bw2Y1D%2Fk56IBTq%2F87gFGqsVXpNGgUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1qS5EyoDmIuHakTCrcAwckf1dO6QHxO1w9pW5HX707WSve0%2BlW4QcIAYTTlUjXtdFKrP2aa71Zk7NPSlX%2FWlnGpJFl%2F1pnWEDKq1v4lzkmnvuYYHag80QhZHI7UgnR8iPpE0K2pvU%2BTAyHBJUFzwJlgAKrb6EzwzAVNE7FUbhHmQYs8agB6SEyNh0p%2FPfiwtR7MzQDYyJedU7F%2FJ3ZdD5Gz%2B4NP4m0W7Ln4Wg7ByQSVuHde6Huc1wFeFK0LTzGbEFeBgkDCRz2cckpU5BEj5hEwlDkk5U%2FKK6J6vu4xOpg7c0YgEMGULHbWnQbFeaJavb7Iund72OYzYOGLNKyO2W65FKUd8TJ5nVhI8yoq32lTtaf3H4xj3jTtujyr3pfFS0sSLTToUe0txeLiYqL5tNC01oYxE1rEL34MCon2fSLRWAako4s6VglpMYD7qdElNU9E2Nai2UX7o91Cc4RIduOKrPH1WvEe5rVSsGKIHHmEUA2%2FWeTM8PWKoCFnaLyqyenyWMuaIiOzcyTFBEUFwcJj4%2BBbY3pmUtCpndddYXZhWFoOJQQf4Hz4GO83WgPrQ%2FFMaFhs5Xv0lU1YvVVEII3UN6znYejpWpe0SDJDTbH%2BiJm19mU0SRpcAumOzBlqe%2BajYcc2%2BYdbaPOMN3I8ssGOqUBU2mNkphkCYN9m%2FbBR7ztEWOnXLGsgES1HUw06lyteu%2BXx6qtLe0%2BKO6Q7SFLdb7SG1q4HkD73ih4raeL%2FgnsDXOmjfwq3%2F170fEXC78PODLEBXdWCdhmBRo00lMgo5B77Ukiz%2B3uy3MK9y2g%2FuKWdwCUAdLqRkKkUSOsyzyjL%2FPb3AdBz6z8mPvMbr6UENLo8oH%2B3AoEWxhjwtQS0koJOGVX1%2FNU&X-Amz-Signature=036d4d645da4c51fff434af3892a1afbb82d85b6a406cffcccde0f1971b2aae6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RG5BPI3J%2F20260130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260130T124237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDgZiMLRJo24%2FuIhQiQCrIEio2W3EwdAg9n%2F299MRxdawIgC%2B3O4fRNhl70%2Fy%2Bw2Y1D%2Fk56IBTq%2F87gFGqsVXpNGgUqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1qS5EyoDmIuHakTCrcAwckf1dO6QHxO1w9pW5HX707WSve0%2BlW4QcIAYTTlUjXtdFKrP2aa71Zk7NPSlX%2FWlnGpJFl%2F1pnWEDKq1v4lzkmnvuYYHag80QhZHI7UgnR8iPpE0K2pvU%2BTAyHBJUFzwJlgAKrb6EzwzAVNE7FUbhHmQYs8agB6SEyNh0p%2FPfiwtR7MzQDYyJedU7F%2FJ3ZdD5Gz%2B4NP4m0W7Ln4Wg7ByQSVuHde6Huc1wFeFK0LTzGbEFeBgkDCRz2cckpU5BEj5hEwlDkk5U%2FKK6J6vu4xOpg7c0YgEMGULHbWnQbFeaJavb7Iund72OYzYOGLNKyO2W65FKUd8TJ5nVhI8yoq32lTtaf3H4xj3jTtujyr3pfFS0sSLTToUe0txeLiYqL5tNC01oYxE1rEL34MCon2fSLRWAako4s6VglpMYD7qdElNU9E2Nai2UX7o91Cc4RIduOKrPH1WvEe5rVSsGKIHHmEUA2%2FWeTM8PWKoCFnaLyqyenyWMuaIiOzcyTFBEUFwcJj4%2BBbY3pmUtCpndddYXZhWFoOJQQf4Hz4GO83WgPrQ%2FFMaFhs5Xv0lU1YvVVEII3UN6znYejpWpe0SDJDTbH%2BiJm19mU0SRpcAumOzBlqe%2BajYcc2%2BYdbaPOMN3I8ssGOqUBU2mNkphkCYN9m%2FbBR7ztEWOnXLGsgES1HUw06lyteu%2BXx6qtLe0%2BKO6Q7SFLdb7SG1q4HkD73ih4raeL%2FgnsDXOmjfwq3%2F170fEXC78PODLEBXdWCdhmBRo00lMgo5B77Ukiz%2B3uy3MK9y2g%2FuKWdwCUAdLqRkKkUSOsyzyjL%2FPb3AdBz6z8mPvMbr6UENLo8oH%2B3AoEWxhjwtQS0koJOGVX1%2FNU&X-Amz-Signature=242792720f273f2a27d0fb8d71f9296ca8d1ea13e69eeb84a4ac595c79fee3e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







