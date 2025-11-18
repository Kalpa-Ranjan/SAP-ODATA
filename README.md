



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Y2LUSS4%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T182337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDbXnR69qlnDkYYXch2gfWIWKs52NaysjwwAlWwl1KIrgIgJDiucnJjxwNrKX7O21zZB4t48C4fCC6EDHF47VovDWMqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMfs3JoudkzyWqt9sircAyBKlMlbt9Gzzf6AkKjWVTGWfJtO9W99JKO56fJNl6%2F7E%2ByZU1AAUmlpbcGt8KdmqVPlvz0qELGOtw4F2oyQIGkMgtV0AUyvHsNKU7aDx39Vf903EOh%2FZhgHxOjjnPe8Iv2SY4xVRilmacIjYowqiN2j7%2BXMTE75cmrpRraX%2BggUrvVOhTGfy7D598ZEOlnfnPd%2FEMyqMBSvcGmLtX%2FNaFCnRgrmz3czBccY4VNGIrx%2FIhyDEUVtcU7aMeSsqlGgiWs6tw8h3IFRgur3DvV95DpvYcthKVXKxrMVWy2TJ%2BEhSPdQy5cvprbxBUjnhjgGLYRJVVrHktR%2BYmPj3akO4%2FmQANpzdA7DQexwKl2EvGP1G9Mj4sODvd5Ud8dSFdkyjcqbyb8TrFEHooR4hZjTVLOOcvVSa5vdYPooYj7a%2F7jlwKh0e8%2Buu39XPdY0z9v0NhL9ia5EXCvywLqqohto6byjH3u42eAu1BYWnPwLVRCunrKGoIgjB%2F01tj049fz9oORwVT7UXYylqTB6Jm1kh%2FaqTB28ESLiuvy5IZCorERUvjk2rKWVHOc8HU5C0qul3HmO6Tqhn%2Bc0Uxus%2Bmj3EK%2BmxzCty%2F1RZ6RSel9k88eU2D5wtqe%2F4hDQ1mSIMMnb8sgGOqUBXCvUSZ8z4DgbOrJDQWGamPRVxeaZMHmajLPXy26JMQGTR4mV9o6JhCKMdoNFuHi2ZKjHFzL3AeoblNcnUv0M7RkP%2BbUGVarJrMjMNB1IUBZBfKqzwuxTigbs3Vn1wmiaXlkn08yCKihoY4ObpyOY747kvNL5GqDcSKXffyLSqGDweLG739jZd2sy8%2FqXOJ3RqL7cZ1P7naHGw21pzAmUbtzZHSxz&X-Amz-Signature=e0b68e58e06704329ba59ccc4e32a44d05b1c88118ad57dffea7e27fb5301131&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Y2LUSS4%2F20251118%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251118T182337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQDbXnR69qlnDkYYXch2gfWIWKs52NaysjwwAlWwl1KIrgIgJDiucnJjxwNrKX7O21zZB4t48C4fCC6EDHF47VovDWMqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMfs3JoudkzyWqt9sircAyBKlMlbt9Gzzf6AkKjWVTGWfJtO9W99JKO56fJNl6%2F7E%2ByZU1AAUmlpbcGt8KdmqVPlvz0qELGOtw4F2oyQIGkMgtV0AUyvHsNKU7aDx39Vf903EOh%2FZhgHxOjjnPe8Iv2SY4xVRilmacIjYowqiN2j7%2BXMTE75cmrpRraX%2BggUrvVOhTGfy7D598ZEOlnfnPd%2FEMyqMBSvcGmLtX%2FNaFCnRgrmz3czBccY4VNGIrx%2FIhyDEUVtcU7aMeSsqlGgiWs6tw8h3IFRgur3DvV95DpvYcthKVXKxrMVWy2TJ%2BEhSPdQy5cvprbxBUjnhjgGLYRJVVrHktR%2BYmPj3akO4%2FmQANpzdA7DQexwKl2EvGP1G9Mj4sODvd5Ud8dSFdkyjcqbyb8TrFEHooR4hZjTVLOOcvVSa5vdYPooYj7a%2F7jlwKh0e8%2Buu39XPdY0z9v0NhL9ia5EXCvywLqqohto6byjH3u42eAu1BYWnPwLVRCunrKGoIgjB%2F01tj049fz9oORwVT7UXYylqTB6Jm1kh%2FaqTB28ESLiuvy5IZCorERUvjk2rKWVHOc8HU5C0qul3HmO6Tqhn%2Bc0Uxus%2Bmj3EK%2BmxzCty%2F1RZ6RSel9k88eU2D5wtqe%2F4hDQ1mSIMMnb8sgGOqUBXCvUSZ8z4DgbOrJDQWGamPRVxeaZMHmajLPXy26JMQGTR4mV9o6JhCKMdoNFuHi2ZKjHFzL3AeoblNcnUv0M7RkP%2BbUGVarJrMjMNB1IUBZBfKqzwuxTigbs3Vn1wmiaXlkn08yCKihoY4ObpyOY747kvNL5GqDcSKXffyLSqGDweLG739jZd2sy8%2FqXOJ3RqL7cZ1P7naHGw21pzAmUbtzZHSxz&X-Amz-Signature=6d3093e593183273e7bd9354817ba016c7915fdaea6b0d41fc22db6673509b29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







