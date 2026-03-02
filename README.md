



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672FFS2JV%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T124609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGgLhoAj6hyhehAHA00bsD%2FnVUcSbxwohEgYFyE9gBwXAiAMcpxK8lt1K8OhPW7uSeoYFGziNcNrZszrEgPt7nKs3SqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNMA3B50XVWS7ipwvKtwDdcNbI69z1tdPDmkKmvA8uHlpQfqtaTYDF1pBGE%2BPV1geq0iE7wzGPDZLQkrQHdwHBuTV7gJamQ4oTJ%2FWVwN4Qwu2e4QhZUOuGh0819s1dsQSo0Ye1dMlhk7OnyebS7d2NZfYTRd33kuD1VVr%2FKwOE05SK4sxG%2FoJBcFrZAIE6igjQa4gJbZuldR1jqIZcczz5qNWqih18n9pGz%2F48o6kJLoXvn7V%2FfvBvw89t2gN1Aot31v7DXwo8BUojtt5WixEM%2F5s6pcaPP02EW%2FtsoMknJ8EGDMrSySaN8ozw3SojgbfI87HhsDgDgfff4L1EkzHKDCgfF3FAZLfEvWcFbsccck8Pi37XCUvGG2NPJQY%2B6HiafYSiujBCbF4DhyE9gMX34ln1yjzBWfe2d1g2AxchNpK6rvU29R1VzkUx0EQ8kdkb%2FjwZ9x0xcgv5jIy1Agd%2BkW3vNn7bGI0C3LTVIAi27LTnLYqebKTlmonm9Fjng0OjZoUmEKLoRCry%2FxR6LOCX74ky0WnWJZssTYnwNtk7jbnfl87Ie5Rv%2FDNWH6sVlEfgtVCGlecey%2BnDreVEeO8FXOU6aDQ9NEU95Uq%2BKror7x3EAZU4pi9Ei%2BG%2BmO68P%2B9cObsGNQoNHOCXWcwjfmVzQY6pgGKvjjYLMwkx5fv989qCfWc28rYfnHgx6Ii%2Fppz%2Bi2854hnp%2BzBEXEr2uFDPP%2BrYa%2BfvAHVXsV%2BrAnRORWPdIlcVg4wUkMm3AzKWwjgGbaQ5OxmOtKR0Gsx8cC%2F87OfnQTcf3CFNWY3nLRwZBd%2FLsv%2FyehRB%2FMN%2B7APxY%2FCYhNDNhei4s4O%2FyqaD3xZQk5wPe92PEbhcS0dsKlGxHgtf9Umx2Zu9hNC&X-Amz-Signature=9df69c8a0ffa80898bf33e0d90ae3e0bf59e8aa239bbf8d92f56fd33b6a6cdcd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672FFS2JV%2F20260302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260302T124609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGgLhoAj6hyhehAHA00bsD%2FnVUcSbxwohEgYFyE9gBwXAiAMcpxK8lt1K8OhPW7uSeoYFGziNcNrZszrEgPt7nKs3SqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMNMA3B50XVWS7ipwvKtwDdcNbI69z1tdPDmkKmvA8uHlpQfqtaTYDF1pBGE%2BPV1geq0iE7wzGPDZLQkrQHdwHBuTV7gJamQ4oTJ%2FWVwN4Qwu2e4QhZUOuGh0819s1dsQSo0Ye1dMlhk7OnyebS7d2NZfYTRd33kuD1VVr%2FKwOE05SK4sxG%2FoJBcFrZAIE6igjQa4gJbZuldR1jqIZcczz5qNWqih18n9pGz%2F48o6kJLoXvn7V%2FfvBvw89t2gN1Aot31v7DXwo8BUojtt5WixEM%2F5s6pcaPP02EW%2FtsoMknJ8EGDMrSySaN8ozw3SojgbfI87HhsDgDgfff4L1EkzHKDCgfF3FAZLfEvWcFbsccck8Pi37XCUvGG2NPJQY%2B6HiafYSiujBCbF4DhyE9gMX34ln1yjzBWfe2d1g2AxchNpK6rvU29R1VzkUx0EQ8kdkb%2FjwZ9x0xcgv5jIy1Agd%2BkW3vNn7bGI0C3LTVIAi27LTnLYqebKTlmonm9Fjng0OjZoUmEKLoRCry%2FxR6LOCX74ky0WnWJZssTYnwNtk7jbnfl87Ie5Rv%2FDNWH6sVlEfgtVCGlecey%2BnDreVEeO8FXOU6aDQ9NEU95Uq%2BKror7x3EAZU4pi9Ei%2BG%2BmO68P%2B9cObsGNQoNHOCXWcwjfmVzQY6pgGKvjjYLMwkx5fv989qCfWc28rYfnHgx6Ii%2Fppz%2Bi2854hnp%2BzBEXEr2uFDPP%2BrYa%2BfvAHVXsV%2BrAnRORWPdIlcVg4wUkMm3AzKWwjgGbaQ5OxmOtKR0Gsx8cC%2F87OfnQTcf3CFNWY3nLRwZBd%2FLsv%2FyehRB%2FMN%2B7APxY%2FCYhNDNhei4s4O%2FyqaD3xZQk5wPe92PEbhcS0dsKlGxHgtf9Umx2Zu9hNC&X-Amz-Signature=335d8446cd83eb3784cec8209b9516822763f83711de708502a602995a8a59eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







