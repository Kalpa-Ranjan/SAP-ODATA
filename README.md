



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAJMQEQ5%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T122608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCIFi4xYWUmYfoHO81IjNnNkqqAv4Dscm6b%2FBKzOhzUWy0AiAdyHr79%2FsAeglHUMx5CTke%2FN1YudsLuj3%2BQeaFdo%2BLhir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMFxFXwo65zbQPxBHrKtwDCqjhWNwxzdvFCiDa029QfSWppk6i1hpU%2BEQKj%2FkldKLszdCL3v3zT7CsiBLCvJJmfzopm4NPgTVcp616UMOb4yNhUbkXriTuEFIvXoPUIIS%2FqXhxqC4MM4jO5sCXBDqpwKaBMpjLGWa1kaMnDhr5F3QE4G6L4Tmt7AESmUJkXK1daNplo3c9Bk0RBShKZ75kaTvA%2FEB7ZyhsTRlupkHgcg8vSkeZ90GiOo76rW%2BtB%2F5HibLwW4umZl4r%2BYvbIlM1UqYgsQuMQvF8LFnJOByY9aAZBq3WSOQx4GIKTmdb7eS8sS2%2BxlSr0ErAldprcCUI7QHfHMIc4t9PEpJAsQ8%2FGqHD4RChZfebLCFM0tXTIA6iSe52zWgCGFReOyKL43GCcLeRwUSgxZhAWS5QUk6xqA5FxI1b%2FAA4gLIeVGX6ITRlTHnb%2FbvDEPgSlcGfiFExQG8zRdg5XzjdfLc9rKeOi%2BxFalZhnZpp7zub%2F51gxPgTVvyf7u8hw8orITZab1jLZQ8ttY7q%2Fii8KchDBMk%2B3obZuLP%2B%2BtcWe4B6Kr9VA0secAKTZ4LSbhTdhxSq7l3vE0RzIXXGYZRLp7nOffXCyHBdebg6zLVwo1eVNfmu4vg8fNkft3rFBnKdzV4w0ZqB1AY6pgFX8G6udXFN4N6JWpx%2Fx4m%2F6NhpkF9lFPwk0bhqzXbcYkQkZbU7630Ovtl5DYKS8sIqeQqA9rQStD9AvaX79V028D0cjms9Tqa%2Fh9CnO%2Bl0Nz%2Bd4N09RY0yf0jEZDm%2FmzZ5sx12Vv6CwkFd8OOc6le6WUfFlwpT6hVOoMifc5HlY%2BUEX3JOCQjDD%2B9URMjwloq%2BS642srnRHcQ3S%2FTftOUJ1Pb%2FdccA&X-Amz-Signature=4c1ba43237a1c49d83b87773357ab959f3233c57c78abe007759827734dfdf78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAJMQEQ5%2F20260815%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260815T122608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEwaCXVzLXdlc3QtMiJGMEQCIFi4xYWUmYfoHO81IjNnNkqqAv4Dscm6b%2FBKzOhzUWy0AiAdyHr79%2FsAeglHUMx5CTke%2FN1YudsLuj3%2BQeaFdo%2BLhir%2FAwgVEAAaDDYzNzQyMzE4MzgwNSIMFxFXwo65zbQPxBHrKtwDCqjhWNwxzdvFCiDa029QfSWppk6i1hpU%2BEQKj%2FkldKLszdCL3v3zT7CsiBLCvJJmfzopm4NPgTVcp616UMOb4yNhUbkXriTuEFIvXoPUIIS%2FqXhxqC4MM4jO5sCXBDqpwKaBMpjLGWa1kaMnDhr5F3QE4G6L4Tmt7AESmUJkXK1daNplo3c9Bk0RBShKZ75kaTvA%2FEB7ZyhsTRlupkHgcg8vSkeZ90GiOo76rW%2BtB%2F5HibLwW4umZl4r%2BYvbIlM1UqYgsQuMQvF8LFnJOByY9aAZBq3WSOQx4GIKTmdb7eS8sS2%2BxlSr0ErAldprcCUI7QHfHMIc4t9PEpJAsQ8%2FGqHD4RChZfebLCFM0tXTIA6iSe52zWgCGFReOyKL43GCcLeRwUSgxZhAWS5QUk6xqA5FxI1b%2FAA4gLIeVGX6ITRlTHnb%2FbvDEPgSlcGfiFExQG8zRdg5XzjdfLc9rKeOi%2BxFalZhnZpp7zub%2F51gxPgTVvyf7u8hw8orITZab1jLZQ8ttY7q%2Fii8KchDBMk%2B3obZuLP%2B%2BtcWe4B6Kr9VA0secAKTZ4LSbhTdhxSq7l3vE0RzIXXGYZRLp7nOffXCyHBdebg6zLVwo1eVNfmu4vg8fNkft3rFBnKdzV4w0ZqB1AY6pgFX8G6udXFN4N6JWpx%2Fx4m%2F6NhpkF9lFPwk0bhqzXbcYkQkZbU7630Ovtl5DYKS8sIqeQqA9rQStD9AvaX79V028D0cjms9Tqa%2Fh9CnO%2Bl0Nz%2Bd4N09RY0yf0jEZDm%2FmzZ5sx12Vv6CwkFd8OOc6le6WUfFlwpT6hVOoMifc5HlY%2BUEX3JOCQjDD%2B9URMjwloq%2BS642srnRHcQ3S%2FTftOUJ1Pb%2FdccA&X-Amz-Signature=1f013bfa83e91aa0e8e94711578fa3a2fde69bda1440572a3ae9b7de3b8c3a50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







