



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HL53OJ7%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T005516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUs%2Bj0GPumhRFFR2sm1YzIxVs%2BQJskrcJisxzrfMiq5AIhAM5ZqA9r2dbPRjK%2F4pHS0NHALDc2MnjsSmKmShIZ1ye9KogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9umkMVf6JJH%2F9YZgq3AMUlIiZOjUy%2Bh2H7yfp%2FRoOv4rn1mlJJNNXnCRd%2FpeY5n6HoFF2%2B0yJqObRB3mA6ET3vHIKOP9GbcZGKZMcvHefX4ETn3suY0nNTwHR0ZpND0QBoCD%2FK%2Fxcm3LBdC1VJKt5IqhvrC6sDI4ZQpGXZdGoYFjDCFBkmMNZnJoUtvxqgIYgY0aOrijSx0VVVgIt3WpgFaIp%2FOHsQhoqzqd1N789VL90hSKoYauXLkFtyZ6RkVuiW%2F7q9qYtPZG%2FnOKbc3PMnk2w1pyhryIR0mbPzE9jPPPss9ivqYLqP9LcMGfF00NHSuBTElknpk9SXtRNx7u4zMoaUYRrYqLirjzMfkzmi7xmEv3jSPzY8NpDf2q1D6t8QKKyqCwh6RDRxHiLQ8VkPHqRvOn9mXkj7fcfhXpjfhfzYaepXgnylDCscj4dPvOzR6neatYzeNCSmoXoizDDQooWliY3omZ3PMN2EzM4lilij4VUuy8x9TWfAW9qgFMGgX9uWOYMXvxGfhH9OPz9A4NL%2FzOgM%2BGnfmSDNwnMGACeM4oqSs9GhMDJue71H7jGVv0Dj3ge5Tj0Ia%2BybYuRPeDSrILtp%2BTHHjZVOX4z1ZDJKvbCLXlvClYDxIxk6AiSPAyxLqjluFXfCjC3xKPUBjqkARoWIt9gwTsxWutwQecOiD1bklhTEfwM7AFa8HwHak1WKvbFMEbbMYTRoKHyLF9IfiBhhL0SECLyT8gq%2BeR%2BHc4OhvdqHP%2B6IyFpBKEPmBD8AnbuWCKIopriRBsHDBN%2B3A%2FfPU6UikRL%2Fak8Zm3YPAhbgUXz5CSQsDkwkXdMEqtCnY1imrlR9XVxDWsL1RX5nxRNsa3JdJbOzmA%2BhPMfBFGMJo2U&X-Amz-Signature=3f75f20c8838c3f9e8ed8771bac4ec1364824dc956cd9b6c8d4b2f8f1ca741af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665HL53OJ7%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T005516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUs%2Bj0GPumhRFFR2sm1YzIxVs%2BQJskrcJisxzrfMiq5AIhAM5ZqA9r2dbPRjK%2F4pHS0NHALDc2MnjsSmKmShIZ1ye9KogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9umkMVf6JJH%2F9YZgq3AMUlIiZOjUy%2Bh2H7yfp%2FRoOv4rn1mlJJNNXnCRd%2FpeY5n6HoFF2%2B0yJqObRB3mA6ET3vHIKOP9GbcZGKZMcvHefX4ETn3suY0nNTwHR0ZpND0QBoCD%2FK%2Fxcm3LBdC1VJKt5IqhvrC6sDI4ZQpGXZdGoYFjDCFBkmMNZnJoUtvxqgIYgY0aOrijSx0VVVgIt3WpgFaIp%2FOHsQhoqzqd1N789VL90hSKoYauXLkFtyZ6RkVuiW%2F7q9qYtPZG%2FnOKbc3PMnk2w1pyhryIR0mbPzE9jPPPss9ivqYLqP9LcMGfF00NHSuBTElknpk9SXtRNx7u4zMoaUYRrYqLirjzMfkzmi7xmEv3jSPzY8NpDf2q1D6t8QKKyqCwh6RDRxHiLQ8VkPHqRvOn9mXkj7fcfhXpjfhfzYaepXgnylDCscj4dPvOzR6neatYzeNCSmoXoizDDQooWliY3omZ3PMN2EzM4lilij4VUuy8x9TWfAW9qgFMGgX9uWOYMXvxGfhH9OPz9A4NL%2FzOgM%2BGnfmSDNwnMGACeM4oqSs9GhMDJue71H7jGVv0Dj3ge5Tj0Ia%2BybYuRPeDSrILtp%2BTHHjZVOX4z1ZDJKvbCLXlvClYDxIxk6AiSPAyxLqjluFXfCjC3xKPUBjqkARoWIt9gwTsxWutwQecOiD1bklhTEfwM7AFa8HwHak1WKvbFMEbbMYTRoKHyLF9IfiBhhL0SECLyT8gq%2BeR%2BHc4OhvdqHP%2B6IyFpBKEPmBD8AnbuWCKIopriRBsHDBN%2B3A%2FfPU6UikRL%2Fak8Zm3YPAhbgUXz5CSQsDkwkXdMEqtCnY1imrlR9XVxDWsL1RX5nxRNsa3JdJbOzmA%2BhPMfBFGMJo2U&X-Amz-Signature=531e9fa4d6808876171f555bc42bbacf2f4ada3fceb419e021437b0eaaefac8a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







