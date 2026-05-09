



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5R7ATLC%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T185307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIA57UeHi5Nh93jL6tac17kdENjVXJo6DAduJALq52ee%2FAiEAgwqmnEe7r4yUNmAgSo3e0GLsNQrwx3m2iv7sWAi%2BeecqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKihJu%2Fmlv%2FccGbwSrcA5ubqyn0v%2BkqBUCynqhvOZAPpUQmk%2BHXyGfBKQlWAFiZc1liaZVU53%2BoVEBow%2BjuqyrQeN2oJjMI%2BCIfy0PMIFDcw5TAYoi7jP0Rw9bJ07WgVSpCaacOomgLvick861AhpyhIrF8QcBTwVfdxEOip9%2FtfhRROHahsCXuVvPtmnExGLrAGmidhNOuEvKJKKzYLzefhxTqQFcESxg%2FSmi1me4WZXda30zZCfEdh2Qs5MiGeNR15xpO1RX9Lv3K8uepf4f16u0sDGy1lgW3wr7fLi4J2f7NhNC8PqaSeUr1FwjcKJK%2FTd%2FFBKmmcgAhtqVk359a5TLM1oHtNRRthSEc%2B%2FgR0pmCqG%2BoD1vNW22VmkuIqKkSACyU19BYxCY5OpYBGgixclyXJ4ZpgVpvUGL6pOS7luUk9TA%2BPKwD4b9ZaKiIW0ZyHtEiof5md7m38c0kmSy1mwbDQGvv%2BNhVePBmFgu7BkSQdxk0%2F%2BeHvu%2FlA3LZgsPG3S%2FUPdjFcab9cylAkBPNWw5IknvKGVunJIMg3FFkdGREZEujqviLpZhr5%2FHOPvfuhPqHQqLAsweq7LrWL6SWHuDRr9FGh%2FOaNR2BmJWYW7sms3LvZZxIswBpZQ0q3fM%2BErVw3ZDOmydwMNLa%2Fc8GOqUBMAuksHwDW3ZLNlx2cjb8xQ9mM2vKfH7qImH%2FPoKSlRF6d6rgRl6d3WBIF4bQg6A%2FxTSCZRaopAEt0hmgk3YvEDxZw5l5wD3ifx606FgFPInBC71G46l%2F0ygVfVEVXL4OlxCiW1i7kZLDwHzPjrlQ12v6IDGUuXFOovodET%2B%2BKhGYYUhBwx3phCiY2xJ6v%2F0ApjPXlECZgnFEPHD1WRiPuaxjQ6SX&X-Amz-Signature=3e3deada84bbd17c868a51ce68bdebc0a9703d20874a9b218463c529744de08e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5R7ATLC%2F20260509%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260509T185307Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECIaCXVzLXdlc3QtMiJHMEUCIA57UeHi5Nh93jL6tac17kdENjVXJo6DAduJALq52ee%2FAiEAgwqmnEe7r4yUNmAgSo3e0GLsNQrwx3m2iv7sWAi%2BeecqiAQI6v%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLKihJu%2Fmlv%2FccGbwSrcA5ubqyn0v%2BkqBUCynqhvOZAPpUQmk%2BHXyGfBKQlWAFiZc1liaZVU53%2BoVEBow%2BjuqyrQeN2oJjMI%2BCIfy0PMIFDcw5TAYoi7jP0Rw9bJ07WgVSpCaacOomgLvick861AhpyhIrF8QcBTwVfdxEOip9%2FtfhRROHahsCXuVvPtmnExGLrAGmidhNOuEvKJKKzYLzefhxTqQFcESxg%2FSmi1me4WZXda30zZCfEdh2Qs5MiGeNR15xpO1RX9Lv3K8uepf4f16u0sDGy1lgW3wr7fLi4J2f7NhNC8PqaSeUr1FwjcKJK%2FTd%2FFBKmmcgAhtqVk359a5TLM1oHtNRRthSEc%2B%2FgR0pmCqG%2BoD1vNW22VmkuIqKkSACyU19BYxCY5OpYBGgixclyXJ4ZpgVpvUGL6pOS7luUk9TA%2BPKwD4b9ZaKiIW0ZyHtEiof5md7m38c0kmSy1mwbDQGvv%2BNhVePBmFgu7BkSQdxk0%2F%2BeHvu%2FlA3LZgsPG3S%2FUPdjFcab9cylAkBPNWw5IknvKGVunJIMg3FFkdGREZEujqviLpZhr5%2FHOPvfuhPqHQqLAsweq7LrWL6SWHuDRr9FGh%2FOaNR2BmJWYW7sms3LvZZxIswBpZQ0q3fM%2BErVw3ZDOmydwMNLa%2Fc8GOqUBMAuksHwDW3ZLNlx2cjb8xQ9mM2vKfH7qImH%2FPoKSlRF6d6rgRl6d3WBIF4bQg6A%2FxTSCZRaopAEt0hmgk3YvEDxZw5l5wD3ifx606FgFPInBC71G46l%2F0ygVfVEVXL4OlxCiW1i7kZLDwHzPjrlQ12v6IDGUuXFOovodET%2B%2BKhGYYUhBwx3phCiY2xJ6v%2F0ApjPXlECZgnFEPHD1WRiPuaxjQ6SX&X-Amz-Signature=040db141ddcc6e01fc3a92c98e73407fa04224766b5b4b915946b2efa3bfd4cd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







