



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVOXAO4N%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T123817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRCs%2FnMiwao2%2BRwg%2FFh6xlzot4d63MpIyFcjrtdJfH0gIhAKydGIeDUa946B5w%2FD7z%2FHpJJpv5vvjko3EhOf5vQ5VfKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwHNJRdNDJgnA61Wkq3AMZqXObMGY8byDlY815IHmc%2BFjSE71BOrcU24J9H9MnP9X1Dihr24%2ByI5Ki%2FX91BO%2FkZO6DgfJaXkbkIHCecY1dpgDpgWwxurz%2BHqXYmnKA2qZrL%2Fk99BcqkZawwvxhafqvfs1gPkteIN%2F7pDJo5n6%2BQsbg94RuH0Oa2e6ZzY%2Bwk0kwwjQUTHoBY8wNjSj0MGeVfTCvQbei4u%2FQ0AfgdDfAdGim%2FELrz4U7raAXMTJo9oBt4qF%2FG%2F8tXFqqPXnM6AphsoE%2F32s849WItuyilQEV8q6C8qq7noROB2X0KJOc0JGocoqVEp8qi9rKEIJ7mDA8sekACZBSCUcCO8a0QRUU4dO2tmQO5J%2F3%2FoUC7%2FAssgkCQamPQV2tZtL2LNmK9Yt92PzWxXPVQDg1Q0G1whMh%2BXKeE4WjGHWKXRQbBHKjB1pQRmStJFevQ63BitmxkbOLd4Y4W73BQG8srIbkE9xvY8l13PNqEUTova30wDo1Hkon87sVw8lCJawM8FLaiy6Q0n7WAQ6cqRB1cQGtGcHvbmAQQonIUdO8kOweWlT8nHEPVxzZuDNN6FRMLOb67bIGCdFPIijQ5CRu3ZssOlIfZIxLj1L0wssNP7FXqnPW6vqAF46iuJholF043zDJouHTBjqkAd8pPxMZmmyUenJe6X9Atgy4nQV99jiGJAdMJbOxnn6zfazRUaAKZVYGTAkNGHrUMXC06YS4JFQNWrmVrQ2r2idh7SgVPKoIeswiChO91eqr%2FGqKybyNt2fCLwKUJ8JrEPN8noIgXsJnwlAPxcSGcufEyCj1knZvthlI5Vf4%2FHFLeCLujTsmW0IEZnGfG74M0piIZF0YfeVd2ZiRyUih2Ss97SFH&X-Amz-Signature=7ed5bafed46d4e8cb6b11116b56b54025a4c2a718a4f91bb493da7f251b33713&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVOXAO4N%2F20260809%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260809T123817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRCs%2FnMiwao2%2BRwg%2FFh6xlzot4d63MpIyFcjrtdJfH0gIhAKydGIeDUa946B5w%2FD7z%2FHpJJpv5vvjko3EhOf5vQ5VfKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwHNJRdNDJgnA61Wkq3AMZqXObMGY8byDlY815IHmc%2BFjSE71BOrcU24J9H9MnP9X1Dihr24%2ByI5Ki%2FX91BO%2FkZO6DgfJaXkbkIHCecY1dpgDpgWwxurz%2BHqXYmnKA2qZrL%2Fk99BcqkZawwvxhafqvfs1gPkteIN%2F7pDJo5n6%2BQsbg94RuH0Oa2e6ZzY%2Bwk0kwwjQUTHoBY8wNjSj0MGeVfTCvQbei4u%2FQ0AfgdDfAdGim%2FELrz4U7raAXMTJo9oBt4qF%2FG%2F8tXFqqPXnM6AphsoE%2F32s849WItuyilQEV8q6C8qq7noROB2X0KJOc0JGocoqVEp8qi9rKEIJ7mDA8sekACZBSCUcCO8a0QRUU4dO2tmQO5J%2F3%2FoUC7%2FAssgkCQamPQV2tZtL2LNmK9Yt92PzWxXPVQDg1Q0G1whMh%2BXKeE4WjGHWKXRQbBHKjB1pQRmStJFevQ63BitmxkbOLd4Y4W73BQG8srIbkE9xvY8l13PNqEUTova30wDo1Hkon87sVw8lCJawM8FLaiy6Q0n7WAQ6cqRB1cQGtGcHvbmAQQonIUdO8kOweWlT8nHEPVxzZuDNN6FRMLOb67bIGCdFPIijQ5CRu3ZssOlIfZIxLj1L0wssNP7FXqnPW6vqAF46iuJholF043zDJouHTBjqkAd8pPxMZmmyUenJe6X9Atgy4nQV99jiGJAdMJbOxnn6zfazRUaAKZVYGTAkNGHrUMXC06YS4JFQNWrmVrQ2r2idh7SgVPKoIeswiChO91eqr%2FGqKybyNt2fCLwKUJ8JrEPN8noIgXsJnwlAPxcSGcufEyCj1knZvthlI5Vf4%2FHFLeCLujTsmW0IEZnGfG74M0piIZF0YfeVd2ZiRyUih2Ss97SFH&X-Amz-Signature=4be3ab1f5a29596029fe59c024d5fdd9cbf4b97d94cd714cfad4393171d7ab52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







