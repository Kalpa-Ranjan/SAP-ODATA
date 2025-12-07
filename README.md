



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XMG2ZLY%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T012119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTvwjmyZp5RKNG%2BDrsWIHUS9cd5O9%2FqmXOhKKVxpVHQwIgbEKkvXAiTuMIRjrrhSR%2BlEI0%2FbjSP1rO9OD5P%2FkBgYYqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPp1KpD2uWBPvJxn1yrcA6691tt%2BrVnJuOuEe8uwaLh7PxpOhfAtYrlLepecfzX9cSB2nQEZVXs8x6CzoZTdXcaipZJzgWDZ94aczNwvyFWnwQ4KdkeA1ii66umunSF1DHBIxJxwPg2Asahe9wNpcbjw%2B2vgFO%2FS2XP8Odkb8fesCCgs4C2gWHdZJDAlBzeMHYAqMeM7kRUchWtxSy5w6sAjxF5FOra91f1wTrHal3N9ICFZ81h7JPR8Xz%2Fz8y42zfhSB4d7vq5BkvWWxeRF3JRWKPpRcKEc7Y7aUH8HDUdGPi%2BgNcmb7bv%2F994hwE3YEjrJx2WlTcbgCD0KhYZxI6jznvkc5vT0kSxfzDBCgFIgrR5qy5V0E%2B%2FUatNLVcFy11mdB6msJ7SQsab7bf5G9h%2Bud1x0ngvcIWuBslA%2BY%2BA8NYTfyvCuEm0j9HKuqGrXWmi9OyjHnkjwxbXKv2GOOAs7Ir27DgIdB0%2F787Y8S0hqjYihrPAz1jE9ZMCMek9rAjVW%2BFsC0McwjrCX7biSJPUYSfIHs3kwyDOl4ut4FbktLmSxRyhbt%2BU0GgZJRSiqBmAnYRHtn29qO%2BDpmA6mtN2PrWKomRpzMJDtyVcRddJZAvkVx2shlvx%2FfDH%2B9wwR2zLp8OonFIABib0pMLv90skGOqUBmTZpoCc9obuTYOH2%2BamXJinFdpkV%2Fb15T8RkpIR9KV%2BPuGNgN%2BmTZc54IbB1KqGeVf4cQh9YEAYtTXhZ4NdjOBcZkSfMEcSU0jndZpGufrKnPads9qTcKKF%2BhCYo2b7Cqnv%2BVN5hLtxtD5EJPqFx%2BAQwU6J9uv0LSsD11wKuoe%2F6GWAlvIfBEHGjQ%2BpVF1mZUdvbvaaFRcHIrfBKcC%2FSWCqLblQV&X-Amz-Signature=9b43ceb6277e3be065336f8c5be7eedf8e8527badad3ee3098428ebd2966cddf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666XMG2ZLY%2F20251207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251207T012119Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDTvwjmyZp5RKNG%2BDrsWIHUS9cd5O9%2FqmXOhKKVxpVHQwIgbEKkvXAiTuMIRjrrhSR%2BlEI0%2FbjSP1rO9OD5P%2FkBgYYqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPp1KpD2uWBPvJxn1yrcA6691tt%2BrVnJuOuEe8uwaLh7PxpOhfAtYrlLepecfzX9cSB2nQEZVXs8x6CzoZTdXcaipZJzgWDZ94aczNwvyFWnwQ4KdkeA1ii66umunSF1DHBIxJxwPg2Asahe9wNpcbjw%2B2vgFO%2FS2XP8Odkb8fesCCgs4C2gWHdZJDAlBzeMHYAqMeM7kRUchWtxSy5w6sAjxF5FOra91f1wTrHal3N9ICFZ81h7JPR8Xz%2Fz8y42zfhSB4d7vq5BkvWWxeRF3JRWKPpRcKEc7Y7aUH8HDUdGPi%2BgNcmb7bv%2F994hwE3YEjrJx2WlTcbgCD0KhYZxI6jznvkc5vT0kSxfzDBCgFIgrR5qy5V0E%2B%2FUatNLVcFy11mdB6msJ7SQsab7bf5G9h%2Bud1x0ngvcIWuBslA%2BY%2BA8NYTfyvCuEm0j9HKuqGrXWmi9OyjHnkjwxbXKv2GOOAs7Ir27DgIdB0%2F787Y8S0hqjYihrPAz1jE9ZMCMek9rAjVW%2BFsC0McwjrCX7biSJPUYSfIHs3kwyDOl4ut4FbktLmSxRyhbt%2BU0GgZJRSiqBmAnYRHtn29qO%2BDpmA6mtN2PrWKomRpzMJDtyVcRddJZAvkVx2shlvx%2FfDH%2B9wwR2zLp8OonFIABib0pMLv90skGOqUBmTZpoCc9obuTYOH2%2BamXJinFdpkV%2Fb15T8RkpIR9KV%2BPuGNgN%2BmTZc54IbB1KqGeVf4cQh9YEAYtTXhZ4NdjOBcZkSfMEcSU0jndZpGufrKnPads9qTcKKF%2BhCYo2b7Cqnv%2BVN5hLtxtD5EJPqFx%2BAQwU6J9uv0LSsD11wKuoe%2F6GWAlvIfBEHGjQ%2BpVF1mZUdvbvaaFRcHIrfBKcC%2FSWCqLblQV&X-Amz-Signature=70ad9a2a26e6394051426788f2624d830dbb0ed5154a1e03bbafb0bab360a37e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







