



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSHAFD5E%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T025337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIF%2B63xt1YkRgQKnKakoE2DnUSDZO%2F4PlIkZ3Oo60ptQ7AiAYMnmOyg06%2FvaRNq31DRJSwKvMq4oIcPwCYnGQhVmnRCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG3Wk3oc1hvXnbyLMKtwDPKevxbGU%2B2fbYmIWNUmsGzU9oGWTfKPYErQVgojzV5ReP%2F1jO8Uh9Us5PtcoOkY2L1LKBajtviRMYWjsSEw6M%2FBuHsl0GrgzikdsIKviPVb8lRQu%2FTaKILQdqGpVFJz%2FJbTFf%2Fu%2BCCaQgL5alkmNIh7BrZ9hb97UvnOlkBMbBtSK%2BkDR8i9FEN9uO8hXiCiEo2Uettab%2F4gQ6S1pEXfxrOL58qAo9%2BsPze2aOD8Vezbevrnm2n%2FJMPifTXtjrChArSTIHsmYT24Cn4IgdIuOeQnCgDjLSDXs7FvHGszgMH%2FhfvXhuIq4aSgKV4Tp8A%2BCPqiWla49kZD8%2FAHQyU54eX%2BWrU%2BYwdbMkYkvu2ca%2Bw0hHSOl2zBCH2pYuJkQFgH11nEdUVau9rpZlk8yvbZ4Qnsbl3Gnn%2BsdnUOJJsojpnotthXcc%2BaQ60B6onmq13UF7hRMMwKt6cGZqt%2FCUT%2BZSwyEtq4QnqOIFcBzOyQSvqClHcjaKdLryYlV8h5tLlLGOasBhaFe27zqGYA2saODicNSGWlTZyLB%2FSgIDbrCUfmqdzntHHfazbMVDhq%2BJf6VNUBUL02hRG%2B%2FKBxAVwCCowf77gI5pduYE1HwVyBgoiXt%2Fqws3DeQiugwC2Qwhoqj0QY6pgE%2FeUTRxJrjK0NRHwKZQrG%2FCLTuUT4siUptZky4GXd4SFzAz87fFNvroyahjTX4df%2FLv4r3MvBsqHy4YpNfTm2zlIRJj64HHgQJfAtB7wbfy3MgQ0FSLSfsH87qHEAQwIXb6mVp9ofzdVoO%2Fd4BOGZOqWsPj6FsL2qqHKo39eAm3ry6bkE74UbTP2zRigHSe64jzKcTkAntyP25oYlfmf9dyGn87UUs&X-Amz-Signature=1f6ab8739be468c3b01ea629c022a0f8a39fa827607fdb252864fb9f209a00bd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSHAFD5E%2F20260610%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260610T025338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJGMEQCIF%2B63xt1YkRgQKnKakoE2DnUSDZO%2F4PlIkZ3Oo60ptQ7AiAYMnmOyg06%2FvaRNq31DRJSwKvMq4oIcPwCYnGQhVmnRCqIBAjb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMG3Wk3oc1hvXnbyLMKtwDPKevxbGU%2B2fbYmIWNUmsGzU9oGWTfKPYErQVgojzV5ReP%2F1jO8Uh9Us5PtcoOkY2L1LKBajtviRMYWjsSEw6M%2FBuHsl0GrgzikdsIKviPVb8lRQu%2FTaKILQdqGpVFJz%2FJbTFf%2Fu%2BCCaQgL5alkmNIh7BrZ9hb97UvnOlkBMbBtSK%2BkDR8i9FEN9uO8hXiCiEo2Uettab%2F4gQ6S1pEXfxrOL58qAo9%2BsPze2aOD8Vezbevrnm2n%2FJMPifTXtjrChArSTIHsmYT24Cn4IgdIuOeQnCgDjLSDXs7FvHGszgMH%2FhfvXhuIq4aSgKV4Tp8A%2BCPqiWla49kZD8%2FAHQyU54eX%2BWrU%2BYwdbMkYkvu2ca%2Bw0hHSOl2zBCH2pYuJkQFgH11nEdUVau9rpZlk8yvbZ4Qnsbl3Gnn%2BsdnUOJJsojpnotthXcc%2BaQ60B6onmq13UF7hRMMwKt6cGZqt%2FCUT%2BZSwyEtq4QnqOIFcBzOyQSvqClHcjaKdLryYlV8h5tLlLGOasBhaFe27zqGYA2saODicNSGWlTZyLB%2FSgIDbrCUfmqdzntHHfazbMVDhq%2BJf6VNUBUL02hRG%2B%2FKBxAVwCCowf77gI5pduYE1HwVyBgoiXt%2Fqws3DeQiugwC2Qwhoqj0QY6pgE%2FeUTRxJrjK0NRHwKZQrG%2FCLTuUT4siUptZky4GXd4SFzAz87fFNvroyahjTX4df%2FLv4r3MvBsqHy4YpNfTm2zlIRJj64HHgQJfAtB7wbfy3MgQ0FSLSfsH87qHEAQwIXb6mVp9ofzdVoO%2Fd4BOGZOqWsPj6FsL2qqHKo39eAm3ry6bkE74UbTP2zRigHSe64jzKcTkAntyP25oYlfmf9dyGn87UUs&X-Amz-Signature=ff229116cf4b880e32bf33ab0069f7220344698ec749b5e647a0cc48bc836ba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







