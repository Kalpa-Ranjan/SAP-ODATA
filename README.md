



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GRZHO3D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T191137Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClIdipQe%2BH2g5JQqGqcFLhapfbX95NoaYJdT2yYVhj8gIgXmQneLoUw9cGt6qMVPCxCf7i281%2FF0Xb5BQWsJVkNoMqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEyxRPYVo4ye8CLBnCrcA6r679%2FjAda4xT2%2BgCWdBa9zXaGED%2FP%2Bzm14YzUymoamP%2FiaglBJU6J%2FODmdMsSTA%2FxR830Nu%2F1z9gA6%2FBcilFxzIiI%2FIHLymqFkoDHQwacwUNrOPeV%2B5SftIynNYaBYxrpHCbqk2KexB9rW%2BaDZmwCdq0MJ8n0rSv2rxpGz4ncIxL%2B1XmpFY8gAqarc%2Be%2BvS%2BgX7fH6Yicn1jMHTO3XpQSrj57ES7QqkFW%2F7NrfLYVuOrlJJ7pLyv1tbnxuEMA6jGi34j02qsS0nhvtLPwK5zutc8b5qGV6L%2Bsd246IgbKi60GgdWrx0WdQMtyrgcGTTpwvekALe7u2f%2BEJpYLdoJLsyEPiRbSBw5aguVQnCRqa9agxaoDAJ3sPON4uiFXuqP1I7CpvpaHOEcB3aUWepHCoaiMDK9ExZtrbhuhUVPi4tfGX5U8NindN0kYBYLAZXHGNDyhdj1zZI%2F6XJLkchfaGSYJ%2FIKcQn%2FJGA03GxzL%2Bj%2BjOxU7kI5hKDe09N28OFKS%2FgGJgEEjOyFPMKLeBCFJ%2BfpeD0DXFgm2C6UUnDQLPHawDfWlDohzyvTQ3aeAXWW6UQdwQ%2FjTGNHFi0bEdvGYlmVGefr2FJ1vH%2FvVjAdqQXyEhvtnaUEhNcR68MPuo%2FtIGOqUB7ci5j0cqhxno58TV%2Fe2lE5hwcHc1vx4SrJZNkrREVZ36OUxedhrTnEXzEaPXfbCAP7QIs6bCImUh9Q5K%2BsuKsY0Z6FIEJIU78dB%2BEt6mKJNGmp3ODC1LiCozcbHjD%2FI4h0N9mpWhSc8gNl%2BMlGuMVsnkLmi6LJLGqVpYA1Sovsx3QOfT1T5sT0tQnUuQxCcbRgY2vsNC0WbwqVwmw6GBUTou0vAy&X-Amz-Signature=6b1329b0a12f7b2d1cab6cd21ec13aecc1a77097849940cd9f708f7c604d41a8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663GRZHO3D%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T191138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClIdipQe%2BH2g5JQqGqcFLhapfbX95NoaYJdT2yYVhj8gIgXmQneLoUw9cGt6qMVPCxCf7i281%2FF0Xb5BQWsJVkNoMqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEyxRPYVo4ye8CLBnCrcA6r679%2FjAda4xT2%2BgCWdBa9zXaGED%2FP%2Bzm14YzUymoamP%2FiaglBJU6J%2FODmdMsSTA%2FxR830Nu%2F1z9gA6%2FBcilFxzIiI%2FIHLymqFkoDHQwacwUNrOPeV%2B5SftIynNYaBYxrpHCbqk2KexB9rW%2BaDZmwCdq0MJ8n0rSv2rxpGz4ncIxL%2B1XmpFY8gAqarc%2Be%2BvS%2BgX7fH6Yicn1jMHTO3XpQSrj57ES7QqkFW%2F7NrfLYVuOrlJJ7pLyv1tbnxuEMA6jGi34j02qsS0nhvtLPwK5zutc8b5qGV6L%2Bsd246IgbKi60GgdWrx0WdQMtyrgcGTTpwvekALe7u2f%2BEJpYLdoJLsyEPiRbSBw5aguVQnCRqa9agxaoDAJ3sPON4uiFXuqP1I7CpvpaHOEcB3aUWepHCoaiMDK9ExZtrbhuhUVPi4tfGX5U8NindN0kYBYLAZXHGNDyhdj1zZI%2F6XJLkchfaGSYJ%2FIKcQn%2FJGA03GxzL%2Bj%2BjOxU7kI5hKDe09N28OFKS%2FgGJgEEjOyFPMKLeBCFJ%2BfpeD0DXFgm2C6UUnDQLPHawDfWlDohzyvTQ3aeAXWW6UQdwQ%2FjTGNHFi0bEdvGYlmVGefr2FJ1vH%2FvVjAdqQXyEhvtnaUEhNcR68MPuo%2FtIGOqUB7ci5j0cqhxno58TV%2Fe2lE5hwcHc1vx4SrJZNkrREVZ36OUxedhrTnEXzEaPXfbCAP7QIs6bCImUh9Q5K%2BsuKsY0Z6FIEJIU78dB%2BEt6mKJNGmp3ODC1LiCozcbHjD%2FI4h0N9mpWhSc8gNl%2BMlGuMVsnkLmi6LJLGqVpYA1Sovsx3QOfT1T5sT0tQnUuQxCcbRgY2vsNC0WbwqVwmw6GBUTou0vAy&X-Amz-Signature=b4e0d462b52cda593e09446705a6724571e148a824b1aae8c90542d7bd0e6b12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







