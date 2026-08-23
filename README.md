



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK5EB5D2%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T122824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIF%2BZt7Sos0B8FmQLWkaDvQopqm%2BXwmeF5vM945AF6wRhAiBeT4IMSSIndy8a%2F%2FnmEPk%2FPUbkOmXg2XnmLgfIDjHCqCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0S1SBLZEEl73aktbKtwDJYBfYvsDTW3vdgKGaBm6mJijbIieyLp0hqxeYPBaZdZU6mBqtp0cThk1MQlsYk3OBL6yf7VisRdSjoNfCmfXgUEnVOqXtnKAlodOyj0XGnizjkHKg7tE477uIkabzr0uOjySf6IKCcJ%2BbPDyrNm2EBfpw%2BNIpkK9R5ZceYkTKE%2FGJTK5uV5GGuWSx1qpE6OoQMsixv9uT04K0wJ4xtjICu8YeLxCsrRNCWlPUOrVzUsL3Spt7zKuxCwvS10oSPqTBSFHcfpM34kY%2BmOvzNrLMQ3nbEDkQ6tjvyJn%2FXkklYL8qE%2FfuWjD%2BtyqmBbQMQk3wpLjFKsQHm1QMMFbGdPzKfX7ifpbAIt46a4fwd5ijL17mnaX43agQcmE7RDslHsHD7G5y7HT0bwWngf1DadQ1xtrbcI1TOMz8BuRIL6KlQzMTmZidl8aV1oKPU6dnxN6f%2BoUgdSLofRhoWKYFC10L6ozYR9vjb0Q93PUtf%2BO6EyUY3bJhhjHHd0PURQKJD5rFzLaxpHmCQr5yTJohl6u00QThdqM55QDujNniBJ%2F9dLkNImgr4LeKkdF%2Bj1pUvx39jgWFQ%2FkoMEO5yaxwpS%2BD%2FK%2B%2B3SH5api%2Fk%2FanO%2F%2Fl9suc7tiUw4Q9rnguqEwqtuq1AY6pgEAw92IVZSoNYE64b7OPN89ws5GM3YhlbnTamI6xE7pvv%2FlF%2Bn7HJgP7St%2B46Q%2FC0gbLc2YyQMXUE8bbSyi6oRaPrJ0tJN9i8BR4j6I66WwsBrZ5%2BYDaoW3TLvcazEUfNqIxCBmNJF1Q5oGML%2B4k0ojqVy2EoBgwg0bNWwPGEPv6RJqX9%2FR8yNAyFqX5%2BVIN7sVGX0bizmo2zkn3jI1JLFM968Psc35&X-Amz-Signature=d9101656fb277ddfa753963f8ff8f1479574837d8d7bdf784bfed523fad2c64c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RK5EB5D2%2F20260823%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260823T122824Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIF%2BZt7Sos0B8FmQLWkaDvQopqm%2BXwmeF5vM945AF6wRhAiBeT4IMSSIndy8a%2F%2FnmEPk%2FPUbkOmXg2XnmLgfIDjHCqCqIBAjS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0S1SBLZEEl73aktbKtwDJYBfYvsDTW3vdgKGaBm6mJijbIieyLp0hqxeYPBaZdZU6mBqtp0cThk1MQlsYk3OBL6yf7VisRdSjoNfCmfXgUEnVOqXtnKAlodOyj0XGnizjkHKg7tE477uIkabzr0uOjySf6IKCcJ%2BbPDyrNm2EBfpw%2BNIpkK9R5ZceYkTKE%2FGJTK5uV5GGuWSx1qpE6OoQMsixv9uT04K0wJ4xtjICu8YeLxCsrRNCWlPUOrVzUsL3Spt7zKuxCwvS10oSPqTBSFHcfpM34kY%2BmOvzNrLMQ3nbEDkQ6tjvyJn%2FXkklYL8qE%2FfuWjD%2BtyqmBbQMQk3wpLjFKsQHm1QMMFbGdPzKfX7ifpbAIt46a4fwd5ijL17mnaX43agQcmE7RDslHsHD7G5y7HT0bwWngf1DadQ1xtrbcI1TOMz8BuRIL6KlQzMTmZidl8aV1oKPU6dnxN6f%2BoUgdSLofRhoWKYFC10L6ozYR9vjb0Q93PUtf%2BO6EyUY3bJhhjHHd0PURQKJD5rFzLaxpHmCQr5yTJohl6u00QThdqM55QDujNniBJ%2F9dLkNImgr4LeKkdF%2Bj1pUvx39jgWFQ%2FkoMEO5yaxwpS%2BD%2FK%2B%2B3SH5api%2Fk%2FanO%2F%2Fl9suc7tiUw4Q9rnguqEwqtuq1AY6pgEAw92IVZSoNYE64b7OPN89ws5GM3YhlbnTamI6xE7pvv%2FlF%2Bn7HJgP7St%2B46Q%2FC0gbLc2YyQMXUE8bbSyi6oRaPrJ0tJN9i8BR4j6I66WwsBrZ5%2BYDaoW3TLvcazEUfNqIxCBmNJF1Q5oGML%2B4k0ojqVy2EoBgwg0bNWwPGEPv6RJqX9%2FR8yNAyFqX5%2BVIN7sVGX0bizmo2zkn3jI1JLFM968Psc35&X-Amz-Signature=ef327351fe3702ed434ff2198cc44f67a80b3d39271e34eb3a83437f05516f4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







