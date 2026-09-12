



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UHHTXWC%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T120956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIUtfxoC9VkcMYrhKDxYZtyZAcLTaCI1slJ0%2BaBLps6wIgaHO5IdAwmJJlTQuas4nXqo3oeZPI%2Fb564pN71i28uXAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFrq55WM%2FERbJB6qSrcA2RXw8s9g%2BilNyJl0zKmyVfhtuz55U13GENKyPdNd4u4eoQtAcKr0NuzcVCehLJs75DJU4I1X1IvZwBPSqWL2MYvUETlwR61Jvh9Xg7xw1k2yUvjcp6VkMmHdUAnsbTxJeqIHpKVY0dEdPQq40o%2BeIXBD4ZkpTXeJAkzm%2BNdQePQRvSkFSb%2FSv6MsmYsAf9cgc00c5LO%2FObLrhlEWlhce7UHGlPckoeoC77CA%2FbYikh7U6p1bOnpROAHWTF%2BZfX6jXnP4P1kq0p5hXihzWQK%2F8ERFVECRk%2FtpKawQy9FIhEKwWFpjpBUrNFjksOuqlL6rW1f8J2gm421Y4HEQ98XyNefqtvObFLt%2FF4VI7FqM2V2ynVAhj%2F3XKFrjHKl1tUgEv7zzwa4LsrS8aygpO9OauvajdTDD7VL6QqtJFvRjhrr0jWD9rfdCzSqB8hH16NFplK30y6Gmzae1N%2BoDw%2Fxm7X79Nn%2FdCc0i%2FBxsDNpyp0RpEmehPcMeH0mmUpOJg%2FxL11t5%2BDHPirbY7piPT2sH%2BOJGpytaFR7tXK58hVHbD6AqZ1fC%2B5%2BU1L97aU1nIhgoIsuplLNHGIsw2qw%2F%2BV%2Fzkqn3pn8tnBt5ReUyiyA6ng9%2BmcTpoDJu9xIxWM2MMjRlNUGOqUBRwdgFYJTtiojPWrkf5EsiPgABb%2ByyqTZPetE%2Fu%2FZesGFGYYxufADhob0apK2Wth9l5FkubLIb7JtNR%2BnJIFhm3ExnRVXs723mCCwF%2FGSgGFGU7T9C8%2BKYUxBr5E7Hmpzu%2Fo2TD%2FusxRIXHN8iDb6Iino7WoTR%2Brt2DMLF08fUKngoiSMGP8wE8DwdP936g21v2gewR0i8vVJ3zxzFMPRZwlRUM1O&X-Amz-Signature=80dfd7db57ea072b2ea25d7f18ad12435c1a558e7275d172b9cc6b3c0a1bb87e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UHHTXWC%2F20260912%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260912T120957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCIUtfxoC9VkcMYrhKDxYZtyZAcLTaCI1slJ0%2BaBLps6wIgaHO5IdAwmJJlTQuas4nXqo3oeZPI%2Fb564pN71i28uXAqiAQItP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGFrq55WM%2FERbJB6qSrcA2RXw8s9g%2BilNyJl0zKmyVfhtuz55U13GENKyPdNd4u4eoQtAcKr0NuzcVCehLJs75DJU4I1X1IvZwBPSqWL2MYvUETlwR61Jvh9Xg7xw1k2yUvjcp6VkMmHdUAnsbTxJeqIHpKVY0dEdPQq40o%2BeIXBD4ZkpTXeJAkzm%2BNdQePQRvSkFSb%2FSv6MsmYsAf9cgc00c5LO%2FObLrhlEWlhce7UHGlPckoeoC77CA%2FbYikh7U6p1bOnpROAHWTF%2BZfX6jXnP4P1kq0p5hXihzWQK%2F8ERFVECRk%2FtpKawQy9FIhEKwWFpjpBUrNFjksOuqlL6rW1f8J2gm421Y4HEQ98XyNefqtvObFLt%2FF4VI7FqM2V2ynVAhj%2F3XKFrjHKl1tUgEv7zzwa4LsrS8aygpO9OauvajdTDD7VL6QqtJFvRjhrr0jWD9rfdCzSqB8hH16NFplK30y6Gmzae1N%2BoDw%2Fxm7X79Nn%2FdCc0i%2FBxsDNpyp0RpEmehPcMeH0mmUpOJg%2FxL11t5%2BDHPirbY7piPT2sH%2BOJGpytaFR7tXK58hVHbD6AqZ1fC%2B5%2BU1L97aU1nIhgoIsuplLNHGIsw2qw%2F%2BV%2Fzkqn3pn8tnBt5ReUyiyA6ng9%2BmcTpoDJu9xIxWM2MMjRlNUGOqUBRwdgFYJTtiojPWrkf5EsiPgABb%2ByyqTZPetE%2Fu%2FZesGFGYYxufADhob0apK2Wth9l5FkubLIb7JtNR%2BnJIFhm3ExnRVXs723mCCwF%2FGSgGFGU7T9C8%2BKYUxBr5E7Hmpzu%2Fo2TD%2FusxRIXHN8iDb6Iino7WoTR%2Brt2DMLF08fUKngoiSMGP8wE8DwdP936g21v2gewR0i8vVJ3zxzFMPRZwlRUM1O&X-Amz-Signature=c617abfd0d697736c3f790360dc3c300d4c6e55018dcbb522bcc042fb2f8936a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







