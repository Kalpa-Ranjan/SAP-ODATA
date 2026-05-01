



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CCFEZRL%2F20260501%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260501T190451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHm1NwrzpBUS382IbbkMj4TzjnYOEQCsGhzcWNzp6YweAiEAqOP7cfBlw%2Be76bAQZb8voJCTYeRdH3OuCbtqdjosydsq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDEzj4Y9Ii5ozc4hp9CrcA3KYQEvBlHb8%2BiRj9v7n1uGXc7Ebd%2FRYF8SLns7vdWx4GCmIkYr2cDbd3SbY%2Bjb29lPx%2BHMYyVmzpozVxqpGp3367XBe2hTF%2Fic8gbvlo6wuntT7QPefdxPBYH19zCo1iFBLYT95Y3Nkk0SreVciMHB%2FruLEhwNp%2Ft6w%2B3SYNEIcHtf5ikcrvTaJPd1CXdYWTdj8gfEvwi6ufa0nHLwMDscW7OdZn3rQgCZ30GN4Ubf7zAdwrWxWDOXQ18IUjbE0KwnHvy9ofg5mlm3sUNT6EPh0TZgI6PcCDDF29OGs49H0%2BBDf9XmkWwpc634Gygg8DGsqBG0iIIry0JMZQ3mqsOjaKgPgWIP%2BQo%2FxYPadX0QtuOOzckXvQQ2eEG%2F6ukr0pmgzinXHA0JLQG%2BEUMN8cMTspaNoU0ylOstzwvbsKEWI%2BRCGxj1hTd%2FbsYXd25sE17mSGypRMZeo7RaReg%2BnNpx7WSAwba3hPX4vY63zd3vnriHjmN0d3OycncQpJefDliQRjH8lVBJvBFv1mfHNkY0gFbXH7P49L2zzQzAs7OPCxLjZVZtnj3JWxlUcMVBu4%2FnEq0I1DMpejzZclSQKO0g3Lm2vdFrijBkk2ggqQauSuX%2F6XLaTuxGlRiVdMNbS088GOqUBuzBImtRlH76DJ2ueuX4jsxWj2dMCmhL5Vd%2FtTgcQfRpEWejXDA0Uy9meWOrf6EXQZs10f%2Baw6DjmuN5ldCX6DAgr4nPhRMTQyKJ96oP4%2F4c918G80cX2tpCJJQANyQ8vTiUCY50oMUKpZEDJeSWeiD4mQrtxOg0v%2F1ULb%2BCeqlZsmVj6CVRQsQqFnqNTfqyoHx7qRKhSVgOOlzTzTfSkN1gOK4lg&X-Amz-Signature=93273be7b68eabd1c958db1544e748f9a9bccded362bef6d08c28f4e56d1c9c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662CCFEZRL%2F20260501%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260501T190451Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIHm1NwrzpBUS382IbbkMj4TzjnYOEQCsGhzcWNzp6YweAiEAqOP7cfBlw%2Be76bAQZb8voJCTYeRdH3OuCbtqdjosydsq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDEzj4Y9Ii5ozc4hp9CrcA3KYQEvBlHb8%2BiRj9v7n1uGXc7Ebd%2FRYF8SLns7vdWx4GCmIkYr2cDbd3SbY%2Bjb29lPx%2BHMYyVmzpozVxqpGp3367XBe2hTF%2Fic8gbvlo6wuntT7QPefdxPBYH19zCo1iFBLYT95Y3Nkk0SreVciMHB%2FruLEhwNp%2Ft6w%2B3SYNEIcHtf5ikcrvTaJPd1CXdYWTdj8gfEvwi6ufa0nHLwMDscW7OdZn3rQgCZ30GN4Ubf7zAdwrWxWDOXQ18IUjbE0KwnHvy9ofg5mlm3sUNT6EPh0TZgI6PcCDDF29OGs49H0%2BBDf9XmkWwpc634Gygg8DGsqBG0iIIry0JMZQ3mqsOjaKgPgWIP%2BQo%2FxYPadX0QtuOOzckXvQQ2eEG%2F6ukr0pmgzinXHA0JLQG%2BEUMN8cMTspaNoU0ylOstzwvbsKEWI%2BRCGxj1hTd%2FbsYXd25sE17mSGypRMZeo7RaReg%2BnNpx7WSAwba3hPX4vY63zd3vnriHjmN0d3OycncQpJefDliQRjH8lVBJvBFv1mfHNkY0gFbXH7P49L2zzQzAs7OPCxLjZVZtnj3JWxlUcMVBu4%2FnEq0I1DMpejzZclSQKO0g3Lm2vdFrijBkk2ggqQauSuX%2F6XLaTuxGlRiVdMNbS088GOqUBuzBImtRlH76DJ2ueuX4jsxWj2dMCmhL5Vd%2FtTgcQfRpEWejXDA0Uy9meWOrf6EXQZs10f%2Baw6DjmuN5ldCX6DAgr4nPhRMTQyKJ96oP4%2F4c918G80cX2tpCJJQANyQ8vTiUCY50oMUKpZEDJeSWeiD4mQrtxOg0v%2F1ULb%2BCeqlZsmVj6CVRQsQqFnqNTfqyoHx7qRKhSVgOOlzTzTfSkN1gOK4lg&X-Amz-Signature=fd343c26bb5df69dc39ea7238e451e9edec7c3cb2e4d83c4d59693a16441fbd6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







