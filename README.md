



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OM7TYLS%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T065511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIDuzWSqOZOQVAzjEnlHSh8WPXTu%2BU35AOOqPkfbvjlobAiEA%2BmfczfmZNoYIz1YO%2BvDLom2253KOwwHbw9xTiRWFpJgq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDE%2BKlz7f3k7a6ZrjOircA5SzIy7tBmaeS2N9YEnuqieg7rQVoBT2DWBtq8G3b2VIeZ0%2BIYJ5bNpFaqt%2BKj6OxsCvXGSXYpwKBc%2BelaQS3rIvo8FxS%2B3WPBzH8rNSV2souxfo%2BkNlA%2F1Z8Xy5L1Y7OEE6JOgLOzi5fpdWS%2FJqvAiXKEjaNZFKykb%2BEmqc1qRprqhXLJRp4avKpNBtkoiHp1RGTiFeGy%2FfZnBbitKaNQ%2FHJKkHdBrQTRVu28T4X5bqtC3UH93h3DIVmcp2bhokWSKhcj%2B8igOwXhXqI9gd%2BuRKQcttgochdEfHUedDaKue25OYkc%2F5csKZr0FSpvkwTb2MeTPtURzCOILPRrZYuQLSq6KCusKOrPLzZSNRzF8WlbMXimXvEc%2FRum51kZSL6xN4Yvw7AiOUnJENlcqahb9ar5f6p10BzuE9%2BM9X1rUBye7FpSAP1bNfSiyRYxW%2BnakTAkWZ4MaLcPpFJPw1FBRFufJ29oaZVt94gB%2FHVTp36TWy6T2y5%2Fd0tb3HBIeO3plmTzAWVGyJMPC54B1oA8vpZBT7DoQ2p9Zf3reAHhuXePrVNUY%2BCckSo%2Fdzi2lndgILpgF0qZdyijPzgVow%2BpjOTGTArhyH7KcRVvXj0qug07shGS09iMKHVLOMMKLd584GOqUBBlN0egAeeW6jugOEuUySKyPYxHQCpvw3KhxFpQOPiXkFFyAsOCRQ4oQmSiEFOOunmvnKccBH1VtvPnof19N3F2nFI4AQUk9vV02lRwYn8DtzP%2BwPo929Ln3O%2F9W6Iah8C55xm%2F1t8H9T8m9a64%2BV5RHG5ypdQAEoJ41MSn8U0ctOQUjIVUb%2F29EWc6eLbczhtmEFxcQCJoEhoq%2FgN38gD%2BhqQIaZ&X-Amz-Signature=7b146fd204ce4c881bb5f39f967f877f08be8938b3b3e1fe4a93031add9e5bda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664OM7TYLS%2F20260411%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260411T065511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJHMEUCIDuzWSqOZOQVAzjEnlHSh8WPXTu%2BU35AOOqPkfbvjlobAiEA%2BmfczfmZNoYIz1YO%2BvDLom2253KOwwHbw9xTiRWFpJgq%2FwMIQBAAGgw2Mzc0MjMxODM4MDUiDE%2BKlz7f3k7a6ZrjOircA5SzIy7tBmaeS2N9YEnuqieg7rQVoBT2DWBtq8G3b2VIeZ0%2BIYJ5bNpFaqt%2BKj6OxsCvXGSXYpwKBc%2BelaQS3rIvo8FxS%2B3WPBzH8rNSV2souxfo%2BkNlA%2F1Z8Xy5L1Y7OEE6JOgLOzi5fpdWS%2FJqvAiXKEjaNZFKykb%2BEmqc1qRprqhXLJRp4avKpNBtkoiHp1RGTiFeGy%2FfZnBbitKaNQ%2FHJKkHdBrQTRVu28T4X5bqtC3UH93h3DIVmcp2bhokWSKhcj%2B8igOwXhXqI9gd%2BuRKQcttgochdEfHUedDaKue25OYkc%2F5csKZr0FSpvkwTb2MeTPtURzCOILPRrZYuQLSq6KCusKOrPLzZSNRzF8WlbMXimXvEc%2FRum51kZSL6xN4Yvw7AiOUnJENlcqahb9ar5f6p10BzuE9%2BM9X1rUBye7FpSAP1bNfSiyRYxW%2BnakTAkWZ4MaLcPpFJPw1FBRFufJ29oaZVt94gB%2FHVTp36TWy6T2y5%2Fd0tb3HBIeO3plmTzAWVGyJMPC54B1oA8vpZBT7DoQ2p9Zf3reAHhuXePrVNUY%2BCckSo%2Fdzi2lndgILpgF0qZdyijPzgVow%2BpjOTGTArhyH7KcRVvXj0qug07shGS09iMKHVLOMMKLd584GOqUBBlN0egAeeW6jugOEuUySKyPYxHQCpvw3KhxFpQOPiXkFFyAsOCRQ4oQmSiEFOOunmvnKccBH1VtvPnof19N3F2nFI4AQUk9vV02lRwYn8DtzP%2BwPo929Ln3O%2F9W6Iah8C55xm%2F1t8H9T8m9a64%2BV5RHG5ypdQAEoJ41MSn8U0ctOQUjIVUb%2F29EWc6eLbczhtmEFxcQCJoEhoq%2FgN38gD%2BhqQIaZ&X-Amz-Signature=914bb7f8d54358d6dce34271ce90717deca660ef05727c04adbb3b11169623df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







