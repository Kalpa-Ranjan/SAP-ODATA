



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEJT3WLN%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIEbF2gmBhY41H%2FrBxPZh1GaD5IUWMoBwAmwOfyYh8XkqAiAYyg9xgnerku4tSTYNx7yF8RvVe15VxbnVNv%2FpYkOCIyr%2FAwgPEAAaDDYzNzQyMzE4MzgwNSIM320D%2FmBbnWfQFWl0KtwDMC%2Fu%2Bl%2FVmeHskSy5ztqbdUY0YYX0YpDeRDsai1BBqkZKWlyG%2FL94RzdGr6S8kB7CtwHjZD23mpmZ046IjuKcBilWlov2afJbZuhmDIgJRJlGpgGel6tFP1tc8mkglcjqtrYah%2F207nEHuN8d6Bs433TOTpDd67BoTZECr0eJG%2FTZZag7F4WoKN8iqcv%2F%2B%2F0OhryK%2Fhgr5dFGdf69aN3ZH4juBLxpin7VYNJPSAP6vtX%2B5GzcvoXXOF49DA6TaiH7FxP%2FYblwDEiD35Ty%2BL59bJgL6HL7KphAD4VcIPO0fzsj%2FlOKTY8jg2l19j5YVt503frkRqa2lbuq9hHcOtEOF%2BUya866N5uMena%2BMwjpzNpbhoWmAMjiExy5mw7suG5KS%2Bz1%2FEEDF9jHQfP9nlvyEtd8Gu1Xu5EJM%2Bt%2BIBur0Nc22a0jWN3t645ByulLmdCn2IG0rLPshWvV%2FZAUsLxIkU%2F8qLl2DLBKYZRLcy3A72My5jjDx3VLfQDH5xgNVe66kitAqVcx2KF8CE%2BAu5JJB8kADIV065YXpgLCduuyi7lREYGuyAk2bPHeZeCBvU444WmhwIRqhpm6l2E59AcabrcGT1Qu79Fj3dlkHGhmUE6%2Fo3DBwEIyfP30cAkw%2BIO6yQY6pgHkmf6kZQdxNOpj%2FjL9Ckjton%2FBJ%2FpJ54DRpftqjgReltEb3P1TLAprCxT646sdsQKNLC5QhojTZG6VXKk7yj9zdSMikRdhzPmz0P8ko3lEijzYPVrBh9DyG5gDYYpSuvdTvC8dEJEK3i4DovifxDxNM0LJy8NcltWcYkDjqULvPVVd%2FPNbQzMMolds142GrzceL6QuMzGoUpWJoN%2FdiARpghKpSpIy&X-Amz-Signature=525b1876320bfe7514371bf0b13298503d498f01c383ae3f24aa0039999090d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEJT3WLN%2F20251202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251202T062606Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJGMEQCIEbF2gmBhY41H%2FrBxPZh1GaD5IUWMoBwAmwOfyYh8XkqAiAYyg9xgnerku4tSTYNx7yF8RvVe15VxbnVNv%2FpYkOCIyr%2FAwgPEAAaDDYzNzQyMzE4MzgwNSIM320D%2FmBbnWfQFWl0KtwDMC%2Fu%2Bl%2FVmeHskSy5ztqbdUY0YYX0YpDeRDsai1BBqkZKWlyG%2FL94RzdGr6S8kB7CtwHjZD23mpmZ046IjuKcBilWlov2afJbZuhmDIgJRJlGpgGel6tFP1tc8mkglcjqtrYah%2F207nEHuN8d6Bs433TOTpDd67BoTZECr0eJG%2FTZZag7F4WoKN8iqcv%2F%2B%2F0OhryK%2Fhgr5dFGdf69aN3ZH4juBLxpin7VYNJPSAP6vtX%2B5GzcvoXXOF49DA6TaiH7FxP%2FYblwDEiD35Ty%2BL59bJgL6HL7KphAD4VcIPO0fzsj%2FlOKTY8jg2l19j5YVt503frkRqa2lbuq9hHcOtEOF%2BUya866N5uMena%2BMwjpzNpbhoWmAMjiExy5mw7suG5KS%2Bz1%2FEEDF9jHQfP9nlvyEtd8Gu1Xu5EJM%2Bt%2BIBur0Nc22a0jWN3t645ByulLmdCn2IG0rLPshWvV%2FZAUsLxIkU%2F8qLl2DLBKYZRLcy3A72My5jjDx3VLfQDH5xgNVe66kitAqVcx2KF8CE%2BAu5JJB8kADIV065YXpgLCduuyi7lREYGuyAk2bPHeZeCBvU444WmhwIRqhpm6l2E59AcabrcGT1Qu79Fj3dlkHGhmUE6%2Fo3DBwEIyfP30cAkw%2BIO6yQY6pgHkmf6kZQdxNOpj%2FjL9Ckjton%2FBJ%2FpJ54DRpftqjgReltEb3P1TLAprCxT646sdsQKNLC5QhojTZG6VXKk7yj9zdSMikRdhzPmz0P8ko3lEijzYPVrBh9DyG5gDYYpSuvdTvC8dEJEK3i4DovifxDxNM0LJy8NcltWcYkDjqULvPVVd%2FPNbQzMMolds142GrzceL6QuMzGoUpWJoN%2FdiARpghKpSpIy&X-Amz-Signature=d8009aa6655f74e2fc6e9b97483ad79d0001ab38a6ce3735c30284c03ef5649c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







