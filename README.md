



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJNVZRS%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T185933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQClFfKkOV2EOYLqBl%2BSeEoAEi9cfLQVcg0%2FUvrEB4FKfQIhANHj%2F0XyV%2B0mdxtB85vwwZ4dBklVZGOiZKe9rSlB6VZ%2BKv8DCCMQABoMNjM3NDIzMTgzODA1IgyYDZgKK6gpxfnN54cq3AMlbBVKL%2BMrnocaLUU1aqYlyjKCB9Y3KKy1kcpqzoMzzv87Xwtf1cmjxFD5yh6Ce6uExog33h1M7SxkpaSIE4gm8OvuiTC5VI5S94%2FAO1ftRuxo%2B3kzY%2BPuf0ZsGYib8iR3Ar3iuSvd79Xue2QR4MKWsrFYBUxM7WlgHuVZpeUT%2F%2FE0CEDy04yATcmTjytauETCz%2F0ANRHJZOeK29ZaLnZgxfUhacHlHPvRlo3zs%2Ffbe1ZBiDnb%2FtULhsFB958PQQPNdcX8ubtaT0%2BPMdwUSkYotNh1tGcs8rMRWycp9kzwTa7nslvH316sj5VGaqizvOn9XIG%2F%2FAYSOI6Y%2Fda0pLJnEB2ecR6ur8L0yS3Tx5ph%2F0JzowvFda2a%2BS47dKaG4qlQoA0gqztVIGdh5XPN1YEvWXwsXYzh%2BBd7lIyU9cKp4sUb40li8rYfFaeUye8ifXhxg1rGU22TzOjelOXNG9yNT4FpTW0qw1vbFPLaPeKT0bzCUNkTCB2%2Ft9EtXbVZ3mznVov0LHKrSn89ij1ptzGejq5YKRxqEWEAzDTIw8WCMF692ISrMBW1cmsGNPo3DhCtrW4Qtkv69m7VD8WIPAQL8pr5LaJ1JVYv0K2QWmkc%2FtIgmApcmf6ITZ%2FhqDCU85PTBjqkAWqm%2FoID%2BAsSVci97VQbJq9xGvethuk6u2KXECHN4yspDQynF1YAsnZO0NPOW0m1LMNof2T2robGUJtyUc9U25hU2uWJUWXMImKm%2FdjUjCLWm5T3Cg3kNpOW79fw8QsHyZDae5ibTSgURanhSfaH%2FV5oqT0vvhqOOeO9JJC8jg0GA5CeS6XH70cU8Hx1fxqPI3zCT1cWBa9oCAX01dJkO%2B9H9Tpl&X-Amz-Signature=1f6e177ec0f8d2f7c0c267cd350221d6f7d9668805ad089559e8ab7232088aef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TOJNVZRS%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T185933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJIMEYCIQClFfKkOV2EOYLqBl%2BSeEoAEi9cfLQVcg0%2FUvrEB4FKfQIhANHj%2F0XyV%2B0mdxtB85vwwZ4dBklVZGOiZKe9rSlB6VZ%2BKv8DCCMQABoMNjM3NDIzMTgzODA1IgyYDZgKK6gpxfnN54cq3AMlbBVKL%2BMrnocaLUU1aqYlyjKCB9Y3KKy1kcpqzoMzzv87Xwtf1cmjxFD5yh6Ce6uExog33h1M7SxkpaSIE4gm8OvuiTC5VI5S94%2FAO1ftRuxo%2B3kzY%2BPuf0ZsGYib8iR3Ar3iuSvd79Xue2QR4MKWsrFYBUxM7WlgHuVZpeUT%2F%2FE0CEDy04yATcmTjytauETCz%2F0ANRHJZOeK29ZaLnZgxfUhacHlHPvRlo3zs%2Ffbe1ZBiDnb%2FtULhsFB958PQQPNdcX8ubtaT0%2BPMdwUSkYotNh1tGcs8rMRWycp9kzwTa7nslvH316sj5VGaqizvOn9XIG%2F%2FAYSOI6Y%2Fda0pLJnEB2ecR6ur8L0yS3Tx5ph%2F0JzowvFda2a%2BS47dKaG4qlQoA0gqztVIGdh5XPN1YEvWXwsXYzh%2BBd7lIyU9cKp4sUb40li8rYfFaeUye8ifXhxg1rGU22TzOjelOXNG9yNT4FpTW0qw1vbFPLaPeKT0bzCUNkTCB2%2Ft9EtXbVZ3mznVov0LHKrSn89ij1ptzGejq5YKRxqEWEAzDTIw8WCMF692ISrMBW1cmsGNPo3DhCtrW4Qtkv69m7VD8WIPAQL8pr5LaJ1JVYv0K2QWmkc%2FtIgmApcmf6ITZ%2FhqDCU85PTBjqkAWqm%2FoID%2BAsSVci97VQbJq9xGvethuk6u2KXECHN4yspDQynF1YAsnZO0NPOW0m1LMNof2T2robGUJtyUc9U25hU2uWJUWXMImKm%2FdjUjCLWm5T3Cg3kNpOW79fw8QsHyZDae5ibTSgURanhSfaH%2FV5oqT0vvhqOOeO9JJC8jg0GA5CeS6XH70cU8Hx1fxqPI3zCT1cWBa9oCAX01dJkO%2B9H9Tpl&X-Amz-Signature=4ae4cf9b40474bb693ab7c3be22396791be17d08c56e30b20dd006489fbe4d82&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







