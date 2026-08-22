



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3OXVGOQ%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T062946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAh9uyYSApEckzY3%2BdAm4%2F7QNeuZEjvC9GPD4Yg%2FHPVkAiEAx5MCPC94TwWuCWh%2FXvdCk5X%2BAiJtpjGcdWdmyhkxZogqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNwoEotX%2BxvOarkj6SrcA%2FneoZtGbsNHVagyETk3YFfeDIO9rj25FKa%2FO06g0TkP8ZnWgI4nO7aI8w09bGQfZI9lgsYnBVcFl%2FSDK6a9YhZIwdzfeI%2FfFgVPacfs98RfMxtxbbkI1QSHQyGCsd2C8ITUiuWVyJ55M3q8j%2BveorpzRTT7pR1mKKIuC%2FnVaXH5NwVdEwR5HpB86xjCqGXUmn1NmjncazJrj747d2m4AQRHmLgYghYx%2FWmkR2%2FAXxGxVemqbISlQ4Rocvp9vkilxoP1ccYp%2B92SyUselSEIFmKGEZQbqXFs6relGs0SWyFvVppsUCIUYX1JYOjTsTK%2BAWNy923Qz%2B7R0W2z1eeNhik2HGx07Wg4y5sbhfKR2X6dROssmOkhNPjyzD%2Fq1MVAQlhOFntzEl1STN%2FKhsWLXkVZx3yfXKpICPMcRIKElfczEuIipka8G%2FLIYplHEoQ6inykiN1OAtK%2B%2FHwsNe5b52eYkCXnwYk7q9y9Llw89Ph%2F057f7gVIjxvHYSVVS4nUMzoTv6r2eXE6CDBPSFAeHWcE6kJ2fRBRoZm8jaHBpXjG7Uk97lvTYQUosuK0k8L1W8RXaTcTF6%2FQnGxV3g7C0UiAokoJciLOks6zBLBM6Hi8RPdQ1RlUueR%2F%2FsYRMJ%2F3pNQGOqUBKkEb1Nd4Veu%2FKGwRgX6l4O3nG9Au9sQSFHvHRGnPI2Wo72jtiHn2PXfcVfmEoiJhdI%2BoQCiGHOvrUcH68N8JoFvx%2FFEpKrvaFyMaPnUn4wTmCjOYvI4APONZsjHEU%2FWisQ3NDYlJgjt5vPKkjAD94tnjaFwPOj%2Fd3dnW9B29qySwNXBygOVVYfhIdBXthEV0QhvcV3eVr8VWHS%2Bbi2LOSkBamiX0&X-Amz-Signature=dd3002d59807db90620eca2ea6a7379ff7e4f9c53f6bd7119e3f3a6ba74ed057&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W3OXVGOQ%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T062946Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAh9uyYSApEckzY3%2BdAm4%2F7QNeuZEjvC9GPD4Yg%2FHPVkAiEAx5MCPC94TwWuCWh%2FXvdCk5X%2BAiJtpjGcdWdmyhkxZogqiAQIt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNwoEotX%2BxvOarkj6SrcA%2FneoZtGbsNHVagyETk3YFfeDIO9rj25FKa%2FO06g0TkP8ZnWgI4nO7aI8w09bGQfZI9lgsYnBVcFl%2FSDK6a9YhZIwdzfeI%2FfFgVPacfs98RfMxtxbbkI1QSHQyGCsd2C8ITUiuWVyJ55M3q8j%2BveorpzRTT7pR1mKKIuC%2FnVaXH5NwVdEwR5HpB86xjCqGXUmn1NmjncazJrj747d2m4AQRHmLgYghYx%2FWmkR2%2FAXxGxVemqbISlQ4Rocvp9vkilxoP1ccYp%2B92SyUselSEIFmKGEZQbqXFs6relGs0SWyFvVppsUCIUYX1JYOjTsTK%2BAWNy923Qz%2B7R0W2z1eeNhik2HGx07Wg4y5sbhfKR2X6dROssmOkhNPjyzD%2Fq1MVAQlhOFntzEl1STN%2FKhsWLXkVZx3yfXKpICPMcRIKElfczEuIipka8G%2FLIYplHEoQ6inykiN1OAtK%2B%2FHwsNe5b52eYkCXnwYk7q9y9Llw89Ph%2F057f7gVIjxvHYSVVS4nUMzoTv6r2eXE6CDBPSFAeHWcE6kJ2fRBRoZm8jaHBpXjG7Uk97lvTYQUosuK0k8L1W8RXaTcTF6%2FQnGxV3g7C0UiAokoJciLOks6zBLBM6Hi8RPdQ1RlUueR%2F%2FsYRMJ%2F3pNQGOqUBKkEb1Nd4Veu%2FKGwRgX6l4O3nG9Au9sQSFHvHRGnPI2Wo72jtiHn2PXfcVfmEoiJhdI%2BoQCiGHOvrUcH68N8JoFvx%2FFEpKrvaFyMaPnUn4wTmCjOYvI4APONZsjHEU%2FWisQ3NDYlJgjt5vPKkjAD94tnjaFwPOj%2Fd3dnW9B29qySwNXBygOVVYfhIdBXthEV0QhvcV3eVr8VWHS%2Bbi2LOSkBamiX0&X-Amz-Signature=7bae0ab1e64669d8b0c5e196241e203f3bd92307772dd49886105104c4762024&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







