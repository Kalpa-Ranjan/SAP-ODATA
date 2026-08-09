



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GJXJK74%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T183146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCftCpd0Tc1WdwRhGzYBLhhnpHLrSFMdEBoPOUMWRX13QIgEEVdIObQoORe4BPO1h1XjfLL3Q6RAC6z%2FoYeHAjldRcqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHc%2B79bvpj%2FD0qtCuSrcAz2kmYto1fW9DAn999%2FEof5l6zszUDzOYTlBywYik2wS4qLDGedwAMbMJcIXa8j6t1L0euG939ylR8oUoNxrJn7lZ0tEeNcPWGV0MglxGtXOYYn4Q%2FiN8EOe3cAPtp150%2BTWEyeV82qHxKuBoeoNANZw7ar8YaNoR0xkaLmui0KxPEQNcOGdmvO8OET8fbBrXGP3FVHiVnybzUMjasqwcvQdKREDkIQofO9wI7GgERyR91RaNsemjrH7Q4GUQJYZ71wkcXGamThehAuWolYjIEJfT4YXV76CPKRkHhElQT0%2FtTyYHUEgwS88RRYx3YNtIqKn7hw0UXmjGY5q1eYTgazJoGw0FRraWwJ5mmwGpJwpxGKAsS7dFBe0Ttty8oG0gLaGaqnmxFqV4prW4wpwNxmSOZ0vhgQNZ0mMma6IJtKi3c9253gYHQUr9VLola0BmA9pLT1ws8%2Fm3bTfElmCxkinMaO7%2Bod1rCZ6gvbMQXNsSIh2%2F%2BS7qc%2F3xej5fRTD%2B0mOJrOgtc7jIzkrSnKmuJFV48VetwxzE5iJP2UGAAHem0kT2vYFrKGbChuMCyvZFMtKXzGIhgMrxqtvvGkWSQDR8vdb4yYQS0UJMKtXuUdnN95fYcGtueBcdL%2BWMKXX4tMGOqUBMrIwCkoDKxMwiUEXWDvi76QDApU8qTDq3pLOViI%2Bvd9eB%2BNtx2Lv53H9hYn2b7GUa9Xiui%2FbXMooSDXqOiKoylDxkkQ585RHLuoPPixzbOS42lW4fdCVzoVF3vMHIvboC213qk95zmLDofzplOV4Vg%2B%2FyR1qzdrjqmA59Knzby135W0VTIv51dcOfV5y%2FFL7I2WH7Z8MVRNl%2BR2JrFlRgPFBvE7U&X-Amz-Signature=f4ded9e55f0adac65c5ddfb4a7e3dc8dd0fefdd5ae7ef1757d1b45e44f953245&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GJXJK74%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T183146Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCftCpd0Tc1WdwRhGzYBLhhnpHLrSFMdEBoPOUMWRX13QIgEEVdIObQoORe4BPO1h1XjfLL3Q6RAC6z%2FoYeHAjldRcqiAQIiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHc%2B79bvpj%2FD0qtCuSrcAz2kmYto1fW9DAn999%2FEof5l6zszUDzOYTlBywYik2wS4qLDGedwAMbMJcIXa8j6t1L0euG939ylR8oUoNxrJn7lZ0tEeNcPWGV0MglxGtXOYYn4Q%2FiN8EOe3cAPtp150%2BTWEyeV82qHxKuBoeoNANZw7ar8YaNoR0xkaLmui0KxPEQNcOGdmvO8OET8fbBrXGP3FVHiVnybzUMjasqwcvQdKREDkIQofO9wI7GgERyR91RaNsemjrH7Q4GUQJYZ71wkcXGamThehAuWolYjIEJfT4YXV76CPKRkHhElQT0%2FtTyYHUEgwS88RRYx3YNtIqKn7hw0UXmjGY5q1eYTgazJoGw0FRraWwJ5mmwGpJwpxGKAsS7dFBe0Ttty8oG0gLaGaqnmxFqV4prW4wpwNxmSOZ0vhgQNZ0mMma6IJtKi3c9253gYHQUr9VLola0BmA9pLT1ws8%2Fm3bTfElmCxkinMaO7%2Bod1rCZ6gvbMQXNsSIh2%2F%2BS7qc%2F3xej5fRTD%2B0mOJrOgtc7jIzkrSnKmuJFV48VetwxzE5iJP2UGAAHem0kT2vYFrKGbChuMCyvZFMtKXzGIhgMrxqtvvGkWSQDR8vdb4yYQS0UJMKtXuUdnN95fYcGtueBcdL%2BWMKXX4tMGOqUBMrIwCkoDKxMwiUEXWDvi76QDApU8qTDq3pLOViI%2Bvd9eB%2BNtx2Lv53H9hYn2b7GUa9Xiui%2FbXMooSDXqOiKoylDxkkQ585RHLuoPPixzbOS42lW4fdCVzoVF3vMHIvboC213qk95zmLDofzplOV4Vg%2B%2FyR1qzdrjqmA59Knzby135W0VTIv51dcOfV5y%2FFL7I2WH7Z8MVRNl%2BR2JrFlRgPFBvE7U&X-Amz-Signature=6472fbb50b701784fe765338038b52230aa8bf4e4cc06b76b520dc3ef938bd50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







