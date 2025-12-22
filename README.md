



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466426NJTXE%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T182428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIFU9pnrsTNVQb4lmVYlAHqAxh35bUu7sC6rXinELFHhnAiEA2mx%2B2GDwbmIa0ifM9%2BXL2rCM49ee9dNTU6LVCrXl1FIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCd0R44Vn0CjYFrICircA%2FGTazHzDznUmYb2SB4ev6SMJ8layp%2Bb3PU8SvzN9KS21AePloEoFaiEdPJaLwzqX7Szg3zzpCGwMD0tCGD6oNISnioOgzSTJbj6MoIvvYJyRTJAdClJuVo1gx6Fy%2BCVlpJaMe%2BOZGrIVaAw8sRI5gTS43xpx7v3DTe7d3TYMncHcZ6%2BND4KpOlN6wqEdoJOhqMd%2FXnxBOwICVjBY0mENKFHprSRocdQUTeCdKW1r8K2az8UlLvo2a8qAzEOwHp3cpq9t0cwc1d5XYHv2dPJK%2FZNScwWJWVdVKwXp4%2BUd%2Bv45AzTFnAD1YdNLvtzbkziIF2vhnVX4eqilq3PR6F%2BUayWVhXLyTpe%2BJ760RdZiwhPpRQh8wBc5j%2B1hszTiFOY1ZH2iMGsXBa1YqE3tW7s6w4zxAnSl45kKfLHGP%2FLQi8GKhB%2FV6okr3Q50nI2uQOtl55fbenPiD8q7GN8H75ouYSRGWiQjX1mab0unOZPOIsgDX0JOqx9x2MhYgDBZlb1HGbdGATavgLTkfKuNmWMJ0OdmLMeEppBT8AiTAJxEQ05jdNQtsYDib9vdZMunyCKQ4d1JkGglz8vYXr8rNy%2Fe0vWv3lNOuO4yCcsKbVKXJeBqLrVwHKLPygC%2BpIMMOKCpsoGOqUBygRXHXkCKqDXLqSQ9GAtSL%2BYGsYHBqisQ6KNbadj8vOhILid1Yl4o968ISFlz05jbNzZJIwwIA2M21zJk14Z4PK7WOf4iZxLM5YB2Nb16x1KnoJj9AYmfuYDFPbHKe72XTFxBf0NmSt6lFmPPI7kIjd0svp9kD4FkZxHsXu4LAeNiJR%2FLQulAkhIDWzsg%2BKnSO95HkCyEroZWX506O1LQ1WnQ87M&X-Amz-Signature=6dee625ec99797db6c12b65e32a62fc6f71fcd96994988666c5e277760fbeee2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466426NJTXE%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T182429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIFU9pnrsTNVQb4lmVYlAHqAxh35bUu7sC6rXinELFHhnAiEA2mx%2B2GDwbmIa0ifM9%2BXL2rCM49ee9dNTU6LVCrXl1FIqiAQI%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCd0R44Vn0CjYFrICircA%2FGTazHzDznUmYb2SB4ev6SMJ8layp%2Bb3PU8SvzN9KS21AePloEoFaiEdPJaLwzqX7Szg3zzpCGwMD0tCGD6oNISnioOgzSTJbj6MoIvvYJyRTJAdClJuVo1gx6Fy%2BCVlpJaMe%2BOZGrIVaAw8sRI5gTS43xpx7v3DTe7d3TYMncHcZ6%2BND4KpOlN6wqEdoJOhqMd%2FXnxBOwICVjBY0mENKFHprSRocdQUTeCdKW1r8K2az8UlLvo2a8qAzEOwHp3cpq9t0cwc1d5XYHv2dPJK%2FZNScwWJWVdVKwXp4%2BUd%2Bv45AzTFnAD1YdNLvtzbkziIF2vhnVX4eqilq3PR6F%2BUayWVhXLyTpe%2BJ760RdZiwhPpRQh8wBc5j%2B1hszTiFOY1ZH2iMGsXBa1YqE3tW7s6w4zxAnSl45kKfLHGP%2FLQi8GKhB%2FV6okr3Q50nI2uQOtl55fbenPiD8q7GN8H75ouYSRGWiQjX1mab0unOZPOIsgDX0JOqx9x2MhYgDBZlb1HGbdGATavgLTkfKuNmWMJ0OdmLMeEppBT8AiTAJxEQ05jdNQtsYDib9vdZMunyCKQ4d1JkGglz8vYXr8rNy%2Fe0vWv3lNOuO4yCcsKbVKXJeBqLrVwHKLPygC%2BpIMMOKCpsoGOqUBygRXHXkCKqDXLqSQ9GAtSL%2BYGsYHBqisQ6KNbadj8vOhILid1Yl4o968ISFlz05jbNzZJIwwIA2M21zJk14Z4PK7WOf4iZxLM5YB2Nb16x1KnoJj9AYmfuYDFPbHKe72XTFxBf0NmSt6lFmPPI7kIjd0svp9kD4FkZxHsXu4LAeNiJR%2FLQulAkhIDWzsg%2BKnSO95HkCyEroZWX506O1LQ1WnQ87M&X-Amz-Signature=ea1bc5cadab7a8aee0bfdb8e6571c9758084c20d3e88cf0d055c033734aad522&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







