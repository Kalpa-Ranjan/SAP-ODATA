



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R36UUAO5%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T182706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJGMEQCIFED%2FBHIgRMPQ%2B0AB%2BoN9wz0X6RbgN%2F3N9tDYUVDEEfZAiAAh6W3mEusdzHrs%2BZguYQL00PbD4djgB4oqCCVR9XBMyr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMXX%2FZplNhTPXcimaOKtwDI47xWK1TaXXxENggz4EV4DoKKadNoc7qAbKDXJoWtrCWfANsoCQ1zpS9LrEPPfkPPnMZ06TZOkaFc2JA6MkXBpk1D5W%2F0dQFdz4zRPKcosmX%2Fo%2Bl%2FeYsyXg2stIZr4iSL4W5lGV0Oj8rptGxxinWSrUjFqD%2F3Foj5G9PWyvxQD15JM2E4qzUd9OmlVC3mbb7LXJJIY6MjqMJeU32NxJCQIv1MlI1f%2BICoG0NAIs5foTqIx8%2BlTIMtzO%2ByO5h9O3HgZtSnltv7n9ZdypOmYx0Ln2g%2B1qzqUwCICwiLQF2NkDDU3aeq0dqnDvMkVDBaaJy%2BdG1BtihZ%2F3IkPr2H6SZbvYzecuby6mCTY4nn13JWN9FQ%2FUovh7kObfH8FbFy93MOT9buhz5Vg%2B86DSQB0iXDmGQQWf3ty%2Fox0PXAm0eEBV3ivCl25guV5ER7TlIaylr%2BaUxc989kcUZZK4FuBG%2BHBk5N12PSDW8EtrUFP76osljOrJJ82sRiw4My5vx%2FYAx8OSLROuTKdO4n83NEKguI0ign89EOdK2r8KjfiRyWT6AderfxLPND2k5o2eRLYCMCSdT%2FnnD8aiR5Ilax%2BIWDIGHFHpLu2Y81o6MTOhwahiPH16o66iLD88fnUUw%2Bdi2zQY6pgGa4b6TMYHB0saiuhONX%2BVzvyvNIv8PJejHxc0MUMXxKjPNocwe3qI0cjusPmU3Q5tXXZ63jxYJnFe2BudLde5RpQfmrRJjpLGAqEP08HV0JcihNQJwuzFzQoRl47Z5%2FYL0dUwniJ2XEw%2FXwPMQ3svkP92tqQuJk6OdSdVdZtOyuLzv2S6MNrcYMWYqx%2BxAkhMv5Tp9y%2FN8rHvAlJYH4qJyOB5fpu5G&X-Amz-Signature=a2fe190f7416547c092239e926d4a98f8446f6b6fff732fc259a52ce94496083&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R36UUAO5%2F20260308%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260308T182706Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFEaCXVzLXdlc3QtMiJGMEQCIFED%2FBHIgRMPQ%2B0AB%2BoN9wz0X6RbgN%2F3N9tDYUVDEEfZAiAAh6W3mEusdzHrs%2BZguYQL00PbD4djgB4oqCCVR9XBMyr%2FAwgaEAAaDDYzNzQyMzE4MzgwNSIMXX%2FZplNhTPXcimaOKtwDI47xWK1TaXXxENggz4EV4DoKKadNoc7qAbKDXJoWtrCWfANsoCQ1zpS9LrEPPfkPPnMZ06TZOkaFc2JA6MkXBpk1D5W%2F0dQFdz4zRPKcosmX%2Fo%2Bl%2FeYsyXg2stIZr4iSL4W5lGV0Oj8rptGxxinWSrUjFqD%2F3Foj5G9PWyvxQD15JM2E4qzUd9OmlVC3mbb7LXJJIY6MjqMJeU32NxJCQIv1MlI1f%2BICoG0NAIs5foTqIx8%2BlTIMtzO%2ByO5h9O3HgZtSnltv7n9ZdypOmYx0Ln2g%2B1qzqUwCICwiLQF2NkDDU3aeq0dqnDvMkVDBaaJy%2BdG1BtihZ%2F3IkPr2H6SZbvYzecuby6mCTY4nn13JWN9FQ%2FUovh7kObfH8FbFy93MOT9buhz5Vg%2B86DSQB0iXDmGQQWf3ty%2Fox0PXAm0eEBV3ivCl25guV5ER7TlIaylr%2BaUxc989kcUZZK4FuBG%2BHBk5N12PSDW8EtrUFP76osljOrJJ82sRiw4My5vx%2FYAx8OSLROuTKdO4n83NEKguI0ign89EOdK2r8KjfiRyWT6AderfxLPND2k5o2eRLYCMCSdT%2FnnD8aiR5Ilax%2BIWDIGHFHpLu2Y81o6MTOhwahiPH16o66iLD88fnUUw%2Bdi2zQY6pgGa4b6TMYHB0saiuhONX%2BVzvyvNIv8PJejHxc0MUMXxKjPNocwe3qI0cjusPmU3Q5tXXZ63jxYJnFe2BudLde5RpQfmrRJjpLGAqEP08HV0JcihNQJwuzFzQoRl47Z5%2FYL0dUwniJ2XEw%2FXwPMQ3svkP92tqQuJk6OdSdVdZtOyuLzv2S6MNrcYMWYqx%2BxAkhMv5Tp9y%2FN8rHvAlJYH4qJyOB5fpu5G&X-Amz-Signature=778957b45fb03cde9d77f4cbd9da94bd9405832905b42eb4c5f14d23cbed8c77&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







