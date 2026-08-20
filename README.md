



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XTUDU7A%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T183014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDORFArOQbQZJW0suRYg7qDP4ZD%2FRs5ZX1%2FoKCMur7pPgIhAOVYewv4hgvKFQfqXMzgT80BuLDR5o%2FijpMJ3C%2FZ2WOWKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHX9DZyOdGGFNK2Yq3AOuVzu3uys8wWPHbvn%2F8Do5uhESScmTyWhB%2FCscx5wnM92L%2FCwbiUXO29syGm0QNr6Lw%2B%2BP7HNQemYgwlLSYniQzF4IFJQ7fyYMpBXLjCJizzgfYzaYAU6x9KGKUJ7apMC1ldrwV707k6D0%2ByX25H3wz5JRJ0cFkUbmqHVCsUYdxcioIIyQkVkksIwNzZpUfCrYSnOGMytHLMaMvDvUnKZGy1MF1W6AtbUqphmR%2Fb8lyZ4WKB4Gw7FAvTPYTRKhoduvMq2qLkqpU7%2BkFf9MrfW1oFui9By6%2Bmgk08fpW50GDsGOv55Pnzxa77CRR0YmmmO6wn71gRa7TMQbw1eSmyuq2RnZbxQWqjYmv4JhVvLvIs7j1Z3CrBE33l0WmHIOPhs1dGNHwOoZtY2ENPXB7b2H5%2BGThinzLNI3vzGL0%2BZ9eW6KhwxxCwRZrx4zNLnhBjKQABv7X%2FN%2FPgLBfhoFUJVWofjTRwoz6YDTv%2FXdJs37%2BFdHRRmv69USKRuty588XlR2p7qXtoWh1z0TQUMbNTFjTp8G6vzPMn1F9BKxsEU%2FuIG1GvjW%2B3b1Vwk1JPQ%2Bni3d%2FGGlITKTzpgeB5BmiggkfQP7wSrW6ALLi1XPTAby032RNEzu8n9DdCKQ9zCp55zUBjqkATmG7KzE0JSyXP5RJhI5HqTQCqEaybbQActBHRD4gKLbAxgMNk558%2BZ6WbolEHPuzBRnBmnUA0ibJ%2BdTsqK7HLvNU20Du7xxU%2Bw2V5gYYeyRwoGa6OwEpv77S8zaEaiM4E7%2FBm1s4wJyIPahy2RlVmeuTFKg0EBl6FpmjV%2FGonJyZFReKSLWV5Hf2XMWUy342x%2FChnWV%2BSLH3AF%2B%2FlxJIWm9Ibmg&X-Amz-Signature=bdfdec245dad05312b1f2520a7d7d2c73b0acf5222ce2085bc6e59155ec5864d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XTUDU7A%2F20260820%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260820T183014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDORFArOQbQZJW0suRYg7qDP4ZD%2FRs5ZX1%2FoKCMur7pPgIhAOVYewv4hgvKFQfqXMzgT80BuLDR5o%2FijpMJ3C%2FZ2WOWKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzwHX9DZyOdGGFNK2Yq3AOuVzu3uys8wWPHbvn%2F8Do5uhESScmTyWhB%2FCscx5wnM92L%2FCwbiUXO29syGm0QNr6Lw%2B%2BP7HNQemYgwlLSYniQzF4IFJQ7fyYMpBXLjCJizzgfYzaYAU6x9KGKUJ7apMC1ldrwV707k6D0%2ByX25H3wz5JRJ0cFkUbmqHVCsUYdxcioIIyQkVkksIwNzZpUfCrYSnOGMytHLMaMvDvUnKZGy1MF1W6AtbUqphmR%2Fb8lyZ4WKB4Gw7FAvTPYTRKhoduvMq2qLkqpU7%2BkFf9MrfW1oFui9By6%2Bmgk08fpW50GDsGOv55Pnzxa77CRR0YmmmO6wn71gRa7TMQbw1eSmyuq2RnZbxQWqjYmv4JhVvLvIs7j1Z3CrBE33l0WmHIOPhs1dGNHwOoZtY2ENPXB7b2H5%2BGThinzLNI3vzGL0%2BZ9eW6KhwxxCwRZrx4zNLnhBjKQABv7X%2FN%2FPgLBfhoFUJVWofjTRwoz6YDTv%2FXdJs37%2BFdHRRmv69USKRuty588XlR2p7qXtoWh1z0TQUMbNTFjTp8G6vzPMn1F9BKxsEU%2FuIG1GvjW%2B3b1Vwk1JPQ%2Bni3d%2FGGlITKTzpgeB5BmiggkfQP7wSrW6ALLi1XPTAby032RNEzu8n9DdCKQ9zCp55zUBjqkATmG7KzE0JSyXP5RJhI5HqTQCqEaybbQActBHRD4gKLbAxgMNk558%2BZ6WbolEHPuzBRnBmnUA0ibJ%2BdTsqK7HLvNU20Du7xxU%2Bw2V5gYYeyRwoGa6OwEpv77S8zaEaiM4E7%2FBm1s4wJyIPahy2RlVmeuTFKg0EBl6FpmjV%2FGonJyZFReKSLWV5Hf2XMWUy342x%2FChnWV%2BSLH3AF%2B%2FlxJIWm9Ibmg&X-Amz-Signature=2b78679bf5e881c8033ef3ec53439345b8252557b25a8670762719404e73031e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







