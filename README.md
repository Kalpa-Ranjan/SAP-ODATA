



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG62H4QD%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T123928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2YWuXllkAKx9VSFoQJ2yZFonHPDMI4ABZyhBYwBC0zAIhANT42CO1mSVRsueMch%2FrVE9dRLkKgjr3NxW%2FvmLbhW7tKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtoY%2BdoeTwOMEC%2Bsgq3ANY3%2FtbV2uqUnZmzY1%2FGRrozi7Qmtw970H1ppQtcRiPZj7MT3pN1cvrEYOuLzyM4HI5fkkPwXnV2Yq0CTTDVYfB8uWgbBT9K7bI%2BNGFut0ERs4%2FpYkSRpb%2Bsa3R7sJDy6iojeIpBnQl0fu0gSG78XrAbQafzRgmWf111%2F3wZo1DiOkh%2BAcB5Z31qu%2BocMRERcsVLMKM35svp%2FZo4iUW68apbH0avIZ1Tuj2GIhTy6ASt0hfFh1lHep1QbgP8469dupZpOiEUWSFWjCFowa2yyFtCT0fD0JLtEGips6kPZG78c8cvuI1OKSasEnJjRlh3h2RSz2f3M3lFWaIp%2B2dMTUwXL8eA5GLJKTNC0NYdqhlARRafzGsTY%2FW1w%2B55Z87Nu4mvuWseOUwCJGtUv3kmdSjFECSTakSWpSPeQdvJMY7X51XJ5muoR%2FYV%2Bl5SqA76dZNHH0t4hRytvKm4UF995FoHxWSSdzLT7k7azCvFipaxhA9jRu5KbnCTeHFUYGws3NJqkjIlufN4WjWhCUge5CdgFQf1QA5p3IPkABQvXFXxUcG0GWHGaJv3UY4dsB1Pg2u0OUuZv%2BH0xb9WnP27llyKRMeArMCOd6isiHmYjDhXpyD32oXCGFRh6yQrjCusrjLBjqkARS06zwuHSn%2BWNhdmFe59%2F5Yt4BFpPv%2FEwYgkaa39x6A%2Bf3NURW1toMkfBK3U6PEGUOWjyHNkqgUL2%2FkDBtqSiBzbhVKoWWI%2Bow8mTUCJR8uzblPYgNi4trMqu%2BGZwZw%2FC2lroeUkbM69Kerq1Jk9o1A3oN6MSXaIfvPwcFkw0DpZg83zoTxupRAeseDb4q72RZZCMaxBbV0eLCGBIfkT5gcK9eK&X-Amz-Signature=277b2b0f49cf63862a6dbd6884b98648537ad05fea8c3e2e0b002ebbcc5659c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UG62H4QD%2F20260119%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260119T123928Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2YWuXllkAKx9VSFoQJ2yZFonHPDMI4ABZyhBYwBC0zAIhANT42CO1mSVRsueMch%2FrVE9dRLkKgjr3NxW%2FvmLbhW7tKogECJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtoY%2BdoeTwOMEC%2Bsgq3ANY3%2FtbV2uqUnZmzY1%2FGRrozi7Qmtw970H1ppQtcRiPZj7MT3pN1cvrEYOuLzyM4HI5fkkPwXnV2Yq0CTTDVYfB8uWgbBT9K7bI%2BNGFut0ERs4%2FpYkSRpb%2Bsa3R7sJDy6iojeIpBnQl0fu0gSG78XrAbQafzRgmWf111%2F3wZo1DiOkh%2BAcB5Z31qu%2BocMRERcsVLMKM35svp%2FZo4iUW68apbH0avIZ1Tuj2GIhTy6ASt0hfFh1lHep1QbgP8469dupZpOiEUWSFWjCFowa2yyFtCT0fD0JLtEGips6kPZG78c8cvuI1OKSasEnJjRlh3h2RSz2f3M3lFWaIp%2B2dMTUwXL8eA5GLJKTNC0NYdqhlARRafzGsTY%2FW1w%2B55Z87Nu4mvuWseOUwCJGtUv3kmdSjFECSTakSWpSPeQdvJMY7X51XJ5muoR%2FYV%2Bl5SqA76dZNHH0t4hRytvKm4UF995FoHxWSSdzLT7k7azCvFipaxhA9jRu5KbnCTeHFUYGws3NJqkjIlufN4WjWhCUge5CdgFQf1QA5p3IPkABQvXFXxUcG0GWHGaJv3UY4dsB1Pg2u0OUuZv%2BH0xb9WnP27llyKRMeArMCOd6isiHmYjDhXpyD32oXCGFRh6yQrjCusrjLBjqkARS06zwuHSn%2BWNhdmFe59%2F5Yt4BFpPv%2FEwYgkaa39x6A%2Bf3NURW1toMkfBK3U6PEGUOWjyHNkqgUL2%2FkDBtqSiBzbhVKoWWI%2Bow8mTUCJR8uzblPYgNi4trMqu%2BGZwZw%2FC2lroeUkbM69Kerq1Jk9o1A3oN6MSXaIfvPwcFkw0DpZg83zoTxupRAeseDb4q72RZZCMaxBbV0eLCGBIfkT5gcK9eK&X-Amz-Signature=16d76de036485fbfded2b21164d7947f165e7b75101000d94980a84d51b772fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







