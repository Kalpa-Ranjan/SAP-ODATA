



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CYLVHIY%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T182443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9Lg78W7BEXzhyzK31VdQS4uSdZFzQGH2N5jmji2fMGAiBVR4Li9V19uXqbMe%2F7QaFFf7kkb2172UrJ2UcPoeNQVyqIBAi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbhbdyvuG8ODl8rMKtwDmNXv%2FqQl5tx7PTGa82rQKejoNMvC0kOIuJ00ncXyqrQE0snDVf9dVkRG%2BGDEqiascswto4Lc5OPZaWYd9kZLxaylUKNX9buKR%2F5jJZxrBKkTndmT%2ByEH7KYrtuueR1BLoi%2FULzmAUNWIH%2FA5YMaGkefoFLLAQ78SsGUkDMCX7iSm3zaj%2F3kc4epCRdnDVgo0N1bTSWs31R5GUupAq3O08AmhL3kpl8fC0LKrFO4RFu2ZFxpp3wX8vWctKVGJi0k8UVtmBvuYeqq0IyGANGLrv1DjdVqHMZqVViNu02xwDJ4m9rlxTqC9HUN7icZuMp5QS5HEW0%2BfpA21q04efXWpM%2BkMh6pq2S2Av7ArwU50mRtU53V%2BhQOVyb12HhuFEO2rZZZB9thP3YKJUt3qU68BkDgQ%2BOY0MiL7448LsmmEUKDz3lNKPWlFFo8WTi8zc9zot8R1Gks4HB3OnF01ZyYTveb27BseYBerunRod5ePR8oJ7RmZfEtEGnVudKFvhDY%2FZh7nGVW6ubixbwcHNXzmHiQ3a%2B2AzdxjCcMtheLFjKQxKU69spYDhoWM5lw0srPuso8H%2F%2BOl0ytxP1HFHsu%2Bz5BCv9H2JTTswTyiVE0d59cCUl9I1JynxYEF1iMw%2Ffr3ywY6pgGWARH38ECvtC9%2FvMTthnVMX72t78YuXzCjd0Xg371cnjZpwcKVDyBaCD6iU0nbuiIZGP4jUzzqM6ac4ORL0HLq1RPWKuUPTsORgnfjWTJW8LxLzIEECDitbMops6O6u2Nf4T088zaYroGQaUueyILfICc2yxHoeYhS5Xf1Dq8c8kUot1yUaZN3UpWsuaK2PoYswIwZ36PaddkeZT7wh%2BPiFRe8cBHJ&X-Amz-Signature=90eb15ea72ade29cc78e6806398f987446b6ec9e30ae979c5aa78821e959633c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666CYLVHIY%2F20260131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260131T182443Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF9Lg78W7BEXzhyzK31VdQS4uSdZFzQGH2N5jmji2fMGAiBVR4Li9V19uXqbMe%2F7QaFFf7kkb2172UrJ2UcPoeNQVyqIBAi2%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjbhbdyvuG8ODl8rMKtwDmNXv%2FqQl5tx7PTGa82rQKejoNMvC0kOIuJ00ncXyqrQE0snDVf9dVkRG%2BGDEqiascswto4Lc5OPZaWYd9kZLxaylUKNX9buKR%2F5jJZxrBKkTndmT%2ByEH7KYrtuueR1BLoi%2FULzmAUNWIH%2FA5YMaGkefoFLLAQ78SsGUkDMCX7iSm3zaj%2F3kc4epCRdnDVgo0N1bTSWs31R5GUupAq3O08AmhL3kpl8fC0LKrFO4RFu2ZFxpp3wX8vWctKVGJi0k8UVtmBvuYeqq0IyGANGLrv1DjdVqHMZqVViNu02xwDJ4m9rlxTqC9HUN7icZuMp5QS5HEW0%2BfpA21q04efXWpM%2BkMh6pq2S2Av7ArwU50mRtU53V%2BhQOVyb12HhuFEO2rZZZB9thP3YKJUt3qU68BkDgQ%2BOY0MiL7448LsmmEUKDz3lNKPWlFFo8WTi8zc9zot8R1Gks4HB3OnF01ZyYTveb27BseYBerunRod5ePR8oJ7RmZfEtEGnVudKFvhDY%2FZh7nGVW6ubixbwcHNXzmHiQ3a%2B2AzdxjCcMtheLFjKQxKU69spYDhoWM5lw0srPuso8H%2F%2BOl0ytxP1HFHsu%2Bz5BCv9H2JTTswTyiVE0d59cCUl9I1JynxYEF1iMw%2Ffr3ywY6pgGWARH38ECvtC9%2FvMTthnVMX72t78YuXzCjd0Xg371cnjZpwcKVDyBaCD6iU0nbuiIZGP4jUzzqM6ac4ORL0HLq1RPWKuUPTsORgnfjWTJW8LxLzIEECDitbMops6O6u2Nf4T088zaYroGQaUueyILfICc2yxHoeYhS5Xf1Dq8c8kUot1yUaZN3UpWsuaK2PoYswIwZ36PaddkeZT7wh%2BPiFRe8cBHJ&X-Amz-Signature=b94cb3f60c5460497a5eb73f6f2a3e195d28947a3679c8d7254758eccfd81079&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







