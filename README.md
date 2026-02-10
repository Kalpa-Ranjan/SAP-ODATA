



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XX4QAR5%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T065834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCL5iETNyk314UxXVAPz23FoRts%2FdeFedty6GsVFCMFGAIgWoe04Y44EEojAU8Va%2Fvf0xOTTICtlRqwUtYgNzT5g%2FQqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHlDuha%2Fk4AqI5%2BiyrcAzXK76aryvZvIvNxKi7mSaKAZM%2BFN9GPFrptG4Eg77HcFIT8haoaXI5yuks8T75KZjVqaRTN4FoEwAbYQWQic8b3Ew7SDzw8E%2FPOT6Mc4hXfHbvP80c4KNyzy8blYK6SSVELX1nU1G%2FS1PbbyPI5pdct1i9gUEMojYZSMn0hxkWmQxtVTGLcQumDeSa%2FZr4BXPNmrUsb%2Fiy71ESlTgZL%2FRuFHOg1ZQPYS%2BMAESIn%2FIQ%2FXmTGRkCNUJgFIFwZNQTffC88lq4twW0ksu%2B0ePrFbSmnygT0G2%2FP0oDkps9Gke%2BxG%2BF%2BliYDEa2STO5mJYHmE%2B%2FW0C3Bxo50Dj3rhRwMHzqIFRi73U4H1mI7WAA7H371tzKGlg6F00emFpR6z0DbNMXO0tM1znPklHyE%2FSPxmWRncbpjrT4H7cSwAG%2Fz6lcA0UL7lW9ixMaXporN%2FJQ23D8%2BX9Dt4jRuI5TDywM9Ns4ccRzjldIXvXb1MbyXQ%2FO47T8K0snmxpSpjyr1pr4wTFirDGVJQaZ4nMcOK27yz76bbbV3DbeEZprTRekAvXsoZicNphb5FsGYBp%2BYtxn8JpHNECZGbIZhC%2FKisTT%2BBEJCf5fvKgm14bKYtlkmiKVfcHgKxLvj5%2B8mmJM3MJ2oq8wGOqUBzsPCum3EV7d3AcdgAVxJPF1%2BBql%2B9EoEfXsEH8twqavZdkLzIgPjg2f3Sc13EBHZOJFyY0sZs407noQv0ZMGdUiWgkPLYdzKYOCO6CZyDERoI2Hw5TUGGBWv8nYk%2B6ZX3eZrocUNXOlE5zsdIbFE75oaVMqwSjKNrqAhp1jx40Gox%2B5OhoaTdFCqqc77nTgtgtSG9Ika4%2F%2FWJ2OiMyVqE12EYmGv&X-Amz-Signature=4c8132d2dfda27dae4b1b155374d287d1f26447c5739d51b203e83ab4882749c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XX4QAR5%2F20260210%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260210T065834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCL5iETNyk314UxXVAPz23FoRts%2FdeFedty6GsVFCMFGAIgWoe04Y44EEojAU8Va%2Fvf0xOTTICtlRqwUtYgNzT5g%2FQqiAQIoP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMHlDuha%2Fk4AqI5%2BiyrcAzXK76aryvZvIvNxKi7mSaKAZM%2BFN9GPFrptG4Eg77HcFIT8haoaXI5yuks8T75KZjVqaRTN4FoEwAbYQWQic8b3Ew7SDzw8E%2FPOT6Mc4hXfHbvP80c4KNyzy8blYK6SSVELX1nU1G%2FS1PbbyPI5pdct1i9gUEMojYZSMn0hxkWmQxtVTGLcQumDeSa%2FZr4BXPNmrUsb%2Fiy71ESlTgZL%2FRuFHOg1ZQPYS%2BMAESIn%2FIQ%2FXmTGRkCNUJgFIFwZNQTffC88lq4twW0ksu%2B0ePrFbSmnygT0G2%2FP0oDkps9Gke%2BxG%2BF%2BliYDEa2STO5mJYHmE%2B%2FW0C3Bxo50Dj3rhRwMHzqIFRi73U4H1mI7WAA7H371tzKGlg6F00emFpR6z0DbNMXO0tM1znPklHyE%2FSPxmWRncbpjrT4H7cSwAG%2Fz6lcA0UL7lW9ixMaXporN%2FJQ23D8%2BX9Dt4jRuI5TDywM9Ns4ccRzjldIXvXb1MbyXQ%2FO47T8K0snmxpSpjyr1pr4wTFirDGVJQaZ4nMcOK27yz76bbbV3DbeEZprTRekAvXsoZicNphb5FsGYBp%2BYtxn8JpHNECZGbIZhC%2FKisTT%2BBEJCf5fvKgm14bKYtlkmiKVfcHgKxLvj5%2B8mmJM3MJ2oq8wGOqUBzsPCum3EV7d3AcdgAVxJPF1%2BBql%2B9EoEfXsEH8twqavZdkLzIgPjg2f3Sc13EBHZOJFyY0sZs407noQv0ZMGdUiWgkPLYdzKYOCO6CZyDERoI2Hw5TUGGBWv8nYk%2B6ZX3eZrocUNXOlE5zsdIbFE75oaVMqwSjKNrqAhp1jx40Gox%2B5OhoaTdFCqqc77nTgtgtSG9Ika4%2F%2FWJ2OiMyVqE12EYmGv&X-Amz-Signature=b0a17da6b7699e2ecf65317649518b598c9d02c99da3cd3f11058b76deb85746&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







