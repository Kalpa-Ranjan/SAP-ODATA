



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KLMUG67%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T025251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJHMEUCIQCIvSjKnkw6R2L95tqMNmH5YPcGHa5gHn7UnkOXc591JwIgGw72mO8FGcGS4%2BceEwY7ZinoqdEB2etABIa1C1Z9%2Fu4q%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDBVI9fmplDQ%2BHze9FyrcA3OgWzopr94qnelInlBGoIEsswxhXCs3ZRZog5Ox8PnkexhIhuWb6hdercv3eXL9M3WMQ%2F%2BqL0ppHsj5sT1Bdx%2FpKDwhXxcLrSrTdy6AhDFNse7%2Fon%2BRtetKlYSPuJfEp%2F8MtP4BwrhtDSeLvYMybQomEcqDWXTAno8yfL5W7Wr2HmhQy56xOwxDy7kkOj%2FmSXtWoGNixqG3E8lvYj5uL5CgBC4dMwkkMKWt3406e0FbFw6gUOS8jLZGWuY%2BMe8ipZBq9T%2BGQlNluMQhP8AHaqVD3TqDNSAmGpRfayLjnceL%2B6v4A84s1T8vUZuUUMomYdm0JwMrTUiJGSwCahsKHlfAOchCk7M1JCzkV0%2Bg2lr5R8865DBkHedDhgNE%2F564%2FmBQymaGBiyG1iUNO64RopLwOQG2WgDxKJv9jUBOiFeGYnfgvx%2FROIJE15EdYzYx0Bqtmt%2B8uzFDWVIrIhE2knhZxjj8P4xWbqqPitb1SFBgEFEy8j10Rro1M0vq1gp0ghLvEoZXlAhu4C566SeqrAJVNnoHEk96Sh6TrULC5fLZ4j%2BBKTljmJIYp2LXvtULcsGCc5ywsqKoDT95M5Sez%2BilbZtLh4zTZhP8eFzyswfZDsY1VcvhzXCU0sOsMIf6stEGOqUBrjK57wvCdVCgsL%2BNmkos%2FVRureBzbD%2BoJrvZh7U2iP8c8wJayA%2BNb64vl%2FO%2BdtwDySVVtf2nsG9ZpWuB5lOXQnrYdgp3jM00HsLFBJEkPmwT%2FVmV7YgFhsNNRclcecXuM12tJpneHueQPvQMfM8jfLGpBem5g2cEtcH3eKS02VAm2TfM4hBbOZUK1oWzGkh39OjVg2DrC4XB2hoiP1L9lfbLjH7s&X-Amz-Signature=01c0737f14d69027eaa17207bd7aa022ad956d086aee96eda229ac69bf0efbf3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667KLMUG67%2F20260613%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260613T025251Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFoaCXVzLXdlc3QtMiJHMEUCIQCIvSjKnkw6R2L95tqMNmH5YPcGHa5gHn7UnkOXc591JwIgGw72mO8FGcGS4%2BceEwY7ZinoqdEB2etABIa1C1Z9%2Fu4q%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDBVI9fmplDQ%2BHze9FyrcA3OgWzopr94qnelInlBGoIEsswxhXCs3ZRZog5Ox8PnkexhIhuWb6hdercv3eXL9M3WMQ%2F%2BqL0ppHsj5sT1Bdx%2FpKDwhXxcLrSrTdy6AhDFNse7%2Fon%2BRtetKlYSPuJfEp%2F8MtP4BwrhtDSeLvYMybQomEcqDWXTAno8yfL5W7Wr2HmhQy56xOwxDy7kkOj%2FmSXtWoGNixqG3E8lvYj5uL5CgBC4dMwkkMKWt3406e0FbFw6gUOS8jLZGWuY%2BMe8ipZBq9T%2BGQlNluMQhP8AHaqVD3TqDNSAmGpRfayLjnceL%2B6v4A84s1T8vUZuUUMomYdm0JwMrTUiJGSwCahsKHlfAOchCk7M1JCzkV0%2Bg2lr5R8865DBkHedDhgNE%2F564%2FmBQymaGBiyG1iUNO64RopLwOQG2WgDxKJv9jUBOiFeGYnfgvx%2FROIJE15EdYzYx0Bqtmt%2B8uzFDWVIrIhE2knhZxjj8P4xWbqqPitb1SFBgEFEy8j10Rro1M0vq1gp0ghLvEoZXlAhu4C566SeqrAJVNnoHEk96Sh6TrULC5fLZ4j%2BBKTljmJIYp2LXvtULcsGCc5ywsqKoDT95M5Sez%2BilbZtLh4zTZhP8eFzyswfZDsY1VcvhzXCU0sOsMIf6stEGOqUBrjK57wvCdVCgsL%2BNmkos%2FVRureBzbD%2BoJrvZh7U2iP8c8wJayA%2BNb64vl%2FO%2BdtwDySVVtf2nsG9ZpWuB5lOXQnrYdgp3jM00HsLFBJEkPmwT%2FVmV7YgFhsNNRclcecXuM12tJpneHueQPvQMfM8jfLGpBem5g2cEtcH3eKS02VAm2TfM4hBbOZUK1oWzGkh39OjVg2DrC4XB2hoiP1L9lfbLjH7s&X-Amz-Signature=c7dedfb2117f0328ead113df3e29a7b80d3c56c00b705aa55aeee45ab274b2d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







