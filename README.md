



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3L22BL2%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T014807Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIBHswjPJSNW10VyciZqGrA8Cs%2B%2B909X6rUnchqBm7oc1AiEA3b8qudTrxKjLVIzVmlrus303hoRVocktChOInr2TzlkqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FzeVAH0tqjiwJ5xCrcAw36Row3dy%2Bw0nu2%2BOLjJIXaHKUg2c4BxNcJz0zaL8dUYgGlMeW%2B7zPr2hOypVBIzhnCfIAY9B%2BIjpJ4QSHdh0tDJBGy9VeBdMb5VcE0apW1%2FIwXRinL2FxKVGGsUxffpkvzGlGWXbJLyhXR%2BG4854oC7F4HxhLucuGFzvFaivHGwRYzUcqB8bITeEvLjx2NnC%2BYONcCik%2BDmaBVEtiNW2nuSXktUa0iAdlfcWfh50%2Br9S2V9gt0iRe0H6%2FQ9inWOH61lnVzlgDpWLX1QBL%2FovrAmv4YxlRBMrkrXjbxxqdmKu97Nuo0aNma7q%2FNQ1Ga36X7yNanRapEzPAd1kuKTVrIp8729SloUQtG34j92f5qpll0%2Fhbz%2Bi%2FvvZGtRafAO9jPQvqJQzB6nUDMVXibfdKzCq%2BDQA%2BRkp0qiORwmwM6nM0xlAOE8LX9NONh5HuTwdtBJdIh8vgsXmZYhqcI83aXTtGmOyvR0TvcSJdEwctVSIgqweHkCDBZ1RXPkQauWp%2BFjvRUTkuW%2BQ563JpLzRVceiBbl6taxmonOr%2BokL7t2XRlo%2FPWvWACWzddggbp5x1xiL4rjalHngabCuR9b8ZzS3JtQnIM8tXKpCy2%2BEVrxZSmsBXbrK2628l%2BMLDEnM4GOqUBTXTC77JEe6omJq%2FX8uCUl3m7EhB8JbMOuRQ7p4fmXrk0V85VvCv2qZyNKWX38VZ7OsJLOo4nFbWWgk1iuGnkd1marmqsrpPXDL978Csr5zeAVkbvOm2zZsQ15uiiKWxvhtv9gVZRKXjf%2Fy1A75aaLreWPl3lf3TTH1UxJvtFvjJPJaGTv0%2BZCSc7y2DzERkArpAIKstJUJnkeLtSYGE5kvKyony4&X-Amz-Signature=167ea97e903b706b42c207d6a10468ba093f3fe30a4cc3c1699c3efeccbb9439&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y3L22BL2%2F20260328%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260328T014808Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJHMEUCIBHswjPJSNW10VyciZqGrA8Cs%2B%2B909X6rUnchqBm7oc1AiEA3b8qudTrxKjLVIzVmlrus303hoRVocktChOInr2TzlkqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA%2FzeVAH0tqjiwJ5xCrcAw36Row3dy%2Bw0nu2%2BOLjJIXaHKUg2c4BxNcJz0zaL8dUYgGlMeW%2B7zPr2hOypVBIzhnCfIAY9B%2BIjpJ4QSHdh0tDJBGy9VeBdMb5VcE0apW1%2FIwXRinL2FxKVGGsUxffpkvzGlGWXbJLyhXR%2BG4854oC7F4HxhLucuGFzvFaivHGwRYzUcqB8bITeEvLjx2NnC%2BYONcCik%2BDmaBVEtiNW2nuSXktUa0iAdlfcWfh50%2Br9S2V9gt0iRe0H6%2FQ9inWOH61lnVzlgDpWLX1QBL%2FovrAmv4YxlRBMrkrXjbxxqdmKu97Nuo0aNma7q%2FNQ1Ga36X7yNanRapEzPAd1kuKTVrIp8729SloUQtG34j92f5qpll0%2Fhbz%2Bi%2FvvZGtRafAO9jPQvqJQzB6nUDMVXibfdKzCq%2BDQA%2BRkp0qiORwmwM6nM0xlAOE8LX9NONh5HuTwdtBJdIh8vgsXmZYhqcI83aXTtGmOyvR0TvcSJdEwctVSIgqweHkCDBZ1RXPkQauWp%2BFjvRUTkuW%2BQ563JpLzRVceiBbl6taxmonOr%2BokL7t2XRlo%2FPWvWACWzddggbp5x1xiL4rjalHngabCuR9b8ZzS3JtQnIM8tXKpCy2%2BEVrxZSmsBXbrK2628l%2BMLDEnM4GOqUBTXTC77JEe6omJq%2FX8uCUl3m7EhB8JbMOuRQ7p4fmXrk0V85VvCv2qZyNKWX38VZ7OsJLOo4nFbWWgk1iuGnkd1marmqsrpPXDL978Csr5zeAVkbvOm2zZsQ15uiiKWxvhtv9gVZRKXjf%2Fy1A75aaLreWPl3lf3TTH1UxJvtFvjJPJaGTv0%2BZCSc7y2DzERkArpAIKstJUJnkeLtSYGE5kvKyony4&X-Amz-Signature=ce0ab2bafde9df31f2c1dbfea758f7e6bcedf30d450b37e22e7adfaa803456e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







