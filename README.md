



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBVD7AL4%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T064321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCd0dYf4zsgdl7KntkHDqoejqHV1moHYkVtqgO9vejBrwIhAJI8hjrkRbdr3DRmH%2Bjcn06wDdKoCc5FmKE0qStxqJPPKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FNdWW45fMteOPVn8q3AM38v216yJI2CobaehdB1yeumooRheBXBBLvzkh5cjSGlOGTaxdeh0qTMfKF0JI1yO36slMbrSCIJMJ%2FSeZpjZoA5KPLY87C2t4cexkH9CQDEutMicNqB4kvd40LQq5fXJ2fdpKPoyClI4wGpjg1GrvQdhDp9%2B3DM08mNaE5JCTKJ%2B9HvWVuAqbEMASKplfzBksFldzMXnz0eaHk7XzG5nMkZ%2FCE940ieO1Cy2S8vnAuDCg6HUpWtyvdv3YyZqnDdlf8ryVVGuFBwDbfeYeLYp9DlwJxNsHkyFBpfdPYmzv1Nwz3ZManbXWP3M8Mj%2BGBguifrwlHRAQfR70U0dj6AXM2%2BlEs6Dnw7%2BL%2FZI%2FBwj0lVhxcpqA2toa67XF3%2BBaQFH2R05XZF2iet9d1Zwwd97aIxeFLNnajHmBmiqS%2FwgKX9cRGnRR2n3yTZDRaTi%2FX6U2a345FeHlDzxZyFx81Gbpkjy%2BCtAAEJyZx1EOe%2FW7o8ujvNyQh7dNDoaLvsyW35ItxP29sbAM6fAySrBKIKv21oKkJ3hZXwaHYr0Jh56YvwU9vTT6iwdWpgrij5RmONCJ6fkhhJsseJqqaQ6SWnMbfY1U%2Bd3ACxfE9eY%2F62BbX1Y1lSwnsHUxyg12yTDD4ZnNBjqkAQqI9ctxxZyRZjNymXyZKSOcDxPFfFoN5AVC8%2FN%2FHBob0ZgmD4CoTiKnq0IT1Y5fPRT035%2BzRIV1p3AWbq%2FU4WDMISSOF8B5%2BtLIuBRfVuIz5kneASTSv5CS8DDVwQpxaxJ2O3%2FT9ZHYsR4G4ehD8o%2Bd%2Ff1HlVHggpndUqluVV19pDL9KOmKC6ZHhXwOTHsVBNqr05wfwAfGLYj7UEq1XDeuNKBK&X-Amz-Signature=7ad70aa8b42706aab3f4e988a0d37940658c5605c5bd5d2da205d4b5feb11f89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBVD7AL4%2F20260303%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260303T064322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCd0dYf4zsgdl7KntkHDqoejqHV1moHYkVtqgO9vejBrwIhAJI8hjrkRbdr3DRmH%2Bjcn06wDdKoCc5FmKE0qStxqJPPKogECJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2FNdWW45fMteOPVn8q3AM38v216yJI2CobaehdB1yeumooRheBXBBLvzkh5cjSGlOGTaxdeh0qTMfKF0JI1yO36slMbrSCIJMJ%2FSeZpjZoA5KPLY87C2t4cexkH9CQDEutMicNqB4kvd40LQq5fXJ2fdpKPoyClI4wGpjg1GrvQdhDp9%2B3DM08mNaE5JCTKJ%2B9HvWVuAqbEMASKplfzBksFldzMXnz0eaHk7XzG5nMkZ%2FCE940ieO1Cy2S8vnAuDCg6HUpWtyvdv3YyZqnDdlf8ryVVGuFBwDbfeYeLYp9DlwJxNsHkyFBpfdPYmzv1Nwz3ZManbXWP3M8Mj%2BGBguifrwlHRAQfR70U0dj6AXM2%2BlEs6Dnw7%2BL%2FZI%2FBwj0lVhxcpqA2toa67XF3%2BBaQFH2R05XZF2iet9d1Zwwd97aIxeFLNnajHmBmiqS%2FwgKX9cRGnRR2n3yTZDRaTi%2FX6U2a345FeHlDzxZyFx81Gbpkjy%2BCtAAEJyZx1EOe%2FW7o8ujvNyQh7dNDoaLvsyW35ItxP29sbAM6fAySrBKIKv21oKkJ3hZXwaHYr0Jh56YvwU9vTT6iwdWpgrij5RmONCJ6fkhhJsseJqqaQ6SWnMbfY1U%2Bd3ACxfE9eY%2F62BbX1Y1lSwnsHUxyg12yTDD4ZnNBjqkAQqI9ctxxZyRZjNymXyZKSOcDxPFfFoN5AVC8%2FN%2FHBob0ZgmD4CoTiKnq0IT1Y5fPRT035%2BzRIV1p3AWbq%2FU4WDMISSOF8B5%2BtLIuBRfVuIz5kneASTSv5CS8DDVwQpxaxJ2O3%2FT9ZHYsR4G4ehD8o%2Bd%2Ff1HlVHggpndUqluVV19pDL9KOmKC6ZHhXwOTHsVBNqr05wfwAfGLYj7UEq1XDeuNKBK&X-Amz-Signature=6f4c6d10911e4618ebfeafffa5e4308eec2f4789cb8e7efe5647fd3e293d5b8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







