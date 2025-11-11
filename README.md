



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T22JZNOE%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T011321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQCUDEDJqhCuF%2FUxMzqcPsVana0xJ9YyRu7tQooGqHGjFwIgMPxxiThvVEyNLCsZn35qaRSVJpwcVnKNa%2BpQqsQzjvcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKYCDVkgXo8w2squ%2FSrcAwJJUXQCPXPMCIcOhmAG6IKfAlrLh%2BfuZo1MsenmjKpFItYzsyeSWBGPRXfKab4oZPoWvmEIf5FC3hfldwZ0WZTrKqTuGe726cjmokmqQIaS2CxQjVboUQ%2BnQlwMiWLy8sasQF7%2FWW4FtUiWoTwAcdxMbxs9Gct3slXoxKj1IGYZ0X1NJKucqIxExI7t63%2B6yrDofU0CPy2hu67I%2FAV%2BgoCBvd0i5B6xmOOhxfFGFuENBjQi8h1VUEiJ5VtRSWp%2BYvu%2FIhwF8Avreta8%2BDY8Dh6B7VpH%2F3V%2BKu%2BQ95qflMu9%2B0bCiIIzAUmvDvrDOXP5sqXYVGwYRQU7LrILZqx0C4PUSPJ3sIFh3XZZlvWitnwL5pnwrqWnRSv0CkXM%2BuiS9m%2B6HIGq6RLE8FcYAAevMGUJSKLsUXs7SsoCvwK7het3KCeVbihWciw54lj4wP5pWG6p38dx7cCVSsj30MWJSo%2Fv%2B7M2YQoX9PE2SJJ0Wvhu%2FWa1jmA7i4cpTVBS%2BwPvrYMCDngYuhoYBB%2B63BSUVZkFsqbj5ScWmpiTyfJocbI6%2FgC3NKg%2FHRzpN0JF%2BnePSVzIUPm4ih%2BqpSQOPMj%2FIgGt84ArvxLI%2FGDJ9Yo2otEMkijRknaoOHz%2FNg9%2FMOT9ycgGOqUBUNbFVcThrGs2AU1jdoQxLGWCUFCHocVp70JRdnRFgW2FpcpH%2BKutttShQvamKHN3v6uSA7mfbKSlfjN2uec90eO08Z5YgHCGeyo7%2BYabsbVebM25caIIwDKrLZpA1zHBgJuUIAJTnMmzmKx4nAweMqgX1HxFjzJi%2FG5%2FmFTRJr4AQur85ahnWaNvC4TP6kbe4FwUzCDPEVcREXMNecMP1KYB4T9s&X-Amz-Signature=cf720f9523845e482337d33df68a5f4c6590785a67c363e6015eeccffda6008a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T22JZNOE%2F20251111%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251111T011321Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQCUDEDJqhCuF%2FUxMzqcPsVana0xJ9YyRu7tQooGqHGjFwIgMPxxiThvVEyNLCsZn35qaRSVJpwcVnKNa%2BpQqsQzjvcq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKYCDVkgXo8w2squ%2FSrcAwJJUXQCPXPMCIcOhmAG6IKfAlrLh%2BfuZo1MsenmjKpFItYzsyeSWBGPRXfKab4oZPoWvmEIf5FC3hfldwZ0WZTrKqTuGe726cjmokmqQIaS2CxQjVboUQ%2BnQlwMiWLy8sasQF7%2FWW4FtUiWoTwAcdxMbxs9Gct3slXoxKj1IGYZ0X1NJKucqIxExI7t63%2B6yrDofU0CPy2hu67I%2FAV%2BgoCBvd0i5B6xmOOhxfFGFuENBjQi8h1VUEiJ5VtRSWp%2BYvu%2FIhwF8Avreta8%2BDY8Dh6B7VpH%2F3V%2BKu%2BQ95qflMu9%2B0bCiIIzAUmvDvrDOXP5sqXYVGwYRQU7LrILZqx0C4PUSPJ3sIFh3XZZlvWitnwL5pnwrqWnRSv0CkXM%2BuiS9m%2B6HIGq6RLE8FcYAAevMGUJSKLsUXs7SsoCvwK7het3KCeVbihWciw54lj4wP5pWG6p38dx7cCVSsj30MWJSo%2Fv%2B7M2YQoX9PE2SJJ0Wvhu%2FWa1jmA7i4cpTVBS%2BwPvrYMCDngYuhoYBB%2B63BSUVZkFsqbj5ScWmpiTyfJocbI6%2FgC3NKg%2FHRzpN0JF%2BnePSVzIUPm4ih%2BqpSQOPMj%2FIgGt84ArvxLI%2FGDJ9Yo2otEMkijRknaoOHz%2FNg9%2FMOT9ycgGOqUBUNbFVcThrGs2AU1jdoQxLGWCUFCHocVp70JRdnRFgW2FpcpH%2BKutttShQvamKHN3v6uSA7mfbKSlfjN2uec90eO08Z5YgHCGeyo7%2BYabsbVebM25caIIwDKrLZpA1zHBgJuUIAJTnMmzmKx4nAweMqgX1HxFjzJi%2FG5%2FmFTRJr4AQur85ahnWaNvC4TP6kbe4FwUzCDPEVcREXMNecMP1KYB4T9s&X-Amz-Signature=03166878c7fda5774ab8348691604fcdab547d57c7fbedf24137dd2538ca5b11&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







