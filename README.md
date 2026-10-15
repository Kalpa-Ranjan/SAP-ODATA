



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5HCU5QY%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T061320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALMZdWYkjEX2HUdwSXe7Jbz%2B7ihU3YGw3uWyQiAU%2F50AiEAxFITHAuJpYgUruNB7k5nfgeH%2BeSuLLBEdnE5FEBPadsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMt1UdX%2FYfIrK74pircA6GeHiOEVV%2FqR1HYf3IMPDXP5n3OfYD5VMwGGaTE%2Bt3DXst4PRGIen7V1qOC56el8qR656LztfRYYNJ7QeJ7AJa6PzsDlNhpmSLtbngzY0rLRw6XvO1q5afIrLSNqGUk%2BpY7GBjR81oCocaq9VY9zq85rnb%2BYQ3%2ByoiRnKHqIQbMBpHv8lu8JTNasAr08bhRclgJUNJdLB%2BTBggAO1wkId3%2BTHiwad5%2F2l%2B4wYLTIx4WZug7aD7BivBdHyHEpktcidOo5IAQF6tzZur6a2utCZb8M3TlTlLsIVOJNuFnUFv1Pr9ppXfuxYHyPTYRkWm3DoYfN1FocK7ucyu47z5Fvcz2JJSIcr9ZzelxcmajWU885huyrWtYDO0OwzarDLtracZw5pf%2F%2FgdBHM1TVzq%2BnA%2B0vpkbIt%2F9yH3hcjPBSZEZx%2BjUT1WbTzyF%2FlJO7Eqnq1fvTqia7ikp01obUExI4Tp9xLGBGNg7IuTfl2T3quzHA9HsdYPcLVP0Z2HUt8NM3p%2FLMx34%2F1owHdDrYa6J6%2BK73vIG08Z7ImfWkMuL9AGvNY%2FymELhRLccU1hZT%2Fk3wn7O8CTR9DBATSNkQvnOxFGAIKEAbNyXS6raSBRA936N%2FU33RLIperr%2BOv3JMJDUwdYGOqUBX4VSXjDR4WM9F821OQQYZBIwq5MAHgpBB4RvOQBBdU88mbxKNwOLSt%2FE9iUMKvqIbYcOh2n9PhojW55Qve0AUi17DkqQOi5cyonAr6h%2F2LeaSitTWUSJsT%2Fs5PT%2B3n0LjhxURCPKJGw6gbvcttI10eWPVVXK6UMZWiz76dTfh7vFM4a9PURnIJN36mpplSEDJ58ZojO%2FyEREvLeRCh086E%2FktZ0C&X-Amz-Signature=95d14c494ada669a15987f0a6a06539d151b1f67ae8e132a9d0f5a8f6e1d5c03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5HCU5QY%2F20261015%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261015T061320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALMZdWYkjEX2HUdwSXe7Jbz%2B7ihU3YGw3uWyQiAU%2F50AiEAxFITHAuJpYgUruNB7k5nfgeH%2BeSuLLBEdnE5FEBPadsqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMt1UdX%2FYfIrK74pircA6GeHiOEVV%2FqR1HYf3IMPDXP5n3OfYD5VMwGGaTE%2Bt3DXst4PRGIen7V1qOC56el8qR656LztfRYYNJ7QeJ7AJa6PzsDlNhpmSLtbngzY0rLRw6XvO1q5afIrLSNqGUk%2BpY7GBjR81oCocaq9VY9zq85rnb%2BYQ3%2ByoiRnKHqIQbMBpHv8lu8JTNasAr08bhRclgJUNJdLB%2BTBggAO1wkId3%2BTHiwad5%2F2l%2B4wYLTIx4WZug7aD7BivBdHyHEpktcidOo5IAQF6tzZur6a2utCZb8M3TlTlLsIVOJNuFnUFv1Pr9ppXfuxYHyPTYRkWm3DoYfN1FocK7ucyu47z5Fvcz2JJSIcr9ZzelxcmajWU885huyrWtYDO0OwzarDLtracZw5pf%2F%2FgdBHM1TVzq%2BnA%2B0vpkbIt%2F9yH3hcjPBSZEZx%2BjUT1WbTzyF%2FlJO7Eqnq1fvTqia7ikp01obUExI4Tp9xLGBGNg7IuTfl2T3quzHA9HsdYPcLVP0Z2HUt8NM3p%2FLMx34%2F1owHdDrYa6J6%2BK73vIG08Z7ImfWkMuL9AGvNY%2FymELhRLccU1hZT%2Fk3wn7O8CTR9DBATSNkQvnOxFGAIKEAbNyXS6raSBRA936N%2FU33RLIperr%2BOv3JMJDUwdYGOqUBX4VSXjDR4WM9F821OQQYZBIwq5MAHgpBB4RvOQBBdU88mbxKNwOLSt%2FE9iUMKvqIbYcOh2n9PhojW55Qve0AUi17DkqQOi5cyonAr6h%2F2LeaSitTWUSJsT%2Fs5PT%2B3n0LjhxURCPKJGw6gbvcttI10eWPVVXK6UMZWiz76dTfh7vFM4a9PURnIJN36mpplSEDJ58ZojO%2FyEREvLeRCh086E%2FktZ0C&X-Amz-Signature=75718fc594c77ca026d1520b411f47d1e31497838f91a2b3b639570764db6834&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







