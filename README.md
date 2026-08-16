



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624CTVZ4H%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T005827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIGbxCjmAOqoKJx4wVwmiqn9bK4FRBpGu%2FNBG4QTTBn2uAiEAry7jDbQvaqvP6TVjLT5uez0Rge9hrhZPcrvhFevu2pkq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDHXAJ51ReavcAVAK%2FyrcA39Y%2Fdm9aSxcq9qsG%2Fgm%2Ff654Qj%2BwNnxmdNfbN3czQVjOoFLWby%2BgMeM1GonwA81cmvon%2FEGNQ00tieTdfO8CW7lQeeoTYPx7jLAGaoivKT0dpqPA7dgZIvVzUC0UjfQxlPSl0dXa61p5j0j4e3xxcOtcY7DGPz4m9Rnc17mHxpXiIqUrHckqK3sDa0XNXS%2BuWcDJuejmxn%2FOcAbMdb3wn5FSdf%2F8Fer7kgob4ufXTwqPc5KGy%2FPa4HsGDBWRDj3CEXRMAXJFpX8VktvNMjsBp%2BW7PvXchSeYDrZ6AAgmfNpLvMKn9TkV9bc2H%2FIh6nXKTaC5U11vWB2apAMn%2BYbzobJiB1guVPrP9vSON6Ms2XPWfa4ZZJG7MLd%2FGzP2m0SXoV1vAyeDQQdVGEi2B3bhCvpVrwF5zqxZ5Dciv4q1UfZY6mV%2F9hItTFTkrb%2FoIvklTnaiNw0akYpZo9Hbqdfkh63RImqXi67rMANPRIJoAu6iLnQjLfnV3G6gV%2BMS7jzA42b5BJeCUJYWkqky9RYTi4Zl4ix9wtFwFWWlF77FKCpY2%2BKfQX%2B8zgmPdbz8xpL%2BuDCFGU69G9ho3k5fdnmF5Km3PT99keD4XgOGkATz8XwYLmPpD03dFB6sjRvMLXtg9QGOqUBAkDLTa3ludb%2F7%2BJMSSYYjY7i5%2FanujSA4mRq%2B4qo6ZnPaWZuRYdeeLe17gBrCecchzOZqXGqMlJpOmyW0LoEGO6yXmJlfAzE6F9qXUp%2BoMFkTpXhxUFYBLePJ%2FsodINJbLjuLkz0%2Bp6zhU%2F%2BzVq2w6GutrZR%2Bo2O%2B3qbqtw5HJ4z4yvEc7sNmzS8zocucG1mq8cFoDW8lYfPmysMK%2Fk9wZUCJV4G&X-Amz-Signature=4e27e519cb77ea9dd3bf4895c0745968aaf77a0606f8af22a5d284f0c98e40da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624CTVZ4H%2F20260816%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260816T005827Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIGbxCjmAOqoKJx4wVwmiqn9bK4FRBpGu%2FNBG4QTTBn2uAiEAry7jDbQvaqvP6TVjLT5uez0Rge9hrhZPcrvhFevu2pkq%2FwMIIRAAGgw2Mzc0MjMxODM4MDUiDHXAJ51ReavcAVAK%2FyrcA39Y%2Fdm9aSxcq9qsG%2Fgm%2Ff654Qj%2BwNnxmdNfbN3czQVjOoFLWby%2BgMeM1GonwA81cmvon%2FEGNQ00tieTdfO8CW7lQeeoTYPx7jLAGaoivKT0dpqPA7dgZIvVzUC0UjfQxlPSl0dXa61p5j0j4e3xxcOtcY7DGPz4m9Rnc17mHxpXiIqUrHckqK3sDa0XNXS%2BuWcDJuejmxn%2FOcAbMdb3wn5FSdf%2F8Fer7kgob4ufXTwqPc5KGy%2FPa4HsGDBWRDj3CEXRMAXJFpX8VktvNMjsBp%2BW7PvXchSeYDrZ6AAgmfNpLvMKn9TkV9bc2H%2FIh6nXKTaC5U11vWB2apAMn%2BYbzobJiB1guVPrP9vSON6Ms2XPWfa4ZZJG7MLd%2FGzP2m0SXoV1vAyeDQQdVGEi2B3bhCvpVrwF5zqxZ5Dciv4q1UfZY6mV%2F9hItTFTkrb%2FoIvklTnaiNw0akYpZo9Hbqdfkh63RImqXi67rMANPRIJoAu6iLnQjLfnV3G6gV%2BMS7jzA42b5BJeCUJYWkqky9RYTi4Zl4ix9wtFwFWWlF77FKCpY2%2BKfQX%2B8zgmPdbz8xpL%2BuDCFGU69G9ho3k5fdnmF5Km3PT99keD4XgOGkATz8XwYLmPpD03dFB6sjRvMLXtg9QGOqUBAkDLTa3ludb%2F7%2BJMSSYYjY7i5%2FanujSA4mRq%2B4qo6ZnPaWZuRYdeeLe17gBrCecchzOZqXGqMlJpOmyW0LoEGO6yXmJlfAzE6F9qXUp%2BoMFkTpXhxUFYBLePJ%2FsodINJbLjuLkz0%2Bp6zhU%2F%2BzVq2w6GutrZR%2Bo2O%2B3qbqtw5HJ4z4yvEc7sNmzS8zocucG1mq8cFoDW8lYfPmysMK%2Fk9wZUCJV4G&X-Amz-Signature=7e2b873a488304774e7bb8a202ce2f01177e2113ee6d81b0a76df30dfe4bfb40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







